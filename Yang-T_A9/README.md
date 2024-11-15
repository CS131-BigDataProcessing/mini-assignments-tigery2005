Adding cron jobs
- open the crontab using command: crontab -e
- copy paste the following cronjobs into the crontab
- save and quit using :wq

	0 3 * * 0 /Users/tiger/mini-assignments-tigery2005/Yang-T_A9/backup.sh
	0 2 * * * rm -rf /Users/tiger/mini-assignments-tigery2005/Yang-T_A9/temp/*
	30 8 * * * df -h | mail -s "Daily Disk Usage Report" tigeryang2005@gmail.com

What do these cron jobs do?
- Every Sunday at 3:00 AM, schedule a backup using tar compression and store it
- Everyday at 2:00 AM delete files in a temp directory
- Everyday at 8:30 AM, send me an email reporting disk usage
