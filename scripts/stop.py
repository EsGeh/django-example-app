#!/usr/bin/env python3

from utils.settings import BASE_DIR, load_config

import subprocess
import os


def stop( env ):
    # run application
    subprocess.call(
        "docker-compose down",
        shell=True,
        env=env
    )

if __name__ == '__main__':

    from argparse import ArgumentParser

    config = load_config()

    parser = ArgumentParser(
        description="stop the webserver"
    )
    args = parser.parse_args()

    stop( config )
