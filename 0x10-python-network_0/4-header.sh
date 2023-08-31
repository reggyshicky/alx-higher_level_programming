#!/bin/bash
#Takes in URL, sends GET request, displays body of response
curl -sH "X-School-User-Id: 98" "$1"
