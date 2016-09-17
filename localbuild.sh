#!/bin/bash
cd $(dirname "$(readlink -f $0)")
docker build -t wikitolearn/python35:0.1 .
