# Change to git_test directory
cd /home/aubrey/Desktop/git_test 

# Activate virtual environment
source .venv/bin/activate

# Process log file
python3 test.py

# Synchronize with GitHub repository
git pull
git add .
git commit -m 'added by process_speedtest_log.sh'
git push
