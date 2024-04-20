def str_to_json(str):
    import json

    return json.loads(str)


def json_to_str(obj):
    import json

    return json.dumps(obj, indent=4)
