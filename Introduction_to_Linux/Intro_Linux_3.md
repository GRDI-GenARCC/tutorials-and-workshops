# Introduction to Linux Tutorial Part 3

- [Home page of the repository](../README.md)
- [Introduction to Linux overview](/Introduction_to_Linux)

[[_TOC_]]

---

## 1.0 Overview

- This is **part three** of four sessions designed to be delivered in a virtual group setting
- This can also be worked through at a self-directed pace outside of workshop sessions
- The material is meant for those with little or no experience with Linux, but can be helpful for intermediate users as well

### 1.1 Prerequisite(s)

- Completion of Intro to Linux parts 1 and 2 (or at least familiarity of the material)
- `bash` command line (Ubuntu in WSL will be the default for all commands shown)

### 1.2 Objectives

- Overall objective --> build a foundation of skills to be confident in using bioinformatics tools in Linux
- This session will focus on some useful utilities in the command line and file permissions

### 1.3 Commands and topics covered in this session

- **Commands**
  - `rmdir`, `mv`, `file`, `chmod`, `ll`, `type`, `alias`, `ln`
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

- Review of part 2
  - `whatis`, `mkdir`, `touch`, `rm`
  - operators, wildcards

### 2.1 Review Exercises

- Here is a self-directed exercise to review the commands from part 2
  - Do as much as you can using the command names above, referring to `--help` if you're stuck
  - Clicking the expansion below will reveal all the suggested solutions

1. What is the difference between -i and -I in rm?
2. What is the usual purpose for `touch`?
3. What is the difference between an absolute path and relative path? --> can you give an example of either of them? (recall the command `realpath`)
4. What does `&&` do between commands?
5. What is the difference between `-v` and `--verbose` for `rm` or `mkdir`?
6. What does the `*` character do?
7. (Challenge) What will happen if you use `rm -Iv` on 3 or less target files? You can test this to verify

<details>
    <summary><b>Solutions</b></summary>
      <ul>
        <li>1. '-i` will prompt for each delete, -I will prompt for a group of > 3 files (or a folder)'</li>
        <li>2. To create an empty file</li>
        <li>3. Absolute path is the full path from root. Relative path is defined by the pwd (present working directory). An example would be if you are in /home/user/testdir. This is the absolute path, root --> home --> user --> testdir. The relative path from testdir to your user folder is simply ../ (`..` is up one level in the directory structure). Using <b>realpath</b> with dir/file(s) outputs the absolute path of the file(s) in that dir.</li>
        <li>4. If the first command executes correctly, it will allow another command to execute in the same line </li>
        <li>5. There is no difference other than the appearance. They are the short and long form for the same options. There must be a space between long form options</li>
        <li>6. `*` will match 0 or more characters.</li>
        <li>7. It will not prompt at all, the files will be removed.</li>
      </ul>
</details>

<br>

---

## 3.0 Instruction

### 3.1 `rmdir`

- **`rmdir` - remove empty directories**
- This command is not used often, but is a great review and companion to `rm`, which is used often
- A simple version of `rm` for directories - checks if they are empty, if so then deletes
- As always, worth looking at the help text `rmdir --help`
  - `-p` and `-v` are useful options once again

Try the commands

```bash
cd
mkdir -pv emptydir/emptydirs{1..7}
ls
rmdir -pv emptydir # does not work because the subdirectories mean this dir is not truly "empty"
mkdir -pv emptydir/emptydir{1..10}
rmdir -v emptydir/* emptydir # alternate way to do this, delete the subdirs, then the main dir
```

- By removing the subdirectories first we ensure that the parent `emptydir` is empty when rmdir executes on it
- An alternative method is to use `rm -r` as we saw in the previous section

<br>

### 3.2 `mv`

- **`mv` - move and/or rename files**
  - This command can either move or rename a file, it all depends on how it is used
  - It essentially changes the absolute path for a file, whether it includes location or file name (the last part of the absolute path)
  - View the help text for the command with `mv --help`
  - Moving a file within the same directory will rename the file
  - Moving file(s) to another dir will move the file(s)
  - We will work from the same `linux_workshop` directory as last time, if you do not have it use these first commands to create it

Try the command(s)

```bash
cd && ls
mkdir -pv linux_workshop/2021microbiome && cd linux_workshop
touch file0 microbiome/file1
```

- Now we're ready to use `mv`
- What are the arguments we should include?
- Start in linux_workshop

Try the commands

```bash
pwd
mv -iv file0 sequencefiles.fa # file0 is not descriptive at all, change to sequencefiles.fa (.fa is fasta file format - also .fasta)
mv -iv sequencefiles.fa 2021microbiome/ # move the sequencefiles.fa into the subfolder
```

- **Discussion**
  - How to move multiple files to a new dir?

<details>
    <summary><b>Solution</b></summary>
      <ul>
        <li>In the help text under `Usage:` you can see</li>
        <li>mv [OPTION]... SOURCE... DIRECTORY</li>
        <li>Which means you can have multiple sources into a single directory</li>
        <li>Either using matching(*) to list multiple files with a single source, or listing them individually</li>
      </ul>
</details>

<br>

Try the commands

```bash
cd ~/linux_workshop # `~` is the shortcut for our user folder, so this path will work regardless of where we are
touch config.yaml manifest.csv readme.md
ls
mv config.yaml manifest.csv readme.md 2021microbiome/
cd 2021microbiome; ls # check new location for files
```

- You can also use pattern matching to move multiple files matching a wildcard pattern with *

### 3.3 `ll`, `type`, and `alias`

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
    - To remove an alias, use the command `unalias`

Try the command(s)

```bash
type ll
type ls
type type
```

- `ll` is important for understanding more about files in our system
  - By just entering `ll` it is the same as entering `ll .`, which is your current directory
    - You can specify a single file to reduce the amount of information provided in the output. In your user directory you can try `ll .bashrc`
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

### 3.4 `ln` and `file`

- In bioinformatics files can be extremely large, a way to be more efficient is to use symbolic links (aka symlinks) so a file is not duplicated needlessly
- The `ln` command can create links, as always let's look at the options using `--help`
  - For this command we only really need `-s`, it is generally preferable to use symbolic (aka soft) links
- We will continue to use the `linux_workshop` workshop for this

Try the command(s)

```bash
cd ~/linux_workshop
touch scriptfile_macOS scriptfile_linux
ln -s scriptfile_linux scriptfile
ll
```

- **Discussion**
  - When could this be useful?
  - Do you see the link in a different colour?

<details>
    <summary><b>Solution</b></summary>
      <ul>
        <li>This examples shows some packages may come with diverging options, due to factors like Operating System (OS)</li>
        <li>The workflow can be built to use the generic name (in this case - scriptfile), which links to the appropriate file</li>
        <li>Overall the main usage for links is to avoid file duplication, but there are useful situations like this as well</li>
      </ul>
</details>

<br>

- Another useful command that can help inform us about a file is `file`
  - let's use `file --help` to look at the information
- Simply outputs information about the file and it's format
  - Also tells basic info for a symlink

Try the command(s)

```bash
touch textfile.txt
file textfile.txt
echo "Some text for the file" >> textfile.txt
echo "echo This script ran successfully" >> scriptfile_linux
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
        <li>`echo` displays text as an output</li>
        <li>`>>` will append to a file, or even create one if the specified filename doesn't exist </li></b>
      </ul>
</details>

<br>

### 3.5 `chmod`

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
chmod -c u+x scriptfile
ll
./scriptfile # execute the file
```

- **Discussion**
  - What did the script do?
  - What does the `./` mean?

<br>

### 3.6 Questions?

<br>

---

## 4.0 Extras

- This section will not be covered during the 1 hour workshop session, they are completely optional
- Answers can be obtained from the tutorial material or by using the bash commands
  - Some questions will invite you to research on the internet to give greater context or understanding

<br>

### 4.1 Movement Shortcuts (repeated from part 2)

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

1. What will happen to a link when the original file is removed? Test this yourself to see

<details>
    <summary><b>This will reveal all the answers, please go through as many as you can before looking</b></summary>
        <ul>
            <li>1. Create a file, then a link to this file, remove the original file. This will cause the link to be `broken`. Create a file --> `touch original_file.txt`, link to the file --> `ln -s original_file.txt link_file.txt`, then `rm -i original_file.txt`. Now try `file link_file.txt` </li>
        </ul>
</details>

<br>

### 4.3 Fun Facts

- Joke: How can you tell if someone uses Linux? - Oh don't worry about it they'll tell you themselves!
- Linux and other computer tech often have little easter eggs and jokes - programmers do not take things too seriously
  - sl (steam locomotive - 'trains' (ha) you not to mistype `ls`)
  - cowsay - like `echo` but with a cow using a speech bubble

```bash
_____________________________
< This tutorial is phenomenal >
 -----------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

<br>
