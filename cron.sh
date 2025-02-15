#!/bin/bash

# Remove all current cron jobs for the user
crontab -r

# Generate a random hour between 8 and 20
RANDOM_HOUR=$((RANDOM % 13 + 8))
RANDOM_MINUTE=$((RANDOM % 60))

# Define the task to run
TASK="cd /opt/soixam/ && ./git.sh"

# Add the new cron job
( crontab -l 2>/dev/null; echo "$RANDOM_MINUTE $RANDOM_HOUR * * * $TASK" ) | crontab -

echo "New cron job set at $RANDOM_HOUR:$RANDOM_MINUTE for task: $TASK"
