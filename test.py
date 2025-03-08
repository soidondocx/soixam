import subprocess
import random
from datetime import datetime

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")

# Define a list of 100 commit messages
commit_messages = [
    "Updated data for today 📅", "Routine update 🚀", "Daily sync 🔄", "Code improvements 🛠️",
    "Minor fixes & updates ✅", "Keeping things fresh 🍃", "Refactoring some code ✨", "Performance improvements ⚡",
    "Optimized workflow 🔧", "Bug fixes and tweaks 🐛", f"Daily update for {current_date} 📌",
    "General maintenance 🏗️", "Enhancements and fixes 🎯", "Polishing the codebase 🔍", "Updated dependencies 📦",
    "Improved stability 🔥", "Cleaning up old files 🗑️", "More efficient code 🚀", "Auto-generated update 🤖",
    "Housekeeping 🏠", "Documentation improvements 📖", "Fixed minor issues 🩹", "Code cleanup 🧹",
    "Enhanced security 🔐", "Reducing technical debt 💰", "Automated commit 🎯", "Tuning performance 🎶",
    "Small tweaks ✏️", "Fixed typo errors ✍️", "Reformatted code structure 🏗️", "Added new features 🌟",
    "Refined existing logic 🔄", "Better exception handling ⚠️", "UI/UX improvements 🎨", "Streamlining processes 🔄",
    "Corrected syntax issues 🚦", "Testing updates 🧪", "Bug squashing session 🦟", "Increased efficiency 💡",
    "Linting and formatting 🌿", "Configuration changes ⚙️", "Code refactor for clarity 📝", "Patching vulnerabilities 🛡️",
    "Database optimizations 🗄️", "Better logging and debugging 📊", "Improved error handling 🔍", "Updated README 📜",
    "More robust validation checks ✅", "Adjusted styles for consistency 🎭", "Project restructuring 🏗️",
    "Enhanced load times 🚀", "Added meaningful comments 💬", "Fixed layout alignment 📏", "Security patches applied 🛠️",
    "Improved API response times ⚡", "Better input sanitization 🧼", "Performance tweaks 🏎️", "Reduced unnecessary calls 📉",
    "Better user authentication 🔐", "Enhanced accessibility features ♿", "Reduced redundant code 🗑️",
    "Making the codebase cleaner 🚿", "Ensuring backward compatibility 🔄", "Making things more efficient 🔥",
    "Upgrading libraries and dependencies 📦", "Simplified logic for readability 🧠", "Fixed broken links 🔗",
    "Automated testing enhancements 🧪", "Deploying minor updates 🚀", "Updated config files 🛠️",
    "Updated localization files 🌍", "Data migration completed 📊", "Version bump 🚀", "Fine-tuning background processes 🎶",
    "Cron job updates ⏳", "Fixed caching issues 🔥", "Updated build scripts ⚙️", "Fixed pipeline failures 🏗️",
    "Testing CI/CD pipelines 🔄", "Backend enhancements 🏗️", "Frontend polish 🎨", "Integrating feedback 💬",
    "Enhancing developer experience 🧑‍💻", "Stability improvements 🏋️", "Preparing for next release 🚀",
    "Optimizing database queries 📊", "Fixed critical bug 🛠️", "Code consistency improvements 📖",
    "Handling edge cases better 🌊", "Cleaning up temporary files 🗑️", "Adjusting permissions settings 🔑",
    "API response optimizations 🔄", "Adding more tests ✅", "Refactoring async functions ⏳",
    "Documenting new changes 📄", "Fixing deployment issues 🚀", "Fixing startup issues 🔄", "Fixing logs verbosity 📊",
    "Bringing more stability 🔧", "Testing environment tweaks ⚡", "Squashed a pesky bug 🐞", "Daily maintenance 🌅"
]

# Select a random commit message
commit_message = random.choice(commit_messages)

# Write the current date to git_log.txt
with open("git_log.txt", "a") as log_file:
    log_file.write(f"{current_date}: {commit_message}\n")

# Git commands to add, commit, and push
commands = [
    "git add -f .",
    f'git commit -m "{commit_message}"',
    "git push"
]

# Execute Git commands
for cmd in commands:
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ Success: {cmd}\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {cmd}\n{e.stderr}")

