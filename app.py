from flask import Flask, request

app = Flask(__name__)

stores= [
    {
        "name" : "My Store",
        "items": [
            {
                "name":"Chair",
                "price": 15.99
            }
        ]
    }
]

@app.get("/store") #http://127.0.0.1:5000/store
def get_stores():
    return {"stores": stores}

# we are creating a store 
@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items":[]}
    stores.append(new_store)
    return new_store, 201

# here we are adding items into an especifict store 
@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name":request_data["name"],"price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message":"Store not found"}, 404

@app.get("store/<string: name>")
def get_store():
    for store in stores:
        if store["name"] == name:
            return store
    return {"message":"Store not found"}, 404