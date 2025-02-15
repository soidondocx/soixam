#!/bin/bash


current_date=$(date +"%Y-%m-%d")


echo "$current_date" >> "/opt/soixam/git_log.txt"


# Add all changes and commit
git add -f .
git commit -m "Daily update for $current_date"

# Push changes to GitHub
git push
