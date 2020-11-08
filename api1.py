import xmltodict
from flask import Flask, Response, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


app = Flask(__name__)
api = Api(app)


class name_matching(Resource):
    def get(self, raw_input_name1, raw_input_name2):
        with open("./json_to_xml.xml") as raw_xml:
            returnxml = xmltodict.parse(raw_xml.read())
        return jsonify(returnxml)


api.add_resource(
    name_matching, "/name/<string:raw_input_name1>/<string:raw_input_name2>"
)
if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
