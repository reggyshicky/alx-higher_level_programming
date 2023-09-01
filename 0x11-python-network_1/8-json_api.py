#!/usr/bin/python3
"""
A python script that takes in a letter sends a POST request to
an URL with the letrer q as a parameter
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    letter = "" if len(argv) == 1 else argv[1]
    value = {"q": letter}

    res = requests.post("http://0.0.0.0:5000/search_user", data=value)
    try:
        r_json = res.json()
        if r_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(r_json.get("id"), r_json.get("name")))
    except ValueError:
        print("Not a valid JSON")
