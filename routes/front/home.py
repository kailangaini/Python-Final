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
            data.append({
                "id": p["id"],
                "title": p["title"],
                "price": p["price"],
                "description": p["description"],
                "image": p["thumbnail"],  # <- rename to match your template
            })

    except Exception as e:
        app.logger.error(f"API Error: {e}")
        data = []

    return render_template('pageFront/home.html', products=data)
