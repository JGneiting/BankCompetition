import logging
from abc import ABC
from src.entry import Entry
import asyncio
import socketio
from src.gamestate import GameState
import ssl


class ServerEntry(Entry):

    def __init__(self, name: str, server='https://bakerbot3000.com'):
        super().__init__(name)
        self.server = server
        self.sio = socketio.AsyncClient()
        self.sio.on('response')(self.handle_response)
        self.sio.on('poll')(self.handle_poll)
        self.sio.on('agent_info')(self.handle_info)

    async def connect(self):
        await self.sio.connect(self.server, transports='websocket')

    async def run(self):
        await self.connect()
        await self.sio.emit('message', 'Hello server!')
        await asyncio.sleep(1)
        await self.sio.emit('message', 'Hello server x2!')
        await asyncio.sleep(1)
        await self.disconnect()

    async def handle_response(self, message):
        print(message)

    async def handle_info(self, message):
        print(message)
        await self.sio.emit('agent_info', f"{self.name}")

    async def handle_poll(self, message):
        state = GameState(gamestate_json=message)
        response = self.bank(state)
        await self.sio.emit('poll-response', response)

    async def disconnect(self):
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
