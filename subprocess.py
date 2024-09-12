import subprocess

# This will run 'other_script.py' simultaneously
subprocess.Popen(['python', 'main.py', "--config"])

# Your main script continues to run
print("Main script is running...")
