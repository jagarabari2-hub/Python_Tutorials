print("|========================================|"
      "| Find the hostname of the host where Python is executing."
      "||========================================|")
print()
import socket
hostname = socket.gethostname()
print("The hostname of the host where Python is executing is:", hostname)
print()
print("|========================================|"
      "| Find the fully qualified domain name of the following websites :" \
      " www.google.com, www.microsoft.com, www.wikipedia.com"
      "||========================================|")
print()
websites = ["www.google.com", "www.microsoft.com", "www.wikipedia.org"]
for website in websites:
    fqdn = socket.getfqdn(website)
    print("The fully qualified domain name of %s is: %s" % (website, fqdn))
print()
print("|========================================|"
      "| Find the IP addresses of the following websites :" \
      " www.google.com, www.microsoft.com, www.wikipedia.com"
      "||========================================|")
print()
websites = ["www.google.com", "www.microsoft.com", "www.wikipedia.org"]
for website in websites:
    ip_address = socket.gethostbyname(website)
    print("The IP address of %s is: %s" % (website, ip_address))