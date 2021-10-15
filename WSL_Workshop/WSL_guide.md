# Using WSL

- Integrations with VS Code
  - opening via command line
  - opening remote via GUI in Windows
  - remote session for Biocluster
- Examples of command line tools being efficient vs. Windows

## Some of the basics
  
- What is WSL?
  - Windows Subsystem for Linux (WSL) is a compatibility layer allowing Linux utilities and commands to run in a Windows system
  - A Linux distribution is installed in this subsystem and users can access the command line and shell languages
  - NOTE: There are two versions of WSL. Currently only version 1 is approved in AAFC. Version 2 is generally better but has some networking challenges.
    - WSL 2 offers greater performance, some graphical capabilities, and is becoming even easier to enable and install with Windows 11. We hope to eventually use version 2.

- What is Ubuntu?
  - A Linux distribution that is generally considered to be user-friendly and well built. It is a free operating system that is managed by a corportation (Canonical) that offers enterprise support at a price.
  - There are many Linux distributions. Some of the most common are Debian, Ubuntu, Linux Mint, Arch Linux, CentOS, and openSUSE.

- Philosophy of Linux/GNU
  - Single responsiblity principle - each program should only do one thing
  - Linux uses small actions that work together

- Opening Ubuntu
  - The main method to open your Ubuntu terminal is the icon from your Windows 10 start menu. You can use your mouse to navigate or simply press the Windows key and start typing "Ubuntu" and you should see your installation.
  - Depending on the file name when it was extracted it could be simply "Ubuntu" or possibly "Ubuntu20.04".
    - If you are using Ubuntu 18 that is completely fine.
  - If for any reason that icon is not available, you can also launch Ubuntu from the PowerShell app. Simply open PowerShell and type `wsl` to launch your default distro (it is possible to have more than one, but it is an uneccessary complication)

### Updates

- **DISCLAIMER!**
  - If you are following this during the live session with a new WSL system, please DO NOT apply updates. It can take 10+ minutes the first time and will make participation difficult.
  - This is a good thing to do after the workshop.

- To perform updates to Ubuntu and all packages, the commands

```bash
sudo apt update # fetch the package lists
sudo apt upgrade # apply them

OR

sudo apt update; sudo apt upgrade # perform both commands with one line, watch for the user prompt asking to apply updates
```

- You can see the Linux philosophy in effect with 2 separate commands that each perform a single task
- Efficiency is another important concept in Linux, often inspired by laziness (doing the most amount of work with the least amount of typing)
  - These commands can be chained together, with either `&&` or `;`
    - `&&` requires the first command to execute for the 2nd one to happen
    - `;` will attempt the 2nd command regardless

- In WSL there is a system message when you open the application for the first time each day, if you have not updated in over a week it will remind you
  - Updating is not absolutely necessary, but allows for security updates. Stability is always a priority with Linux packages so there is little-to-no risk of updates.

### Installing/Removing packages

- `apt` is the package manager, in full it is called `advanced package tool`
- "Admin mode" in Linux is called `sudo`, which means "super user do"
- We need to use `sudo` to use the package manager
  - At least for the first usage of `sudo` in a given session, you must enter your password
- NOTE: Updates should be applied before new packages installed. Depending on the current state of your updates this may be required.

- If you already have an up to date system here are a few small packages to try installing
  - `tree` - gives a simple visual of file structure in the specified directory (defaults to pwd)
    - The output can be very long if a subdirectory contains a lot of files/dirs (do not use in `/`, or in conda)
    - Remember that 'ctrl+c' is the kill/interrupt to stop any command, like `tree` when listing too much information
  - `tldr` - give a simplified and focused help text for a specified command
    - The package itself is small, but may need to load some information upon first usage
  - `htop` - an interactive process-viewer and process-manager
    - Allows you to see hardware utilization and which processes are using resources
  - `cowsay` - outputs a message just like `echo`, but with a cow using a "speech bubble".
    - Just for fun.

## File System

- Ubuntu uses a typical Linux file system, but your user directory will be empty to begin with
  - If you do not have anything in your user dir, make a projects directory (or something else if you would like, just have something)
    - Also create a file in that directory, we'll add some text so it's not empty

```bash
cd; ls
mkdir -v projects
echo "Index file for projects dir. Add info for each project added to this dir" > projects/index.txt
ls projects/
```

### Mounting your Windows storage

- To access your Windows file system from Ubuntu you navigate through the `/mnt` folder
- Then use the path `mnt` --> `c` --> `Users` and to your username. From there you can access Documents, Downloads, or whatever you require
  - This can be to perform a one-time action without changing your working directory, such as copying file(s)
    - ie. `cp /mnt/c/Users/USERNAME/Documents/metadata.csv ~/projects`
  - You can change directory to the Windows file system to use command line tools on Windows files
    - `cd /mnt/c/Users/USERNAME/` then navigate from within the Windows files

- One of the advantages that WSL 1 has is that it has faster access to files in Windows. The practical applications of this are narrow, but if you have to work on files in Windows from Ubuntu or vice versa then WSL 1 will be better than version 2. 

### Accessing your WSL storage from File Explorer

- There are 2 ways to do this, from within Ubuntu and within File Exporer in Windows
- In Ubuntu
  - Simply use the command `explorer.exe .`
  - You can specify any point in your Ubuntu file system, `.` will open the explorer window in your pwd
- In Windows
  - Opening File Explorer (the folder icon) then entering `\\wsl$` in the address bar will show icons to access any WSL distros
    - The full address for your own Ubuntu distro and user can save a few steps of navigation -> `\\wsl$\Ubuntu-20.04\home\USERNAME`
    - If you ever need to find information about your WSL distro you can use PowerShell -> `wsl -l -v`
      - This will show any distros installed in WSL, the version, and the current state (running, stopped, etc.)
  - From here you have typical File Explorer access to your WSL files
    - Depending on the files in you use in Ubuntu it may be a good idea to back these up in a Windows location. WSL is stable feature but it can be easy to make errors that affect the file system

## Using bash with Windows files

- text filtering?
- selective deletions?

## 