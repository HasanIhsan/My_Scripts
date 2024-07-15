#!/bin/sh

# If a command fails then the deploy stops
set -e

printf "\033[0;32mDeploying updates to GitHub...\033[0m\n"

#updating the whole repos
# Add changes to git
git add .
 

userinput=""
#press ESC to quit entering message
echo "Press ESC key to quit"
printf "\033[0;32mrebuilding repos $(date):\033[0m\n" 

# read a single characters
while IFS= read -r -n1 key
do
# if input == ESC key
if [[ $key == $'\e' ]];
then
break;
fi
# Add the key to the variable which is pressed by the users.
userinput+=$key
done

git commit -m "$userinput"

# Push source
git push origin main

 