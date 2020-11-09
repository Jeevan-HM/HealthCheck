import xmltodict
from flask import Flask, Response, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


app = Flask(__name__)
api = Api(app)


# class test(Resource):
#     def get(self):
#         with open("./json_to_xml.xml") as raw_xml:
#             returnxml = xmltodict.parse(raw_xml.read())
#         return jsonify(returnxml)
class test(Resource):
    def post(self):
        data = request.data
        json_response = {
            "DocType": "OATDA",
            "DigiLockerId": "1234567899876543210",
            "status": True,
            "Name": "test",
        }
        return jsonify(json_response)

    # def get(self):
    #     data = request.data
    #     print(data)
    #     json_response = {
    #         "DocType": "OATDA",
    #         "DigiLockerId": "1234567899876543210",
    #         "status": 200,
    #     }
    #     return jsonify(json_response)


api.add_resource(test, "/test")
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
