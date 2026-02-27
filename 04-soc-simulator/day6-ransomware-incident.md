# Day 6 — SOC Simulation: Ransomware Incident

## Incident Overview

On February 26, 2026, a high-severity security alert was triggered indicating potential ransomware activity on a Linux server.

---

## Alert Details

- Alert Name: Suspicious File Encryption Activity
- Severity: High
- Affected Host: Linux-Server-01
- Detection Source: Endpoint Security Monitoring
- Time Detected: 10:14 AM

---

## Incident Timeline

| Time       | Event Description |
|------------|-------------------|
| 10:12 AM   | User downloaded suspicious file from unknown source |
| 10:13 AM   | Unusual file modification activity detected |
| 10:14 AM   | Multiple files renamed with .encrypted extension |
| 10:14 AM   | Security alert triggered |
| 10:16 AM   | SOC analyst began investigation |
| 10:20 AM   | Host isolated from network |

---

## Indicators of Compromise (IOCs)

- Multiple files renamed with `.encrypted`
- High CPU usage
- Rapid file modification activity
- Suspicious process execution

---

## Investigation Actions

1. Verified alert in monitoring dashboard.
2. Checked running processes.
3. Reviewed file changes.
4. Disconnected host from network.
5. Began forensic image collection.

---

## Impact Assessment

- Several user files encrypted.
- No evidence of lateral movement.
- Containment successful.

---

## Mitigation & Recovery

- Isolated infected host.
- Restored files from backup.
- Reset user credentials.
- Implemented stricter download restrictions.
- Scheduled full malware scan.

---

## Conclusion

The incident was identified as a simulated ransomware attack. 
Rapid detection and response limited impact and prevented further system compromise.
