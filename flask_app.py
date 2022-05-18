from flask import Flask, request
from flask_restful import Resource, Api
from sun_coords import is_glare


app = Flask(__name__)
api = Api(app)

class SunGlare(Resource):


    def get(self):

        return {'default request': 'Please post a json containing the required information'}

    def post(self):

        inputs = request.get_json()
        output = is_glare(inputs)


        return {'glare:': bool(output)}


api.add_resource(SunGlare, '/')

if __name__ == '__main__':
    app.run(debug=False)
