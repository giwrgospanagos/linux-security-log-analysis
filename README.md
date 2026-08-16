# Linux Security & Log Analysis Lab

## Overview

This project demonstrates basic Linux security monitoring and authentication log analysis using simulated SSH authentication logs.

The objective was to identify failed login attempts, analyze suspicious authentication patterns, and automate the detection process using Python.

## Environment

- Operating System: Ubuntu Linux
- Environment: WSL2
- Analysis Language: Python 3
- Log Source: Simulated SSH authentication log
- Purpose: Educational security lab

## Objectives

- Analyze authentication logs
- Identify failed login attempts
- Identify source IP addresses
- Identify targeted usernames
- Detect potential brute-force patterns
- Automate log analysis using Python
- Document security findings

## Tools & Technologies

- Linux
- Bash
- Python
- SSH log analysis
- WSL2

## Analysis Performed

The authentication log was analyzed to identify:

1. Failed authentication attempts
2. Source IP addresses
3. Targeted usernames
4. Repeated authentication failures
5. Potential brute-force sources

## Results

The analysis identified:

- `192.168.1.50` — 3 failed attempts
- `10.0.0.15` — 3 failed attempts
- `admin` — 4 failed attempts

The Python script automatically identified both IP addresses as potential brute-force sources based on the configured threshold of 3 or more failed attempts.

## Python Automation

The `analyze_logs.py` script automates the analysis of the authentication log.

It:

- Counts failed authentication attempts by IP
- Counts failed attempts by username
- Identifies potential brute-force sources

Run the analysis with:

```bash
python3 analyze_logs.py

Project Structure
linux-security-log-analysis/
│
├── README.md
├── analyze_logs.py
├── auth-lab.log
│
├── evidence/
│
└── report/
    └── security-assessment.md
Security Considerations

Repeated failed authentication attempts can indicate password guessing or brute-force activity.

In a real environment, repeated authentication failures should be investigated and appropriate controls such as account lockout policies, firewall restrictions, strong authentication and monitoring should be considered.

Disclaimer

This project uses simulated authentication log data for educational purposes.

No unauthorized systems or accounts were targeted.
