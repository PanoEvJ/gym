import json
from dataclasses import dataclass, field

from fastapi import FastAPI, HTTPException, Request, Response

app = FastAPI()


@dataclass
class Channel:
    id: str
    name: str
    description: str
    tags: list[str] = field(default_factory=list)


channels: dict[str, Channel] = {}

with open("channels.json", encoding="utf-8") as file:
    channels_list = json.load(file)
    for channel_raw in channels_list:
        channel = Channel(**channel_raw)
        channels[channel.id] = channel


@app.get("/")
def read_root() -> Response:
    return Response("The server is running")


print(channels)
