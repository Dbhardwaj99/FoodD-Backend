from flask import Flask, jsonify
import os

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
        },
        {
            "id": 4,
            "name": "Mozzarella Sticks",
            "description": "Golden fried cheese sticks with marinara sauce.",
            "price": 6.49,
            "imageURL": "https://example.com/mozzarella.png",
            "calories": 450,
            "protein": 12,
            "carbs": 35
        },
        {
            "id": 5,
            "name": "Nachos",
            "description": "Corn chips topped with cheese and jalapeños.",
            "price": 7.25,
            "imageURL": "https://example.com/nachos.png",
            "calories": 550,
            "protein": 10,
            "carbs": 60
        },
        {
            "id": 6,
            "name": "Stuffed Mushrooms",
            "description": "Mushrooms filled with cheese and herbs.",
            "price": 6.99,
            "imageURL": "https://example.com/mushrooms.png",
            "calories": 320,
            "protein": 8,
            "carbs": 15
        },
        {
            "id": 7,
            "name": "Onion Rings",
            "description": "Crispy fried onion rings served with dip.",
            "price": 4.99,
            "imageURL": "https://example.com/onionrings.png",
            "calories": 400,
            "protein": 5,
            "carbs": 50
        },
        {
            "id": 8,
            "name": "Bruschetta",
            "description": "Toasted bread with tomato, basil, and olive oil.",
            "price": 5.75,
            "imageURL": "https://example.com/bruschetta.png",
            "calories": 280,
            "protein": 6,
            "carbs": 30
        },
        {
            "id": 9,
            "name": "French Fries",
            "description": "Golden fries with a choice of dips.",
            "price": 3.99,
            "imageURL": "https://example.com/fries.png",
            "calories": 370,
            "protein": 4,
            "carbs": 55
        },
        {
            "id": 10,
            "name": "Shrimp Cocktail",
            "description": "Chilled shrimp with cocktail sauce.",
            "price": 9.49,
            "imageURL": "https://example.com/shrimp.png",
            "calories": 210,
            "protein": 20,
            "carbs": 10
        },
        {
            "id": 11,
            "name": "Quesadilla",
            "description": "Cheese quesadilla with salsa.",
            "price": 6.49,
            "imageURL": "https://example.com/quesadilla.png",
            "calories": 430,
            "protein": 14,
            "carbs": 40
        },
        {
            "id": 12,
            "name": "Samosa",
            "description": "Spiced potato-filled pastry.",
            "price": 4.50,
            "imageURL": "https://example.com/samosa.png",
            "calories": 320,
            "protein": 5,
            "carbs": 38
        },
        {
            "id": 13,
            "name": "Buffalo Cauliflower",
            "description": "Cauliflower bites tossed in buffalo sauce.",
            "price": 5.99,
            "imageURL": "https://example.com/cauliflower.png",
            "calories": 280,
            "protein": 9,
            "carbs": 28
        },
        {
            "id": 14,
            "name": "Meatballs",
            "description": "Savory beef meatballs in marinara sauce.",
            "price": 7.99,
            "imageURL": "https://example.com/meatballs.png",
            "calories": 500,
            "protein": 22,
            "carbs": 15
        },
        {
            "id": 15,
            "name": "Caprese Skewers",
            "description": "Tomato, mozzarella, and basil on skewers.",
            "price": 5.25,
            "imageURL": "https://example.com/caprese.png",
            "calories": 260,
            "protein": 10,
            "carbs": 14
        },
        {
            "id": 16,
            "name": "Potato Wedges",
            "description": "Seasoned crispy potato wedges.",
            "price": 4.75,
            "imageURL": "https://example.com/wedges.png",
            "calories": 350,
            "protein": 6,
            "carbs": 52
        },
        {
            "id": 17,
            "name": "Cheese Platter",
            "description": "Assorted cheeses with crackers.",
            "price": 11.99,
            "imageURL": "https://example.com/cheeseplatter.png",
            "calories": 700,
            "protein": 30,
            "carbs": 40
        },
        {
            "id": 18,
            "name": "Falafel Bites",
            "description": "Fried chickpea balls served with hummus.",
            "price": 6.25,
            "imageURL": "https://example.com/falafel.png",
            "calories": 340,
            "protein": 12,
            "carbs": 34
        },
        {
            "id": 19,
            "name": "Calamari",
            "description": "Crispy fried calamari rings with aioli.",
            "price": 9.75,
            "imageURL": "https://example.com/calamari.png",
            "calories": 480,
            "protein": 21,
            "carbs": 25
        },
        {
            "id": 20,
            "name": "Deviled Eggs",
            "description": "Classic deviled eggs with paprika.",
            "price": 3.99,
            "imageURL": "https://example.com/deviledeggs.png",
            "calories": 200,
            "protein": 9,
            "carbs": 2
        }
    ]
}

@app.route("/appetizers", methods=["GET"])
def get_appetizers():
    return jsonify(appetizers)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # default 5000 for local
    app.run(host="0.0.0.0", port=port)
