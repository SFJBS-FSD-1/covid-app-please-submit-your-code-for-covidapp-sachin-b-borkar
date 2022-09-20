from flask import Flask,jsonify,request
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)
recipes =[
            {"id":1,
             "name":"dosa",
             "description":"masala"},
            {"id":2,
             "name":"chapati",
             "description":"wheet"}]

class allRecipes(Resource):
    def get(self):
        return jsonify(recipes)

    def post(self):
        data = request.get_json()
        recipes.append(data)
        return jsonify(recipes)

class oneRecipe(Resource):
    def get(self,recipe_id):
        for recipe in recipes:
            if recipe["id"] == recipe_id:
                return jsonify(recipe)
        else:
            return jsonify({"message":"ID not found"})

    def put(self,recipe_id):
        for recipe in recipes:
            if recipe["id"] == recipe_id:
                data = request.get_json()
                recipe.update({"id": data["id"], "name": data["name"], "description": data["description"]})
                return jsonify(recipes)
        else:
            return ({"message":"ID not found"})

    def delete(self,recipe_id):
        for recipe in recipes:
            if recipe["id"] == recipe_id:
                recipes.remove(recipe)
                return jsonify(recipes)
        else:
            return ({"message":"ID not found"})

api.add_resource(allRecipes,"/recipes")
api.add_resource(oneRecipe,"/recipes/<int:recipe_id>")
app.run()