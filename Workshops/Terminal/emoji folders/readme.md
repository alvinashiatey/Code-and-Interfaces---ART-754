# Emoji Folders

This workshop will teach you how to script the creation of folders with random emoji names.

## Step 1

Let's begin by creating a shell script named `emoji-folder.sh` in a directory of your choice. I would challenge you to create both the folder and the shell file, using only the terminal. Keep in mind that the `mkdir` command can be used to create a directory, while the `touch` command can be used to create a file. Additionally, the `cd` command can be used to navigate to a specific directory.
At the start of your script, add the following line:

```bash
#!/bin/bash
```

This line is called a shebang. It tells the terminal that the script should be run using the bash shell. This is important because there are many different shells, and they all have different syntax. For example, the `echo` command works in bash, but not in zsh. The shebang ensures that the script is run using the correct shell.

## Step 2

Next, we need to create an array of emojis. Add the following line to your script:

```bash
emojis=("🙂" "😃" "🥳" "🎉" "📁" "📂" "📚" "🌈" "🎨️" "7️⃣" "5️⃣" "4️⃣" "🌟" "🔥" "⚡️" "✨" "🌟" "💡" "🔒" "🔑" "💎" "🌞" "🌙" "🌸" "🍀" "🌊" "⭐️")
```

This line creates an array named `emojis` and populates it with a bunch of emojis. The emojis are enclosed in quotes and separated by spaces. The parentheses indicate that the emojis should be stored in an array. The array is named `emojis`.

## Step 3

Now let's define a variable for the number of folders we want to create. Add the following line to your script:

```bash
numFolders=10
```

This line creates a variable named `numFolders` and sets it equal to 10. We will use this variable to determine how many folders we want to create.

## Step 4

Next, we will create a root folder to store all of our emoji folders. We will check to make sure that the folder does not already exist before creating it. Add the following lines to your script:

```bash
if [ -d "emojis" ]; then
  rm -rf emojis
fi
mkdir emojis
```

Here we use an `if` statement to check if the folder named `emojis` exists. If it does, we delete it using the `rm` command. The `-rf` flag tells the `rm` command to delete the folder recursively and forcefully. The `rm` command is used to delete files and folders. The `mkdir` command is used to create a folder. We use the `mkdir` command to create a folder named `emojis`.

## Step 5

Next, we need to create a loop that will create the folders. Add the following lines to your script:

```bash
for ((i=0; i<$numFolders; i++)); do
done
```

## Step 5

Within the loop, we would have to generate our random folder name and create the folder. Add the following lines to your script, this will go within the loop:

```bash
  name=$(printf "%s\n" "${emojis[@]}" | sort --random-sort | tr -d '\n')
  mkdir emojis/$name
```

The first line creates a variable named `name` and sets it equal to a random string of emojis using the `sort` command line tool and the `tr` tool to delete all occurrences of the newline character `\n`. The second line creates a folder with the name of the random string of emojis.

## Step 6

Now we can run our script. Make sure that the script is executable by running the following command in the terminal:

```bash
chmod +x emoji-folder.sh
```

This command makes the script executable. Now we can run the script by typing the following command in the terminal:

```bash
./emoji-folder.sh
```






