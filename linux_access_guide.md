# Linux Access Guide

March 8, 2021

This workshop requires a bash terminal, which can be obtained in several ways. Each method will have a guide below.

**Only one of these options is required**. We will discuss this guide during the first workshop session.

1. Biocluster account
2. Online terminal
3. WSL in Windows 10 (Windows Subsystem for Linux)
4. mobaXterm - local session (only if the others are not available -> this is not a full Linux environment, and some commands will not work as written)

How to obtain each environment

## Biocluster

This should be your first option if you plan to use bioinformatics tools in this high-performance computing environment. While connected to the AAFC network (VPN if necessary), login to Redmine using your AAFC credentials [here](https://redmine.biodiversity.agr.gc.ca/projects/biocluster) (same username & password as logging into your computer)

- See the link for "Requesting Biocluster Access", also found [here](https://redmine.biodiversity.agr.gc.ca/projects/biocluster/wiki/Requesting_Biocluster_Access)
- Review the [Terms of Use](https://redmine.biodiversity.agr.gc.ca/projects/biocluster/wiki/Biocluster_Terms_of_Use)
- The [User Guide](https://redmine.biodiversity.agr.gc.ca/projects/biocluster/wiki/Biocluster_User_Guide) has resources for using the system, including links to some Linux training if you want a head-start

<br>

- Connect to the Biocluster using the "Powershell" Windows app with the command "ssh username@biocluster.agr.gc.ca". You will then be prompted for a password. On Linux there are typically no asterisks “*” or indicators of password entry but keystrokes are still being entered.
- There are also apps like PuTTY and mobaXterm to connect to the biocluster with "username@biocluster.agr.gc.ca". They can be used as portable applications without the need for installation or admin rights on your device.
- We will use the Biocluster in "interactive mode", so you must enter the command `qlogin` before using tools to avoid using resources on the head node.

<br>

## Online Terminal

This is the simplest option but will be a bit slower. There are publicly available resources you can find by searching google for “online terminal”. For some of these services there is no account is required, though you may create one if you wish. It will not be as useful as Biocluster or WSL for long term use but will be an easy option for the workshop.

<br>

## WSL

Windows Subsystem for Linux is the best environment for this training, but the install is more complicated. WSL is a relatively new feature in Windows 10 that allows for a Linux command line within Windows. You must have build Version 1709 or higher (check by pressing Windows Key and typing 'winver' and pressing enter)

- Typically installation is very simple using the Windows Store, but on AAFC devices the process is different.
a) Enable the WSL feature. You must have admin privileges or have your local IT team enable the WSL feature (file an IM/IT ticket). This is accomplished by enabling the feature in "Turn Windows features on or off".
b) Restart the device.
c) Use the manual download for the appx file from [this](https://docs.microsoft.com/en-us/windows/wsl/install-manual) page - Ubuntu 20.04 is the best option
d) Finish the install and setup your user account - NOTE that there is no visible "*" symbols when typing a Linux password but keystrokes are being recorded.

<br>

## MobaXterm - local terminal

mobaXterm is a useful terminal app that allows for ssh connection to services like the biocluster. You can use the application in "portable mode" which does not require admin rights or installation. If there is no other suitable option you can select "Start local terminal" but there are a few commands that will not work properly because it is not a complete Linux system.
