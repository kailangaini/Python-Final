from flask import render_template, abort
from app import app
import requests

@app.get('/product_details/<int:product_id>')
def product_details(product_id):
    # Fetch single product from DummyJSON
    url = f'https://dummyjson.com/products/{product_id}'
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        p = response.json()

        # Normalize to match your template
        product = {
            "id": p["id"],
            "title": p["title"],
            "price": p["price"],
            "description": p["description"],
            "image": p["thumbnail"],    # convert thumbnail -> image
        }

        return render_template('pageFront/product_details.html', product=product)
    else:
        abort(404)
