# Change to the direstory where the log file will be stored
cd /home/aubrey/Desktop/git_test/logs

# Create file name for the log file
today=$(date '+%Y-%m-%d')
echo $today
logfile=${today}.log
echo $logfile
 
# Create timestamp
timestamp=$(date +'%Y-%m-%dT%H:%M:%S%:z')
echo $timestamp

# Append timestamp to the log file
echo $timestamp >> $logfile

# Run speedtest and append results to log file
speedtest >> $logfile