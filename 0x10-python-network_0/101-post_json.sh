#!/bin/bash
# send a JSON POST request
curl -sH "Content-Type" -d $(cat $2) $1
