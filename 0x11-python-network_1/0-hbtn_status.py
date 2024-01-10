#!/usr/bin/python3
""" a Python script that fetche a url """


if __name__ == "__main__":
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        web_content = response.read()
        decoded_content = web_content.decode('utf-8')

        print("Body response:")
        print('\t- type:', type(web_content))
        print('\t- content:', web_content)
        print('\t- utf8 conent:', decoded_content)
