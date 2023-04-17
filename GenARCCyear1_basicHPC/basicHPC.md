# Outline
1. Assumptions:
    - Windows user
    - have a cluster account
    - can access GC network
1. basic ssh connection
    - Windows
    - Linux
    - Mac
1. basic linux commands
    - how to see directory
    - how to navigate
    - basics of linux (create, delete, edit, cd, ls)
    - interact with files
	- interact with software
	- putting and retreiving data
	- make a file via nano or touch

---
# 1. Connecting to Cluster from Windows/Linux/Mac

In Windows PowerShell, the **ssh** tool can be used to connect to the cluster. 
```
> ssh username@address
username@address's password: 
```

From there, depending on the cluster setup, you may have to connect to an interactive container

**Note:** SSH has been included with the Windows operating system since Windows 7. If your operating system is older than Windows 7, you will need to use a third-party tool such as Putty.