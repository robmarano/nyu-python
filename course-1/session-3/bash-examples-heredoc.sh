#!/usr/bin/env bash

export RUN_USER="ubuntu"
export RUNUSER_PROG="/sbin/runuser"
#export COMMAND="echo $USER"

export COMMAND="echo $USER ; echo $HOME ; cd /tmp ; echo $PWD"
sudo ${RUNUSER_PROG} -l ${RUN_USER} -c "${COMMAND}"

export COMMAND="echo $USER; \
echo $HOME; \
cd /tmp; \
echo $PWD"
sudo ${RUNUSER_PROG} -l ${RUN_USER} -c "${COMMAND}"

export COMMAND=$(cat <<-'HERE1a'
	echo $USER
	echo $HOME
	cd /tmp
	echo $PWD
HERE1a
)
sudo ${RUNUSER_PROG} -l ${RUN_USER} -c "${COMMAND}"

