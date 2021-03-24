# Introduction to Linux Tutorial Part 3

[[_TOC_]]

---

## 1.0 Overview

- This is **part three** of three sessions designed to be delivered in a virtual group setting
- It will be about 1 hour of instruction with an additional 0.5 hours set aside for extra material and questions
- This can also be worked through at a self-directed pace outside of workshop sessions
- The material is meant for those with little or no experience with Linux, but can be helpful for intermediate users as well

### 1.1 Prerequisite(s)

- Completion of Intro to Linux parts 1 and 2 (or at least familiarity of the material)
- Shell environment (WSL, Biocluster, online terminal, MobaXTerm-local)

### 1.2 Objectives

- Overall objective --> build a foundation of skills to be confident in using bioinformatics tools in Linux
- This session will focus on some useful utilities in the command line and file permissions

### 1.3 Commands and topics covered in this session

- **Commands**
  - `mv`, `less`, `cat`, `more`, `file`, `chmod`, `ll`, `echo`
- **Topics**
  - symbolic links (symlinks)

- Reminder: information about commands can be accessed within a terminal by using

```bash
man <command_name>
<command_name> --help
whatis <command_name> # only one line summary
```

- more documentation at [manual-pages](https://www.kernel.org/doc/man-pages/)

### 1.4 Questions?

</br>

---

## 2.0 Review

- Review of part 2
  - `whatis`, `mkdir`, `touch`, `rm`, `rmdir`
  - operators, wildcards
  - Why are Linux users so introverted? - They never get out of their shell!

<br>

- Corrections/Clarifications
  - When using `rmdir` the option `--ignore-fail-on-non-empty` does not allow the command to remove the directory(ies), it hides the warning instead that they are non-empty (the condition non-empty causes the delete to fail)
    - Either remove any child directories first or use `rm -r` to remove these dirs (-iv or -Iv is also recommended)
- I failed to use alias properly, we will cover that command a little today

<br>

---

## 3.0 Instruction

### 3.1 `mv`

- **`mv` - move and/or rename files**
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

- **Discussion**
  - How to move multiple files to a new dir?

<details>
    <summary><b>Solution</summary>
      <ul>
        <li>In the help text under `Usage:` you can see</li>
        <li>mv [OPTION]... SOURCE... DIRECTORY</li>
        <li>Which means you can have multiple sources into a single directory</li>
        <li>Either using matching(*) to list multiple files with a single source, or listing them individually</li></b>
      </ul>
</details>

<br>

### 3.2 `ll`, `type`, and `alias`

- The long listing format of `ls`, the same as `ls -alF`
- `ll --help` lists the info for `ls`
- `type` will determine if a command is an `alias` that has been set
  - **`type` - display information about command type**
  - **`alias` - define or display aliases**
- `alias` can be used to shortcut commands to simpler or alternate commands
  - `alias --help` gives info and only one option
  - Use this by indicating `alias name_of_alias="command being aliased"`
  - Use **caution** if you want to alias any commands, these will only be temporary and must be set each time you login
    - A good example is using `alias` to make a command safer - like `alias rm="rm -Iv"`
    - To set a permanent alias you can read more [here](https://www.tecmint.com/create-alias-in-linux/)

Try the command(s)

```bash
type ll
type ls
type type
```

- `ll` is important for understanding more about files in our systems
- In the output there is a 10-character section comprising of certain letters or dashes (-) indicating file permissions
  - The first digit is usually `l`, `d`, or `-` meaning link, directory, or file
  - `rwx` stand for read, write, execute respectively
    - The 3 instances of them mean `owner`, `group`, and `world`
  - The digit is the number of hard links
  - Username of the files owner
  - Group that owns the file
  - Size in bytes
  - Date and time of last modification (timestamp modified in `touch`)

<br>

### 3.2 `ln` and `file`

- In bioinformatics files can be extremely large, a way to be more efficient is to use symbolic links (aka symlinks) so a file is not duplicated needlessly
- The `ln` command can create links, as always let's look at the options using `--help`
  - For this command we only really need `-s`, it is generally preferable to use symbolic (aka soft) links
- We should have a testdir in place for this, if you do not have one from before please create one

Try the command(s)

```bash
cd ~/testdir
touch scriptfile_macOS scriptfile_linux
ln -s scriptfile_linux scriptfile
ll
```

- **Discussion**
  - When could this be useful?
  - Do you see the link in a different colour?

<details>
    <summary><b>Solution</summary>
      <ul>
        <li>This is useful for the above mentioned situation in reducing storage usage</li>
        <li>The situation with the scripts can be used to run system specific commands for a workflow - ie. Snakemake</li>
        <li>Different colour for the link may vary by terminal, this is out of curiosity</li></b>
      </ul>
</details>

<br>

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
  - What does `echo` do? (hint: check with `whatis`)
  - What about the `>>` operator?

<details>
    <summary><b>Solution</summary>
      <ul>
        <li>echo displays text as an output</li>
        <li>>> will append to a file, or even create one if the specified filename doesn't exist </li></b>
      </ul>
</details>

<br>

### 3.3 `chmod`

- This subject can be very complicated so we are only covering the basics. Use caution with this command!
- Only the file's owner or the superuser can change the permissions
- From the `ll` command we can see permissions for a file - read, write and execute for user, group, and world
- In bioinformatics it is sometimes necessary to make a script executable (able to act as a program)
  - So if permissions are `rw-`, we need to change this to `rwx`
  - This can be done using octal numbers representing binary for rwx, but the easier version is to use `u+x`
    - You can also specify the permissions for `u`= user, `g`= group, `o`= other
      - ie. u=rwx, g=rw
    - This gives the user permission to execute the file(s)
  
Try the command(s)

```bash
chmod --help
ll
chmod -c u+x scriptfile_linux 
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

### 3.5 `echo`

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

- How can you tell if someone uses Linux? - Oh don't worry about it they'll tell you themselves!
- Linux and other computer tech often have little easter eggs and jokes - programmers do not take things too seriously
  - sl
  - fortune
  - cowsay
  - apt moo

<br>
