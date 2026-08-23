import random
import socket
import time
from flask import Flask,request
app=Flask(__name__)
@app.get("/")
def home():
    return {"message":"Welcome to Big Sale!","pod":socket.gethostname(),"timestamp":time.time()}
@app.get("/buy")
def buy():
    return {"status":"success","item":random.choice(["Smartphone","Shoes","Headphones","Laptop"]),"user":request.args.get("user","customer"),"served_by_pod":socket.gethostname()}
@app.get("/health")
def health():
    return {"status":"healthy"}
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
