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

@router.get("/players/{username}")
async def players_get(request: web.BaseRequest):
    url = f"{config['dyn_url']}/standalone/dynmap_new.json"

    resp = await request_json(url)
    username = request.match_info['username']
    raw_players = resp['players']

    players = [Player(DynmapPlayer(d)) for d in raw_players] # Not just DynmapPlayer cuz we need the dict

    print(username)
    for p in players:
        if p.username == username:
            return json_response(p.dict)
    
    return web.Response(status=404)

app.add_routes(router)
web.run_app(app)