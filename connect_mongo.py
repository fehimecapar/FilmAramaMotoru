from pymongo import MongoClient
from opensearchpy import  OpenSearch

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')


client = MongoClient("mongodb://localhost:27017")

db = client.admin
collection = db["film"]

INDEX_NAME = 'film_arsiv_sistemi'

os_client = OpenSearch(
    hosts=["https://admin:admin@localhost:9200/"],
    http_compress=True,
    use_ssl=True,  # DONT USE IN PRODUCTION
    verify_certs=False,  # DONT USE IN PRODUCTION
    ssl_assert_hostname=False,
    ssl_show_warn=False,
)

body = []
res = db.film.find()
count = 0
for i in res:
    if count < 1000:
        try: 
            embedding = model.encode(i["Plot"]).tolist() 
            print("embedded")
            body.append(
                {"update": {"_index": INDEX_NAME, "_id": str(i["_id"])}}
            )
            
            # body.append({"doc": {"director": i["Director"], "genre": i["Genre"], "origin_ethnicity": i["Origin/Ethnicity"], "title": i["Title"],
            # "plot": i["Plot"] , "release_year": i["Release Year"], "wiki_page": i['Wiki Page'], "vtext": embedding}, "doc_as_upsert": True})
            body.append({"doc": {"vtext": embedding}, "doc_as_upsert": True})
            count += 1
            continue
        except Exception as e:
            print(e)
            continue
    try:
        os_client.bulk(body=body)
        count = 0
        print(len(body), " data added...")
        body = []
        
    except Exception as e:
        print(e)


