# Index
Welcome to the unofficial MRT Rest API!
This API is written in python and fully open source. It can retrieve the position of players,
their usernames, etc. It utilizes the dynmap.

## GET /
Responds with the name of the project and version.

## GET /players
Responds with an array of Player (see below) objects.

## GET /players/{username}
Responds with a Player object or 404 if it's not found.

## GET /info
Responds with the current Info (see below) of the server.

# Schemas

## Info
| Name | Description |
| ---- | ----------- |
| latency `float` | The latency of the server. |
| players `int` | The amount of players. |
| motd `str` | The MOTD of the server. |
| software `str` | The software of the server, usually `Paper`. |
| plugins `Array of strings` | The plugins on the server. |
| version `str` | The current version of the server. |

## Player
| Name | Description |
| ---- | ----------- |
| username `str` | The username of the player. |
| x `float` | The X position of the player. |
| y `float` | The Y position of the player. |
| z `float` | The Z position of the player. |
| world `str` | The world the player is in. |

