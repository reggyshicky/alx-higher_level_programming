#!/bin/bash
# Takes URL, sends request to URL, displays content length
curl -sI "$1" | grep 'Content-Length:'| cut -c 17-
