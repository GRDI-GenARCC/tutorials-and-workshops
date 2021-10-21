# WSL User Guide

- [Home page of the repository](../README.md)
- [WSL Resources Overview](./README.md)
- [WSL/Ubuntu Installation Guide](./WSL_installation.md)

[[_TOC_]]

## Some of the basics
  
- What is WSL?
  - Windows Subsystem for Linux (WSL) is a compatibility layer allowing Linux utilities and commands to run in a Windows system
  - A Linux distribution is installed in this subsystem and users can access the command line and shell languages
    - WSL vs Linux vs Ubuntu
      - WSL is the feature that allows Linux to be installed in your Windows 10. There are many varieties of Linux, with Ubuntu being one of the most common.
  - NOTE: There are two versions of WSL. Currently only version 1 is approved in AAFC. Version 2 is generally better but has some networking challenges.
    - WSL 2 offers greater performance, some graphical capabilities, and is becoming even easier to enable and install with future Windows 10 builds and Windows 11. We hope to eventually use version 2.

- What is Ubuntu?
  - A Linux distribution that is generally considered to be user-friendly and well built. It is a free operating system that is managed by a corportation (Canonical) that offers enterprise support at a price.
  - There are many Linux distributions. Some of the most common are Debian, Ubuntu, Linux Mint, Arch Linux, CentOS, and openSUSE. In WSL there are other some other distros available to install but it is strongly recommended to use Ubuntu.

- Philosophy of Linux/GNU
  - Single responsiblity principle - each program should only do one thing
  - Linux uses small actions that work together

- Opening Ubuntu
  - The main method to open your Ubuntu terminal is the icon from your Windows 10 start menu. You can use your mouse to navigate or simply press the Windows key and start typing "Ubuntu" and you should see your installation.ls
  - Depending on the file name when it was extracted it could be simply "Ubuntu" or possibly "Ubuntu20.04".
    - If you are using Ubuntu 18 that is completely fine.
  - If for any reason that icon is not available, you can also launch Ubuntu from the **PowerShell** app. Simply open PowerShell and type `wsl` to launch your default distro (it is possible to have more than one, but it is an uneccessary complication)

### Updates

- **DISCLAIMER!**
  - If you are following this during the live session with a new WSL system, please DO NOT apply updates right now. It can take 10+ minutes the first time and will make participation difficult. This is a good thing to do after the workshop.
  - For other commands in the workshop you can try to do these in real time, but if the pace is too quick remember these guides will be available and there are recordings of the workshop as well.

- To perform updates to Ubuntu and all packages, the commands

```{bash}
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
    - As noted in the [installation instructions](https://gccode.ssc-spc.gc.ca/bioinformatics_aafc/training_documentation/linux_resources/-/blob/dev/WSL_Workshop/WSL_installation.md) you do not need to use the same password as your Windows login. It can be simple as you are already behind a personal login and security is not as great a concern at that point. However if you cannot remember your password it will require a full reinstall of Ubuntu. Please remember or record it somewhere safe.
    - If you need to change your password you can use the command `passwd`. You need to enter the old password, then 2 prompts are given to match the new password.
- NOTE: Updates should be applied before new packages installed. Depending on the current state of your updates this may be required.

- If you already have an up to date system here are a few small packages to try installing
  - `tree` - gives a simple visual of file structure in the specified directory (defaults to pwd)
    - The output can be very long if a subdirectory contains a lot of files/dirs (do not use in `/`, or in conda)
    - Remember that 'ctrl+c' is the kill/interrupt to stop any command, like `tree` when listing too much information
  - `tldr` - give a simplified and focused help text for a specified command
    - The package itself is small, but may need to load some information upon first usage
  - `htop` - an interactive process-viewer and process-manager
    - Allows you to see hardware utilization and which processes are using resources
    - Press `q` or F10 to quit
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

- Remember to view a text file the best application is `less`. We can read `index.txt` with the command
  - Alternatively for a small file such as this one you can use `cat` to print it to the command line

```bash
less projects/index.txt
# Use q to quit less
```

### Mounting your Windows storage

- To access your Windows file system from Ubuntu you navigate through the `/mnt` folder
- Then use the path `mnt` --> `c` --> `Users` and to your username. From there you can access Documents, Downloads, or whatever you require
  - This can be to perform a one-time action without changing your working directory, such as copying file(s)
    - ie. `cp /mnt/c/Users/USERNAME/Documents/metadata.csv ~/projects`
  - You can change directory to the Windows file system to use command line tools on Windows files
    - `cd /mnt/c/Users/USERNAME/` then navigate from within the Windows files

- One of the advantages that WSL 1 has is that it has faster access to files in Windows. The practical applications of this are narrow, but if you have to work on files in Windows from Ubuntu or vice versa then WSL 1 will be better than version 2.

- If you will access your Windows storage at all then it is a good idea to create a link in your user directory. This is a shortcut to access your Windows storage in future situations

```bash
cd; ls
ln -s /mnt/c/Users/USERNAME/
```

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
- You can pin the location to your Quick Access menu if you want a shortcut to access the Ubuntu storage in the future

## Using bash with Windows files

- There are times when using the command line can be more effective on files in Windows than utilities in Windows would be
  - This is especially true for a large set of files, as you may encounter in Bioinformatics
- I will demonstrate on a smaller subset of copied data, but limited storage can mean it's better to create symbolic links (symlinks) from the data in Windows storage
  - There does not seem to be a published storage size for WSL 1, but for version 2 it is 256 GB. It is possibly using the same style of virtual hard drive for both versions.
  - To create symbolic links for a directory simply specify it as the target. `ln -s TARGET` and the link to the dir will be created in your pwd
  - To create links to each file requires a slight tweak - you must use a wildcard to match a pattern in a directory then specify a target directory.
    - eg. `ln -s TARGET/*files .`
- Sorting and displaying information is very fast through the command line. The command `du` can be used to display disk usage information. The options `-h` for human readable (from bytes to KB, MB, etc.) and `-s` for summarize (displays totals for subdirectories, doesn't show each file) are very useful.
- Selecting subset of the files to delete
  - If I wanted to move or remove a subset of my files this is another operation where the command line may be more efficient. Wildcard matching is very fast and convenient. For these example files I want to remove all the reverse strand sequences.
    - It's always safe to list the files first - `ls -1 *R2*`
    - Then they can be removed - `rm -Iv *R2*`

## VS Code Integrations

- An IDE (Integrated Development Environment) that allows for code-editing or working with a variety of data files. VS Code is a free software from Microsoft
  - It is approved on the AAFC software list. It can be installed in Program Files, requiring an IT Ticket and assistance from IT Client services. Altervatively it can be installed in the LocalApps folder of your user folder without Admin rights
  - [https://code.visualstudio.com/](https://code.visualstudio.com/)
- VS Code can be used for programming in Python or writings bash scripts, or simply to look at text or tabulated files
  - The markdown for this workshop was written using VS Code.

- There are integrations in VS Code that work nicely with WSL. If VS Code is installed you can launch a remote session connected to your WSL file system using `code .`, specifying the location (`.` is the pwd)
- If VS Code is open from Windows, use the >< icon in the bottom-left to connect a remote session to WSL. This may require the WSL extension to be installed first. Extensions are accessed via the "blocks" icon on the left panel, or by using "ctrl+shift+x"
  - Search for and install the "Remote - WSL" extension
- When a VS Code window is connected to VS Code you have access to the Ubuntu filesystem of the location you are working in. You can create and modify files in Ubuntu but using a graphical window.
  - There are also great shortcuts for version control - see more material [here](https://gccode.ssc-spc.gc.ca/bioinformatics_aafc/training_documentation/git_resources)
