# Conda Get Started

## Links to other Conda pages in this repository

- [Conda home page](/Conda) - Home page of the Conda repository
- [Conda installation guide](/Conda/conda_installation_guide.md) - How to install Conda from a Linux terminal
- [Conda usage](/Conda/conda_usage.md) - List of useful Conda commands

## Table of contents

[[_TOC_]]

## Getting started with conda

Now that conda is install on your Linux terminal. Let's do a short demo of the basic Conda commands.

<br>

### Create an environment

You can create your first environment with the command:

```bash
conda create -n my_first_env
```

<br>

### Install packages

To search a package, you can search directly on [anaconda.org](https://anaconda.org/) and use the search bar to find your package. But the Anaconda search tool is sometimes not working correctly if you don't have the exact name of the package. This is why **the best way to search for a package is to Google it**. Simply Google `conda <your package name>` and the first result should be page of the page of the package on [anaconda.org](https://anaconda.org/).

Let's install the Blast package in the environment you just created.

```bash
# Install the blast package
conda install -n my_first_env blast
```

**You can specify the version of the package you want to install using `conda install -n my_first_env blast=2.12.0`**

Now let's see if Blast is installed in the miniconda repository and which version you installed.

```bash
# Get the path to blastn executable
which blastn

# Check which version of Blast is installed
blastn -version
```

You should get an error message like: `Command 'blastn' not found`. This is because you installed the Blast package on the `my_first_env` environment and you are currently in the `base` environment.

<br>

### List environments

The name of the active environment is always display on the left side of your command prompt. *e.g.* `(base) username@hostname:~$`. The name between the parenthesis is the name of the active environment. To list the available environments use the command:

```bash
conda env list
```

### Activate an environment

To use the Blast package you installed you need to activate the `my_first_env` environment.

```bash
conda activate my_first_env
```

Now that the environment is active we can verify again if Blast is installed in the miniconda repository and which version you installed.

```bash
# Get the path to blastn executable
which blastn

# Check which version of Blast is installed
blastn -version
```

<br>

### Clone an environment

A good practice is to use meaningful environment name. We did a poor job naming our first environment (my_first_env). Let's duplicate and rename this environment to fix this.

```bash
# Clone the environment
conda create -n blast_env --clone my_first_env
```

You created a new environment, let's see the list of available Conda environments.

```bash
conda env list
```

<br>

### Remove an environment

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

### Use a conda environment in a script

To use conda environment from a shell script, you need to run the conda source script like you did in your *bashrc* file (see [Installation step 3](conda_installation_guide.md#installation)). Then you will be able to activate the environment you want from your script.

We will create a bash script that run the `blastn -version` command. Name your script `blast_version.sh`. Copy the following line in your script:

```bash
#!/bin/bash

# Run the conda source script
source ~/miniconda3/etc/profile.d/conda.sh

# Activate your environment
conda activate blast_env

blastn -version
```

Change the permission of your script to make it executable and run it.

```bash
# Change permission to make the file executable
chmod 744 blast_version.sh

# Run the script
./blast_version.sh
```

<br>

---

- [Conda home page](/Conda) - Home page of the Conda repository
- [Conda installation guide](/Conda/conda_installation_guide.md) - How to install Conda from a Linux terminal
- [Conda usage](/Conda/conda_usage.md) - List of useful Conda commands
