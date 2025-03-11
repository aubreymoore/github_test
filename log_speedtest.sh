cd /home/aubrey/Desktop/git_test/logs
today=$(date '+%Y-%m-%d')
echo $today
timestamp=$(date +'%Y-%m-%dT%H:%M:%S%:z')
echo $timestamp
logfile=${today}.log
echo $logfile
echo $timestamp >>$logfile
speedtest >>$logfile