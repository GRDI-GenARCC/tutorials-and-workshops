# Assumptions
- Windows user accessing a linux cluster
- have a cluster account
- can access GC network



---
# 1. Connecting to Cluster from Windows/Linux/Mac

In Windows PowerShell, the `ssh` tool can be used to connect to the cluster. 
```bash
ssh username@address
```
Replace `username` with your cluster account name and `address` with the address of the cluster.

You will see the following prompt appear. Enter the password associated with your cluster account. You will not see anything appear as you type. That is for security reasons. Rest assured, your key strokes are being recorded.
```
username@address's password: 
```
From there, depending on the cluster setup, you may have to connect to an interactive container

**Note:** `ssh` has been included with the Windows operating system since Windows 7. If your operating system is older than Windows 7, you will need to use a third-party tool such as `Putty`.


</br>

---
# 2. Viewing Directories

Once you have logged in, you will be in your home directory. You can see the directories in your home directory using the `ls` command:
```bash
ls
```
This will show you a list of directories in your home directory. If you have not set created any folders or files in this directory yet, the `ls` command will return nothing.


</br>

---
# 3. Navigating Directories

## 3.1 Changing Directories

To change directories, use the `cd` command. For example, to change to a directory called `mydir`:
```bash
cd mydir
```

You do not need to enter one directory at a time. For example, if `mydir` was in a folder called `parent_folder`, you could still `cd` into `mydir`:
```bash
cd parent_folder/mydir
```
- If your path has spaces in the folder names, you can simply enclose the entire path in single quotes `'example/path to folder/'`

You can even enter directories outside of your current folder by specifying a direct path (full paths starting with the drive letter [e.g. C:]). For example, if your current directory is `parent_folder/mydir`, you can move to `C:\Users\user_name\Desktop`:
```bash
cd C:\Users\user_name\Desktop
```

To enter the immediate parent directory (the folder containing your current folder):
```bash
cd ..
```

To go back to your home directory (within the GPSC only):
```bash
cd
```


## 3.2 Autocomplete

You can `autocomplete` a path, folder, or file name by pressing the `tab` key after typing out a few characters. This will do 1 of 3 things:

1. If there are no other targets with the same starting characters, it will `autocomplete` the target name.
1. If there are multiple targets with the same order of typed characters, it will `autocomplete` up to the point where the target names differ. Then, type a couple more characters and press `tab` again to fill the rest.
1. If the target name does not exist, was typed out incorrectly, or there are multiple targets with the same order of typed characters provided but with different names, pressing `tab` will return nothing and a chiming sound might play indicating the `autocomplete` action cannot be performed.



## 3.3 Making Directories

If you need to create a folder on the cluster in your user account, you can either:

1. `cd` into the directory that will contain the new folder and make a new dirctory right there
```bash
mkdir new_folder_name
```

2. Specify the direct path and then the new folder name 
```bash
mkdir example/location/new_folder_name
```

Remember that you can enclose paths in single quotes if the path has spaces in it. However, it is best to create folders with underscores `_` instead of spaces as it makes autocompleting much more user-friendly.



## 3.4 Removing Directories

Removing directories is similar to making directories:
```bash
rmdir path/to/folder
```

However, this only works if the folder is empty. If the folder contains data, you will have to run the following command:
```bash
rm -r path/to/folder
```
- **This will not delete the entire path.** It will only delete the last folder in the path text (i.e. `folder` in `path/to/folder`). 
- The `-r` means "recursive" and will look through all subfolders within the specified directory and delete those contents too


</br>

---
# 4. Working with Files

## 4.1 Making Files

To make a file, use the `touch` command. For example, to make a file called `myfile.txt`:
```bash
touch myfile.txt
```

To `make` a file and `add text` at the same time:
```bash
echo 'This is a test' > data.txt
```

You can also append text to this file by changing the `>` to `>>`
```bash
echo 'This is a test' >> data.txt
```


## 4.2 Deleting Specific Files

To delete a file, you can use the `rm` (remove) command:
```bash
rm myfile.txt
``` 


## 4.3 Editing Files

There are many ways to see the contents of, and edit, files in a Linux environment. `Nano` is one such method:
```bash
nano data.txt
```

- This will change the terminal into a text editor. To navigate the editor, one must use the `arrow keys` on the keyboard to reposition the cursor before adding, editing, or deleting text. 

You can also copy information from another source and `right-click` in the open `nano` session to paste content. Do note, however, that if you have `left-mouse-clicked` elsewhere in the terminal screen during a `nano` session and see a thicker cursor where you clicked, you may have to `right-click` again to paste your data. To avoid this, just click on the top bar of the terminal to activate the window rather than inside the terminal.

To save your edits:
```
ctrl+o
<enter>
ctrl+x
```

- `ctrl+o` means hold down the `ctrl` key on the keyboard and press the `o` key (also on the keyboard)
- `<enter>` means press the enter/return key on the keyboard.



## 4.4 Downloading Files

To download files from the internet, you can use the `wget` command. For example, to download a file called `example.zip`, use the following command:
```bash
wget https://example.com/example.zip
```


## 4.5 Uploading Data

To upload data to the cluster from your local windows machine, you can use `sftp`. To do so, open a fresh terminal session on your local windows system and perform the following commands:

```bash
sftp username@address
```
- Replace `username` with your cluster account name and `address` with the address of the cluster.

You will see the following prompt appear. Enter the password associated with your cluster account. 

- You will not see anything appear as you type. That is for security reasons. Rest assured, your key strokes are being recorded.
```bash
user@address password:
```

If you did not navigate to the folder with your data on your local machine before running the `sftp` command, you can use the `lcd` command after starting the `sftp` session. 
```bash
lcd C:\location_of_data
```
- `lcd` means **local change directory**, indicating to `sftp` that you want to change the current directory of your local machine. 
- Note that you **cannot** use `tab` to perform autocomplete when using `sftp`

Then navigate to where on the cluster you would like the data to be stored. For example, if you have a folder called `test_data`:
```bash
cd test_data
```
- Here, `cd` is telling the `sftp` session to **change directories** to the location you specify on the cluster.

To begin the file selection and transfer process:
```bash
put path_to_file
```
- `path_to_file` can just be the file name if the file exists at the same level as the current directory

If you want to send to the cluster all files, folders, and the contents of all subfolders within your current local directory, you can simply type: 
```bash
put -r .
```
- The `-r` will look through all subfolders within the specified directory
- the `.` refers the the current directory when no specific file name is provided. 



## 4.6 Retrieving Data

To retrieve information from the cluster back onto your local machine, follow the same `sftp` login command and directory changing process as described in "Uploading Data". You will navigate to where the data is located on the cluster and to where on your local system you would like the data to be stored.

At this point, the only thing that changes is the key word `put` which is replaced with `get`:
```bash
get path_to_file
```


</br>

---
# 5. Using Mamba to Install Software via Bioconda

This will need Anaconda or miniconda to perform. More information on installing miniconda can be found here https://github.com/GRDI-GenARCC/tutorials-and-workshops/blob/main/Conda/conda_installation_guide.md

Mamba is a package manager that allows you to install and manage software packages in an HPC system. To use mamba to install software via Bioconda, you need to first install mamba.

You can install mamba using the following command:

```bash
conda install mamba -c conda-forge
```

Once you have installed mamba, you can use it to install software packages via Bioconda. For example, to install a package called `samtools`, use the following command:

```bash
mamba install -c bioconda samtools
```

</br>

---
# 6. Launching Jobs Using a SLURM Scheduler

The SLURM scheduler is a workload manager that allows you to submit and manage jobs in an HPC system. To launch a job using a SLURM scheduler, you need to create a job script and submit it to the scheduler.

Here is an example job script:

```bash
#!/bin/bash -l
#SBATCH --job-name=sleeper
#SBATCH --output=sleep.out
#SBATCH --error=sleep.err
#SBATCH --time=00:00:60
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2000M
#SBATCH --comment="something identifying about the job"

echo hello
sleep 60
echo goodbye
```

This script sets the job name to `sleeper`, the output and error files to `sleep.out` and `sleep.err`, the job time to `60 seconds`, the number of tasks and CPUs per task to `1`, the amount of memory per CPU to `2000 Mb`, and sets a comment associated with your job so you can identify it. The script also prints "hello" and "goodbye" to the output file.

To submit the job script to the SLURM scheduler, use the following command:
```bash
sbatch hello_sleeper.sh
```
- Replace `hello_sleeper.sh` with the name of your job script.

To see the progress of your submission, use the following command:
```bash
squeue -u <username>
```

