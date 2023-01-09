from pymongo import MongoClient
import os_connection
import text_embedding

client = MongoClient("mongodb://localhost:27017")

db = client.admin
collection = db["film"]

INDEX_NAME = 'film_arsiv_sistemi'

os_client = os_connection.connection()

body = []
res = db.film.find()
count = 0
for i in res:
    if count < 1000:    
        vtext = text_embedding.text_embed(i["Plot"])
        if "error" not in vtext:
            body.append(
                {"update": {"_index": INDEX_NAME, "_id": str(i["_id"])}}
            )
            
            body.append({"doc": {"director": i["Director"], "genre": i["Genre"], "origin_ethnicity": i["Origin/Ethnicity"], "title": i["Title"],
            "plot": i["Plot"] , "release_year": i["Release Year"], "wiki_page": i['Wiki Page'], "vtext": vtext}, "doc_as_upsert": True})
            count += 1
            continue
                     
    try:
        if "error" not in os_client:
            res = os_client.bulk(body=body)
            count = 0
            print(len(body), " data added...")
            body = []

    except Exception as e:
        print(e)


