# Introduction to Linux Tutorial Part 1

- [Home page of the repository](../README.md)
- [Introduction to Linux overview](/Introduction_to_Linux)

---

## 1. Overview

- Introduction
- Review of "Home" page or README

<br>

- The material is meant for those with little or no experience with Linux, but can be helpful for intermediate users as well
  - These sessions are introductory. It takes time and practise to become proficient with Linux (as with any new technology skill)
  - Patience for both instructors and learners will help everyone to achieve their best results
- This material is largely derived from the book [The Linux Command Line](https://linuxcommand.org/tlcl.php) by William Shotts
  - **This is an excellent resource for further study!**
- Here are some other resources for Linux and Bioinformatics related training
  - freecodecamp.org has great resources for many tech-related topics, including Linux and command line!
    - [The 50 Most Popular Linux & Terminal Commands - Full Course for Beginners](https://www.freecodecamp.org/news/learn-the-50-most-used-linux-terminal-commands/) is a 5-hour video (best to watch in pieces) that will cover much more than this tutorial. It is fairly recent and well curated for useful commands. 
    - [Command Line Crash Course](https://www.youtube.com/watch?v=yz7nYlnXLfE) is a 35-minute video with the basics of the command line. 
    - [The Linux Commands Handbook](https://www.freecodecamp.org/news/the-linux-commands-handbook/) has a long list of useful commands with useful details about them.
  - Excellent and in-depth Linux Tutorial - [Ryan's Tutorials](https://ryanstutorials.net/linuxtutorial/)

<br>

### 1.1 Prerequisites

- Access to the GPSC is prefered, but any `bash` command line will suffice.
  - If you do not have access to the GPSC or the Biocluster and are a Windows user, you may follow [this guide](/WSL_Workshop/WSL_installation.md) to install Ubuntu in Windows Subsystem for Linux (WSL). Note that WSL is permitted on AAFC workstations, but that may not be the case in other departments.
  - [Replit](https://replit.com) also offers a browser-based `bash` command line. Note that some of the commands covered in this tutorial aren't available on this platform.


<br>

### 1.2 Objectives

- Overall objective --> build a foundation of skills in Linux
- Learn some background information about Linux
- Define some key terms related to Linux and the command line interface (CLI)
- Study and practice some basic command line functions

<br>

### 1.3 Commands covered in this session

- `pwd`, `cd`, `ls`, `--help`, `man`, and `exit`
- It is arguably more important to learn how to use commands than to learn the commands themselves
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
- not all commands have `--help` configured

- We will use `man` as the default for the workshop
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
  - Sequence files are usually in `.fasta`, which is essentially a text file. Command line tools can interact very well with text files
  - It is simple to setup environments with specific compilers, languages, tools, etc. Containers are a relatively new option for this
    - eg. May need tools that work for version 2.15.1 and not 2.16
- Open source nature of Linux and bioinformatics tools
- High performance computers (HPCs) usually have a Linux operating system (OS)
  - When connecting to HPC (e.g. GPSC), the command line is your interface

<br>

### 2.3 Definitions

NOTE: Some organizations use terms more specifically, these are the general definitions.

- Command line interface (CLI)
  - Text session where the user enters commands with options and arguments. Output is displayed from the OS
- Shell
  - Program that takes commands from the keyboard and interprets them for the OS
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
  - A popular Linux distribution based on Debian (another distribution)
  - Widely used and considered to be very user-friendly
- Terminal
  - The terminal gives access to the shell - e.g. The window or program that allows you to use bash or another shell
  - Can refer to the software that hosts the shell/CLI
  - Can also refer to the physical hardware used to interface with the OS
- Prompt
  - Short for command prompt, refers to the small section preceding a command
  - In bash this has:
    - User
    - Name of the computer
    - Current directory
    - Usually ends with $
- GUI (pronounced gooey)
  - Graphical user interface
- WSL (Windows Subsystem for Linux)
  - A compatibility layer allowing Linux commands in Windows. Linux distributions are installed and can use most command line features.

<br>

### 2.4 Questions

<br>

---

## 3. Instructions

### 3.0 Access the CLI (command line interface)

- If you are connected to the GPSC, the Biocluster, or are in Ubuntu in WSL, you are already using the CLI
- In an Ubuntu desktop environment, you can use the "Terminal" application for the CLI. Alternatively you can use `Ctrl-Alt-T`

<br>

### 3.1 Basic Navigation

There are shortcuts to help navigate the CLI. These shortcuts range from simple to complex, but all make for a much greater shell experience.
- `tab` - will autocomplete if you begin to write a command that is part of bash-completion, or a filename in a given directory
- `up arrow` - will scroll to previous commands entered in the shell
  - You can navigate back through these commands with the `down arrow`
- `>` `<` - used to control cursor placement in the text
- **copy/paste** - this can depend on which terminal you are using, and the configurations
  - Typically, paste is `right-click`
  - On the GPSC can use `ctrl+shift+c` and `ctrl+shift+v` used for copy and paste respectively (hold `ctrl`, `shift`, then press the `c` key. To paste hold `ctrl`, `shift`, then press `v`)
- `ctrl+c` - interrupt/kill the current process in the terminal

#### Exercise 3.1.1

  - Copy some text from outside your shell and paste it into the command line
  - This does not need to execute properly in Linux, in fact it's safer if it doesn't
  - Feel free to use text from this tutorial

- We will learn to use these navigation shortcuts throughout the tutorial

<br>

### 3.2 `pwd`

**`pwd` - print name of current working directory**
  - This shows the directory in which you are currently located (working)
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
        <li>e.g. <code>file1</code> and <code>File1</code> are completely separate files in Linux (not in Windows)</li>
      </ul>
</details>

<br>

### 3.3 `ls`

**`ls` - list directory contents**
  - Shows the files and directories of a given location (defaults to `.`, your current directory, unless an argument is provided)
  - Not restricted to your current directory, can specify a location to use `ls` without changing your current working directory
  - The directory that is specified at the end of this command is a **command argument**

Try the commands

```bash
cd # make sure to begin in your user directory
ls
ls . # The command above defaults to `.` as the location, unless one is specified
ll -s # ll may not be an "alias" in your shell
ls /
ls -a
ls -A # may be set to "la" in your shell
ls -a /home
ls -al
```

- `ls -a` uses a **command option** to see all contents, including hidden files and directories that start with a `.`
  - eg. Hidden files -> `.bash_history` in your home directory (your 'user' directory)
  - In some systems this is *aliased* to `la` (more on `alias` later)
  
- `ls -a /home` combines an option, `-a`, with an argument, `/home`

- **Discussion**
  - What are some other options we can use with `ls`?
  - How do they help?

<details>
    <summary>Solution</summary>
      <ul>
        <li>These are not the only options, as all arguments have their usages</li>
        <li><code>-h</code> for human readable (when viewing file sizes)</li>
        <li><code>-l</code> use long list format
        <li><code>-s</code> to view the file size</li>
        <li><code>-S</code> to sort by file size</li>
        <li><code>-t</code> to sort by modification time</li>
        <li><code>-1</code> to view in one column, </li>
      </ul>
</details>

<br>

### 3.4 Command Line Options and Arguments

- These are important for basic linux and in scientific tools
- A good way to learn them is to view the `man` pages before attempting to use a command

```bash
man pwd
```

- These options can enhance the usage of a command - displaying the changes, or asking for inputs, etc.
- The command is what you want to do, the options/parameters are how you want to do it, and the arguments are the things you want to apply these to
- Options are usually not required, but for some commands they are necessary
- These options can be used together, for instance `ls -1hast` will display all contents in one column sorted by last modification time with the "human readable" size listed as well. This is equivalent to `ls -1 -h -a -s -t` or `ls -1ha -st`

<br>

### 3.5 `cd`

- **`cd` - change directory**
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
        <li><code>man cd</code></li>
      </ul>
</details>

<br>

- `/` is a critical directory in Linux systems, it is the `root` directory
  - All other storage branches from this location, even other drives (in `/mnt`)
  - If you are using WSL you will be able to use your Windows drives (c, d, etc.) in `/mnt` (for more on WSL-specific usage see the [WSL Workshop](/WSL_Workshop))

<br>

#### Exercise 3.51

- Try the commands
- Use `pwd` to see where you are at any point, or look at the prompt

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
- A useful command for viewing the absolute path of files is `realpath`
  - For more in-depth information, see the help text
  - Simple usage is to use `realpath DIRNAME/*` to see the abs path of all files in the given directory

- **Example**
  - If you are in `/home` and wish to go to your user account, this can be achieved by using `cd USERNAME` (substituting your own account name)
  - The relative path to do the same thing is `cd ./USERNAME`
  - An absolute path includes all the directories from root
    - In my home directory, for this workshop, I have a directory called `tutorials`, and within that is `linux_intro` (remember no spaces in files/directories!)
    - The absolute path is `/home/meb000/tutorials/linux_intro` whereas if I was already in my user directory, I could just use `tutorials/linux_intro` as a relative path

<br>


### 3.6 `exit`

- **`exit` - exit the shell**
- Likely the most simple command you will use!
- Do not use this yet if you wish to do the extra questions

<br>

### 3.8 Questions

<br>

---

## 4.0 Extras

- This section will not be covered during the hour workshop session, they are completely optional
- Answers can be obtained from the tutorial material or by using the bash commands
  - Some questions will invite you to research on the internet to give greater context or understanding

<br>

### 4.1 Questions

1. When could your pwd be different from the actual directory you are in?
2. How do you view hidden files? What are some hidden files in your home directory?
3. Type in the command `yes` and press enter. What do you do now?

<details>
    <summary>This will reveal all the answers, please go through as many as you can before looking</summary>
        <ul>
            <li> 1. This can occur during a script, the working directory can vary depending on the files that are being altered </li>
            <li> 2. Using the command <code>ls -a`</code>. Files relating your bash shell such as <code>.bash_history</code>, <code>.bashrc</code>, and <code>.bash_logout</code> are common </li>
            <li> 3. The only way out of this loop is <code>Ctrl+c</code>. It may take a few moments before the loop actually stops after you pressthe command.<li>
        </ul>
</details>

<br>

## Fun Fact

- The mascot for Linux is Tux

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/TuxFlat.svg/800px-TuxFlat.svg.png" alt = "Tux" width="150"/>

- The document you are reading is written in a language called "Markdown", if you view the source in the main GitHub repo you will see what the unformatted version looks like
  - The click-to-expand sections are written using raw html
