#!/bin/bash
git pull
git status
git add *
git status
git commit -m $0
#git push
echo $0