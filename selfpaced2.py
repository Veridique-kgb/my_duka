from flask import Flask, render_template, request, redirect,url_for
from database import get_products, get_sales, get_stock, insert_products,insert_sales, insert_stock

app=Flask(__name__)

@app.route("/")
def home():
    number = 100
    name = "Jack"
    value = 45
    numbers = [1,2,3,4,5]
    return render_template("index.html", number=number, name=name, value=value, numbers=numbers)

@app.route("/products")
def products():
    product_data=get_products()
    return render_template("products.html",product_data=product_data)

@app.route

