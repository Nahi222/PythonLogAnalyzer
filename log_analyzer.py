# log analyzer.py
from collections import defaultdict
import re
# Open the auth.log file in read mode

ip_counts = defaultdict(int)
with open("fake_auth.log", "r") as log_file:
	for line in log_file:
		if "Failed password" in line:
		#Extract ip address
			ip_match = re.search(r" from (\d+\.\d+\.\d+\.\d+)",line)
			ip = ip_match.group(1) if ip_match else "Unknown IP"
			ip_counts[ip] +=1

		#Extract username
			user_match = re.search(r"for (invalid user )?(\w+)",line)
			user = user_match.group(2) if user_match else "Unknown User"

		#Extract timestamp
			timestamp = line[:15]

			print(f"[!] Failed login detected:")
			print (f" Time 	: {timestamp}")
			print (f" Username : {user}")
			print (f" IP Addr :{ip}")
			print ("-" * 40)
			print("\n=== Failed Login Summary ===")
for ip, count in sorted(ip_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{ip} → {count} failed attempts")
