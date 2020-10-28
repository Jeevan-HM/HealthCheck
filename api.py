from pymongo import MongoClient
import config as cfg
import xml.etree.ElementTree as e
import lxml.etree as etree
from xml.dom import minidom

client = MongoClient(cfg.uri)
db_name = cfg.dbname
db = client[db_name]
data = cfg.data

# def insert_data(data):
#     document = db.collection.insert_one(data)
# insert_data(data)
person = [data.get("person1_id")]
person[0]["api_url"]
version = "1.0"
txn = person[0]["txn"]
sample_data = [person[0]["sample _data"]]

root = e.Element("PullURIRequest", attrib={"ver": version, "txn": txn})
doc_details = e.SubElement(root, "DocDetails")
for i in sample_data:
    e.SubElement(doc_details, "UID").text = i["UID"]
    e.SubElement(doc_details, "DOB").text = i["DOB"]
    e.SubElement(doc_details, "Full_Name").text = i["Full_Name"]
    e.SubElement(doc_details, "gender").text = i["gender"]
    e.SubElement(doc_details, "phone_number").text = i["phone_number"]

e.SubElement(root, "email").text = person[0]["email"]
xml = e.ElementTree(root)
xml.write("TEST.xml")
print(xml)