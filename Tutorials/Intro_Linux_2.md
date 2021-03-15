# Introduction to Linux Tutorial Part 2

[[_TOC_]]

---

## 1.0 Overview

- This is **part two** of three sessions designed to be delivered in a virtual group setting
- It will be about 1 hour of instruction with an additional 0.5 hours set aside for extra material and questions
- This can also be worked through at a self-directed pace outside of workshop sessions
- The material is meant for those with little or no experience with Linux, but can be helpful for intermediate users as well

### 1.1 Prerequisite(s)

- Completion of Intro to Linux part 1 (or at least familiarity of the material)
- Shell environment (WSL, Biocluster, online terminal, MobaXTerm-local)

### 1.2 Objectives

- Overall objective --> build a foundation of skills to be confident in using bioinformatics tools in Linux
- This session will focus on manipulating files and directories
  - Other snippits will be included such as operators and line comments

### 1.3 Commands and topics covered in this session

- **Commands**
  - `whatis`, `mkdir`, `touch`, `rm`, `rmdir`
- **Topics**
  - symbolic links (symlinks), operators, wildcards

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

<br>

- Corrections/Clarifications
  - `ls` is not a version of `ll`, it's the opposite (`ll` is short for `ls -alF`)
  - Also discovered that `la` is a shortcut for `ls -A` (`-A` is almost-all, omits `.` and `..`)
    - We'll discuss these shortcuts more in part 3
  - Clarify bash vs. shell
    - `bash` is a command language, acts as your shell (inside a terminal)
    - `fish` or `zsh` are other shells (`zsh` is now the standard on macOS devices)
  - Challenge exercise in part 1 now looks for a file called `fstab`, not for dir called `apt`

<br>

---

## 3.0 Instruction

### 3.1 `mkdir`

- **`mkdir` - make directory**
- View the help text using `mkdir --help`
- It is best to only use arguments if you understand the consequences

Try the commands

```bash
cd
mkdir -v testdir
```

- **Discussion**
  - What does `-v` add to this command?
    - This a very useful argument for many commands
  - Which option should we use to create multiple nested directories?

<details>
    <summary><b>Solution</summary>
        <ul>
            <li>The option -v is for verbose (prints out what the command is doing)</li>  
            <li>To create nested directories we need the option -p or --parents</li>
            <li>This will make parent directories as needed </li>
            <li>Sometimes using the full name of the command options gives clarity to what the option is doing</li></b>
        </ul>
</details>

<br>

Additional commands

```bash
mkdir --parents --verbose testdir/testdir1/testdir2
mkdir -v testingdir0 testingdir1
```

- **Discussion**
  - What is the resulting difference in these two commands?

<details>
    <summary><b>Solution</summary>
        <ul>
            <li>Nested directories vs. separate directories</li>
            <li>In the man page/help text you can determine if a command has multiple 'targets' by looking for the elipsis ("...")</li>
            <li>If you have access to the command `tree` you can see this in the directory structure</li></b>
        </ul>
</details>

<br>

### 3.2 `touch`

- **`touch` - change file timestamps**
- The common usage is to create an empty file
- The options are for very specific use-cases, generally just use `touch FILENAME`

Try the commands

```bash
cd && ls
cd testdir
touch file1 file2.txt
```

- Commands can be chained together in bash with `&&`
  - Note that other shells have different operators (eg. `;` in fish)
- We will look at other operators in part 3
- File types must be assigned manually (`.txt` `.fastq` `.md` etc.)

#### Exercise 3.21

- Create a file in testdir1 and testdir2 in a single command
- Name these files whatever you would like

<details>
    <summary><b>Solution</summary>
        - touch testdir1/filewhatever testdir1/testdir2/filewhatever1</b>
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
    <summary><b>Solution</summary>
        - let's start by using -iv for interactive, verbose</b>
</details>

<br>

Try the commands

```bash
cd && ls
cd testdir/testdir1 && ls
rm -iv filewhatever # substitute whichever filename you used
rm -iv testdir2
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
    <summary><b>Solution</summary>
        <ul>
            <li> Look at the documentation/arguments</li>
            <li> For a directory we need to use -r (recursive)</li>
            <li> Recursion - a method of solving a problem where the solution depends on solutions to smaller instances of the same problem </li>
            <li><a>https://en.wikipedia.org/wiki/Recursion_(computer_science)</a></li></b>
        </ul>
</details>

<br>

Try the commands

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

Try the commands

```bash
cd && ls
cd testdir/
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

Try the commands

```bash
rm -Iv file* # remember this is the same as using ./file*
# rm defaults to the current dir unless one is specified
ls # also defaults to current dir, same as using ls .
```

- The matching removes all files that begin with 'file'
  - The `*` will match 0 or more characters
- Using the option `-I` prompts for the delete of all files, instead of individually like with `-i`
- This is a very basic form of regular expressions (RegEx), which are very difficult but useful tools to filter through files or anything related to strings or expressions
- We will not cover regex in any of the tutorials, but you are welcome to look it up for yourself

### 3.4 `rmdir`

- **`rmdir` - remove empty directories**
- A simple version of rm for directories - checks if they are empty, if so then deletes
- As always, worth looking at the help text `rmdir --help`
  - `-p` and `-v` are useful options once again

Try the commands

```bash
cd
mkdir -pv emptydir/emptydirs{1..7}
ls
rmdir -pv emptydir
rmdir -pv --ignore-fail-on-non-empty emptydir
```

- The option --ignore-fail-on-non-empty was required because the subdirectories mean the main directory was not actually empty
- An alternate way to do this is:

```bash
mkdir -pv emptydir/emptydir{1..10}
rmdir -v emptydir/* emptydir
```

- By removing the subdirectories first we ensure that the parent `emptydir` is empty when rmdir executes on it

<br>

### 3.5 Questions?

---

## 4.0 Extras

- There should be about 30 minutes after each workshop to work on these questions and exercises with an instructor available for help if needed
- These can also be completed at your own pace outside of workshop sessions
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
        <ul><b>
            <li> 1. `mkdir dir{A..Z}` and `mkdir dir{A..Z}{z..a} </li>
            <li> 2. `rm -rIv dir*` --> the I is for an interactive prompt, but now it only asks once for all the dirs together </li>
        </p></b>
</details>

<br>

### 4.3 Fun Facts

- \#notafact -> Astronauts use Linux - they can't open Windows in space!
- This tutorial was created using VS Code - an editor from Microsoft that is incredible for markdown, programming, web development, etc.
  - There are extensions to work with different filetypes - including fasta and fastq files
- VS Code is very simple to use inside of Windows (no admin required) and WSL

<br>
