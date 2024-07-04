#!/bin/bash
# This script takes in a URL, sends a GET request with a header variable, and displays the response body
curl -s -H "X-School-User-Id: 98" "$1"
