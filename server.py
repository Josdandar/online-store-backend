from flask import Flask #IMPORTING EXTERNAL ELEMENTS 
from data import me #You can import classes, function, vars
from data import mock_catalog 
from flask import abort

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

@app.get("/api/catalog")
def catalog():
    return json.dumps(mock_catalog)

@app.get("/api/catalog/count")
def catalog_count():
    count = len(mock_catalog)
    return json.dumps(count)

@app.get("/api/category/<cat>")
def prods_by_category(cat):
    results = []
    for prod in mock_catalog: 
        if prod["category"] == cat:
            results.append(prod)

    return json.dumps(results)

@app.get("/api/product/<id>")
def prod_by_id(id):
    #find the product equal to the id 
    for prod in mock_catalog:
        if prod["_id"] == id:
            return json.dumps(prod)
    return abort(404, "Invalid Id")

@app.get("/api/product/search/<text>")
def search_product(text):
    results = []
    for prod in mock_catalog:
        if text.lower() in prod["title"].lower():
            results.append(prod)
    return json.dumps(results)

@app.get("/api/categories")
def get_categories():
    result = []
    for prod in mock_catalog:
        cat = prod["category"]

app.run(debug=True)