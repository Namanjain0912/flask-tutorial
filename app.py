from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Naman Welcomes you"

@app.route("/home")
def home():
    return "This is home page"

@app.route("/calculate")
def calculate():
    sum1 = 0
    for i in range(1, 5):
        sum1 += i
    return f"The sum is {sum1}"

from controller import *
from model.user_model import user_model

        
