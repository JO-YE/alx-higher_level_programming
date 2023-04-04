#!/bin/bash
# send a requedt and display only the status code 
curl -s $1 -o /deb/none -w '%{http_code}'
