#!/bin/bash

ARRAY=(1 2 3 4 {A..F})

while read element ; do
    echo $element
done <<< $(echo ${ARRAY[*]})
