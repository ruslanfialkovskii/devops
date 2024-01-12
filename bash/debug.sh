#!/bin/bash -x

#Use set -x as trace
#set -n as dry run 
#set -u will error unset variable

#debuging for loops
#break - exits a loop without the control condition being met
#continue - skips processing the rest of this loop and moves to the next iteration
#readonly - sets a variable to readonly that it  can't be change

echo "Enter a filename to read: "
read FILE

while read -r SUPERHERO; do
    echo "Superhero name: $SUPERHERO"
done < "$FILE"