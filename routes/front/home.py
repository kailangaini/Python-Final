from app import app, render_template
import requests

@app.get('/')
@app.get('/home')
def home():
    url = 'https://dummyjson.com/products'

    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        raw_data = res.json().get("products", [])

        # Normalize data so HTML works the same as before
        data = []
        for p in raw_data:
            image_url = p.get("thumbnail") or (p["images"][0] if p.get("images") else None)

            data.append({
                "id": p["id"],
                "title": p["title"],
                "price": p["price"],
                "description": p["description"],
                "image": image_url,
            })

    except Exception as e:
        app.logger.error(f"API Error: {e}")
        data = []

    return render_template('pageFront/home.html', products=data)
