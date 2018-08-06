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

# Save the commit messages to this variable
COMMIT_MSG=$1

# Pull all the changes from the repo to the local repository
git pull
# Add all changed files to the current commit
git add *
# See the current status of the local repository
git status
# Commit all changes added
git commit -a -m "$COMMIT_MSG"
# Push the committed changes to the repository
git push
