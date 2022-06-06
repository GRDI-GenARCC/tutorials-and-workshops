# Conda Get Started

## Links to other Conda pages in this repository

- [Conda home page](/Conda) - Home page of the Conda repository
- [Conda installation guide](/Conda/conda_installation_guide.md) - How to install Conda from a Linux terminal
- [Conda usage](/Conda/conda_usage.md) - List of useful Conda commands

## Getting started with conda

Now that conda is installed on your Linux terminal. Let's do a short demo of the basic Conda commands.

<br>

### Activate the base environment

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
**You'll note that your shell prompt becomes prepended with "(base)". This is how Conda tells you which environment 
   is currently active.**

#### Windows

From the Start Menu, open the **Anaconda Prompt**. You will note that your shell prompt is already prepended with 
"(base)", indicating that the base environment is already activated.

<br>

### Create an environment

You can create your first environment with the command:

```bash
conda create -n my_first_env
```

<br>

### Install packages

To search a package, you can search directly on [anaconda.org](https://anaconda.org/) and use the search bar to find 
your package. The Anaconda search tool doesn't always find what you're looking for if you don't have the exact name of 
the package. This is why **the best way to search for a package is to Google it**. 
Simply Google `conda <your package name>` and the first result should be the page of the package on 
[anaconda.org](https://anaconda.org/).

Let's install the cowpy package in the environment you just created.

```bash
# Install the cowpy package in your newly created environment
conda install -n my_first_env cowpy
```

You can specify the version of the package you want to install using `conda install -n my_first_env cowpy=1.1.5`

Now let's see if cowpy is installed in the miniconda repository and which version you installed.

```bash
# Get the path to cowpy executable (Linux only)
which cowpy

```

Nothing is returned. This is because you installed the cowpy package on the `my_first_env` environment, 
and you are currently in the `base` environment.

<br>

### List environments

The name of the active environment is always displayed on the left side of your command prompt. 
*e.g.* `(base) username@hostname:~$`. The name between the parentheses is the name of the active environment. To list 
the available environments use the command:

```bash
conda env list
```

### Activate an environment

To use the cowpy package you installed you need to activate the `my_first_env` environment.

```bash
conda activate my_first_env
```

Now that the environment is active we can verify again where the cowpy package.

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

<br>

### Clone an environment

A good practice is to use meaningful environment names. We did a poor job naming our first environment (my_first_env). 
Let's duplicate and rename this environment to fix this.

```bash
# Clone the environment
conda create -n cowpy_env --clone my_first_env
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

### Export an environment

You can export a conda environment in order to allow others, or your future self, to easily recreate it. The best way 
to export a conda environment is in a [YAML](https://en.wikipedia.org/wiki/YAML) file. You can create the `.yml` 
file of your active environment. You can then include the file to a git repository, for instance.  Let's try this 
with our cowpy_env environment:

```bash
# activate the environment you want to export
conda activate cowpy_env
# create yml file with all packages dependencies and versions
conda env export > cowpy_env.yml
```

You can also modify your `.yml` file or create one from scratch. More details on this in the 
[conda user-guide](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually)

<br>

### Import an environment

You can import an environment from a `.yml` file with the following command:

```bash
# The name of your environment is defined in the yml first line
conda env create --file my_env.yml
```

Let's create a new environment from our cowpy_env.yml, but we'll change the name of the environment:

```bash
conda env create -n new_cow_env --file cowpy_env.yml
```

List the existing conda environments to see our newly created environment, then deactivate the current environment
```bash
# list all conda environments
conda env list
# deactivate current environment
conda deactivate
```

<br>

### Use a Conda environment in a script (Linux)

To use a Conda environment from a shell script, you need to run the conda source script like you did in your *bashrc* 
file (see [Installation step 3](conda_installation_guide.md#installation)). Then you will be able to activate the 
environment you want from your script.

We will create a bash script that runs the `cowpy` command. Use your favourite text editor to copy the following
lines and name your script `cow_says_hello.sh`.

```bash
#!/bin/bash

# Run the conda source script
source ~/miniconda3/etc/profile.d/conda.sh

# Activate your environment
conda activate new_cow_env

cowpy "Hello from my Script!"
```

Change the permission of your script to make it executable and run it.

```bash
# Change permission to make the file executable
chmod u+x cow_says_hello.sh

# Run the script
./cow_says_hello.sh
```

<br>

---

- [Conda home page](/Conda) - Home page of the Conda repository
- [Conda installation guide](/Conda/conda_installation_guide.md) - How to install Conda from a Linux terminal
- [Conda usage](/Conda/conda_usage.md) - List of useful Conda commands
