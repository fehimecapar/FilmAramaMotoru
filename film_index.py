from opensearchpy import  OpenSearch

INDEX_NAME = 'film_arsiv_sistemi'

client = OpenSearch(
    hosts=["https://admin:admin@localhost:9200/"],
    http_compress=True,
    use_ssl=True,  # DONT USE IN PRODUCTION
    verify_certs=False,  # DONT USE IN PRODUCTION
    ssl_assert_hostname=False,
    ssl_show_warn=False,
)

def create_index():
    settings = {
        "settings": {
            "index": {
                "knn": True,
            }
        },
        "mappings": {
            "properties": {
                "vimg": {
                    "type": "knn_vector",
                    "dimension": 512,
                    "method": {
                        "name": "hnsw",
                        "space_type": "cosinesimil",
                        "engine": "nmslib",
                        }
                    },
                }
            },
        }
    res = client.indices.create(index=INDEX_NAME, body=settings, ignore=[400])
    print(res)

def knn_update(data):
    return data
