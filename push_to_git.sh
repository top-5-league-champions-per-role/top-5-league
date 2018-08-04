#!/bin/bash

# -z switch will test the expansion of "$1" string
# Basically, it will check if the "$1" expansion is a null string or not
if [ -z "$1"]
	then
		echo "No arguments supplied to the script. Sample usage:"
		echo "./push_to_git.sh \"Your commit message here\""
		echo "NOTE: Please remember to include the quotes!"
		exit 1
fi

echo "*args: " $1

git pull
git status
git add *
git status
git commit -m $1
git push
