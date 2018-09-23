# url.py
import urllib.request
url = "http://dfedorov.spb.ru/python3/src/romeo.txt"
with urllib.request.urlopen(url) as webpage:
    for line in webpage:
        line = line.strip()
        line = line.decode('utf-8')
        print(line)
