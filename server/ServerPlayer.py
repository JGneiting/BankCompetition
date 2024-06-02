from src.player import Player


class ServerPlayer(Player):
    def __init__(self, id_, name):
        super().__init__(name)
        self.id = id_
        self.response = ""
        self.responded = False

    def save_response(self, response):
        if not self.is_banked:
            self.response = response
        self.responded = True
