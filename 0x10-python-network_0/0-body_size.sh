#!/bin/bash
# a script that send a request to a URL and display the content length
curl -sI $1 | grep Content-Length | cut -d " " -f 2
