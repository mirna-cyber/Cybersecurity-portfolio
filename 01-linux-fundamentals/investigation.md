# SSH Brute Force Investigation

## Summary
Analysis of auth.log revealed multiple failed SSH login attempts.

## Key Findings
- Repeated failed logins detected
- External IP 203.0.113.5 performed multiple attempts
- Pattern consistent with SSH brute force activity
- One successful login observed for user mirna

## Risk Assessment
HIGH — External brute force activity detected.

## Recommended Actions
- Block offending IP at firewall
- Enable fail2ban
- Enforce strong password policy
- Consider SSH key authentication

## Tools Used
- grep
- awk
- sort
- uniq
