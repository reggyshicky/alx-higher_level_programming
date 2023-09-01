#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the
URL  and displays the body of the response
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    p = requests.get(url)

    if p.status_code >= 400:
        print("Error code: {}".format(p.status_code))
    else:
        print(p.text)
