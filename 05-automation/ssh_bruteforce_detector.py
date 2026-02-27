import re
from collections import Counter
from datetime import datetime

log_file = "../01-linux-fundamentals/auth.log"
threshold = 5

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
    
    if count >= threshold:
        print("⚠ ALERT: Potential Brute Force Attack Detected!")
        
        # Simulated IP Blocking
        print(f"🚫 Simulating firewall block for IP: {ip}")
        
        # Simulated Email Alert
        send_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print("\n📧 Simulated Email Alert Sent")
        print("To: soc_team@company.com")
        print("Subject: High Severity Alert - SSH Brute Force Detected")
        print(f"Time: {send_time}")
        print(f"Details: {ip} exceeded {threshold} failed login attempts.\n")
