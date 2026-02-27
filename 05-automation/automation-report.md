# Automation Project — SSH Brute Force Detector

## Overview

This Python script analyzes Linux authentication logs to detect potential SSH brute force attacks.

## Features

- Parses auth.log
- Extracts IP addresses from failed login attempts
- Counts failed attempts per IP
- Triggers alert if attempts exceed threshold

## Technologies Used

- Python
- Regex
- Collections (Counter)

## Security Impact

Automating log analysis improves detection speed and reduces manual investigation time.

## Automation Enhancements

- Simulated automatic IP blocking
- Simulated SOC email alert notification
- Configurable detection threshold
- Timestamped alert reporting

This demonstrates basic Security Orchestration and Automated Response (SOAR) concepts.
