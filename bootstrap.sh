#!/usr/bin/env bash

apt-get install build-essential gcc --assume-yes
apt-get update --fix-missing
apt-get install vim git zlib1g-dev --assume-yes
apt-get install python3 --assume-yes
apt-get install python3-venv --assume-yes
apt-get install bpython --assume-yes


export RUN_USER="ubuntu"
export RUNUSER_PROG="/sbin/runuser"

export COMMAND=$(cat <<-'HERE1a'
    echo "\"echo \"in .profile\" >> $HOME/.profile\""
    echo "\"echo \"in .bashrc\" >> $HOME/.bashrc\""
HERE1a
)

${RUNUSER_PROG} -l ${RUN_USER} -c "${COMMAND}"

