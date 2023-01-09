from opensearchpy import  OpenSearch
def connection():
    try: 
        client = OpenSearch(
            hosts=["https://admin:admin@localhost:9200/"],
            http_compress=True,
            use_ssl=True,  # DONT USE IN PRODUCTION
            verify_certs=False,  # DONT USE IN PRODUCTION
            ssl_assert_hostname=False,
            ssl_show_warn=False,
        )
        return client
    except Exception as e:
        return {"error": e}