#!/usr/bin/env python3

from utils.settings import BASE_DIR, load_config
from utils.functions import exec_in_container

from pathlib import Path
import os

if __name__ == '__main__':

    from argparse import ArgumentParser

    config = load_config()

    parser = ArgumentParser(
        description="open bash to the container, optionally exec CMD there"
    )
    parser.add_argument(
        "CMD",
        nargs='*',
    )
    args = parser.parse_args()

    CMDS= \
        (vars(args)['CMD'])

    print( CMDS )

    exec_in_container( 
        *CMDS,
        env=config
    )
