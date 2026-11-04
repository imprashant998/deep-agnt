CONTINUE_PROMPT = "Please continue from where you left off!"

TERMINAL_STATUS = {
    "end_turn": "complete",
    "tool_use": "tool_use",
    "refusal": "refused",
}


def complete(llm, messages, max_tokens=200, max_continues=3):
    """Get the whole reply, continuing when cut off. Return text and status."""
    text = ""
    messages = list(messages) # copies the caller's list
    max_attempts = max_continues +1
    for attempt in range(max_attempts):
        response = llm.messages.create(messages=messages, max_tokens=max_tokens)
        text += response.text
        reason = response.stop_reason

        if reason in TERMINAL_STATUS:
            return {"text": text, "status": TERMINAL_STATUS[reason]}

        if reason != "max_tokens":
            raise ValueError(f"Unexpected stop_reason: {reason!r}")

        messages.append({"role": "assistant", "content": response.text})
        if attempt + 1 < max_attempts:
            # we won't request to continue in the last attempt
            messages.append({"role": "user", "content": CONTINUE_PROMPT})
    # exited the for loop, means it reached the max attempt without returning
    return {"text": text, "status": "truncated"}
