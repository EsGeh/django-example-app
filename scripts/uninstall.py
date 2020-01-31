#!/usr/bin/env python3

from utils.settings import BASE_DIR, load_config, create_docker_env_file

from pathlib import Path
import shutil
import os


def rm_dirs( config ):
    path = Path( BASE_DIR, config['RUNTIME_DIR'] )
    print( "removing dir '{}'".format( path ) )
    shutil.rmtree(
        path,
        ignore_errors=True
    )

def rm_docker_env_file( config ):
    path = Path(
        BASE_DIR / ".env"
    )
    print( "removing '{}'".format( path ) )
    path.unlink()


if __name__ == '__main__':

    from argparse import ArgumentParser

    create_docker_env_file( overwrite = False )
    config = load_config()

    parser = ArgumentParser(
        description="clean up the repository: remove xml database, remove sql database"
    )
    args = parser.parse_args()

    from stop import stop

    stop( config )

    rm_dirs( config )
    rm_docker_env_file( config )
