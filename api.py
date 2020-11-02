from pymongo import MongoClient
import config as cfg
import xml.etree.ElementTree as et
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

root = et.Element("PullURIRequest", attrib={"ver": version, "txn": txn})
doc_details = et.SubElement(root, "DocDetails")
for i in sample_data:
    et.SubElement(doc_details, "UID").text = i["UID"]
    et.SubElement(doc_details, "DOB").text = i["DOB"]
    et.SubElement(doc_details, "Full_Name").text = i["Full_Name"]
    et.SubElement(doc_details, "gender").text = i["gender"]
    et.SubElement(doc_details, "phone_number").text = i["phone_number"]

et.SubElement(root, "email").text = person[0]["email"]
xml = et.ElementTree(root)
et.dump(xml)
xml.write("json_to_xml.xml")