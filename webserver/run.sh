#!/bin/#!/usr/bin/env bash

if [[ "$#" -ne 2 ]]; then
  echo "Usage: $0 <path to ssl key file> <path to ssl cert file>"
  exit 1
fi

export FLASK_ENV=assets.py
sudo python -m flask run -h 0.0.0.0 -p 6969 --key=$1 --cert=$2
