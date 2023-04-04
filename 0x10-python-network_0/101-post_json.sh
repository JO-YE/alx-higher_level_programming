#!/bin/bash
# send a JSON POST request
curl -sH "Content-Type: application/json" -d $(cat $2) $1
