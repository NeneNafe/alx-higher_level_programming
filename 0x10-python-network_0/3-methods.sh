#!/bin/bash
# Displays all HTTP methods the server will accept
curl -sI -X OPTIONS HEAD PUT "$1" | grep "Allow:" | cut -d " " -f 2
