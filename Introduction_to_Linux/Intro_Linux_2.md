# Introduction to Linux Tutorial Part 2

- [Home page of the repository](../README.md)
- [Introduction to Linux overview](/Introduction_to_Linux)

[[_TOC_]]

---

## 1.0 Overview

- This is **part two** of four sessions designed to be delivered in a virtual group setting
- This can also be worked through at a self-directed pace outside of workshop sessions
- The material is meant for those with little or no experience with Linux, but can be helpful for intermediate users as well

### 1.1 Prerequisite(s)

- Completion of Intro to Linux part 1 (or at least familiarity of the material)
- `bash` command line (Ubuntu in WSL will be the default for all commands shown)

### 1.2 Objectives

- Overall objective --> build a foundation of skills to be confident in using bioinformatics tools in Linux
- This session will focus on manipulating files and directories
  - Other snippits will be included such as operators and line comments

### 1.3 Commands and topics covered in this session

- **Commands**
  - `whatis`, `mkdir`, `touch`, `rm`
- **Topics**
  - Operators, wildcards, curly braces

- Reminder: information about commands can be accessed within a terminal by using

```bash
man <command_name>
<command_name> --help
```

- An extremely simple help command that can be useful is `whatis`
- Outputs a single line summary of what a command does

```bash
whatis <command_name>
whatis ls
whatis whatis
whatis mkdir
```

- more documentation at [manual-pages](https://www.kernel.org/doc/man-pages/)

### 1.4 Questions?

</br>

---

## 2.0 Review

- Review of part 1
  - History of Linux and definitions
  - Command line options and arguments
  - `--help`, `man`, `pwd`, `cd`, `ls`, `clear`, and `exit`
- Clarification - console vs shell

### 2.1 Review Exercises

- Here is a self-directed exercise to review the commands from part 1
  - Do as much as you can using the command names above, referring to `--help` if you're stuck
  - Clicking the expansion below will reveal all the suggested solutions

1. Change directory to your 'root' directoty hint - "`/` is root"
2. Now go to your user folder (there is more than one way to do this)
3. List the contents one item per line
4. Now change directory to /home
5. Which option for `ls` will reverse the sorting order?
6. For the command `ls -S /tmp` - which is the option and which is the argument?
7. (Challenge) If you are in your home directory and want to change to root directory using the relative path, what is the command?

<details>
    <summary><b>Solutions</b></summary>
      <ul>
        <li>cd /</li>
        <li>cd  OR cd /home/USERNAME --> use whoami to find username OR cd ~</li>
        <li>ls -1</li>
        <li>cd /home (absolute path) OR cd .. (relative path) </li>
        <li>-r reverses the sort order, by defaults contents are sorted alphabetically</li>
        <li>-S is the option (sort by file size), and /tmp is the argument</li>
        <li>cd ../.. - This goes up 2 parent directories (user --> home --> root)</li>
      </ul>
</details>

<br>

---

## 3.0 Instruction

### 3.1 `mkdir`

- **`mkdir` - make directory**
- View the help text using `mkdir --help`
- It is best to only use options if you understand the consequences

#### 3.11 A Note About Directory Structure

- Previously `testdir` was used as a test directory
  - `linux_workshop` will now be used, and the testfiles will attempt to relate to bioinformatics
  - Examples will also try to emulate real world usage
- In Ubuntu on WSL the user folder is blank upon account creation, in a full Ubuntu system you would have `Documents`, `Downloads`, `Photos`, etc.
- As with filenames, it is important to have detailed names for directories
  - It also helps to structure things so autocomplete can be used easily
    - Use lower case
    - Different starting letters
      - eg. Using p for `projects` and `personal_files` causes an extra step in navigation before using tab. Instead use `projects` and `my_files` to avoid this (if possible)
    - Using dates (YEAR.MO, YEAR-MON-DAY, etc.) can be a great way to keep items structured. Although this may come at the cost of convenience with tools like autocomplete, the benefits exceed the drawbacks when you are further into a structure and do not access it as often

Try the commands

```bash
cd
mkdir -v linux_workshop
```

- **Discussion**
  - What does `-v` add to this command?
    - This a very useful argument for many commands
  - Which option should we use to create multiple nested directories?

<details>
    <summary><b>Solution</b></summary>
        <ul>
            <li>The option -v is for <b>verbose</b> (prints out what the command is doing)</li>  
            <li>To create nested directories we need the option -p or --parents</li>
            <li>This will make parent directories as needed </li>
            <li>Sometimes using the full name of the command options gives clarity to what the option is doing</li>
        </ul>
</details>

<br>

Additional commands

```bash
mkdir --parents --verbose linux_workshop/2021microbiome/raw_data
mkdir -v scripts environments
```

- **Discussion**
  - What is the resulting difference in these two commands?

<details>
    <summary><b>Solution</b></summary>
        <ul>
            <li>Nested directories vs. separate directories</li>
            <li>In the man page/help text you can determine if a command has multiple 'targets' by looking for the elipsis ("...")</li>
            <li>If you have access to the command `tree` you can see this in the directory structure</li>
        </ul>
</details>

<br>

### 3.2 `touch`

- **`touch` - change file timestamps**
- The common usage is to create an empty file
- The options are for very specific use-cases, generally just use `touch FILENAME`

Try the commands

```bash
cd && ls # uses the AND operator
cd linux_workshop
touch manifest.csv manifest.txt
```

- Commands can be chained together in bash with `&&` (this is an operator)
  - This means the second command will only execute after the first command is successful (logical `AND`)
    - Using a semi-colon will ensure the 2nd command will execute regardless of the first command ie. `cd; ls`
- File types must be assigned manually (`.txt`, `.fastq`, `.md`, etc.)

#### Exercise 3.21

```bash
.
└── 2021microbiome
    ├── file1
    └── raw_data
        └── file2
```

- Create a file in 2021microbiome and raw_data (as shown above with file1 and file2) in a single command
- Name them whatever you would like (or use file1 and file2 as defaults, we will delete them shortly)

<details>
    <summary>Solution</summary>
        - touch 2021microbiome/file1 2021microbiome/raw_data/file2
</details>

<br>

### 3.3 `rm`

- **`rm` - remove files or directories**
- Use great caution when learning this command!
- Linux gives users great freedom - one of the great aspects of this OS
  - However this comes with the drawback that mistakes are not prevented, you can delete important files and the system may not stop you

- Let's view some information with `rm --help`

- **Question**
  - which arguments should we use to be cautious when deleting files?

<details>
    <summary><b>Solution</b></summary>
        - let's start by using -iv for interactive, verbose
</details>

<br>

Try the commands

```bash
cd && ls
cd linux_workshop/2021microbiome && ls
rm -iv file1 # substitute whichever filename you used
rm -iv raw_data
```

- \# is used to comment out code in bash, any text after the \# in the same line will not execute
- It is also used as a line comment in python and some other languages
  - There are line comments and block comments
  - Line comments will be ignored by interpreter after the \#
  - Block comments will cause a whole section of code/commands to be ignored
  - This is extremely important in scripting/programming

- **Discussion**
  - Why didn't the last command work?

<details>
    <summary>Solution</summary>
        <ul>
            <li> Look at the documentation/arguments</li>
            <li> For a directory we need to use -r (recursive)</li>
            <li> Recursion - a method of solving a problem where the solution depends on solutions to smaller instances of the same problem </li>
            <li><a>https://en.wikipedia.org/wiki/Recursion_(computer_science)</a></li>
        </ul>
</details>

<br>

Try the commands

```bash
rm -ivr raw_data
```

- This command descends into dir, removes files, then removes the dir itself

- **Question**
  - What if we want to delete multiple files at once?

<details>
    <summary><b>Solution</b></summary>
        <ul>
            <li> For dissimilar files you can list each one separated by a space </li>
            <li> For common bioinformatics situations where filenames are very similar - we need to use wildcard matching </li>
            <li> A "string" is a collection of characters </li>
            <li> The asterisk symbol will match zero or more characters - depending on where it is placed you can match specific patterns</li>
        </p>
</details>

<br>

Try the commands

```bash
cd && ls
cd linux_workshop/
touch filename{01..09}.cpp
ls
touch file{01..09}.py
ls
```

- The curly braces `{}` can be used to generate sequences
  - There are many creative ways to do this, look this up for more examples
  - eg. mkdir dir{1..16..2}{1..10} will create dirs with 1 to 16 counting by 2, combined with each number in sequence 1 to 10
- This dir is getting a bit cluttered, let's remove all the files we just created
- Be **careful** when using `*` in an `rm` command
- You can confirm the files you plan to remove by first using `ls TARGET` to see the list of files, then use `rm` on the TARGET files

Try the commands

```bash
ls file*
rm -Iv file* # remember this is the same as using ./file*
# rm defaults to the current dir (.) unless one is specified
ls # also defaults to current dir, same as using ls .
```

- The matching removes all files that begin with 'file'
  - The `*` will match 0 or more characters
- Using the option `-I` prompts for the delete of all files, instead of individually like with `-i`
- This is a very basic form of regular expressions (RegEx), which are very difficult but useful tools to filter through files or anything related to strings or expressions
- We will not cover regex in any of the tutorials, but you are welcome to look it up for yourself

<br>

### 3.4 Questions?

---

## 4.0 Extras

- This section will not be covered during the 1 hour workshop session, they are completely optional
- Answers can be obtained from the tutorial material or by using the bash commands
  - Some questions will invite you to research on the internet to give greater context or understanding

<br>

### 4.1 Movement Shortcuts

- From **The Linux Command Line** by William Shotts (Chapter 8)
  - "In fact, one of the most cherished goals of the command line is laziness; doing the most work with the fewest number of keystrokes. Another goal is never having to lift our fingers from the keyboard and reach for the mouse."
- These commands can be very efficient in using Linux once you know them well
- The commands with Alt may not work in each environment
  - **Ctrl-a** Move cursor to the beginning of the line.
  - **Ctrl-e** Move cursor to the end of the line.
  - **Ctrl-f** Move cursor forward one character; same as the right arrow key.
  - **Ctrl-b** Move cursor backward one character; same as the left arrow key.
  - **Alt-f** Move cursor forward one word.
  - **Alt-b** Move cursor backward one word.
  - **Ctrl-l** Clear the screen and move the cursor to the top-left corner. The clear command does the same thing.

<br>

### 4.2 Challenge Questions

1. How would create directories 'dirA' through 'dirZ' with one command? What if you wanted to have two letter suffix, one ascending the alphabet while the other descends?
2. How would you remove these directories with one command?

<details>
    <summary><b>This will reveal all the answers, please go through as many as you can before looking</b></summary>
        <ul>
            <li> 1. `mkdir dir{A..Z}` and `mkdir dir{A..Z}{z..a} </li>
            <li> 2. `rm -rIv dir*` --> the I is for an interactive prompt, but now it only asks once for all the dirs together </li>
        </ul>
</details>

<br>

### 4.3 Fun Facts

- \#notafact -> Astronauts use Linux - they can't open Windows in space!
- This tutorial was created using VS Code - an editor from Microsoft that is incredible for markdown, programming, web development, etc.
  - There are extensions to work with different filetypes - including fasta and fastq files
- VS Code is approved software and is very simple to use inside of Windows (no admin required) and WSL

<br>
