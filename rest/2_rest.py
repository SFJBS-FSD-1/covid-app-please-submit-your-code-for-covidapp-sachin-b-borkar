from flask import Flask,request,jsonify
app = Flask(__name__)

recipes =[{"id":1,"name":"dosa","description":"masala"},{"id":2,"name":"chapati","description":"wheet"}]

@app.route("/", methods = ["GET"])
def home_get():
    if request.method == "GET":
        json_data=jsonify(recipes)
        return json_data

@app.route("/recipes/<int:id>", methods=["GET"])
def home_get_id(id):
    print(id)
    if request.method == "GET":
        json_data = jsonify(recipes)
        for i in recipes:
            if i["id"] == id:
                return (i)
        else:
            return ({"message":"ID not found"})

@app.route("/recipes/<int:id>", methods=["DELETE"])
def home_del_id(id):
    print(id)
    if request.method == "DELETE":
        json_data = jsonify(recipes)
        for i in recipes:
            if i["id"] == id:
                recipes.remove(i)
            return jsonify(recipes)
        else:
            return ({"message":"ID not found"})

@app.route("/recipes/<int:id>", methods=["PUT"])
def home_update_id(id):
    print(id)
    if request.method == "PUT":
        json_data = jsonify(recipes)
        for i in recipes:
            if i["id"] == id:
                data = request.get_json()
                i.update({"id":data["id"],"name":data["name"],"description":data["description"]})
                return jsonify(recipes)
        else:
            return ({"message":"ID not found"})
@app.route("/recipes/", methods=["POST"])
def home_add_id():
    if request.method == "POST":
        json_data = jsonify(recipes)
        data = request.get_json()
        recipes.append(data)
        return jsonify(recipes)

app.run()