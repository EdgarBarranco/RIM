#!/bin/bash
docker run -dp 0.0.0.0:8501:8501 --restart="always" --mount type=volume,src=inv-app,target=//app --name Inventory inv

