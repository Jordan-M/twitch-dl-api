import json
import m3u8

from twitchdl import utils, twitch
from twitchdl.exceptions import ConsoleError
from twitchdl.logging import logger

def info(video: str):
    video_id = utils.parse_video_identifier(video)
    if video_id:
        logger.info("Fetching video...")
        video = twitch.get_video(video_id)

        if not video:
            raise ConsoleError("Video {} not found".format(video_id))

        logger.info("Fetching access token...")
        access_token = twitch.get_access_token(video_id)

        logger.info("Fetching playlists...")
        playlists = twitch.get_playlists(video_id, access_token)

        logger.info("Fetching chapters...")
        chapters = twitch.get_video_chapters(video_id)

        return video_json(video, playlists, chapters)

    clip_slug = utils.parse_clip_identifier(video)
    if clip_slug:
        logger.info("Fetching clip...")
        clip = twitch.get_clip(clip_slug)
        if not clip:
            raise ConsoleError("Clip {} not found".format(clip_slug))
        
        return json.dumps(clip)

    raise ConsoleError("Invalid input: {}".format(video))

def video_json(video, playlists, chapters):
    playlists = m3u8.loads(playlists).playlists

    video["playlists"] = [
        {
            "bandwidth": p.stream_info.bandwidth,
            "resolution": p.stream_info.resolution,
            "codecs": p.stream_info.codecs,
            "video": p.stream_info.video,
            "uri": p.uri
        } for p in playlists
    ]

    video["chapters"] = chapters

    return video
