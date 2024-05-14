FROM python:3.12-slim
VOLUME /app
WORKDIR /app
ADD ./app/main.py .
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install streamlit panda
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
