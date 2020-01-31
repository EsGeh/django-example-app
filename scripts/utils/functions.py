

import subprocess
import shlex

def run(
        env,
        build=False,
        cmd=[]
):
    if len(cmd) > 0:
        # run application
        subprocess.call(
            shlex.split("docker-compose run webserver") + cmd,
            env=env
        )
    else:
        # run application
        subprocess.call(
            shlex.split("docker-compose up -d") + (["--build"] if build else []),
            env=env
        )

def exec_in_container(
    *args,
    env=None
):
    from functools import reduce
    cmd = \
        [ "docker-compose", "exec", "webserver", "bash" ]

    if len(args) != 0:
        cmd.append( "-c" )
        cmd.append(
            reduce(lambda x,y: x + " " + y, args )
        )
    print( "cmd: " + str(cmd) )
    subprocess.check_call(
        cmd,
        env=env
    )
