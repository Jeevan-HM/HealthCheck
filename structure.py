from bson.objectid import ObjectId
from pymongo import MongoClient
import config as cfg
import xml.etree.ElementTree as et
import lxml.etree as etree
from xml.dom import minidom

client = MongoClient(cfg.uri)
db_name = cfg.dbname
db = client[db_name]
data = cfg.data
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
# del document_details["DocType"]
# del document_details["DigiLockerId"]
doc_details = et.SubElement(root, "DocDetails")
# et.SubElement(doc_details, "DocType").text = "OACT"
# et.SubElement(doc_details, "DigiLockerId").text = "12345678936"

for key in document_details:
    et.SubElement(doc_details, key).text = document_details[key]
xml = et.ElementTree(root)
et.dump(xml)
xml.write("json_to_xml.xml")
