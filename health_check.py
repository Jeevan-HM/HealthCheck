import config as cfg
import xml.etree.ElementTree as et
import lxml.etree as etree
import requests
from flask import Flask, request, jsonify, Response
from flask_restful import Api, Resource, reqparse
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
import datetime

app = Flask(__name__)
api = Api(app)

client = MongoClient(cfg.uri)
db_name = cfg.dbname
db = client[db_name]
data = cfg.data


class xml_generator(Resource):
    def get(self):
        global message
        global status
        status = False
        message = ""
        global data
        # db.collection.insert_one(data)
        data = list(db.collection.find())
        for language in data:
            language["_id"] = str(language["_id"])
        # data = data.get("sample_data")
        root = et.Element(
            "PullURIRequest",
            attrib={
                "xmlns": "http://tempuri.org/",
                "ver": "1.0",
                "ts": str(ObjectId(language["_id"]).generation_time),
                "txn": language["sample_data"]["txn"],
                "orgId": language["sample_data"]["orgId"],
                "format": "xml/pdf/both",
            },
        )
        document_details = language["sample_data"]["doc_details"]
        doc_details = et.SubElement(root, "DocDetails")

        for key in document_details:
            et.SubElement(doc_details, key).text = document_details[key]
        xml = et.ElementTree(root)
        xml.write("json_to_xml.xml")
        headers = {"Content-Type": "application/xml"}
        URL = "http://0.0.0.0:5000/test"
        # response = requests.get(URL, data=xml, headers=headers)
        # json_response = response.json()
        # return jsonify({"Response": json_response})
        xml = et.tostring(root)
        response = requests.post(URL, data=xml, headers=headers, timeout=5)
        # print(response["DocType"])
        return_response = response.json()
        # print(return_response)
        # for key, value in return_response.items():
        id = return_response["DigiLockerId"]
        message = "DigiLockerId Exitsts"
        status = return_response["status"]
        json_response = {"status": status, "message": message, "id": id}
        return json_response
        #     id = return_response["DigiLockerId"]
        #     stauts = return_response["status"]
        #     message = key + "returned"
        # print(id)
        # print(status)
        # print(message)
        # return {"status": status, "ID": id, "message": message}

        # latency = response.elapsed
        # print("latency", latency)


api.add_resource(xml_generator, "/")
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
