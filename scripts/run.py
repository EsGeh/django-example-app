#!/usr/bin/env python3


from stop import stop

from utils.settings import BASE_DIR, load_config
from utils.functions import run
from pathlib import Path
import shutil


def copy_dir(src, dst):
    print( "'{}' -> '{}'".format( src, dst ) )
    if Path(dst).exists():
        shutil.rmtree(
            dst
        )
    shutil.copytree(
            src=src,
            dst=dst
    )

if __name__ == '__main__':

    from argparse import ArgumentParser

    config = load_config()

    parser = ArgumentParser(
        description="run the webserver"
    )
    parser.add_argument(
        "--build",
        action = "store_true"
    )
    parser.add_argument(
        "CMD",
        nargs="*"
    )
    args = parser.parse_args()

    stop(
            env = config
    )

    CMD= vars(args)['CMD']
    run(
        env=config,
        build = args.build,
        cmd=CMD
    )
