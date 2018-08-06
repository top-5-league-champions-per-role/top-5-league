#!/bin/bash

# Check the number of arguments ($#)
# If it is equal (-eq) to 0, then exit
if [[ $# -eq 0 ]]
	then
		echo "No arguments supplied to the script. Sample usage:"
		echo "./push_to_git.sh \"Your commit message here\""
		echo "NOTE: Please remember to include the quotes!"
		exit 1
fi

COMMIT_MSG=$1  # save the commit messages to this variable

git pull
git add *
git status
git commit -a -m "$COMMIT_MSG"
git push
