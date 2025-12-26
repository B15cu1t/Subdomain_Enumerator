import requests
import threading

#<---Make sure to change the domain to whichever one you want to enumerate--->
domain = "example.com"

with open('subdomains.txt') as file:
    subdomains = file.read().splitlines()

discovered_subdomains = []

lock = threading.Lock()

def check_subdomains(subdomain):
    
    url = f'https://{subdomain}.{domain}'
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("[+] Discorvered subdomain: ", url)
        with lock:
            discovered_subdomains.append(url)

threads = []

for subdomain in subdomains:
    thread = threading.Thread(target=check_subdomains, args=(subdomain,))
    thread.start()
    threads.append(thread)
    
for thread in threads:
    thread.join()
    
with open(f"discovered_subdomains_for_{domain}.txt", "w") as f:
    for subdomain in discovered_subdomains:
        print(subdomain, file = f)
