#!/usr/bin/python3
"""
script that takes your github credentials and uses
the github API  to display your id
"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", auth=auth)
    print(res.json().get("id"))
