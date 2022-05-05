# WSL/Ubuntu Installation Instructions

- [Home page of the repository](../README.md)
- [WSL Workshop](/WSL_workshop)

- Ubuntu is a widely-used and beginner-friendly Linux distribution. With the addition of the Windows Subsystem for Linux feature that is now available on devices running Windows 10 in some departments, we can use an Ubuntu command line interface within our Windows OS.
- You may require IT Client services to enable the WSL feature, as this requires Admin rights, but the rest can be completed with regular permissions

## Enabling the WSL Feature (IT Client Services or Admin account)

- The simplest way to do this is press the Windows Key on the keyboard (usually between ctrl and alt on the left), or open the Start Menu.
- Then begin to type "Turn Windows features on or off", you can select the option as soon as it appears.
- Enable the "Windows Subsystem for Linux" feature. We will be using version 1, so that is all that is required.
- Now restart the device and WSL is fully enabled
  - This can be confirmed using powershell and typing the command "wsl --list"
  - You are likely to get a message about "No distros are installed", this is correct and requires the next step

## Installing Ubuntu (regular user permissions)

- The new Windows 10 build (Summer 2021, version 20H2) seems to block the installation of .appx packages that normally come from the Windows store
- We simply rename the .appx into a .zip and open the Ubuntu install file
- You will need to download the .appx file from this [Microsoft page](https://docs.microsoft.com/en-us/windows/wsl/install-manual) or from the direct link to the recommended version - Ubuntu 20.04 [here](https://aka.ms/wslubuntu2004) (Note - this will begin the download immediately using your web browser)
- Note the name of this download, as you will need to match it to the first part of the rename command. Also note the location of this download, if it is **not** in your Downloads folder you will need to adjust accordingly with powershell.
- You will also need to have powershell work in the correct location. It will open in `C:\User\username` by default. Simply change directory in powershell with `cd Downloads` to then work in `C:\Users\username\Downloads`
- Once you are in the proper location, use these commands:
```powershell
Rename-Item .\NAME_OF_YOUR_DOWNLOAD.AppxBundle .\Ubuntu.zip
Expand-Archive .\Ubuntu.zip .\Ubuntu
cd Ubuntu
```
- You now have a regular folder called Ubuntu in your file explorer
- There should be one file in your newly created Ubuntu directory ending in `_x64.appx`. We rename and expand it:
```powershell
Rename-Item .\UBUNTU_VERSION_x64.appx .\Ubuntu.zip
Expand-Archive .\Ubuntu.zip .\Ubuntu
```
- Open this folder and run `ubuntu.exe` to install:
```powershell
cd .\Ubuntu
.\ubuntu.exe
```
  - You will be prompted to select a username and password. This username should be **lower case letters only**. 
  - The Ubuntu username and password do not need to match your Windows credentials. 
  - There is no visual indicator when you type in characters for a password. **It will record your typing even though it appears blank.**

- Once installation is complete, to use WSL in the future, you can:
  - Search for Ubuntu in the start menu; if using Ubuntu 20.04 LTS, you should see ubuntu2004.exe or ubuntu.exe in the Start Menu
  - Open ubuntu2004.exe (ubuntu.exe) in the folder that was previously extracted
