# Introduction to Linux Tutorial Part 4

- [Home page of the repository](../README.md)
- [Introduction to Linux overview](/Introduction_to_Linux)

[[_TOC_]]

---

## 1.0 Overview

- This is **part four** of four sessions designed to be delivered in a virtual group setting
- This can also be worked through at a self-directed pace outside of workshop sessions
- The material is meant for those with little or no experience with Linux, but can be helpful for intermediate users as well

### 1.1 Prerequisite(s)

- Completion of Intro to Linux parts 1,2 and 3 (or at least familiarity of the material)
- `bash` command line (Ubuntu in WSL will be the default for all commands shown)

### 1.2 Objectives

- Overall objective --> build a foundation of skills to be confident in using bioinformatics tools in Linux
- This session will focus on some useful utilities in the command line and file permissions
- This session contains more intermediate commands - however it is not necessary to remember them all - use this guide as a reference
  - Part of learning Linux/command line is knowing where to find resources for when you need them later
  - Unless you use something constantly you will need to lookup command names and options

### 1.3 Commands and topics covered in this session

- **Commands**
  - `less`, `cat`, `more`, `echo`, `tar`, `wget`
- **Topics**
  - Variables

- Reminder: information about commands can be accessed within a terminal by using

```bash
man <command_name>
<command_name> --help
whatis <command_name> # one line summary
```

- more documentation at [manual-pages](https://www.kernel.org/doc/man-pages/)

### 1.4 Questions?

</br>

---

## 2.0 Review

- Review of part 3
  - `rmdir`, `mv`, `file`, `chmod`, `ll`, `type`, `alias`, `ln`

### 2.1 Review Exercises

- Here is a self-directed exercise to review the commands from part 3
  - Do as much as you can using the command names above, referring to `--help` if you're stuck
  - Clicking the expansion below will reveal all the suggested solutions

1. What will `rmdir` do if you target a non-empty directory?
2. How can you distinguish between renaming and moving file(s) with `mv`?
3. What are the `ls` options included in the preset `ll` command? Which command can you use to figure this out?
4. Which option is the most common and useful for `ln`?
5. (Challenge) What do the following characters mean in regards to file/directory details?
  a. `d`, `l`, `-`, `r`, `w`, `x`

<details>
    <summary><b>Solutions</b></summary>
      <ul>
        <li>1. A warning message is given and the directory is NOT removed</li>
        <li>2. The simple answer is that `moving` a file within the same directory renames it, and targeting another directory moves it. What is really happening is that you are modifying the absolute path of the file, whether it is just location(moving) or also changing the last portion of the absolute path (name)</li>
        <li>3. `ls -a -l -F` (shown separately for detail), also equivalent to `ls -alF`. To find this alias use `type`</li>
        <li>4. `-s` to create a symbolic link</li>
        <li>5. d = directory, l = link, `-` = file, `r` = read, `w` = write, `x` = execute</li>
      </ul>
</details>

<br>

---

## 3.0 Instruction

### 3.1 `less`, `more`, and `cat`

- These are all commands to view text in a file
  - `cat` displays the contents to the output
    - 'concatenate file(s) to the standard output'
  - `more` views a file one page/screen at a time
  - `less` is a play-on-words of "less is more", and is very similar to `more` but with improvments
  - As always, let's look at `less --help`

- **Question**
  - This looks different than with usual help text, why is this?

<details>
    <summary><b>Solution</b></summary>
      <ul>
        <li>The information is being displayed by the `less` command</li>
        <li>Usually help text is displayed using `cat`</li>
      </ul>
</details>

</br>

Try the command(s)

```bash
less -N /usr/share/common-licenses/GPL-3
h # Display the help text
# note the commands to move by lines, pages, and search
q # Quit (in this case from the help text)
e # Forward one line
y # Backward one line
f # Forward one window
b # Backward one window
/`pattern` # Search forward for matching line
?`pattern` # Search backward for matching line
q # Quit - this time from `less`
```

- It is not necessary to memorize the commands for `less`, but it is important to know where they are (remember `h` within `less`)

<br>

### 3.2 `echo`

- `echo` is used to display a line of text
- This can be very simple, but in combination with other options and commands it is very versatile
- As per usual, start with `echo --help`
  - However, this doesn't work. Instead try `/bin/echo --help`
  - Alternatively, use `man echo`
  - There is really not much in terms of options, but we'll see some other ways to use it

Try the commands

```bash
cd
echo *
echo t*
echo .*
echo $((5*5))
echo Five times five is $((5*5))
echo {Z..A}
echo $(ls -l)
echo \ # you will need to type additional text and press enter/return again
echo \\
```

- **Discussion**
  - There are many other examples but we'll stop there and discuss these ones
  - What is the difference in parentheses for some expressions?
  - What does the backslash (\\) do in this example?

<br>

### 3.3 `tar` and `gunzip`

- **`tar` - GNU 'tar' saves many files together into a single tape or disk archive, and can restore individual files from the archive**
  - common archiving utility
- help text is very lengthy, here are some common examples (these are from the help text)
  
```bash
  tar -cf archive.tar foo bar  # Create archive.tar from files foo and bar.
  tar -tvf archive.tar         # List all files in archive.tar verbosely.
  tar -xf archive.tar          # Extract all files from archive.tar.
```

- `-c` creates an archive
- `-x` extracts an archive
- `-f` use archive file or device archive
- `-t` displays or lists files in archived file
- `-v` verbosely list files processed
- `-z` zip, filter the archive through gzip (zip or unzips)

- The most common usage in my experience is `tar -xvzf file.tar.gz` to extract and unzip

- **`gzip` - Compress or uncompress FILEs**
  - Often used as part of tar, but still helpful to know as a separate command
  - The help text is relatively small, but there are many useful options
    - Note `-k` for keep, as gzip will compress them remove the original
- **`gunzip` - Uncompress FILEs**
  - Very similar options to `gzip`
  - Use to uncompress the .gz file back to the original file

Try the commands

```bash
# If you do not already have a `playgound`, make some files
touch files{0..6}.txt
# Zip them into gzip format with
gzip -v files*
# Unzip them back to txt files
gunzip -v *.gz
# Combine them all into an archive as gz files
# c = create archive, f =  archive file
# z = gzip, gunzip, v = verbose
tar -czvf archive_files.tar files*
# Now to unpack them and unzip them
# x = extract or get
tar -xzvf archive_files.tar
```

- **Discussion**
  - What happened to the files once added to the .tar archive?
    - `--remove-files` will modify this
  - Note the use of the wildcard with the file extension, this is another method to match all files of a certain extension

### 3.4 `wget`

- **`wget` - GNU Wget 1.20.3, a non-interactive network retriever.**
  - In simple terms, use this to download a file from a web address
  - It is usually pre-installed, but this is not guaranteed
  - There are many options available if needed, but in it's simplest form it looks like this

```bash
wget -v [url address]
```

- `wget` is non-interactive - which means it can even work when you are not logged in. This can be useful in scripts when files must be downloaded.
- When learning to use this command it can be helpful to use the option `--spider`, which will not download anything, but check that the target exists

```bash
wget -v --spider https://repo.anaconda.com/miniconda/Miniconda3-py39_4.9.2-Linux-x86_64.sh
```

- This file is the installer for conda - a package and environment manager system that is very useful in bioinformatics
  - There is now a user guide for conda [here](../Conda/README.md)

### 3.5 Variables

- This concept becomes more useful in bash scripting, but we will discuss some of the basics here
- A name and value are provided and a reference is created

```bash
me=Batman
who_am_I="I am" # requires quotations to capture two words
nocturnal="the night"
# Now print these variables
echo $me # $ indicates a variable, if we used 'me' it would simply print the word, not our variable
echo $who_am_I # try using `tab` for autocomplete
echo $nocturnal
# Variables can be combined
combined="$who_am_I $nocturnal"
echo "I'm $me, $combined"
# Variables can be re-assigned 
me="Lego Batman"
echo "I'm $me, $combined" # use 'up arrow' twice to access previous command instead of re-typing it
```

### 3.6 Questions?

<br>

---

## 4.0 Extras

- This section will not be covered during the 1 hour workshop session, they are completely optional
- Answers can be obtained from the tutorial material or by using the bash commands
  - Some questions will invite you to research on the internet to give greater context or understanding
- Now that you have a basic mastery of using the `--help` command, there is a package you can install that will highlight the most common or simple usage of many commands called `tldr` (too long, didn't read)
  - Use `sudo apt install tldr` then simply use `tldr "command name"'
  - This package is another tool to learn commands along with `man`, `--help`, and `whatis`

<br>

### 4.1 Challenge Questions

1. If you had three types files (let's assume there are 100s of digits after the name in each) -> Jim.txt, Jim.md, and James.txt -> How could you filter to choose only the Jim.txt files??

<details>
    <summary><b>This will reveal all the answers, please go through as many as you can before looking</b></summary>
        <ul>
            <li>1. Pattern matching can apply in various ways. In this case you need the characters 'J' and 'i', as 'J' alone would match 'James'. Then you can specify '.txt' at the end. Everything else in the middle can be captured with  '*'. So final answer 'Ji*.txt' </li>
        </ul>
</details>

<br>

### 4.2 Fun Facts

- Joke: Why are Linux users so introverted? - They never get out of their shell!
- The name Linux comes from the first name of the "creator" of Linux, Linus Torvalds, combined with Unix
- There are many distributions that use the Linux kernel - the core of the OS
  - The most popular is Ubuntu, which itself is based on Debian
- The components of a "Linux" system include: the kernel, the GNU utilites (including the terminal), the X server (which produces the graphics), the desktop environment, and more
  - Some versions/distros modify others - such as Linux Mint. It is based on Ubuntu (which is based on Debian). Mint and Ubuntu are generally accepted as the most beginner friendly.
- One of the underlying philosophies of Linux/GNU is that each program does one thing well. This is seen in the `tar` and `gzip` commands. They each have one specific purpose and do one thing well. You must often use them together to get the required result, there is no command that does both as that would violate this philosophy.

<br>
