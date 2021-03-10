# Introduction to Linux Tutorial Part 1

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
  - This is an excellent resource for further study!

### 1.1 Prerequisite(s)

- Shell environment (WSL, Biocluster, cocalc, MobaXTerm-local)
- **Discuss**
  - Which Linux environments are you using? Poll in the chat
  - Warning for MobaXterm local sessions

### 1.2 Objectives

- Overall objective --> build a foundation of skills to be confident in using bioinformatics tools in Linux
- Learn some background information about Linux
- Define some key terms about Linux and the command line interface (CLI)
- Study and practice some basic command line functions

### 1.3 Commands covered in this session

- `pwd`, `cd`, `ls`, `mkdir`, `touch`, `rm`, and `exit`
- **As this is the very first session we may not cover all the planned material**
  - This will be adjusted over the next 2 sessions if necessary
- It is arguably more important to learn how to use commands than to learn the commands themself
  - Learning how to learn
- Information about commands can usually be accessed within a terminal by using:

```bash
man <command_name>
```

- Not all systems have manual entries for all commands
- A shorter summary can often be found by using

```bash
<command_name> --help
```

- more documentation at [manual-pages](https://www.kernel.org/doc/man-pages/)

### 1.4 Questions

<br>

---

## 2. Introduction

### 2.1 Quick history of Linux

<details>
    <summary><b>Click to expand</b></summary>
        <p>Linux comes from an early operating system called Unix. Users would connect to multi-user mainframe computers by display and keyboard only. Text is very light-weight compared to graphic user interfaces (GUI). Interacting with an operating system above the computer components was a "shell".</p>
        <img src="https://cdn-media-1.freecodecamp.org/images/8dQXHBemVAUp4xgVzFqgEHGyNjCsQT0usHBw" alt = "Shell Diagram" width="200"/>
        <p>Users interacted with the system by sending input and receiving output. Multiple users could use the system simultaneously. They used programs or commands in a programming language - initially sh (shell, or Bourne shell), now bash ("Bourne again shell"). Thus the command line has been the basis of Linux systems ever since. It can be confusing to learn but offers the best performance, can be automated with scripts, and many important scientific tools use the CLI for development.</p>  
        <br>
</details>

<br>

### 2.2 Definitions

NOTE: Some organizations use terms more specifically, these are the general definitions.

- Command line interface
  - Text session where the user enters commands with options and arguments. Output is displayed from the operating system (OS).
- Shell
  - A text-mode application containing a CLI to the OS
  - Note that in casual usage - shell, prompt, terminal, and console all typically refer to the same thing
- Console application
  - A command line program that functions without a required graphical interface
- Bash
  - Commonly distributed shell, or command language interpreter for Linux
  - An enhanced version of the original sh (Bourne shell)
- Ubuntu
  - A popular Linux distribution (distro) based on Debian (another distro)
  - Widely used and considered to be very user friendly
- Terminal
  - Often used synonymously with shell
  - More accurately - the terminal gives access to the shell
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

### 2.3 Questions

<br>

---

## 3.0 Instruction

- In a Ubuntu desktop environment, you can use the "Terminal" application for the CLI (command line interface). Alternatively you can use **Ctrl-Alt-T**
- If you are in Ubuntu in WSL or connected to the Biocluster, you're already using CLI

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

- #### Exercise 3.11

  - Copy some text from outside your shell and paste it into the command line
  - This does not need to execute properly in Linux, in fact it's safer if it doesn't
  - Feel free to use text from this tutorial  

- We will learn to use these other navigation shortcuts throughout the tutorial

<br>

### 3.2 `pwd`

- **`pwd` - print name of current/working directory**
  - This shows the current directory you are located in (aka "working in")
  - It seems very simple but can be helpful for scripts that will use varying working directories while executing

Try the command(s)

```bash
pwd
PWD
```

- **Discussion**
  - Why did the second command not work?

<details>
    <summary><b>Solution</summary>
      <ul>
        <li>Linux is case sensitive, only the exact command will work</li>
        <li>This also applies to filenames and directories</li></b>
      </ul>
</details>

<br>

### 3.3 `ls`

- **`ls` - list directory contents**
  - Shows the files and directories of a given location (defaults to pwd unless specified)
  - This is a shortcut for `ll -s` (we will explore `ll` later)
  - The `-s` is a **command option**
  - These options give flexibility to commands
  - Not restricted to your current directory, can specify a location to use `ls` without changing your `pwd`
  - The directory that is specified at the end of the command is a **command argument**

Try the command(s)

```bash
ls
ll -s
ls /usr/bin
ls -a
ls -a /bin
```

- `ls -a` uses the option to see all contents, including hidden files and folders that start with a `.`
  - eg. `.bash_history` in your home directory (your 'user' folder)
- `ls -a /bin` combines an option, `-a`, with an argument, `/bin`

- **Discussion**
  - What are some other options we can use with `ls`?
  - How do they help?

<details>
    <summary><b>Solution</summary>
      <ul>
        <li>These are not the only options, as all arguments have their usages</li>
        <li>-h for human readable</li>
        <li>-s to view the file size</li>
        <li>-S to sort by file size</li>
        <li>-t to sort by modification time</li>
        <li>-1 to view in one column, </li></b>
      </ul>
</details>

<br>

### 3.4 Command Line Options and Arguments

- these are important for basic linux and especially in scientific tools
- a good way to learn them is to use the `--help` argument before attempting to use a command

```bash
pwd --help
pwd -h
```

- `-h` is often a shortcut for `--help` but can also have a meaning as an argument, use caution and check the options before using a command
- These options can enhance the usage of a command - displaying the changes, or asking for inputs, etc.
- Usually not required, but for some commands they are necessary
- These options can be used together, for instance `ls -1hast` will display all contents in one column sorted by last modification time with the "human readable" size listed as well

<br>

### 3.5 `cd`

- `cd` means change directory (aka folder)
- `/` is used in directory structure (Windows is `\`)
  - The directory location `/` is **root**, there are no separate 'drives' like in Windows
- `.` is your current dir (a single dot character)
- `..` will go to parent (two dots)
- Also helpful, `cd -` (cd 'dash') will go to the previous directory

- **Discussion**
  - How do you view the command line options for `cd`

<details>
    <summary><b>Solution</summary>
      <ul>
        <li>cd --help</li></b>
      </ul>
</details>

<br>

- `/` by istelf is a critical directory in Linux systems, it is the root directory
  - all other storage branches from this location, even other drives (in /mnt)

<br>

#### Exercise 3.51

- Try the command(s)
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
cd etc
cd
cd etc
```

- If it is installed, use `tree` to view the file structure
- Note that using paths like `home` or `etc` only works if they are a subdirectory of your current directory, otherwise a full or absolute path must be used
- Absolute path will include the full address to the location, whereas a relative path uses `.` and `..`

- **Example**
  - If you are in `/home` and wish to go to your user account, this can be achieved by using `cd USERNAME` (substituting your own account name)
  - The relative path to do the same thing is `cd ./USERNAME`

### Challenge 3.6

- Find a system folder called "apt" using the commands from this session
- Exploration only. DO NOT try to modify anything - just navigate directories and check for contents

<details>
  <summary><b>Solution</b></summary>
    <ul><b>
      <li>cd /usr/lib/apt</li>
      <li>The directory is in root -> usr -> lib -> apt</li>
      <li>apt means advanced package tool and handles the installation and removal of software packages</li>
      <li>apt will be discussed in part 3</li></b>
</details>
<br/>

### 3.7 Discussion

- Relative vs absolute paths
- '~' refers to /home/USERNAME/
- To find username use `whoami`

- **Optional** (Do not use in WSL terminal!) - use `clear` to clear your terminal

<br>

### 3.8 Break

- Take a 5 minute break

<br>

---

## 4.0 Instruction

- Any questions?
- We will now cover `mkdir`, `touch`, `rm`, and `exit`

<br>

### 4.1 `mkdir`

- This command is short for 'make directories'
- View the information using `mkdir --help`
- It is best to only use arguments if you understand the consequences

Try the command(s)

```bash
cd
mkdir -v testdir
```

- **Discussion**
  - What does `-v` add to this command?
    - (This a very useful argument for many commands)
  - What should we use to create multiple nested directories?

Additional commands

```bash
mkdir -pv testdir/testdir1/testdir2
mkdir -v testingdir0 testingdir1
```

- **Discussion**
  - What is the resulting difference in these two commands?

<br>

### 4.2 `touch`

- Change file timestamps
- There are many options for this command, but commonly used to create a new file

Try the command(s)

```bash
cd && ls
cd testdir
touch file1 file2.txt
```

- Commands can be chained together in bash with `&&`
- We will look at other operators in part 2 and 3
- File types must be assigned manually (`.txt` `.fastq` `.md` etc.)

#### Exercise 4.21

- Create a file in testdir1 and testdir2 at the same time
- Name these files whatever you would like

<details>
    <summary><b>Solution</summary>
        - touch testdir1/filewhatever testdir1/testdir2/filewhatever1</b>
</details>

<br>

### 4.3 `rm`

- Use great caution when learning this command!
- Linux gives users great freedom - one of the great aspects of this OS
  - However this comes with the drawback that mistakes are not prevented, you can delete important files and the system may not stop you
- `rm` is used to 'remove files or directories'
- Let's view some information with `rm --help`

- **Question**
  - which arguments should we use to be cautious when deleting files?

<details>
    <summary><b>Solution</summary>
        - let's start by using -iv for interactive, verbose</b>
</details>

<br>

Try the command(s)

```bash
cd && ls
cd testdir/testdir1 && ls
rm -iv filewhatever #substitute whichever filename you used
rm -iv testdir2
```

- \# is used to comment out code in bash, any text after the \# in the same line will not execute
- It is also used as a line comment in python and some other languages

- **Discussion**
  - why didn't the last command work?

<details>
    <summary><b>Solution</summary>
        <ul>
            <li> Look at the documentation/arguments</li>
            <li> For a directory we need to use -r (recursive)</li>
            <li> Recursion - a method of solving a problem where the solution depends on solutions to smaller instances of the same problem </li>
            <li><a>https://en.wikipedia.org/wiki/Recursion_(computer_science)</a></li></b>
        </ul>
</details>

<br>

Try the command(s)

```bash
rm -ivr testdir2
```

- This command descends into dir, removes files, then removes the dir itself

- **Question**
  - What if we want to delete multiple files at once?

<details>
    <summary><b>Solution</b></summary>
        <ul><b>
            <li> For dissimilar files you can list each one separated by a space </li>
            <li> For common bioinformatics situations where filenames are very similar - we need to use wildcard matching </li>
            <li> A string is generally a collection of characters </li>
            <li> The asterisk symbol will match zero or more characters </li>
        </p></b>
</details>

<br>

Try the command(s)

```bash
cd && ls
cd testdir/
touch filename{01..09}.cpp
ls
touch file{01..09}.py
ls
```

- The curly braces `{}` can be used to generate sequences
  - There are many creative ways to do this, we will cover some of them in future sessions
- This dir is getting a bit cluttered, let's remove all the files we just created
- Be **careful** when using `*` in an `rm` command

Try the command(s)

```bash
rm -v file*
ls
```

- The matching removes all files that begin with 'file'
- This is a very basic form of regular expressions (RegEx), which are very difficult but useful tools to filter through files or anything related to strings or expressions
- We will not cover regex in any of the tutorials, but you are welcome to look it up for yourself

<br>

### 4.4 `exit`

- When you are finished using the shell, use `exit`
- This simply ends the shell session

<br>

---

## 5.0 Challenge Exercises

- There should be about 30 minutes after each workshop to work on these questions and exercises with an instructor available for help if needed
- These can also be completed at your own pace outside of workshop sessions
- Answers can be obtained from the tutorial material or by using the bash commands
  - Some questions will invite you to research on the internet to give greater context or understanding

<br>

### 5.1 Questions

1. When could your pwd be different from the actual directory you are in?
2. How do you view hidden files? What are some of the hidden files in your home directory?
3. How would create directories 'dirA' through 'dirZ' with one command?
4. How would you remove these directories with one command?
5. 

<details>
    <summary><b>This will reveal all the answers, please go through as many as you can before looking</b></summary>
        <ul><b>
            <li> 1. This can occur during a script, the working directory can vary depending on the files that are being altered </li>
            <li> 2. Using the command `ls -a`. Files relating your bash shell such as .bash_history, .bashrc, and .bash_logout are common </li>
            <li> 3. `mkdir dir{A..Z}` </li>
            <li> 4. `rm -rIv` --> the I is for an interactive prompt, but now it only asks once for all the dirs together </li>
            <li> The asterisk symbol will match zero or more characters </li>
        </p></b>
</details>


<br>

## Fun Fact

- The mascot for Linux is Tux

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/TuxFlat.svg/800px-TuxFlat.svg.png" alt = "Tux" width="150"/>

- The document you are reading is made with a language called "Markdown", if you view the source in the main repo you will see what the unformatted version looks like
  - The expansion sections are written using raw html
