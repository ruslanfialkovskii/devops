#!/bin/bash

VAR="This is string"

read -r -a Words <<< "$VAR"

echo "First word is ${Words[0]}"
echo "Second word is ${Words[1]}"
echo "Third word is ${Words[2]}"