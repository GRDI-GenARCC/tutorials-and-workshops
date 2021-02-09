# Introduction to Linux Tutorial

WIP Notes
- search EDIT inside the doc to highlight questions or comments. File issues with gitlab to discuss them.

- EDIT
    - is it excessive to number each subsection?
    - other simple commands? cal, date
    - include exit at end of tutorial
    - line 146 fix HTML
    - image at the end
    - include HOW to look up commands
    - short guide about how to get CLI (biocluster, WSL)
    - expand the overview to be more specific
    - 'shadowbox' questions and answers
    - Table of Contents
    - hint instead of spoiler
    - Intro_Linux_0 - show roadmap of each tutorial/session
---
# 1. Overview

1.1 Prerequisite(s):
- Shell environment (WSL, Biocluster)

1.2 Objectives:
- Learn some background information about Linux
- Define some key terms about Linux and the command line interface (CLI)
- Learn some basic command line functions

1.3 Commands covered in this session
- `pwd`, `cd`, `ls`, `mkdir`, `touch`, `rm`
- information about these commands can be accessed within a terminal by using 
```bash
man <command_name>
```
- a shorter summary can often be found by using 
```bash
<command_name> --help
```
- more documentation at [manual-pages](https://www.kernel.org/doc/man-pages/)

1.4 Questions?

</br>

---
# 2. Introduction

## 2.1 Quick history of Linux
<details>
    <summary>Click to expand</summary>
        <p>Linux comes from an early operating system called Unix. Users would connect to multi-user mainframe computers by display and keyboard only. Text is very light-weight compared to graphic user interfaces (GUI). Interacting with an operating system above the computer components was a "shell".</p>
        <img src="https://cdn-media-1.freecodecamp.org/images/8dQXHBemVAUp4xgVzFqgEHGyNjCsQT0usHBw" alt = "Shell Diagram" style="width:160px;height:100px;"/>
        <p>Users interacted with the system by sending input and receiving output. They used programs or commands in a programming language - initially sh, now bash. Thus the command line has been the basis of Linux systems ever since. It can be confusing to learn but offers the best performance, can be automated with scripts, and many important scientific tools use cli for development.</p>  
        <br />
</details>

Questions?

## 2.2 Definitions

EDIT - should this be collapsed??

NOTE: some organizations use terms more specifically, these are the general definitions

- command line interface
    - text session where the user enters commands with optional arguments. Output is displayed from the operating system (OS).
- shell
    - a text-mode application containing a CLI to the OS
    - note that in casual usage, shell, prompt, terminal, and console all refer to the same thing
- console application
    - a command line program that functions without a required graphical interface
- bash
    - commonly distributed shell, or command language interpreter for Linux
    - an enhanced version of the original, called sh
- Ubuntu
    - a popular Linux distribution (distro) based on Debian (another distro)
    - widely used and considered to be very user friendly
- terminal
    - often used synonymously with shell
    - more accurately - the terminal gives access to the shell
    - can refer to the software that hosts the shell/CLI
    - can also refer to the physical hardware used to interface with the OS
- prompt
    - short for command prompt, refers to the small section preceeding a command
    - in bash this has:
        - user
        - name of the computer
        - current directory (folder)
        - usually ends with $
- GUI (pronounced gooey)
    - graphical user interface 


2.3 Questions??

<br />

---
# 3.0 Instruction part 1

In a Ubuntu desktop environment, you can use the "Terminal" application for the CLI. Alternatively you can use **Ctrl-Alt-T**. 

If you are in Ubuntu in WSL or connected to the Biocluster, you're already using CLI.

## 3.1 Basic Navigation
- There are shortcuts to help navigate the CLI. These shortcuts range from simple to complex, but all make for a much greater shell experience.
- **tab** - will autocomplete if you begin to write a command that is part of bash-completion, or a filename in a given directory
- **up arrow** - will scroll to previous commands entered in the shell
    - you can navigate back through these commands with the down arrow
- **left/right arrows** - used to control cursor placement in the text
- **copy/paste** - this can depend on which terminal you are using, and the configurations
    - typically paste is right-click
    - sometimes ctrl+shift+c and ctrl+shift+v used for copy and paste respectively

- test this now by copying some text outside your terminal and pasting it into the shell

## 3.2 `pwd`
- **`pwd` - print name of current/working directory**
    - print working directory
    - try each of the following
```bash
pwd
PWD
```
- note that Linux is case sensitive, only the exact command will work

## 3.3 `ls`
- **`ls` - list directory contents** 
    - this is a shortcut for `ll -s` (we will explore `ll` later)
    - the `-s` is a **command line argument**
    - these arguments give flexibility and options to commands
    - not restricted to your current directory, can specify a location to use `ls` without changing your `cwd`
```bash
ls
ll -s
ls /usr/bin
ls -a
```
- ls -a uses the option to see all contents, including hidden files and folders that start with a `.`
eg. `.bash_history` in your home directory (your 'user' folder)

**Question** - What are some other arguments we can use with `ls`?

## 3.4 Command Line Arguments
    - these are important for basic linux and especially in scientific tools
    - a good way to learn them is to use the `--help` argument before attempting to use a command
```bash
pwd --help
pwd -h
```
- `-h` is often a shortcut for `--help` but can also have a meaning as an argument, use caution and know the arguments before using a command
- these arguments can enhance the usage of a command - giving options to make them visible, or ask for inputs, etc.
- usually not required, but for some commands they are necessary

## 3.5 `cd`
- `cd` means change directory (aka folder)
- `/` is used in directory structure (Windows is `\`)
    - the directory location `/` is **root**, there are no separate 'drives' like in Windows
- `.` is your current dir (a single dot character) 
- `..` will go to parent (two dots)
- also helpful, `cd -` will go to the previous directory
- mini-exercise 
    - view the command line arguments for `cd` (EDIT - fix HTML)
    <details>
    <summary>Click here for the solution</summary>
        cd --help
        OR
        man cd
</details>

- `/` by istelf is a critical directory in Linux systems, it is the root directory
    - all other storage branches from this location, even other drives (in /mnt)

<br />

EDIT - add more than just cd and pwd to the exercise?
## 3.4 Exercise 1
- Try the following commands (use pwd to see where you are at any point, or look at the promp)

```bash
cd /
pwd
cd home
cd ..
pwd
cd
cd ../..
pwd
cd etc
cd
cd etc
```

- if it is installed, use `tree` to view the file structure
- note that using paths like `home` or `etc` only works if they are a subdirectory of your current directory, otherwise a full or absolute path must be used
- absolute path will include the full address to the location, whereas a relative path uses `.` and `..`
**Example** 
    - if you are in `/home` and wish to go to your user account, this can be achieved by using `cd USERNAME` (substituting your own account name)
    - the relative path to do the same thing is `cd ./USERNAME`

## 3.5 Self-Directed Exercise 1
- find a system folder called "apt" using the commands from this session
- exploration only. DO NOT modify anything, just navigate directories and check for contents

<details>
    <summary>Click here for the solution</summary>
        - cd /usr/lib/apt
        - the directory is in root -> usr -> lib -> apt
        - apt means advanced package tool and handles the installation and removal of software packages
        - apt will be discussed in part 3
</details>
<br/>

--- 
## 3.5 Discussion
- any errors?
- relative vs absolute paths
- '~' refers to /home/USERNAME/
- to find username use `whoami`


- **Optional** (DO NOT USE in WSL!) - use `clear` to clear your terminal 

<br />

Take a 5 minute break

<br />

---
# 4.0 Instruction part 2
- Any questions?

## 4.1 `mkdir`

- this command is short for 'make directories'
- view the documentation using `man mkdir`
- it is best to never use arguments unless you understand what you are doing!

Try the command
```bash
cd
mkdir -v testdir
```
- what does `-v` add to this command?
- this a very useful argument for many commands

**Discussion** - what should we use to create multiple nested directories?

Additional commands
```bash
mkdir -pv testdir/testdir1/testdir2
mkdir -v testingdir0 testingdir1
```

**Discussion** - what is the resulting difference in these two commands?

## 4.2 `touch`
- change file timestamps
- there are many options for this command, but commonly used to create a new file

Try the command
```bash
cd && ls
cd testdir
touch file1 file2.txt
```
- commands can be chained together in bash with &&
- we will look at other operators in part 2 and 3
- must assign filetypes manually! (ie - .txt .fastq)

**Exercise** - create a file in testdir1 and testdir2 at the same time
<details>
    <summary>solution</summary>
        - touch testdir1/filewhatever testdir1/testdir2/filewhatever1
</details>

## 4.3 `rm`
- use great caution when learning this command!
- Linux gives users great freedom - one of the great aspects of this OS
- however this comes with the drawback that mistakes are not prevented, you can delete important files and the system may not stop you

- `rm` is used to 'remove files or directories'
- let's view documentation with `man rm`

**Question** - which arguments should we use?
<details>
    <summary>spoiler</summary>
        - let's start by using -iv for interactive, verbose
</details>

Try the command
```bash
cd && ls
cd testdir/testdir1 && ls
rm -iv filewhatever #substitute whichever filename you used
rm -iv testdir2
```
- \# is used to comment out code in bash, any text in the same line will not be executed
- used in python and other languages as well (we'll look at this in a challenge exercise)

**Discussion** - why didn't the last command work?
<details>
    <summary>spoiler</summary>
        <ul>
            <li> look at the documentation/arguments</li>
            <li> for a directory we need to use -r (recursive)</li>
            <li> recursion - a method of solving a problem where the solution depends on solutions to smaller instances of the same problem </li>
            <li><a>https://en.wikipedia.org/wiki/Recursion_(computer_science)</a></li>
        </p>
</details>

Try the command
```bash
rm -ivr testdir2
```
- descends into dir, removes files, then removes the dir itself

**Question** - what if we want to delete multiple files at once?
<details>
    <summary>spoiler</summary>
        <ul>
            <li> we need to use string matching </li>
            <li> a string is generally a collection of characters </li>
            <li> the asterisk symbol will match zero or more characters </li>
        </p>
</details>

Try the command
```bash
cd && ls
cd testdir/
touch filename{01..09}.cpp
ls
touch file{01..09}.py
ls
```

- getting a bit cluttered, let's remove all the files we just created
- be **VERY** careful when using * in an rm command

```bash
rm -v file*
ls
```

- the matching removes all files that begin with 'file'
- this is a very basic form of regular expressions (RegEx), which are very difficult but useful tools to filter through files or anything related to strings or expressions
- we will not cover regex in any of the tutorials, but you are welcome to look it up for yourself

#### Tidbit - The mascot for Linux is Tux
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/TuxFlat.svg/800px-TuxFlat.svg.png" alt = "Tux" style="width:71.2px;height:86px;"/>
