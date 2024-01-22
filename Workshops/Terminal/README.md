# Terminal | Command Line

This is a brief guide to using the command line. We will utilize a terminal emulator to navigate our computer and execute commands. There are many free terminal emulators available, and most operating systems come with one already installed. On Mac, there is the Terminal App, and on Windows, there is the Command Prompt App. Personally, I use [Warp](https://www.warp.dev/), a free terminal emulator for Mac that includes an AI assistant feature, which is helpful when resolving errors.

## Commands

A command is a directive to the computer to perform a specific task. Commands are entered into the terminal and are executed when the user presses the enter key. They consist of two parts: the command itself and the arguments. The command is the instruction to the computer, while the arguments are the data that the command will operate on. For example, the command `ls` is used to list the contents of a directory. The argument is the directory that you want to list the contents of. If you want to list the contents of the current directory, you would type `ls .` and press enter. The `.` is a special argument that represents the current directory. If you wanted to list the contents of the parent directory, you would type `ls ..` and press enter. The `..` is a special argument that represents the parent directory.

### Common Commands on Mac and Linux

| Command | Description                      |
|---------|----------------------------------|
| `ls`    | List the contents of a directory |
| `cd`    | Change directory                 |
| `pwd`   | Print working directory          |
| `mkdir` | Make directory                   |
| `touch` | Create a file                    |
| `rm`    | Remove a file                    |
| `mv`    | Move a file                      |
| `cp`    | Copy a file                      |
| `cat`   | Print the contents of a file     |
| `man`   | Print the manual for a command   |

### `cd`

The `cd` command is used to change the current directory. The `cd` command takes one argument which is the directory that you want to change to. If you want to change to the parent directory you would type `cd ..` and press enter. If you want to change to the current directory you would type `cd .` and press enter. If you want to change to a directory that is a child of the current directory you would type `cd <directory name>` and press enter. If you want to change to a directory that is a sibling of the current directory you would type `cd ../<directory name>` and press enter.

### `man`

The `man` command is used to print the manual for a command. The `man` command takes one argument which is the command that you want to print the manual for. If you want to print the manual for the `cd` command you would type `man cd` and press enter. If you want to print the manual for the `ls` command you would type `man ls` and press enter.

## How to install command line tools: Homebrew

[Homebrew](https://brew.sh/) is a package manager for Mac, similar to an app store for terminal applications and commands. It is used to install command line tools. To install Homebrew, open the terminal and paste the following command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

To install a command line tool using Homebrew, open the terminal and type `brew install <package name>` and press enter. For example, to install the `tree` command line tool, open the terminal and type `brew install tree` and press enter.

## Demos

[ASCII Art with the jp2a command line tool](./ascii/readme.md)

## Shell Scripting

We can automate tasks by writing shell scripts. A shell script is a file that contains a list of commands that are executed when the file is run. To run a shell script, open the terminal and type `./<script name>` and press enter. For example, to run the script `./scripts/hello-world.sh`, open the terminal and type `./scripts/hello-world.sh` and press enter.

For today's class, we will be writing shell scripts for the following tasks:

-  [Creating a directory and randomizing folder names](./emoji%20folders/readme.md)
-  [Accessing an API and saving an image from a URL](./random%20wiki%20images/readme.md)
