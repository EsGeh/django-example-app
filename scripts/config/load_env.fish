#!/bin/fish

if not set -q SCRIPT_DIR
	echo "ERROR in (status -m): \$SCRIPT_DIR is undefined!"
	exit 1
end
set BASE_DIR "$SCRIPT_DIR/.."

#######################################
# actual script
#######################################

set RUNTIME_DIR "runtime_data"

###################################################
# export all these variables, so 
# they can be referenced in the docker-compose.yaml
###################################################

# convert bash syntax to fish syntax:
set commands (cat ./scripts/config/env.conf | grep -E --invert-match '^#|^[[:space:]]*$' | sed 's/^\(.*\)=\(.*\)/set -x \1 \2/' | sed 's/\$(/(/g')

for cmd in $commands
	echo "cmd: $cmd"
	eval "$cmd"
end
