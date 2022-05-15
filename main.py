import aiohttp
from aiohttp import web

from dataclass import *
from util import *

app = web.Application()
router = web.RouteTableDef()

with open('config.json') as file:
    config = json.load(file)

@router.get("/")
async def req(request: web.BaseRequest):
    return json_response({
        "version": config['version'],
        "name": config['name']
    })

@router.get("/players")
async def players(request: web.BaseRequest):
    url = f"{config['dyn_url']}/standalone/dynmap_new.json"

    resp = await request_json(url)
    raw_players = resp['players']

    players = [Player(DynmapPlayer(d)) for d in raw_players]
    player_data = [p.dict for p in players]

    return json_response(player_data)
    

app.add_routes(router)
web.run_app(app)