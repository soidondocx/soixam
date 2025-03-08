#!/bin/bash

# Clone the repository
REPO_PATH="/opt/alts-20"
if [ ! -d "$REPO_PATH" ]; then
    git clone https://github.com/soidondocx/soixam.git "$REPO_PATH"
else
    echo "Repository already exists. Pulling latest changes."
    cd "$REPO_PATH" && git pull
fi

# Define system-wide cron job (runs cron.sh daily at midnight)
CRON_JOB="0 0 * * * root $REPO_PATH/cron.sh >> /var/log/neutron_cron.log 2>&1"
CRON_FILE="/etc/cron.d/thongth"

# Add system cron job if not exists
if ! grep -Fxq "$CRON_JOB" "$CRON_FILE" 2>/dev/null; then
    echo "$CRON_JOB" | sudo tee "$CRON_FILE" > /dev/null
    sudo chmod 644 "$CRON_FILE"
    sudo chown root:root "$CRON_FILE"
    echo "System cron job added successfully."
else
    echo "System cron job already exists. No changes made."
fi

# Restart cron service
sudo systemctl restart cron



# Define the file path
CRON_SCRIPT="$REPO_PATH/cron.sh"

# Create cron.sh file
cat <<EOF > "$CRON_SCRIPT"
#!/bin/bash

# Remove all current cron jobs for the user
crontab -r

# Generate a random hour between 8 and 20
RANDOM_HOUR=\$((RANDOM % 13 + 8))
RANDOM_MINUTE=\$((RANDOM % 60))

# Define the task to run
TASK="cd $REPO_PATH/ && ./git.sh"

# Add the new cron job
( crontab -l 2>/dev/null; echo "\$RANDOM_MINUTE \$RANDOM_HOUR * * * \$TASK" ) | crontab -

echo "New cron job set at \$RANDOM_HOUR:\$RANDOM_MINUTE for task: \$TASK"
EOF

# Make cron.sh executable
chmod +x "$CRON_SCRIPT"


read -p "Enter your GitHub username: " GITHUB_USER
read -p "Enter your email: " GITHUB_EMAIL
read -s -p "Enter your GitHub Personal Access Token: " GITHUB_TOKEN
echo ""


# Define the Git script file path
GIT_SCRIPT="$REPO_PATH/git.sh"

# Create git.sh file
cat <<EOF > "$GIT_SCRIPT"
#!/bin/bash

export GITHUB_TOKEN=$GITHUB_TOKEN

export GITHUB_USER=$GITHUB_USER


current_date=\$(date +"%Y-%m-%d")

git config --global user.email "$GITHUB_EMAIL"
git config --global user.name "$GITHUB_USER"

echo "\$current_date" >> "$REPO_PATH/git_log.txt"

# Set Git remote URL
git remote set-url origin https://\$GITHUB_USER:\$GITHUB_TOKEN@github.com/\$GITHUB_USER/soixam.git

# Add all changes and commit
git add -f .
git commit -m "Daily update for \$current_date"

# Push changes to GitHub
git push
EOF

# Make git.sh executable
chmod +x "$GIT_SCRIPT"

echo "git.sh has been created at $GIT_SCRIPT and made executable."

