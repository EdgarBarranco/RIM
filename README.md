# RIM
This is a simple "Refrigerator Inventory Management" system

![Screenshot of RIM](/img/RIM.png)

The application was written in python using streamlit and panda.
```
pip3 install streamlit panda
```
The application is located under /app/main.py
To run: 
```
streamlit run main.py --server.port=8501 --server.address=0.0.0.0
```
It creates a file “inventory.csv” where the the data is stored.

This application can also be run from docker. 

Create the volume:
```
docker volume create inv-app
```
Build the image:
```
docker build -t inv .
```
Run the docker container:
```
docker run -dp 0.0.0.0:8501:8501 --restart="always" --mount type=volume,src=inv-app,target=//app --name Inventory inv
```
