# Introduction to Linux Tutorial Part 4

[[_TOC_]]

---

- This section will mainly be a placeholder until there is a better idea of which material will spillover from parts 1, 2, 3

## 1.0 Overview

- This is **part four** of four sessions designed to be delivered in a virtual group setting
- This can also be worked through at a self-directed pace outside of workshop sessions
- The material is meant for those with little or no experience with Linux, but can be helpful for intermediate users as well

### 1.1 Prerequisite(s)

- Completion of Intro to Linux parts 1,2 and 3 (or at least familiarity of the material)
- Shell environment (WSL, Biocluster, online terminal, MobaXTerm-local)

### 1.2 Objectives

- Overall objective --> build a foundation of skills to be confident in using bioinformatics tools in Linux
- This session will focus on some useful utilities in the command line and file permissions

### 1.3 Commands and topics covered in this session

- **Commands**
  - `less`, `cat`, `more`, `echo`, `tar`, `wget`
- **Topics**
  - symbolic links (symlinks)

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
  - `rmdir`, `mv`, `file`, `chmod`, `ll`

### 2.1 Review Exercises

- Here is a self-directed exercise to review the commands from part 3
  - Do as much as you can using the command names above, referring to `--help` if you're stuck
  - Clicking the expansion below will reveal all the suggested solutions

1. What is the difference between -i and -I in rm?
2. What is the functional purpose of `touch`?
3. What is the difference between an absolute path and relative path? --> can you give an example of either of them?
4. What does `&&` do between commands?
5. What is the difference between `-v` and `--verbose` for `rm` or `mkdir`?
6. What does the `*` character do?
7. (Challenge Question) What will happen if you use `rm -Iv` on 3 or less target files? You can test this to verify

<details>
    <summary><b>Solutions</summary>
      <ul>
        <li>1. '-i will prompt for each delete, -I will prompt for a group of > 3 files (or a folder)'</li>
        <li>2. To create an empty file</li>
        <li>3. Absolute path is the full path from root. Relative path is defined by the pwd (present working directory). An example would be if you are in /home/user/testdir. This is the absolute path, root --> home --> user --> testdir. The relative path from testdir to your user folder is simply ../ (`..` is up one level in the directory structure)</li>
        <li>4. If the first command executes correctly, it will allow another command to execute in the same line </li>
        <li>5. There is no difference other than the appearance. They are the short and long form for the same options. There must be a space between long form options</li>
        <li>6. `*` will match 0 or more characters.</li>
        <li>7. It will not prompt at all, the files will be removed.</li></b>
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
    <summary><b>Solution</summary>
      <ul>
        <li>The information is being displayed by the `less` command</li>
        <li>Usually help text is displayed using `cat`</li></b>
      </ul>
</details>

</br>

Try the command(s)

```bash
less /usr/share/common-licenses/GPL-3
h
# note the commands to move by lines, pages, and search
q
e
y
f
b
/
?
q
less -N /usr/share/common-licenses/GPL-3
```

- It is not necessary to memorize the commands for `less`, but it is important to know where they are

<br>

### 3.2 `echo`

- `echo` is used to display a line of text
- This can be very simple, but in combination with other options and commands it is very versatile
- As per usual, start with `echo --help`
- Now instead use `man echo`
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
  - What does the backslash (\\) do?

<br>

### 3.3 `tar`

### 3.4 `wget`

### 3.5 Variables

<br>

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

1. TBD

<details>
    <summary><b>Empty</b></summary>
        <ul><b>
            <li> Empty here too </li>
        </p></b>
</details>

<br>

### 4.3 Fun Facts

- Why are Linux users so introverted? - They never get out of their shell!
- How can you tell if someone uses Linux? - Oh don't worry about it they'll tell you themselves!
- Linux and other computer tech often have little easter eggs and jokes - programmers do not take things too seriously
  - sl
  - cowsay
  - apt moo

<br>
