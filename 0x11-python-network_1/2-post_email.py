#!/usr/bin/python3
"""A python script that sends a POST request to the passed URL
with email as a parameter"""


from urllib import request, parse
import sys

if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
