#!/bin/bash

numImages=20

mkdir -p random_wiki_images

rm -f random_wiki_images/*

user_agent="MyImageDownloader/1.0"

for (( i=0; i<numImage; i++ )); do
    summary=$(curl -s -L -A "$user_agent" "https://en.wikipedia.org/api/rest_v1/page/random/summary")

    title=$(echo "$summary" | grep -o '"title":"[^"]*' | cut -d'"' -f4)

    image_url=$(echo "$summary" | grep -o '"originalimage":{[^}]*"source":"[^"]*' | cut -d'"' -f6)

    if [ ! -z "$image_url" ] && [ "$image_url" != "null" ]; then
        curl -s -o "random_wiki_images/r_wiki_$title.jpg" "$image_url"
    else
        echo "No image found for this article."
    fi
done