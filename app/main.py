import streamlit as st
import pandas as pd

# Function to load data from CSV file
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        data = pd.DataFrame(columns=['Item', 'Quantity'])
    return data


# Function to save data to CSV file
def save_data(data, file_path):
    data.to_csv(file_path, index=False)


# Main function to run the Streamlit app
def main():
    st.title("Refrigerator Inventory Management")

    # Load existing data or create an empty DataFrame
    file_path = "inventory.csv"
    inventory_data = load_data(file_path)

    # Sidebar to add new items
    st.sidebar.header("Add New Item")
    new_item = st.sidebar.text_input("Item Name:")
    new_quantity = st.sidebar.number_input("Quantity:", value=1)

    if st.sidebar.button("Add Item"):
        if new_item.strip() != "":
            # Check if the item already exists in the inventory
            if new_item in inventory_data['Item'].values:
                # Update quantity if item already exists
                idx = inventory_data.index[inventory_data['Item'] == new_item].tolist()[0]
                inventory_data.loc[idx, 'Quantity'] += new_quantity
            else:
                # Add new item to the inventory
                inventory_data = inventory_data._append({'Item': new_item, 'Quantity': new_quantity}, ignore_index=True)

            # Save the updated inventory
            save_data(inventory_data, file_path)
            st.success(f"{new_quantity} {new_item}(s) added successfully!")
            st.rerun()

    # Display current inventory
    st.header("Current Inventory")

    for idx, row in inventory_data.iterrows():
        col1, col2, col3 = st.columns([0.5, 4, 1])
        with col1:
            if col1.button("&#45;", key=f"dec_{idx}"):
                if inventory_data.at[idx, "Quantity"] > 0:
                    inventory_data.at[idx, "Quantity"] -= 1
                    if inventory_data.at[idx, "Quantity"] == 0:
                        inventory_data = inventory_data.drop(index=idx)
                    save_data(inventory_data, file_path)
                    st.rerun()
        with col3:
            if col3.button("&#43;", key=f"inc_{idx}"):
                inventory_data.at[idx, "Quantity"] += 1
                save_data(inventory_data, file_path)
                st.rerun()
        with col2:
            st.write(row['Item'], row['Quantity'])


if __name__ == "__main__":
    main()
