from app import app, render_template
import requests

@app.get('/cart')
def cart():
    product_ids = [1, 2, 3]

    images = []

    for pid in product_ids:
        url = f"https://dummyjson.com/products/{pid}"
        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            p = r.json()

            # Get product image (thumbnail or first image)
            image_url = p.get("thumbnail") or (p["images"][0] if p.get("images") else None)
            images.append(image_url)
        except:
            images.append(None)

    # Pass the images to the template
    return render_template("pageFront/cart.html", images=images)
