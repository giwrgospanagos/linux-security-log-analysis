from collections import Counter

log_file = "auth-lab.log"

failed_ips = Counter()
failed_users = Counter()

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" not in line:
            continue

        parts = line.split()

        # Extract source IP
        ip = parts[-4]
        failed_ips[ip] += 1

        # Extract username
        if "invalid user" in line:
            username = parts[parts.index("user") + 1]
        else:
            username = parts[parts.index("for") + 1]

        failed_users[username] += 1

print("=== Failed Login Analysis ===")

print("\nFailed attempts by IP:")
for ip, count in failed_ips.most_common():
    print(f"{ip}: {count}")

print("\nFailed attempts by username:")
for username, count in failed_users.most_common():
    print(f"{username}: {count}")

print("\nPotential brute-force sources:")
for ip, count in failed_ips.most_common():
    if count >= 3:
        print(f"{ip} -> {count} failed attempts")

