from enum import Enum
import re

from os import path
from typing import List, Optional

from twitchdl import twitch, utils
from twitchdl.commands.download import get_clip_authenticated_url
from twitchdl.download import download_file
from twitchdl.logging import logger

class Period(Enum):
    LAST_DAY = 1,
    LAST_WEEK = 2,
    LAST_MONTH = 3,
    ALL_TIME = 4


def clips(
        channel_name: str,
        period: Optional[Period] = Period.ALL_TIME,
        limit: Optional[int] = 10,
        download: Optional[bool] = False
) -> List[str]:
    generator = twitch.channel_clips_generator(channel_name, period, limit)

    if download:
        return _download_clips(generator)

    return list(generator)

def _target_filename(clip):
    url = clip["videoQualities"][0]["sourceURL"]
    _, ext = path.splitext(url)
    ext = ext.lstrip(".")

    match = re.search(r"^(\d{4})-(\d{2})-(\d{2})T", clip["createdAt"])
    date = "".join(match.groups())

    name = "_".join([
        date,
        clip["id"],
        clip["broadcaster"]["login"],
        utils.slugify(clip["title"]),
    ])

    return "{}.{}".format(name, ext)


def _download_clips(generator):
    for clip in generator:
        target = _target_filename(clip)

        if path.exists(target):
            logger.info("Already downloaded: {}".format(target))
        else:
            url = get_clip_authenticated_url(clip["slug"], "source")
            logger.info("Downloading: {}".format(target))
            download_file(url, target)
