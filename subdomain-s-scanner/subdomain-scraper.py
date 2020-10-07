import requests, sys
single_thread = True

domain_name =  str(sys.argv[1])
if len(sys.argv[1]):
   num_workers = int(sys.argv[2])
   if not num_workers > 0:
      sys.exit("The optional paramenter num_workers only accepts positive numbers")
   single_thread = False
   import threading

subdomains_list = open("subdomains.txt", "r").read().splitlines()

def discover_subdomains():
   global domain_name
   while True:
      try:
         subdomain_name = subdomains_list.pop()
      except IndexError:
         """this happens when subdomains_list is empty"""
         return
      else:
         url = f"http://{subdomain_name}.{domain_name}"
         try:
            requests.get(url)
         except requests.ConnectionError:
            pass
         else:
            log = f"discovered subdomain : {url}"
            if not single_thread:
               log = threading.current_thread().name + f" {log}"
            print(log)

if single_thread:
   discover_subdomains()
else:
   threads = []
   for i in range(num_workers):
      thread = threading.Thread(target=discover_subdomains)
      thread.start()
      threads.append(thread)
   for thread in threads:
      thread.join()
      print("all threads completed execution")
