# Conda Get Started

## Links to other Conda pages in this repository

- [Conda home page](/Conda) - Home page of the Conda repository
- [Conda installation guide](/Conda/conda_installation_guide.md) - How to install Conda from a Linux terminal
- [Conda usage](/Conda/conda_usage.md) - List of useful Conda commands

<br>

## 1. Overview

### 1.1 Prerequisites

- Conda installed in a Linux terminal
  - An installation guide is available [here](/Conda/conda_installation_guide.md)
  - Installation on Windows is also possible, but some of the instructions in this tutorial may have to be adapted.
- Conda-forge channel added to your conda configurations (see [Installation Guide](/Conda/conda_installation_guide.md#5-configure-conda) for details).

<br>

### 1.2 Commands covered in this session

- `conda activate`, `conda list`, `conda create`, `conda install`, `conda deactivate`
- `conda env list`, `conda env export`, `conda env create`, `conda env remove`
- Information about the listed commands can be found by using --help. E.g. `conda create --help`

<br>

### 1.3 Questions

<br>

## 2. Introduction
 
### 2.1 What is Conda?

Conda is an open source package and environment manager. It provides an easy way for users to install packages in 
isolated environments without worrying about dependencies and conflicting requirements.

<br>

### 2.2 Benefits of Conda

- Conda can be installed by any user into their own userspace (**you don't need admin rights**). This provides maximum 
control to users over their Conda installation.
- You can quickly install any version of a software without worrying about dependency conflicts with other software 
and/or other users' configurations
- You can have multiple environments. *e.g.* One for each of your projects or pipelines.
- You can easily export and import Conda environments from other users to replicate an environment.

<br>

### 2.3 Conda installation

Conda can be installed on all platforms (Windows, macOS, Linux), but most bioinformatics and data analysis packages are 
only available on Linux and macOS. If you have a Windows computer we recommend using the Windows Subsystem for Linux 
(WSL). See [WSL Installation Guide](/WSL_Workshop/WSL_installation.md) for more info. 
[The Conda installation guide page](/Conda/conda_installation_guide.md) focuses on the Linux installation of Miniconda,
but its installation and the usage is very similar for other platforms.

<br>

### 2.4 Common terms

Conda has a simple syntax. There is only a short list of commands to know for basic Conda users. Before getting to the 
list of commands, here is a terminology table of the most common terms used in conjunction with Conda:

| Term | Definition |
| --- | --- |
| Conda package | An [archive](https://en.wikipedia.org/wiki/Archive_file) containing all of the executable files and configuration files necessary for a specific software tool or library, as well as metadata about the external dependencies of that software |
| Conda Environment | A directory into which Conda packages can be installed |
| Install | When a Conda package is installed, it is downloaded from [Anaconda's online package repository](https://anaconda.org/), and unpacked into a given Conda environment |
| Activate | When a Conda environment is activated, it means that Conda has modified the user's system environment in such a way that the software and libraries in the Conda environment are now accessible to the user |
| Base Environment | The default Conda environment that is created when Conda is installed. It should initially only contain the Conda package and its dependencies. Installing packages directly into the base environment is not recommended |
| Conda Channels | Location where packages are stored. Conda packages are downloaded from remote channels which are URLs to directories containing conda packages. You can search for channels and packages at [Anaconda Cloud](https://anaconda.org/). Some of these channels are managed by communities of users who collaborate on packaging software |

<br>

### 2.5 Questions

<br>

## 3.0 Instruction

- If you are connected to the GPSC or the Biocluster, you're already using CLI
- In an Ubuntu desktop environment, you can use the "Terminal" application for the CLI (command line interface). Alternatively you can use **Ctrl-Alt-T**
- If you are in Windows, open the "Anaconda Prompt" application.

<br>

### 3.1 Activate the base environment

#### Linux

If it isn't already, enable the `conda` command (see [Conda installation guide](/Conda/conda_installation_guide.md) for 
more details).

```bash
source ~/miniconda3/etc/profile.d/conda.sh
```

activate Conda's base environment
   ```bash
   conda activate
   ```
You'll note that your shell prompt becomes prepended with "(base)". This is how Conda tells you which environment 
is currently active.

#### Windows

If you have opened the **Anaconda Prompt**, you will notice that your shell prompt is already prepended with 
"(base)", indicating that the base environment is already activated.

<br>

### 3.2 List packages in your current environment

To see all packages and their versions installed in your current environment, run the following:
```bash
conda list
```

### 3.3 Create an environment

You can see what options are available for the `conda create` command:
```bash
conda create --help
```

Let's create our first environment with the command:

```bash
conda create -n my_first_env
```

<br>

### 3.4 Install packages

To search a package, you can search directly on [anaconda.org](https://anaconda.org/) and use the search bar to find 
your package. The Anaconda search tool doesn't always find what you're looking for if you don't have the exact name of 
the package. This is why **the best way to search for a package is to use your search engine**. 
Simply look up `conda <your package name>` in your search engine, and the first result should be the page of the package
on [anaconda.org](https://anaconda.org/).

Let's install the cowpy package in the environment you just created.

```bash
# Install the cowpy package in your newly created environment
conda install -n my_first_env cowpy
```

You can specify the version of the package you want to install using `conda install -n my_first_env cowpy=1.1.5`

Now let's see if cowpy is installed in the miniconda repository.

```bash
# Get the path to cowpy executable (Linux only)
which cowpy

```

Nothing is returned. This is because you installed the cowpy package on the `my_first_env` environment, 
and you are currently in the `base` environment.

<br>

### 3.5 List environments

The name of the active environment is always displayed on the left side of your command prompt. 
*e.g.* `(base) username@hostname:~$`. The name between the parentheses is the name of the active environment. To list 
the available environments use the command:

```bash
conda env list
```

<br>

### 3.6 Activate an environment

To use the cowpy package you installed you need to activate the `my_first_env` environment.

```bash
conda activate my_first_env
```

Now that the environment is active we can verify again where the cowpy package was installed.

```bash
# Get the path to cowpy executable
which cowpy
```

Now let's make use of our cowpy package

```bash
# directly from the bash terminal
cowpy Hello!
```
OR
```bash
# open python interpreter
python
```
```python
from cowpy import cow
msg = cow.Moose().milk("Hello!")
print(msg)
# close python interpreter
exit()
```

Now we'll install the tree package in our current environment. This time, we will specify which channel we want it to 
be downloaded from:
```bash
conda install -c conda-forge tree
conda list
```

We can now use our new tree package to view the directory tree of the tutorials/conda directory on the GPSC, or any other directory you have access to:
```bash
tree /gpfs/fs7/grdi/genarcc/tutorials/conda
```

<br>

### 3.7 Clone an environment

A good practice is to use meaningful environment names. We did a poor job naming our first environment (my_first_env). 
Let's duplicate and rename this environment to fix this.

```bash
# Clone the environment
conda create -n conda_tutorial_env --clone my_first_env
```

You created a new environment, let's see the list of available Conda environments.

```bash
conda env list
```

<br>

### 3.8 Remove an environment

Now that we created a clone of our first environment with a meaningful name, let's clean and remove our first environment.

You can't remove an active environment. So first you need to deactivate the *my_first_env* environment and then remove it.

```bash
# Deactivate the environment
conda deactivate

# Remove the environment
conda env remove -n my_first_env

# List environment to verify it is correctly removed
conda env list
```

<br>

### 3.9 Export an environment

You can export a conda environment in order to allow others, or your future self, to easily recreate it. The best way 
to export a conda environment is in a [YAML](https://en.wikipedia.org/wiki/YAML) file. You can create the `.yml` 
file of your active environment. You can then include the file to a git repository, for instance.  Let's try this 
with our conda_tutorial_env environment:

```bash
# activate the environment you want to export
conda activate conda_tutorial_env
# create yml file with all packages dependencies and versions
conda env export > conda_tutorial_env.yml
# view your newly created conda_tutorial_env.yml file
cat conda_tutorial_env.yml
```

You can also modify your `.yml` file or create one from scratch. More details on this in the 
[conda user-guide](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually).

<br>

### 3.10 Import an environment

The name of your environment is defined in the first line of the .yml file. If you wish to use the same name, you can
use `conda env create --file filename.yml`. We will create a new environment from our conda_tutorial_env.yml, but we'll change 
the name of the environment:

```bash
conda env create -n cowpy_env --file conda_tutorial_env.yml
```

List the existing conda environments to see our newly created environment, then deactivate the current environment
```bash
# list all conda environments
conda env list
# deactivate current environment
conda deactivate
```

<br>

### 3.11 Use a Conda environment in a script (Linux)

To use a Conda environment from a shell script, you need to run the conda source script like you did in your *.bashrc* 
file (see [Installation step 3](conda_installation_guide.md#installation)). Then you will be able to activate the 
environment you want from your script.

We will create a bash script that runs the `cowpy` command. Use your favourite text editor to copy the following
lines and name your script `cow_says_hello.sh`.

```bash
#!/bin/bash

# Run the conda source script
source ~/miniconda3/etc/profile.d/conda.sh

# Activate your environment
conda activate cowpy_env

cowpy "Hello from my script!"
```

Change the permission of your script to make it executable and run it.

```bash
# Change permission to make the file executable
chmod u+x cow_says_hello.sh

# Run the script
./cow_says_hello.sh
```

<br>

### 3.12 Questions

<br>

## 4. Tips and best practices

- **Build multiple small environments**  
   Conda environments can become too complex if you install too many packages in a single environment. In some cases, 
   the package manager becomes unable to resolve the dependencies which will creates problems with your environment. To avoid this:
  - Do not install all your packages in your base environment
  - Create one environment for each pipeline/projects
- Use meaningful names for your environments
- Add your environment file (`.yml`) to your Git project. Your environment will change while you are working on your pipeline or project.

<br>

## 5. Acknowledgements 

This tutorial was originally created by AAFC's Bioinformatics Research Support Network [(BRSN)](mailto:aafc.bioinfosupport.aac@agr.gc.ca) 
in their repository and was cloned and adapted for the purposes of GenARCC with the BRSN's permission.

<br>

---

- [Conda home page](/Conda) - Home page of the Conda repository
- [Conda installation guide](/Conda/conda_installation_guide.md) - How to install Conda from a Linux terminal
- [Conda usage](/Conda/conda_usage.md) - List of useful Conda commands
