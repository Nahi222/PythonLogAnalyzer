# 🔍 Python Log Analyzer

This project is a beginner-friendly Python script built to analyze authentication logs and detect failed login attempts. It's designed to help understand basic log parsing and cyber threat detection in a simple, hands-on way.

The script scans each line of a log file (like `auth.log`) and identifies failed login attempts by searching for specific keywords. It then extracts key details such as the **timestamp**, **username**, and **IP address** of the failed attempt. Finally, it summarizes the number of failed login attempts by each IP address, helping you quickly identify potentially malicious activity.

---

## 💡 What It Does

- Reads and processes a simulated `auth.log` file.
- Detects lines with failed login attempts (e.g., "Failed password").
- Extracts:
  - 🕒 Timestamp of attempt
  - 👤 Username (if available)
  - 🌐 IP address
- Displays each failed attempt in a clean, readable format.
- Prints a summary showing the number of failed attempts per IP.

---

## 🛠️ How to Use

1. **Install Python 3**  
   Make sure Python 3 is installed on your system.

2. **Set up the project**  
   Download or clone the repository, and place the following files in the same directory:
   - `log_analyzer.py` – The Python script.
   - `fake_auth.log` – A sample log file (or replace it with your own).

3. **Run the script**  
   Open your terminal in the project directory and run:

   ```bash
   python3 log_analyzer.py
View the output
The script will print out:

Detected failed login attempts (with timestamp, username, and IP).

A final summary of how many times each IP attempted to log in.

📂 Example Output
plaintext
Copy
Edit
[!] Failed login detected:
Time     : Jun 29 15:02:01
Username : root
IP Addr  : 192.168.1.100
----------------------------------------

=== Failed Login Summary ===
192.168.1.100 → 2 failed attempts
10.0.0.5 → 1 failed attempts
172.16.5.44 → 1 failed attempts
🙋‍♂️ Why I Built This
I created this tool as a fun side project to apply what I’m learning in cybersecurity and Python. It helped me practice working with regular expressions, log formats, and simple automation for security monitoring.

👨‍💻 Author
Jarif Ferdous
Cybersecurity student, tech enthusiast, gamer
🌐 My Portfolio | 💼 LinkedIn | 📧 Email

⚠️ Note
This script is for educational use. If you’re analyzing real logs, make sure to apply proper security and privacy measures.