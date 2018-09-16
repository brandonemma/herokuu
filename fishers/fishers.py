import os
from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    return "This is how it works"




if __name__=="__main__":
    app.run()