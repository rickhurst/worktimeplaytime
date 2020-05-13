# Worktime Playtime

A python script and ansible playbooks to help me manage procrastination by blocking commonly visited websites in my host file

Triggered by root cron at the start and end of each working day e.g.:-

``` python worktimeplaytime.py worktime ```

``` python worktimeplaytime.py playtime ```

Can be disabled by placing a textfile in my home folder e.g. /Users/rickhurst/worktimeplaytime.txt with `ignore` as the content
