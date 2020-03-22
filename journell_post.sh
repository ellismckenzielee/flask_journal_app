#! /bin/bash

echo "Hello!"
echo "Do you wish to add a new post to Journell?"

read response

if [ $response == "y" ]
then 
    echo "Please enter the title"
    read title
    echo "Please enter the content"
    read content
fi

touch "journal_app/new_content/$title.txt"
echo "journal_app/new_content/$content" >> $title.txt