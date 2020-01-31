from pathlib import Path
from configparser import ConfigParser, ExtendedInterpolation

from collections.abc import MutableMapping
import shlex
import os

BASE_DIR = Path( __file__ ).parent.parent.parent
SCRIPT_DIR = Path( __file__ ).parent.parent

orig_config_file = SCRIPT_DIR / "config" / "default_env.conf"
env_file = BASE_DIR / ".env"


def load_config(
    include_local_path=True
):
    from itertools import chain
    parser = ConfigParser()
    parser.optionxform=str
    with open(env_file) as lines:
        lines = chain(("[config]",), lines)  # This line does the trick.
        parser.read_file(lines)
    print( "Loaded from {}:".format( env_file ) )
    for k,v in parser['config'].items() :
        print( "{k}={v}".format( k = k, v = v ) )
    print( "------------------------------" )
    config = dict(parser['config'])
    if include_local_path:
        path = os.environ['PATH']
        config = { "PATH": path, ** config }
    return config

def create_docker_env_file(
        overwrite = False
):
    if overwrite or not env_file.exists():
        import subprocess
        user = subprocess.check_output(
                shlex.split("id -u"),
                universal_newlines=True
            ).rstrip("\n")
        group = subprocess.check_output(
                shlex.split("id -g"),
                universal_newlines=True
            ).rstrip("\n")

        print( "user id: {}, group id: {}".format( user, group) )
        print( "writing docker .env file to {}, appended user and group".format( env_file ) )
        config = __load_orig_config( orig_config_file )
        config['config']['USER'] = user
        config['config']['GROUP'] = group
        __write_as_env(
            config,
            env_file 
        )

def __load_orig_config( filename ):
    config = ConfigParser(
        interpolation = ExtendedInterpolation()
    )
    # make keys case sensitive
    config.optionxform=str
    # print( "path: %s" % orig_config_file )
    config.read( orig_config_file )
    print( "Loaded from '{}':".format( orig_config_file ) )
    for k,v in config['config'].items() :
        print( "{k}={v}".format( k = k, v = v ) )
    print( "------------------------------" )
    return config


def __write_as_env( cfg, filename ):
    # create a new config parser with the right output options:
    # and copy the fields into it:
    config = ConfigParser()
    config.optionxform=str
    config['config'] = {}
    for k, v in cfg.items('config'):
        config['config'][k] = v
    # write the file:
    with open(filename, "w") as f:
        config.write(
            f,
            space_around_delimiters=False
         )
    # skip the section header '[ bla ]'
    with open( filename, "r+" ) as f:
        d = f.readlines()
        f.seek(0)
        for l in d[1:]:
            f.write(l)
        f.truncate()
