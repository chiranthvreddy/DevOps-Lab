from flask import Flask, jsonify
app = Flask(__name__)
products = ["Laptop", "Phone", "Headphones"]

@app.get("/")
@app.get("/products")
def get_products():
    return jsonify(products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
