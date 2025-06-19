class ChatMemory:
    def __init__(self, window_size=5):
        self.window_size=window_size
        self.history=[]

    def add_turn(self, user_input, bot_response):
        self.history.append(f"User: {user_input}\nBot: {bot_response}")
        if len(self.history) > self.window_size:
            self.history.pop(0)

    def get_context(self):
        return "\n\n".join(self.history)