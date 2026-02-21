# Day 3 — Brute Force Detection

## Summary
Log analysis identified repeated failed login attempts targeting the root account.

## Findings
Failed password for root from 192.168.1.10 port 22 ssh2

## Risk Level
Medium — suspicious internal activity detected.

## Conclusion
The activity indicates a potential brute force attempt from an internal host. Recommend monitoring the source IP and enforcing stronger authentication controls.
