Twitch Downloader API
======================

A hard fork of [twitch-dl](https://github.com/ihabunek/twitch-dl) that aims to make the code more developer friendly. 

Migration Plan
--------------
### Phase 1: Ensure all commands are able to be called programmatically (Done)

In this phase, we will leverage this existing implementations and only return data when absolutely necessary (e.g. when listing videos). The goal of phase 1 is to be able to accomplish everything you could in the CLI version by passing the CLI arguments as method arguments.

| Command  | Status   |
| -------  | ------   |
| videos   | Migrated |
| download | Migrated |
| clips    | Migrated |
| info     | Migrated |
| env      | Migrated |

### Phase 2: Clean up existing code

Once we are able to work with the commands programmatically, we will refactor the codebase. The main goal for this phase is to make sure that all method parameters and return values are all explicitly typed, adding documentation to each method, and removing methods that were specifically for CLI purposes.

### Phase 3: Write documentation
Adding documentation will be reserved for after the codebase is in a clean, stable condition. Once that point is reached, thorough documentation will be written including working examples for common scenarios.

### Phase 4: Extend the API capabilities

After the code is cleaned up and documentation is written, the final phase will be to extend some of the APIs to put more power in the hands of the developer. This will include things like returning video bytes and progress callbacks. 

If you have any suggestions for extended capabilities, please open an issue for tracking.

Resources
---------
Twitch-dl-api resources will not be written until phase 3. In the meantime, please take a look at the original twitch-dl resources or open an issue against this repo.

* [twitch-dl Documentation](https://twitch-dl.bezdomni.net/)
* [twitch-dl Source code](https://github.com/ihabunek/twitch-dl)
* [twitch-dl Issues](https://github.com/ihabunek/twitch-dl/issues)
* [twitch-dl Python package](https://pypi.org/project/twitch-dl/)

Requirements
------------

* Python 3.7 or later
* [ffmpeg](https://ffmpeg.org/download.html), installed and on the system path

Quick start
-----------

See [installation instructions](https://twitch-dl.bezdomni.net/installation.html)
to set up twitch-dl.

For more info see [the documentation](https://twitch-dl.bezdomni.net/usage.html).

License
-------

Copyright 2018-2022 Ivan Habunek <ivan@habunek.com>

Licensed under the GPLv3: http://www.gnu.org/licenses/gpl-3.0.html

Useful links for dev
--------------------

* https://supersonichub1.github.io/twitch-graphql-api/index.html
* https://github.com/SuperSonicHub1/twitch-graphql-api
