import re
from collections import Counter

log_file = "../01-linux-fundamentals/auth.log"

failed_attempts = []

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
            if match:
                failed_attempts.append(match.group(1))

ip_counts = Counter(failed_attempts)

print("=== SSH Brute Force Detection Report ===\n")

for ip, count in ip_counts.items():
    print(f"IP Address: {ip} | Failed Attempts: {count}")
    
    if count >= 5:
        print("⚠ ALERT: Potential Brute Force Attack Detected!\n")
