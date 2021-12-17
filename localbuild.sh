#!/bin/bash
cd $(dirname "$(readlink -f $0)")
docker build -t wikitolearn/python38:0.1 .
