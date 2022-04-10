import random
class bot:
    def __init__(self, bot_name) -> None:
        self.bot_name = bot_name
        self.phrase = set()

    def add_phrase(self, phrase):
        self.phrase.add(phrase)

    def delete_phrase(self, phrase):
        self.phrase.discard(phrase)

    def talk(self):
        return random.choice(list(self.phrase))
