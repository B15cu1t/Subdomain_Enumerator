# Subdomain Enumerator  
**Python-Based Reconnaissance Tool (Educational Project)**

---

## Overview
This project is a **Python-based subdomain enumeration tool** developed for educational purposes to demonstrate how **domain reconnaissance** is performed during the early stages of security assessments.

The tool automates the process of discovering active subdomains for a given domain using a **wordlist-based approach**, helping illustrate how publicly accessible services can be identified through basic enumeration techniques.

---

## Project Description
The script reads potential subdomain names from a wordlist and attempts to resolve them by sending HTTP requests to constructed URLs in the format: https://subdomain.target-domain

Each request is executed in parallel using **multithreading**, allowing for faster enumeration while maintaining thread safety.  
Discovered subdomains are logged both to the terminal and to an output file for later analysis.

This project focuses on **automation, concurrency, and reconnaissance fundamentals**, not exploitation.

---

## Features
- Wordlist-based subdomain enumeration  
- Multithreaded scanning for improved performance  
- Thread-safe handling of shared resources  
- Live terminal output for discovered subdomains  
- Automatic export of results to a text file  

---

## Technologies Used
- **Python**
- **requests** – HTTP request handling  
- **threading** – Concurrent execution  
- **Locks (thread synchronization)** – Safe shared data access  
- **File I/O** – Reading wordlists and saving results  

---

## Educational Goals
Through this project, I gained practical experience with:
- Web reconnaissance techniques used in security assessments
- Multithreaded programming in Python
- Race condition prevention using thread locks
- Handling network errors and unreachable hosts
- Automating repetitive security-related tasks

This project strengthened my understanding of **how attack surfaces are discovered** and why exposed subdomains can pose security risks if not properly managed.

---

## Ethical Disclaimer
⚠️ **This project is intended strictly for educational and authorized use only.**

- It must only be used on domains you own or have explicit permission to test  
- It must not be used for unauthorized scanning or reconnaissance  
- It must not be used as part of malicious activity  

Unauthorized reconnaissance can be illegal and unethical.  
This repository exists to promote **cybersecurity awareness and defensive learning**.

---

## Relevance
Subdomain enumeration is a critical phase of penetration testing and security auditing.  
Understanding how this process works helps organizations:
- Identify unintended exposed services
- Reduce attack surface
- Improve asset management
- Strengthen overall security posture

---

## Possible Improvements
Future enhancements could include:
- DNS-based resolution instead of HTTP-only checks  
- Rate limiting and timeout configuration  
- Support for custom protocols (HTTP/HTTPS selection)  
- Output formats such as JSON or CSV  
- Asynchronous implementation for better scalability  
