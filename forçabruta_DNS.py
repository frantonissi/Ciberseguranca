import sys
import requests

host = sys.argv[1]
wordlist = sys.argv[2]

file = open(wordlist)

for i in file.readlines():
    arq = i.replace('\n', '')
    url = host+ "/" + arq
    re = requests.get(url)
    code = re.status_code
    
    if code != 404:
        print(code, url)