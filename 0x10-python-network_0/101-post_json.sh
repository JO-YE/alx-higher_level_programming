#!/bin/bash
# send a JSON POST request
curl -sH -X POST "Content-Type: application/json" -d '$(cat '$2')' $1
