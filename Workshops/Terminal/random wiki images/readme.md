# Random Wiki Images

This is a simple script that will download a random image from Wikipedia to a folder

## Step 1

Let's crete a shell script named `random-wiki-image.sh` in a directory.

At the start of your script, add the following line:

```bash
#!/bin/bash
```

## Step 2

Let create a variable for the number of images to download. Add the following line to your script:

```bash
numImages=10
```

## Step 3

Now let's create a folder to store the images. Add the following line to your script:

```bash
mkdir -p random_wiki_images
```

## Step 4

let's remove any existing images from the folder. Add the following line to your script:

```bash
rm -f random_wiki_images/*
```

## Step 5

Now let's download the images. Add the following line to your script:

```bash
user_agent="MyImageDownloader/1.0"

for (( i=0; i<num_images; i++ )); do
    summary=$(curl -s -L -A "$user_agent" "https://en.wikipedia.org/api/rest_v1/page/random/summary")

    title=$(echo "$summary" | grep -o '"title":"[^"]*' | cut -d'"' -f4)

    image_url=$(echo "$summary" | grep -o '"originalimage":{[^}]*"source":"[^"]*' | cut -d'"' -f6)

    if [ ! -z "$image_url" ] && [ "$image_url" != "null" ]; then
        curl -s -o "random_wiki_images/r_wiki_$title.jpg" "$image_url"
    else
        echo "No image found for this article."
    fi
done
```

Okay now this is a lot of code, so let's break it down.

First, we will create a variable for the user agent, which is simply a string that identifies us to the server. Next, we will create a for loop that will iterate for the desired number of image downloads. We will utilize the `curl` command to retrieve a random article from Wikipedia and then use `grep` to extract the title and image URL from the response. Finally, we will use `curl` once more to download the image.

## Step 6

Now let's make the script executable. Run this command in your terminal:

```bash
chmod +x random-wiki-image.sh
```

This command makes the script executable. Now we can run the script by typing the following command in the terminal:

```bash
./random-wiki-image.sh
```

