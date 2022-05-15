import json
from typing import Union
from aiohttp import web


class DynmapPlayer:
    """A Dynmap player according to dynmap_new.json.

    Attributes
    ----------
    world: :class:`str`
        The world the player is in.

    armor: :class:`int`
        The armor the player has.

    name: :class:`str`
        The player's username.

    x: :class:`float`
        The X position of the player.

    y: :class:`float`
        The Y position of the player.

    z: :class:`float`
        The Z position of the player.

    """

    def __init__(self, data: dict) -> None:
        self.world: str = data["world"]
        self.armor: int = data["armor"]
        self.name: str = data["name"]
        self.x: float = data["x"]
        self.y: float = data["y"]
        self.z: float = data["z"]


class Player:
    """
    Represents an Online Player.

    Attributes
    ----------
    username: :class:`str`
        The username of the player. Retrieved from Dynmap.

    x: :class:`float`
        The X position of the player.

    y: :class:`float`
        The Y position of the player.

    z: :class:`float`
        The Z position of the player.

    dynmap: :class:`DynmapPlayer`
        The :class:`DynmapPlayer` object of the player.

    """

    def __init__(self, dynmap_user: DynmapPlayer) -> None:
        self.username = dynmap_user.name
        self.x = dynmap_user.x
        self.y = dynmap_user.y
        self.z = dynmap_user.z
        self.world = dynmap_user.world
        self.dynmap = dynmap_user

    @property
    def dict(self):
        return {
            "username": self.username,
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "world": self.world,
        }


def json_response(data: Union[list, dict]):
    return web.Response(text=json.dumps(data))
