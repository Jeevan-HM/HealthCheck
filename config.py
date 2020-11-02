uri = "mongodb://localhost:27017"
dbname = "Sample_data"
collection = "SampleInput"

data = {
    "person1_id": {
        "api_url": "https://register/api/format/xml",
        "sample _data": {
            "UID": "1234 5678 9123",
            "DOB": "01/01/2001",
            "Full_Name": "Jeevan HM",
            "gender": "male",
            "phone_number": "1234567890",
        },
        "email": "test@gmail.com",
        "txn": "1a2b3cd4",
        "status": 1,
    }
}


{
    "_id": {
        "$oid": "5f99be00b6e21131ce9000c3"
    },
    "person1_id": {
        "api_url": "https://register/api/format/xml",
        "sample _data": {
            "UID": "1234 5678 9123",
            "DOB": "01/01/2001",
            "Full_Name": "Jeevan HM",
            "gender": "male",
            "phone_number": "1234567890"
        },
        "email": "test@gmail.com",
        "txn": "1a2b3cd4",
        "status": 1
    }
}
