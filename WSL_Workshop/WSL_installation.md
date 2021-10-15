# Ubuntu Installation Instructions

- [Home page of the repository](../README.md)
- [WSL Workshop](/WSL_workshop)

- Ubuntu is a widely-used and beginner-friendly Linux distribution. With the addition of the Windows Subsystem for Linux feature that is now available on AAFC devices running Windows 10, we can use a Ubuntu command line interface within our Windows OS.
- The [BRSN](https://collab.agr.gc.ca/co/BRS-SRB/SitePages/Home.aspx) (Bioinformatics Research Support Network) is excited to offer an [Introduction to Linux](https://gccode.ssc-spc.gc.ca/bioinformatics_aafc/training_documentation/intro_to_linux_workshop/-/blob/master/README.md) workshop for users interested in using Linux and command line tools for Bioinformatics or other purposes
- The [software review committee approved WSL](https://collab.agr.gc.ca/co/ndlm-gncob/Lists/Software%20List/AllItems.aspx?FilterField1=FL&FilterValue1=W) for use this summer, **however** there is a work-around required to install Ubuntu with the latest build of Windows 10 (Version 20H2)
- You may require IT Client services to enable the WSL feature, as this requires Admin rights, but the rest can be completed with regular permissions

## Enabling the WSL Feature (IT Client Services or Admin account)

- The simplest way to do this is press the Windows Key on the keyboard (usually between ctrl and alt on the left), or open the Start Menu.
- Then begin to type "Turn Windows features on or off", you can select the option as soon as it appears.
- Enbable the "Windows Subsystem for Linux" feature. We will be using version 1, so that is all that is required.
- Now restart the device and WSL is fully enabled
  - This can be confirmed using powershell and typing the command "wsl --list"
  - You are likely to get a message about "No distros are installed", this is correct and requires the next step

## Installing Ubuntu (regular user permissions)

- The new Windows 10 build (Summer 2021, version 20H2) seems to block the install of .appx packages that normally come from the Windows store
- We simply rename the .appx into a .zip and open the Ubuntu install file
- You will need to download the .appx file from this [Microsoft page](https://docs.microsoft.com/en-us/windows/wsl/install-manual) or I have the direct link to the recommended version - Ubuntu 20.04 [here](https://aka.ms/wslubuntu2004) (Note - this will begin the download immediately using your web browser)
- Note the name of this download, as you will need to match it to the first part of the rename command. Also note the location of this download, if it is **not** in your Downloads folder you will need to adjust accordingly with powershell.
- You will also need to have powershell work in the correct location. It will open in `C:\User\username` by default. Simply change directory in powershell with `cd Downloads` to then work in `C:\Users\username\Downloads`
- Once you are in the proper location, use these commands

```powershell
Rename-Item .\NAME_OF_YOUR_DOWNLOAD.appx .\Ubuntu.zip
Expand-Archive .\Ubuntu.zip .\Ubuntu
```

- You will now have a regular folder called Ubuntu in your file explorer
- Now you simply need to open this folder and run `Ubuntu.exe` to install
  - When selecting a username and password they not need to match your Windows credentials, and there is no visual indicator when you type in characters for a password. **It will record your typing even though it appears blank.**

- Once installation is complete, to use WSL in the future, you can:
  - Search for Ubuntu in the start menu; if using Ubuntu 20.04 LTS, you should see ubuntu2004.exe in the Start Menu
  - Open ubuntu2004.exe in the folder that was previously extracted
