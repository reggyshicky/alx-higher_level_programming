#!/usr/bin/python3
"""
script that takes in a URL, sends a request to thr URL
and displays the value of the variable X-Request-Id
in the response header
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    p = requests.get(argv[1])
    print(p.headers.get("X-Request-Id"))
