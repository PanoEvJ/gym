import json
from dataclasses import dataclass, field

import uvicorn
from fastapi import FastAPI, HTTPException, Response

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
    return Response("The server is running!")


@app.get("/channels/{channel_id}", response_model=Channel)
def read_channel(channel_id: str) -> Channel:
    channel = channels.get(channel_id)
    if channel is None:
        raise HTTPException(status_code=404, detail="Channel not found")
    return channel


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
