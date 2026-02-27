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
