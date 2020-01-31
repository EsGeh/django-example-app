#!/usr/bin/env python3

from utils.settings import BASE_DIR, load_config, create_docker_env_file
from utils.functions import exec_in_container, run
from stop import stop

from pathlib import Path
import shlex
import shutil
import pwd
import os
import subprocess
from time import sleep

BASE_DIR = Path( __file__ ).parent.parent
DEP_DIR = BASE_DIR / "dependencies"


SQLDB_WAIT_TIME=20

def create_dir(dir):
    print( "creating dir '{}'".format( dir ) )
    Path(dir).mkdir(
            parents = True,
            exist_ok = True
    )

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

def create_dirs( config ):
    create_dir(
        BASE_DIR / config['DATABASE_DATA_DIR']
    )

    """
    this extra copy is necessary in order to
    resolve symlinks. Docker won't resolve
    them.
    """
    copy_dir(
        src=config['RES_DIR'],
        dst=config['RES_DIR_RUNTIME']
    )

def init_sqldb( config ):
    # print( "env in config:" )
    # subprocess.check_call(
    #     ["env",],
    #     env=config
    # )

    try:
        subprocess.check_call(
            ["docker-compose", "up", "-d"],
            env=config
        )

        print( "wait {}s for the sql database to get ready... :-P".format( SQLDB_WAIT_TIME ) )
        sleep( SQLDB_WAIT_TIME )

        exec_in_container(
            "python", "manage.py", "makemigrations",
            env=config,
        )
        exec_in_container(
            "python", "manage.py", "migrate",
            env=config,
        )

    finally:
        subprocess.check_call(
            ["docker-compose", "down"],
            env=config,
        )


if __name__ == '__main__':

    from argparse import ArgumentParser

    parser = ArgumentParser(
        description="initialize the repository: create directories, initialize xml database, initialize sql database"
    )
    parser.add_argument(
        "--build",
        action = "store_true",
        help = "rebuild docker image from Dockerfile",
    )
    args = parser.parse_args()

    # orig_config_file -> env_file:
    create_docker_env_file()

    # load env_file:
    config = load_config()

    create_dirs( config )

    # rebuild docker image:
    if args.build:
        run(
            env = config,
            build = True,
        )
        stop(
            env = config,
        )

    init_sqldb( config )
