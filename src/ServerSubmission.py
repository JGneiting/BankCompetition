from abc import ABC
from src.entry import Entry
import asyncio
import websockets


class ServerEntry(Entry, ABC):

    def __init__(self, name: str, server='https://bakerbot3000.com/bankcompetition/'):
        super().__init__(name)
        self.server = server
        asyncio.get_event_loop().run_until_complete(self.run_client())

    async def run_client(self):
        async with websockets.connect(self.server) as websocket:
            await websocket.send("Hello server!")
            response = await websocket.recv()
            print(response)
        
