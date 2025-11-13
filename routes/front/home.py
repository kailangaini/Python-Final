from app import app, render_template
import requests

@app.get('/')
@app.get('/home')
def home():
    url = 'https://fakestoreapi.com/products'
    try:
        res = requests.get(url, timeout=5)
        res.raise_for_status()  # raises HTTPError for bad codes
        try:
            data = res.json()
        except ValueError:
            app.logger.error(f"Non-JSON response from {url}: {res.text[:200]}")
            data = []
    except requests.RequestException as e:
        app.logger.error(f"Error fetching products: {e}")
        data = []

    return render_template('pageFront/home.html', products=data)
