#!/bin/bash
# a URL that sends and displays a response

curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2