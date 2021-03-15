# Introduction to Linux Tutorial Part 3

[[_TOC_]]

## Mapping out the content

- List of other resources?
- Intro_Linux_0 - show roadmap of each tutorial/session

- `mv`, `less`, `cat`, `more`, `file`, `chmod`, `ll`, `echo`

## 3.0 Instruction part 1

- In a Ubuntu desktop environment, you can use the "Terminal" application for the CLI (command line interface). Alternatively you can use **Ctrl-Alt-T**
- If you are in Ubuntu in WSL or connected to the Biocluster, you're already using CLI

### 3.1 `mv`

- **`mv` - move and rename files**
  - This command can either move or rename a file, it all depends on how it is used
  - View the help text for the command with `mv --help`
  - Moving a file within the same directory will rename the file
  - Moving file(s) to another dir will move the file(s)
  - We need a test directory to manipulate files safely, let's do this first

Try the command(s)

```bash
cd && ls
mkdir -pv testdir/insidedir && cd testdir
touch file0 insidedir/file1
```

- Now we're ready to use `mv`
- What are the arguments we should include?
- Start in testdir

Try the command(s)

```bash
pwd
mv -iv file0 file00
mv -iv file00 insidedir/
```

<br>

### 3.2 `ll`, `type`, and `alias`

- The long listing format of `ls`, exactly the same as `ls -l`
- `ll --help` lists the info for `ls`
- `type` will determine if a command is an `alias` that has been set
- `alias` can be used to shortcut commands to simpler or alternate commands
  - We will not cover how to alias commands, use **caution** and look this up yourself if you wish to know more

Try the command(s)

```bash
type ll
type ls
type type
```

- **Discussion**
  - What are the options for `ll`?
  - What do they do?

- `ll` is important for understanding more about files in our systems
- In the output there is a 10-character section comprising of certain letters or dashes (-) indicating file permissions
  - The first digit is usually `l`, `d`, or `-` meaning link, directory, or file
  - `rwx` stand for read, write, execute respectively
    - The 3 instances of them mean `owner`, `group`, and `world`
  - The digit is the number of hard links
  - Username of the files owner
  - Group that owns the file
  - Size in bytes
  - Date and time of last modification

<br>

### 3.2 `ln` and `file`

- In bioinformatics files can be extremely large, a way to be more efficient is to use symbolic links (aka symlinks) so a file is not duplicated needlessly
- The `ln` command can create links, as always let's look at the options using `--help`
  - For this command we only really need `-s`, it is generally preferable to use symbolic (aka soft) links
- We should have a testdir in place for this, if you do not have one from before please create one

Try the command(s)

```bash
touch scriptfile_macOS scriptfile_linux
ln -s scriptfile_linux scriptfile
ll
```

- **Discussion**
  - When could this be useful?
  - Do you see the link in a different colour?

EDIT - add expansion html for answer each time? For self-directed I suppose it is necessary

- Another useful command that can help inform us about a file is `file`
- Simply outputs information about the file and it's format
  - Also tells basic info for a symlink

Try the command(s)

```bash
touch textfile.txt
file textfile.txt
echo "Some text for the file" >> textfile.txt
file textfile.txt
file scriptfile_linux
file scriptfile
```

- **Discussion**
  - What does `echo` do?
  - What about the `>>` operator?

- intro the command whatis
ENTER THE PROPER ANSWER
<details>
    <summary><b>Solution</summary>
      <ul>
        <li>The information is being displayed by the `less` command</li>
        <li>Usually help text is displayed using `cat`</li></b>
      </ul>
</details>

<br>

### 3.3 `chmod`

- This subject can be very complicated so we are only covering the basics. Use caution with this command!
- Only the file's owner or the superuser can change the permissions (more on superuser later)
- From the `ll` command we can see permissions for a file - read, write and execute for user, group, and world
- In bioinformatics it is sometimes necessary to make a script executable (able to act as a program)
  - So if permissions are rw-, we need to change this to rwx...
  - This can be done using octal numbers representing binary for rwx, but the easier version is to use `u+x`
    - This gives the user permission to execute the file(s)
  
Try the command(s)

```bash
chmod --help
ll
chmod -c scriptfile_linux
ll
./scriptfile_linux
```

- **Discussion**
  - What did the script do?
  - What does the `./` mean?

<br>

### 3.4 `less`, `more`, and `cat`

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

### 3.5 Break

- Take a 5 minute break

<br>

---

## 4.0 Instruction part 2

- Any questions?
- We will now cover `echo`, redirection, variables, and expansion

<br>

### 4.1 `echo`

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

### 4.2 Redirection


Extras - conda??















































## Mapping out the content

- List of other resources?
- Intro_Linux_0 - show roadmap of each tutorial/session
- HOW to look up commands
- other simple commands? cal, date

## Part 3

- review
- head/tail
- apt
- grep
- piping
- df
- nano (incl. cursor tricks)
- environment
- conda??

---

## 1. Overview

- This tutorial is designed to be delivered in a virtual group setting as part two of three sessions
- It will be about 1 hour of instruction with an additional 0.5 hours set aside for exercises
- This can be worked through at a self-directed pace outside of workshop sessions
- The material is meant for those with little or no experience with Linux

### 1.1 Prerequisite(s)

- Shell environment (WSL, Biocluster, cocalc, MobaXTerm-local)
- Completion of Intro to Linux part 1 (or at least familiarity of the material)

### 1.2 Objectives

- Overall objective --> build a foundation of skills to be confident in using bioinformatics tools in Linux
- This session will focus on file navigation and simple commands
- EDIT - more?

### 1.3 Commands and topics covered in this session

- **Commands**
  - `mv`, `less`, `cat`, `more`, `file`, `chmod`, `ll`, `echo`
- **Topics**
  - symbolic links (symlinks), operators, wildcards

- information about commands can be accessed within a terminal by using

```bash
man <command_name>
```

- a shorter summary can often be found by using

```bash
<command_name> --help
```

- more documentation at [manual-pages](https://www.kernel.org/doc/man-pages/)

### 1.4 Questions?

</br>

---

## 2. Review

- Review of part 1
- `pwd`, `cd`, `ls`, `mkdir`, `touch`, `rm`, and `exit`

<br />

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




## 3.0 Instruction part 1

- In a Ubuntu desktop environment, you can use the "Terminal" application for the CLI (command line interface). Alternatively you can use **Ctrl-Alt-T**
- If you are in Ubuntu in WSL or connected to the Biocluster, you're already using CLI

### 3.1 `mv`

- **`mv` - move and rename files**
  - This command can either move or rename a file, it all depends on how it is used
  - View the help text for the command with `mv --help`
  - Moving a file within the same directory will rename the file
  - Moving file(s) to another dir will move the file(s)
  - We need a test directory to manipulate files safely, let's do this first

Try the command(s)

```bash
cd && ls
mkdir -pv testdir/insidedir && cd testdir
touch file0 insidedir/file1
```

- Now we're ready to use `mv`
- What are the arguments we should include?
- Start in testdir

Try the command(s)

```bash
pwd
mv -iv file0 file00
mv -iv file00 insidedir/
```

<br>

### 3.2 `ll`, `type`, and `alias`

- The long listing format of `ls`, exactly the same as `ls -l`
- `ll --help` lists the info for `ls`
- `type` will determine if a command is an `alias` that has been set
- `alias` can be used to shortcut commands to simpler or alternate commands
  - We will not cover how to alias commands, use **caution** and look this up yourself if you wish to know more

Try the command(s)

```bash
type ll
type ls
type type
```

- **Discussion**
  - What are the options for `ll`?
  - What do they do?

- `ll` is important for understanding more about files in our systems
- In the output there is a 10-character section comprising of certain letters or dashes (-) indicating file permissions
  - The first digit is usually `l`, `d`, or `-` meaning link, directory, or file
  - `rwx` stand for read, write, execute respectively
    - The 3 instances of them mean `owner`, `group`, and `world`
  - The digit is the number of hard links
  - Username of the files owner
  - Group that owns the file
  - Size in bytes
  - Date and time of last modification

<br>

### 3.2 `ln` and `file`

- In bioinformatics files can be extremely large, a way to be more efficient is to use symbolic links (aka symlinks) so a file is not duplicated needlessly
- The `ln` command can create links, as always let's look at the options using `--help`
  - For this command we only really need `-s`, it is generally preferable to use symbolic (aka soft) links
- We should have a testdir in place for this, if you do not have one from before please create one

Try the command(s)

```bash
touch scriptfile_macOS scriptfile_linux
ln -s scriptfile_linux scriptfile
ll
```

- **Discussion**
  - When could this be useful?
  - Do you see the link in a different colour?

EDIT - add expansion html for answer each time? For self-directed I suppose it is necessary

- Another useful command that can help inform us about a file is `file`
- Simply outputs information about the file and it's format
  - Also tells basic info for a symlink

Try the command(s)

```bash
touch textfile.txt
file textfile.txt
echo "Some text for the file" >> textfile.txt
file textfile.txt
file scriptfile_linux
file scriptfile
```

- **Discussion**
  - What does `echo` do?
  - What about the `>>` operator?

- intro the command whatis
ENTER THE PROPER ANSWER
<details>
    <summary><b>Solution</summary>
      <ul>
        <li>The information is being displayed by the `less` command</li>
        <li>Usually help text is displayed using `cat`</li></b>
      </ul>
</details>

<br>

### 3.3 `chmod`

- This subject can be very complicated so we are only covering the basics. Use caution with this command!
- Only the file's owner or the superuser can change the permissions (more on superuser later)
- From the `ll` command we can see permissions for a file - read, write and execute for user, group, and world
- In bioinformatics it is sometimes necessary to make a script executable (able to act as a program)
  - So if permissions are rw-, we need to change this to rwx...
  - This can be done using octal numbers representing binary for rwx, but the easier version is to use `u+x`
    - This gives the user permission to execute the file(s)
  
Try the command(s)

```bash
chmod --help
ll
chmod -c scriptfile_linux
ll
./scriptfile_linux
```

- **Discussion**
  - What did the script do?
  - What does the `./` mean?

<br>

### 3.4 `less`, `more`, and `cat`

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

### 3.5 Break

- Take a 5 minute break

<br>

---

## 4.0 Instruction part 2

- Any questions?
- We will now cover `echo`, `redirection`, variables, and expansion

<br>

### 4.1 `echo`

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
echo \ # you will need to type something and press enter/return
echo \\
```

- **Discussion**
  - There are many other examples but we'll stop there and discuss these ones
  - What is the difference in parentheses for some expressions?
  - What does the backslash (\\) do?

### 4.2 Redirection

- 





## Part 2

- start with review!

- chmod (review rm with -f - challenge question)
- wildcard


3. How would create directories 'dirA' through 'dirZ' with one command?
4. How would you remove these directories with one command?

<details>
    <summary><b>This will reveal all the answers, please go through as many as you can before looking</b></summary>
        <ul><b>
            <li> 3. `mkdir dir{A..Z}` </li>
            <li> 4. `rm -rIv` --> the I is for an interactive prompt, but now it only asks once for all the dirs together </li>
            <li> The asterisk symbol will match zero or more characters </li>
        </p></b>
</details>

### Fun Fact

- Astronauts use Linux - they can't open Windows in space!

## Extra

- cal, date, tree, others??