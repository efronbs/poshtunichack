#!/bin/#!/usr/bin/env bash

if [[ "$#" -ne 2 ]]; then
  echo "Usage: $0 <path to ssl cert file> <path to ssl private key file>"
  exit 1
fi

export FLASK_APP="assets.py"
python3 -m flask run -h 0.0.0.0 -p 6969 --cert=$1 --key=$2
