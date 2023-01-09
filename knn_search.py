from pprint import pprint
import text_embedding
import os_connection

client = os_connection.connection()

text = input("please enter basic summary for film: ")

search_text = text_embedding.text_embed(text)

query = {
        "query": {
                      "knn": {
                      "vtext": {
                          "vector": search_text,
                          "k": 18
                      }
                      }
                    
                  },
                  "_source": False,
                  "fields": ["_id", "title"],      
      }
try:
    if "error" not in client: 
        response = client.search(body=query, index="film_arsiv_sistemi")
        pprint(response["hits"]["hits"])

except Exception as e:
    print(e)