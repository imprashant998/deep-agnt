def count_tokens(text):
    """Number of tokens, excluding any special tokens."""
    return len(tokenizer.encode(text,add_special_tokens=False))


def roundtrip(text):
    """Encode then decode, returning the original text."""
    token_ids = tokenizer.encode(text)
    decoded = tokenizer.decode(token_ids,skip_special_tokens = True)
    return decoded


def token_strings(text):
    """The individual tokens, in order, as strings."""
    token_ids = tokenizer.encode(text,add_special_tokens = False)
    return tokenizer.convert_ids_to_tokens(token_ids)
