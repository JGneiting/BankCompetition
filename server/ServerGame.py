import time
from server.ServerPlayer import ServerPlayer
from src.player import Player
from src.game import Game
import server
import json
from src.gamestate import GameStateENCODER


class ServerRoom:
    def __init__(self):
        self.players = {}
        self.game = None

    def add_player(self, id_, name):
        self.players[id_] = ServerPlayer(id_, name)

    def remove_player(self, id_):
        del self.players[id_]

    def message_received(self, id_, message):
        self.game.server_room[id_].save_response(message)

    def launch_game(self):
        self.game = ServerGame(self.players)


class ServerGame(Game):
    def __init__(self, players: dict):
        self.server_room = players
        super().__init__(20, list(players.values()))

    def all_banked(self):
        return all(player.banked for player in self.state.players)

    def wait_for_responses(self):
        while not all(player.responded for player in self.state.players):
            time.sleep(0.1)

    def clear_responded(self):
        for player in self.state.players:
            player.responded = False

    def end(self):
        server.socketio.emit("end", f"Game over! {self.state.get_results()}")

    def poll(self):
        if self.all_banked():
            self.state.next_round()
            return
        self.clear_responded()
        server.socketio.emit("poll", json.dumps(self.state, cls=GameStateENCODER))
        self.wait_for_responses()
        if "True" in [player.response for player in self.state.players]:
            self.poll()
