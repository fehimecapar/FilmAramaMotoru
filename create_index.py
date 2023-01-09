import os_connection

client = os_connection.connection()

INDEX_NAME = 'film_arsiv_sistemi'

def create_index():
    settings = {
        "settings": {
            "index": {
                "knn": True,
            }
        },
        "mappings": {
            "properties": {
                "vtext": {
                    "type": "knn_vector",
                    "dimension": 384,
                    "method": {
                        "name": "hnsw",
                        "space_type": "cosinesimil",
                        "engine": "nmslib",
                        }
                    },
                }
            },
        }
    try:
        if "error" not in client:
            res = client.indices.create(index=INDEX_NAME, body=settings, ignore=[400])
            print(res)
    except Exception as e:
        print(e)

create_index()