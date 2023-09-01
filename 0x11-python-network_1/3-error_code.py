#!/usr/bin/python3
"""
Script takes in a URL and sends a request to the URL
then displays the body of the response decode in utf-8
"""

if __name__ == "__main__":
    from sys import argv
    from urllib import request, error

    url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode("utf-8"))

    except error.HTTPError as e:
        print("Error code:", e.code)
