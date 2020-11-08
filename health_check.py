import config as cfg
import xml.etree.ElementTree as et
import lxml.etree as etree
import requests
from flask import Flask, request, jsonify, Response
from flask_restful import Api, Resource, reqparse
from pymongo import MongoClient
from bson.objectid import ObjectId
import json

app = Flask(__name__)
api = Api(app)

client = MongoClient(cfg.uri)
db_name = cfg.dbname
db = client[db_name]
data = cfg.data


class xml_generator(Resource):
    def get(self):

        global data
        # db.collection.insert_one(data)
        data = data.get("sample_data")
        root = et.Element(
            "PullURIRequest",
            attrib={
                "xmlns": "http://tempuri.org/",
                "ver": "1.0",
                "ts": str(ObjectId("5c51aca67c76124020edbbaf").generation_time),
                "txn": data["txn"],
                "orgId": data["orgId"],
                "format": "xml/pdf/both",
            },
        )
        document_details = data["doc_details"]
        doc_details = et.SubElement(root, "DocDetails")

        for key in document_details:
            et.SubElement(doc_details, key).text = document_details[key]
        xml = et.ElementTree(root)
        xml.write("json_to_xml.xml")
        xml = """json_to_xml.xml"""
        headers = {"Content-Type": "application/xml"}
        URL = "http://0.0.0.0:5000/test"
        response = requests.get(URL, data=xml, headers=headers)
        json_response = response.json()
        latency = response.elapsed
        return jsonify({"Response": json_response})


api.add_resource(xml_generator, "/")
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
