def ask_for_json(llm, prompt, schema, max_attempts=3):
    """Ask until the reply validates. Return the object, or None after max_attempts."""
    messages = [{"role":"user","content":prompt}]
    for attempt in range(max_attempts):
        response = llm.messages.create(messages=messages).text
        is_json = validate(response,schema)
        if is_json[0]:
            return is_json[0]
        else:
            error = is_json[1]
            messages.append({"role":"assistant", "content":response})
            messages.append({"role":"user","content":error})
    return None
