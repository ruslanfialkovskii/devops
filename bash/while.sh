#!/bin/bash

counter=0
while [ $counter -lt 10 ] ; do
    touch file$counter
    let counter=counter+1
done