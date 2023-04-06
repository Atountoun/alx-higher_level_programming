#!/bin/bash
# This script passes a header to a GET request
curl -s "$1" -H "X-School-User-Id: 98"
