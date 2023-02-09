from flask import Flask #IMPORTING EXTERNAL ELEMENTS 
from data import me #You can import classes, function, vars

import json #Importing something inside python itself 

app = Flask(__name__) #Creating a new instance 


@app.get("/")
def home():
    return "Hello World!"

@app.get("/about")
def about():
    return "Jose De Anda"

@app.get("/contact/me")
def contact():
    return "josdandar@gmail.com"

@app.get("/api/development/address")
def address():
    address = me["address"]
    # return str(address["street"]) + " " + str(address["number"])
    return f"{address['street']}"
    #Gotta decide if using double or single quotes 


########3
@app.get("/api/developer")
def developer():
    return json.dumps(me)#parse into a string 

app.run(debug=True)