# Day 4 — SQL Injection Investigation

## Objective
Identify possible SQL injection attempts in web server logs.

## Method
Analyzed access.log using grep to detect suspicious query patterns such as OR 1=1 and comment operators (--).

## Findings
IP address 192.168.1.25 made multiple suspicious login attempts containing SQL injection patterns.

## Risk Level
High — indicates active web attack attempt.

## Conclusion
The activity from 192.168.1.25 suggests an attempted SQL injection attack targeting the login page. Monitoring and web application firewall rules are recommended.
