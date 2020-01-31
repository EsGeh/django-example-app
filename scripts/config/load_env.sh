#!/bin/bash

if [[ "$SCRIPT_DIR" == "" ]]; then
	echo "ERROR in ./scripts/config/load_env.sh: \$SCRIPT_DIR is undefined!"
	exit 1
fi
BASE_DIR="$SCRIPT_DIR/.."

#######################################
# actual script
#######################################


# these are the default settings used by all scripts:

RUNTIME_DIR=runtime_data

###################################################
# export all these variables, so 
# they can be referenced in the docker-compose.yaml
###################################################
set -a
source $SCRIPT_DIR/config/env.conf
set -a
# (stop exporting variables)
