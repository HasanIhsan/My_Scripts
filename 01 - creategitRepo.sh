#!/bin/sh

# If a command fails then the deploy stops
set -e

printf "\033[0;32mCreating New GitHub Repositorie...\033[0m\n"

#creating a new repos
#create a echo for a README.md file
#press ESC to quit entering message
printf "\033[0;32mAdd README.md FIle Message $(date):\033[0m\n" 
echo "Press ESC key to quit"
echo -e "\n"

README=""

# README.md file message same as before
while IFS= read -r -n1 key1
do
# if input == ESC key
if [[ $key1 == $'\e' ]];
then
break;
fi
# Add the key to the variable which is pressed by the users.
README+=$key1
done

echo "$README" >> README.md

# git init
git init
echo -e "\n"



#git add README.md 
git add README.md
echo -e "\n"



#git commit -m 
git commit -m "first commit"
echo -e "\n"



#git branch -M main 
git branch -M main
echo -e "\n"



#this is where you will paste in the given http link by github
remoteConnectHttp=""
#press ESC to quit entering message
echo "Press ESC key to quit"
printf "\033[0;32mcreating repos $(date):\033[0m\n" 
printf "\033[0;32mPlease paste the remote Connect Http link GitHub has Provided\033[0m\n" 

# read a single characters
while IFS= read -r -n1 key
do
# if input == ESC key
if [[ $key == $'\e' ]];
then
break;
fi
# Add the key to the variable which is pressed by the users.
remoteConnectHttp+=$key
done

#git remove add origin
git remote add origin "$remoteConnectHttp"
echo -e "\n"


# Push source
git push -u origin main
 

 