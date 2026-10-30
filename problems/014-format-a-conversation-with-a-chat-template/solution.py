def format_chat(messages):
    """The prompt string, ready for the assistant to continue."""
    # beacuse in the end, we need a string not list of dict for the model to generate
    if not tokenizer.chat_template:
        prompt = "".join(f"{m['role']}:{m['content']}{chr(10)}" for m in messages)
        return prompt + "assistant:"
    return tokenizer.apply_chat_template(
                                        messages,
                                        tokenize = False,
                                        add_generation_prompt = True)
    # add generation prompt is adding the little important "assistant:" 
    #for model to know that it is their turn


def format_for_training(messages):
    """The full conversation including the assistant's reply."""
    if not tokenizer.chat_template:
        prompt = "".join(f"{m['role']}:{m['content']}{chr(10)}" for m in messages)
        return prompt
    return tokenizer.apply_chat_template(
                                        messages,
                                        tokenize=False,
                                        add_generation_prompt = False)
    
    
