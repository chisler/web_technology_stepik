# def parse_qs(qs):
#     if not qs:
#         return {}
#     variables = [v.split("=") for v in qs.split("&")]
#     return {x[0]: x[1] for x in variables if len(x) == 2}

def app(environ, start_response):
    qs = environ.get('QUERY_STRING', None)
    data = bytes(
        b"\n".join([param.encode("utf-8") for param in qs.split("&")])
    )
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return [data]
