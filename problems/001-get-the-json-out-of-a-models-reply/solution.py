import json


def parse_model_json(reply):
    """Return the JSON object in a model's reply, or None if there isn't one."""
    start = reply.find('{')
    if start == -1:
        return None
    end = reply.rfind('}')
    if end == -1:
        return None
    try:
        return json.loads(reply[start:end+1])
    except:
        return None


