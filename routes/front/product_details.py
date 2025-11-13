from flask import render_template, abort
from app import app
import requests

@app.get('/product_details/<int:product_id>')
def product_details(product_id):
    # Get product from FakeStoreAPI
    response = requests.get(f'https://fakestoreapi.com/products/{product_id}')

    if response.status_code == 200:
        product = response.json()
        return render_template('pageFront/product_details.html', product=product)
    else:
        abort(404)
