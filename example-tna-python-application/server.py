def application(env, start_response):
    data = "Hello, World!\n"
    start_response(
        "200 OK", [("Content-Type", "text/plain"), ("Content-Length", str(len(data)))]
    )
    return [bytes(data, "utf-8")]
