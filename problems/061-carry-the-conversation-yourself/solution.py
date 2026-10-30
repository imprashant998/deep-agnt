class Chat:
    """A conversation with a model."""

    def __init__(self, llm, system):
        self.llm = llm
        self.system = system
        self.messages = []

    def send(self, text):
        """Send the user's message. Return the model's reply."""
        new_msg = {"role":"user","content":text}
        self.messages.append(new_msg)
        try:
            response = self.llm.messages.create(
                #messages=[{"role": "user", "content": self.system + " " + text}],
                messages = self.messages,
                system = self.system,
                max_tokens=300,
            )
        except:
            self.messages.pop()
            raise
        # we must not miss to record the response 
        self.messages.append({"role":"assistant","content":response.text})
        return response.text
