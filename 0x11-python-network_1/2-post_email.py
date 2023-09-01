#!/usr/bin/python3
"""
script that takes ina URL  and an email and sends a POST
request to the passed URL  with the email as a parameter
and displays the body of the response
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv
    url = argv[1]
    param = {"email": argv[2]}
    data = urllib.parse.urlencode(param).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
