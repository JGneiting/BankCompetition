from bankcompetition.src.bankcompetition.entry import Entry
import asyncio
import socketio
from bankcompetition.src.bankcompetition.gamestate import GameState


class ServerEntry(Entry):

    def __init__(self, name: str, server='https://bakerbot3000.com'):
        super().__init__(name)
        self.server = server
        self.run_game = True
        self.sio = socketio.AsyncClient()
        self.sio.on('response')(self.handle_response)
        self.sio.on('poll')(self.handle_poll)
        self.sio.on('end')(self.disconnect)

    async def connect(self):
        await self.sio.connect(self.server, transports='websocket')

    def start(self):
        print("starting")
        asyncio.run(self.run())

    async def run(self):
        print("Running")
        await self.connect()
        print("connected")
        await self.sio.emit('agent_info', f"{self.name}")
        while self.run_game:
            await asyncio.sleep(0.01)

    async def handle_response(self, message):
        print(message)

    async def handle_poll(self, message):
        state = GameState(gamestate_json=message)
        print(state)
        response = self.bank(state)
        if response == True:
            response = "True"
        else:
            response = "False"
        await self.sio.emit('poll-response', response)

    async def disconnect(self, message=""):
        print(message)
        self.run_game = False
        await self.sio.disconnect()

    """
    :type gamestate: GameState
    :rtype: bool
    """
    def bank(self, gamestate: GameState) -> bool:
        return True
        

if __name__ == "__main__":
    entry = ServerEntry("Server")
    asyncio.run(entry.run())
