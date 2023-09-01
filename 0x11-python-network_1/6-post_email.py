#!/usr/bin/python3
"""
script that takes in a URL and sends a POST request to the
URL with an email as a parameter and displays the bosy of the response
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    value = {"email": argv[2]}
    r = requests.post(url, data=value)
    print(r.text)
