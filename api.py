##Put and delete -HTTP Verb 
## Working With API-S JSON


from flask import Flask, jsonify, request

app = Flask(__name__)


## Initial Data in my to list 

items=[
    {"id": 1, "name": "learning flask", "description": "Flask is a micro web framework written in Python. It is designed to make getting started quick and easy, with the ability to scale up to complex applications."},
    {"id": 2, "name": "learning Django", "description": "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design."},
    {"id": 3, "name": "learning FastAPI", "description": "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints."},
    {"id": 4, "name": "learning Pyramid", "description": "Pyramid is a lightweight Python web framework aimed at small to large applications. It is designed to make real-world web application development and deployment more productive."},
]

@app.route("/")
def  Home ():
    return """
    <style>
        h1 {
            text-align: center;
            margin-top: 20%;
        }
    </style>
    <h1>Welcome to the TODO List with Flask</h1>
    """




## GEt : Retrive the All the Items 

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)
    

## Get the specific item by id
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item_by_id(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404
    

    
## post the item or add the item to the list

@app.route("/items", methods=["POST"])
def add_item():
    if not request.json or "name" not in request.json:
        return jsonify({"error": "Bad Request"}), 400
    new_item={
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json["name"],
        "description": request.json.get("description", "")
    }
    items.append(new_item)
    return jsonify(new_item), 201


## Put : Update the item by id

@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        if not request.json:
            return jsonify({"error": "Bad Request"}), 400
        item["name"] = request.json.get("name", item["name"])
        item["description"] = request.json.get("description", item["description"])
        return jsonify(item)
    

## Delete the item by id
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global items
    items = next((item for item in items if item["id"] != item_id), None)
    return jsonify({"message": "Item deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
