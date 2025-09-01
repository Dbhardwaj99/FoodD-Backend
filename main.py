from flask import Flask, jsonify

app = Flask(__name__)

# Mock Data
appetizers = {
    "request": [
        {
            "id": 1,
            "name": "Spring Rolls",
            "description": "Crispy rolls stuffed with vegetables.",
            "price": 5.99,
            "imageURL": "https://example.com/springrolls.png",
            "calories": 300,
            "protein": 6,
            "carbs": 45
        },
        {
            "id": 2,
            "name": "Garlic Bread",
            "description": "Toasted bread with garlic and butter.",
            "price": 3.49,
            "imageURL": "https://example.com/garlicbread.png",
            "calories": 250,
            "protein": 7,
            "carbs": 32
        },
        {
            "id": 3,
            "name": "Chicken Wings",
            "description": "Spicy wings with ranch dip.",
            "price": 8.99,
            "imageURL": "https://example.com/chickenwings.png",
            "calories": 600,
            "protein": 25,
            "carbs": 20
        }
    ]
}

@app.route("/appetizers", methods=["GET"])
def get_appetizers():
    return jsonify(appetizers)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
