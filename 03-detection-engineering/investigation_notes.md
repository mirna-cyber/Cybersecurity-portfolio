# Day 3 — Brute Force Detection

## Objective
Detect possible SSH brute-force attacks from auth.log.

## Method
Used grep, awk, sort, and uniq to identify repeated failed login attempts.

## Findings
The IP address 192.168.1.10 generated the highest number of failed SSH login attempts, indicating potencial brute-force activity.

## Conclusion
Analysis of the auth.log file revealed repeated failed SSH login attempts originating from IP address 192.168.1.10. The pattern of activity is consistent with potential brute-force attack. It is recommended to monitor this IP, implement account lockout polocies, and consider blocking the source if the activity persists.
