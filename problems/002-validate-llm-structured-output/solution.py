import json
def validate_response(raw, schema):
    """Parse and validate a model's JSON reply against a {field: type} schema.

    Return the cleaned dict, or None if it cannot be trusted.
    """
    try:
        response = json.loads(raw)
    except:
        return None
    # first thing json.loads not necessarliy always return a json
    # though this would be rare
    if not isinstance(response,dict):
        return None
    # now we need to validate against the schema
    # response is a dict 
    validated_response = {}
    for k,v in schema.items():
        if k in response and type(response[k]) == v:
            validated_response[k] = response[k]
        else:
            return None # because everything in schema is required
    return validated_response
    
