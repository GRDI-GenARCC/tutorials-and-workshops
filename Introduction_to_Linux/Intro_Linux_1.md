# Introduction to Linux Tutorial Part 1

- [Home page of the repository](../README.md)
- [Introduction to Linux overview](/Introduction_to_Linux)

[[_TOC_]]

---

## 1. Overview

- Introduction and BRSN
- Review of "Home" page or README

<br>

- The material is meant for those with little or no experience with Linux, but can be helpful for intermediate users as well
  - These session are introductory, it takes time and practice to become proficient with Linux (as with any new technology skill)
  - Patience for both instructors and learners will help everyone achieve their best results
  - Many users have great expertise in other areas of science, this is the beginning of process to gain yet another area of expertise
- This material is largely derived from the book [The Linux Command Line](https://linuxcommand.org/tlcl.php) by William Shotts
  - **This is an excellent resource for further study!**
- Here are some other resources for Linux and Bioinformatics related training
  - Excellent and in-depth Linux Tutorial - [Ryan's Tutorials](https://ryanstutorials.net/linuxtutorial/)
  - The [BRSN resource page](https://collab.agr.gc.ca/co/BRS-SRB/SitePages/Resource%20Overview.aspx#title-1175) is repository with links and information for many other resources

<br>

### 1.1 Prerequisite(s)

- Ubuntu installed in WSL (Windows Subsystem for Linux)
  - An installation guide is available [here](/WSL_Workshop/WSL_installation.md) - current as of August 2021
  - For many users at AAFC this will be the most simple and practical way to access Linux
  - Ubuntu in WSL is a great environment for training, practice, and even some light data analysis. For anything above this you should use a full-fledged Linux workstation or the [Biocluster](https://redmine.biodiversity.agr.gc.ca/projects/biocluster/wiki/Biocluster_User_Guide) - use your AAFC credentials to access this site
- Any `bash` command line will suffice, but the guide will focus on Ubuntu in WSL as it is now widely available to AAFC users

<br>

### 1.2 Objectives

- Overall objective --> build a foundation of skills in Linux
- Learn some background information about Linux
- Define some key terms about Linux and the command line interface (CLI)
- Study and practice some basic command line functions

<br>

### 1.3 Commands covered in this session

- `pwd`, `cd`, `ls`, `clear`, `--help`, `man`, and `exit`
- It is arguably more important to learn how to use commands than to learn the commands themself
  - Learning how to learn - searching is a great skill
- **Information about commands can usually be accessed within a terminal by using the following**

```bash
man <command_name>
```

- `man` pages often require pressing `q` to exit
- Not all systems have manual entries for all commands
- A shorter summary can often be found by using

```bash
<command_name> --help
```

- We will use `--help` as the default for the workshop
- More documentation is available at [manual-pages](https://www.kernel.org/doc/man-pages/)

<br>

### 1.4 Questions

<br>

---

## 2. Introduction

### 2.1 Quick history of Linux

<details>
    <summary><b>Click to expand</b></summary>
        <p>Linux comes from an early operating system called Unix. Users would connect to multi-user mainframe computers by display and keyboard only. Text is very light-weight compared to graphic user interfaces (GUI). Interacting with an operating system above the computer components was a "shell". GNU and eventually Linux are open source components branching away from Unix.</p>
        <img src="https://cdn-media-1.freecodecamp.org/images/8dQXHBemVAUp4xgVzFqgEHGyNjCsQT0usHBw" alt = "Shell Diagram, freecodecamp.org" width="200"/>
        <p>Users interacted with the system by sending input and receiving output. Multiple users could use the system simultaneously. They used programs or commands in a programming language - initially sh (shell, or Bourne shell), now bash ("Bourne again shell"). Thus the command line has been the basis of Linux systems ever since. It can be confusing to learn but offers the best performance, can be automated with scripts, and many important scientific tools use the command line interface (CLI) for development.</p>  
</details>

<br>

### 2.2 Linux in Bioinformatics

- Linux is the preferred way to use bioinformatics tools for many practical and historical reasons
  - Sequence files are usually in .fasta, which is essentially a text file. Command line tools can interact very well with text files
  - It is simple to setup environments with specific compilers, languages, tools, etc. Containers are a relatively new option for this
    - eg. May need tools that work for version 2.15.1 and not 2.16
- Open source nature of Linux and bioinformatics tools
- High performance computers usually have Linux OS
  - When connecting to HPC (eg. [Biocluster](https://redmine.biodiversity.agr.gc.ca/projects/biocluster/wiki/Biocluster_User_Guide)) the command line is your interface

<br>

### 2.3 Definitions

NOTE: Some organizations use terms more specifically, these are the general definitions.

- Command line interface
  - Text session where the user enters commands with options and arguments. Output is displayed from the operating system (OS)
- Shell
  - Program that takes commands from the keyboard and interprets them for the operating system
  - `bash` acts the default shell for most Linux distributions
  - In Windows there is a language called PowerShell
  - Other shells are available such as: `zsh`, `fish`
- Console
  - The window that hosts your shell and runs programs
- Console application
  - A command line program that functions without a required graphical interface
- bash
  - Commonly distributed command language for Linux
  - bash acts as your shell when using it in the command line
  - An enhanced version of the original sh (Bourne shell)
- Ubuntu
  - A popular Linux distribution (distro) based on Debian (another distro)
  - Widely used and considered to be very user friendly
- Terminal
  - The terminal gives access to the shell - eg. The window or program that allows you to use bash or another shell
  - Can refer to the software that hosts the shell/CLI
  - Can also refer to the physical hardware used to interface with the OS
- Prompt
  - Short for command prompt, refers to the small section preceeding a command
  - In bash this has:
    - User
    - Name of the computer
    - Current directory (folder)
    - Usually ends with $
- GUI (pronounced gooey)
  - Graphical user interface
- WSL (Windows Subsystem for Linux)
  - A compatibility layer allowing Linux commands in Windows. Linux distributions are installed and can use most command line features. In AAFC only version 1 is approved at this time.

<br>

### 2.4 Questions

<br>

---

## 3.0 Instruction

- In a Ubuntu desktop environment, you can use the "Terminal" application for the CLI (command line interface). Alternatively you can use **Ctrl-Alt-T**
- If you are in Ubuntu in WSL or connected to the Biocluster, you're already using CLI
- Review window placement for the workshop
  - Teams or markdown document split to one side
  - Ubuntu window
  - other (slido)

<br>

### 3.1 Basic Navigation

- There are shortcuts to help navigate the CLI. These shortcuts range from simple to complex, but all make for a much greater shell experience.
- **tab** - will autocomplete if you begin to write a command that is part of bash-completion, or a filename in a given directory
- **up arrow** - will scroll to previous commands entered in the shell
  - You can navigate back through these commands with the down arrow
- **left/right arrows** - used to control cursor placement in the text
- **copy/paste** - this can depend on which terminal you are using, and the configurations
  - Typically paste is right-click
  - Sometimes ctrl+shift+c and ctrl+shift+v used for copy and paste respectively
- **ctrl+c** - interrupt/kill the current process in the terminal
  - :wink:

- #### Exercise 3.11

  - Copy some text from outside your shell and paste it into the command line
  - This does not need to execute properly in Linux, in fact it's safer if it doesn't
  - Feel free to use text from this tutorial
  - In Ubuntu/WSL you can configure options by right-clicking the top of the window and choosing "Properties"

- We will learn to use these navigation shortcuts throughout the tutorial

<br>

### 3.2 `pwd`

- **`pwd` - print name of current/working directory**
  - This shows the current directory you are located in (aka "working in")
  - It seems very simple but can be helpful for scripts that will use varying working directories while executing

Try the commands

```bash
pwd
PWD
```

- **Discussion**
  - Why did the second command not work?

<details>
    <summary>Solution</summary>
      <ul>
        <li>Linux is case sensitive, only the exact command will work</li>
        <li>This also applies to filenames and directories</li>
        <li>eg. file1 and File1 are completely separate files in Linux (not in Windows)</li>
      </ul>
</details>

<br>

### 3.3 `ls`

- **`ls` - list directory contents**
  - Shows the files and directories of a given location (defaults to `.`, your current directory, unless an argument is provided)
  - Not restricted to your current directory, can specify a location to use `ls` without changing your `pwd`
  - The directory that is specified at the end of this command is a **command argument**

Try the commands

```bash
ls
ls . # The command above defaults to `.` as the location, unless one is specified
ll -s # ll may not be an "alias" in your shell
ls /
ls -a
ls -A # may be set to "la" in your shell
ls -a /home
```

- `ls -a` uses a **command option** to see all contents, including hidden files and folders that start with a `.`
  - In Ubuntu this is "aliased" to `la` (more on `alias` later)
  - eg. Hidden files -> `.bash_history` in your home directory (your 'user' folder)
- `ls -a /home` combines an option, `-a`, with an argument, `/home`

- **Discussion**
  - What are some other options we can use with `ls`?
  - How do they help?

<details>
    <summary>Solution</summary>
      <ul>
        <li>These are not the only options, as all arguments have their usages</li>
        <li>-h for human readable (when viewing file sizes)</li>
        <li>-s to view the file size</li>
        <li>-S to sort by file size</li>
        <li>-t to sort by modification time</li>
        <li>-1 to view in one column, </li>
      </ul>
</details>

<br>

### 3.4 Command Line Options and Arguments

- These are important for basic linux and especially in scientific tools
- A good way to learn them is to use the `--help` argument before attempting to use a command

```bash
pwd --help
pwd -h
```

- `-h` is often a shortcut for `--help` but can also have a meaning as an argument, use caution and check the options before using a command
- These options can enhance the usage of a command - displaying the changes, or asking for inputs, etc.
- The command is what you want to, the options/parameters are how you want to do it, and the arguments are the things you want to apply these to
- Options are usually not required, but for some commands they are necessary
- These options can be used together, for instance `ls -1hast` will display all contents in one column sorted by last modification time with the "human readable" size listed as well. This is equivalent to `ls -1 -h -a -s -t` or `ls -1ha -st`

<br>

### 3.5 `cd`

- **`cd` - change directory (aka folder)**
- `/` is used in directory structure (Windows is `\`)
  - The directory location `/` is **root**, there are no separate 'drives' like in Windows
- `.` is your current dir (a single dot character)
- `..` will go to parent (two dots)
- Also helpful, `cd -` (cd 'dash') will go to the previous directory

- **Discussion**
  - How do you view the command line options for `cd`

<details>
    <summary>Solution</summary>
      <ul>
        <li>cd --help</li>
      </ul>
</details>

<br>

- `/` is a critical directory in Linux systems, it is the **root** directory
  - All other storage branches from this location, even other drives (in /mnt)
  - If you are using WSL you will be able to use your Windows drives (c, d, etc) in /mnt (for more on WSL-specific usage see the [WSL Workshop](/WSL_Workshop))

<br>

#### Exercise 3.51

- Try the commands
- Use pwd to see where you are at any point, or look at the prompt

```bash
cd /
pwd
cd home
cd ..
pwd
cd
cd ../..
pwd
cd lib # change to lib while in Root
cd
cd lib # change to lib while in user directory
```

- Note that using paths like `home` or `lib` only works if they are a subdirectory of your current directory, otherwise a full or absolute path must be used
- Absolute path will include the full address to the location, whereas a relative path uses `.` and `..`
- The package `tree` can be used to view the file structure
  - For instructions on how to install packages using `apt` see [Using WSL](/WSL_Workshop/Using_WSL.md)
- A useful command for viewing the absolute path of files is `realpath`
  - For more in-depth information, see the help text
  - Simple usage is to use `realpath DIRNAME/*` to see the abs path of all files in the given directory

- **Example**
  - If you are in `/home` and wish to go to your user account, this can be achieved by using `cd USERNAME` (substituting your own account name)
  - The relative path to do the same thing is `cd ./USERNAME`
  - An absolute path includes all the directories from root
    - For my directory to create this workshop I have a folder called `gitlab_gccode`, and within that is `linux_resources` (remember no spaces in files/folders!)
    - The absolute path is `/home/mat/gitlab_gccode/linux_resources` whereas if I was already in my user directory, I could just use `gitlab_gccode/linux_resources` as a relative path

<br>

### Challenge 3.6

- Find a system file called "fstab" (**F**ile **S**ystem **TAB**le) using the commands from this session
- Exploration only. DO NOT try to modify anything - just navigate directories and check for contents
- Hint: it can be useful to list contents in 1 column (default is alphabetical descending sort)

<details>
  <summary>Solution</summary>
    <ul>
      <li>cd /etc/fstab</li>
      <li>The directory is in root -> etc -> fstab </li>
      <li>fstab can be configured to mount drives upon system startup, such as network drives </li>
    </ul>
</details>

<br/>

- **Discussion**
  - Were you able to find the file? Why or why not?
  - Relative vs absolute paths
  - '~' refers to /home/USERNAME/
  - To find username use `whoami`

<br>

### 3.7 `exit`

- **`exit` - exit the shell**
- Likely the most simple command you will use!
- Do not use this yet if you wish to do the extra questions

<br>

### 3.8 Questions

<br>

---

## 4.0 Extras

- This section will not be covered during the 1 hour workshop session, they are completely optional
- Answers can be obtained from the tutorial material or by using the bash commands
  - Some questions will invite you to research on the internet to give greater context or understanding

<br>

### 4.1 Questions

1. When could your pwd be different from the actual directory you are in?
2. How do you view hidden files? What are some of the hidden files in your home directory?
3. Type in the command `yes` and press enter. What do you do now?

<details>
    <summary>This will reveal all the answers, please go through as many as you can before looking</summary>
        <ul>
            <li> 1. This can occur during a script, the working directory can vary depending on the files that are being altered </li>
            <li> 2. Using the command `ls -a`. Files relating your bash shell such as .bash_history, .bashrc, and .bash_logout are common </li>
            <li> 3. The only way out of this loop is <b>Ctrl+c</b> </li>
        </ul>
</details>

<br>

## Fun Fact

- The mascot for Linux is Tux

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/TuxFlat.svg/800px-TuxFlat.svg.png" alt = "Tux" width="150"/>

- The document you are reading is written in a language called "Markdown", if you view the source in the main gitlab repo you will see what the unformatted version looks like
  - The click-to-expand sections are written using raw html
