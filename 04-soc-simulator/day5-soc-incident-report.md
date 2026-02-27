# Day 5 — SOC Incident Report

## Incident Summary

On February 26, 2026, multiple failed SSH login attempts were detected targeting the root account on a Linux server.

## Alert Details

- Log Source: /var/log/auth.log
- Event Type: SSH Brute Force Attempt
- Target Account: root
- Source IP: 192.168.1.10
- Port: 22

## Evidence

Example log entries:

Failed password for root from 192.168.1.10 port 22 ssh2

Multiple repeated attempts were observed from the same IP address.

## Investigation Steps

1. Reviewed authentication logs.
2. Filtered failed login attempts using grep.
3. Identified repeated login attempts from a single IP.
4. Confirmed attack pattern consistent with brute force behavior.

## Impact Assessment

- No successful login detected.
- Attack was unsuccessful.
- System integrity not compromised.

## Mitigation Recommendations

- Disable root SSH login.
- Implement Fail2Ban.
- Enforce key-based authentication.
- Monitor repeated failed login attempts.

## Conclusion

This incident was identified as a brute force SSH attack attempt. 
The attack was unsuccessful, and mitigation measures are recommended to prevent future attempts.
