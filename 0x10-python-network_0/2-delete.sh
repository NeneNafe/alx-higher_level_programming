#!/bin/bash
# sends a DELETE request to the URL and displays the body of response
curl -s "$1" -X DELETE
