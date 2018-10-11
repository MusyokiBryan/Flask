from flask import Flask, jsonify, make_response, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


cart = []

class Cart(Resource):
	def get(self):
	    return make_response(jsonify({"Status" : "Ok", "Message" : "Success", "cart" : cart }),200)

	def post(self):
	    data = request.get_json()
	    id = len(cart) + 1
	    name = data['name']
	    desc = data['desc']
	    price = data['price']

	    product = {
	        "id" : id,
	        "Description" : {
	            "name" : name,
	            "desc" : desc,
	            "Price" : price
	        }
	    }

	    cart.append(product)

	    return make_response(jsonify(
	        {
	            "Status" : "Ok",
	            "Message" : "Successfully Posted",
	            "cart" : cart
	        }
	    ),201)

api.add_resource(Cart, "/")

if __name__ == "__main__":
	app.run(debug=True)
