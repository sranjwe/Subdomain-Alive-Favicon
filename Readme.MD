# Subdomain-Alive-Favicon

One tool to
-Enumerate subdomain of given domain.      
-Check alive Domains.
-Get Favicon hash.

# Usage
 `#python3 subfav.py -h domain.tld`
 
 # Features:-
 1) Enumerate Subdomains and store it in subdomains.txt
 2) Check for alive domains having status code 200 and store it in alive.txt
 3) Generate Favicon Hash of each domain and store it in favhash.txt
 
 # Prerequisites:-
 1) Subfinder :- `#go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest`
 2) python3 :- `#apt install python3`
 3) pip3, mmh3
