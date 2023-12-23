import sys
from typing import List, Optional
from enum import Enum

from twitchdl import twitch
from twitchdl.exceptions import ConsoleError
from twitchdl.logging import logger

class Sort(Enum):
    Time = 1,
    Views = 2

class BroadcastType(Enum):
    Archive = 1,
    Highlight = 2,
    Upload = 3

def videos(
        channel_name: str,
        type: BroadcastType = BroadcastType.Archive,
        game_name: Optional[str] = None, 
        limit: Optional[int] = 10,
        sort: Optional[Sort] = Sort.Time
    ) -> List[str]:
    game_ids = _get_game_ids(game_name)

    total_count, generator = twitch.channel_videos_generator(
        channel_name, limit, sort.name, type.name, game_ids)

    return list(generator)

def _get_game_ids(names):
    if not names:
        return []

    game_ids = []
    for name in names:
        logger.info("Looking up game '{}'...".format(name))
        game_id = twitch.get_game_id(name)
        if not game_id:
            raise ConsoleError("Game '{}' not found".format(name))
        game_ids.append(int(game_id))

    return game_ids
