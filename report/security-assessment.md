# Linux Security & Log Analysis Report

## 1. Executive Summary

This assessment demonstrates the analysis of simulated Linux SSH authentication logs.

The objective was to identify failed authentication attempts, determine their source IP addresses, identify targeted usernames, and detect patterns that could indicate brute-force activity.

A Python script was developed to automate the analysis.

The analysis identified two potential brute-force sources:

- 192.168.1.50 — 3 failed attempts
- 10.0.0.15 — 3 failed attempts

The username `admin` was the most frequently targeted account, with 4 failed authentication attempts.

---

## 2. Scope

**Environment:** Ubuntu Linux running through WSL2

**Assessment Type:** Authentication log analysis

**Data Source:** Simulated SSH authentication log

**Analysis Tool:** Python 3

All data used in this assessment was generated specifically for this educational laboratory.

---

## 3. Methodology

The assessment followed these steps:

### Step 1 — Log Collection

A simulated SSH authentication log was created containing successful and failed authentication events.

### Step 2 — Failed Login Detection

Failed authentication attempts were identified using Linux command-line tools.

Example:

```bash
grep "Failed password" auth-lab.log
### Step 3 — IP Analysis

Source IP addresses associated with failed authentication attempts were extracted and counted.

### Step 4 — Username Analysis

Usernames targeted by failed authentication attempts were identified and counted.

### Step 5 — Automated Analysis

A Python script was developed to automate the detection process.

The script identifies:

- Failed authentication attempts by IP
- Failed attempts by username
- Potential brute-force sources

---

## 4. Findings

### Finding 01 — Repeated Authentication Failures

**Severity:** Medium

Two IP addresses generated three failed authentication attempts each:

- `192.168.1.50`
- `10.0.0.15`

Repeated authentication failures can be an indicator of password guessing or brute-force activity.

Because the data is simulated, this finding represents a detection scenario rather than a confirmed attack.

### Recommendation
In a real environment:

Investigate the source IP addresses.
Review authentication logs for additional activity.
Implement account lockout or rate-limiting controls where appropriate.
Restrict SSH access to trusted networks.
Consider stronger authentication mechanisms such as SSH keys or MFA.
Finding 02 — Frequently Targeted Username

Severity: Low–Medium

The username admin appeared in four failed authentication attempts.

Attackers commonly target predictable or privileged usernames.

Recommendation
Avoid predictable administrative usernames where possible.
Disable unnecessary accounts.
Use strong authentication mechanisms.
Monitor repeated attempts against privileged accounts.
5. Automated Detection

The analyze_logs.py Python script was developed to automate the analysis.

Example output:

Failed attempts by IP:
192.168.1.50: 3
10.0.0.15: 3


Failed attempts by username:
admin: 4
test: 1
user: 1


Potential brute-force sources:
192.168.1.50 -> 3 failed attempts
10.0.0.15 -> 3 failed attempts

The script uses a threshold of three or more failed attempts to flag a potential brute-force source.

6. Security Recommendations

For a real Linux environment:

Monitor authentication logs regularly.
Restrict SSH access using firewall rules.
Use SSH keys instead of password authentication where appropriate.
Implement rate limiting or intrusion prevention mechanisms.
Disable unnecessary user accounts.
Monitor privileged account activity.
Maintain current security updates.
7. Conclusion

This laboratory demonstrated a basic security monitoring workflow using Linux command-line tools and Python.

The project covered authentication log analysis, source IP identification, username analysis, pattern detection and automation.

The exercise demonstrates practical skills relevant to junior cybersecurity roles, including Linux, log analysis, scripting and security monitoring.

Disclaimer

This project uses simulated authentication logs for educational purposes.

No unauthorized systems, accounts or networks were targeted.
