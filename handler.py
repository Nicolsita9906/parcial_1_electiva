def hello(event, context):
    name = event.get("Nicol Valeria", "World")
    return {"message": "Hello, {name}!"}
