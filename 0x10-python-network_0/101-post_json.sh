#!/bin/bash
# send a JSON POST request
curl -s -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
