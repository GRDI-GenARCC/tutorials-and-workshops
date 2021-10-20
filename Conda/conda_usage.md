# Conda usage

## Links to other Conda pages in this repository

- [Conda home page](/Conda) - Home page of the Conda repository
- [Conda installation guide](/Conda/conda_installation_guide.md) - How to install Conda from a Linux terminal
- [Conda get started](/Conda/conda_get_started.md) - Beginners tutorial for basic Conda commands

## Table of contents

[[_TOC_]]

## List of useful Conda commands

### Manage Conda environment

Conda environments are useful to isolate and manage multiple softwares/versions/dependencies that differs from your different projects or analysis. Here is a list of basic commands to manage your Conda environments.

<br>

#### Create a new environment

```bash
conda create -n my-first-env
```

#### Activate an environment

```bash
conda activate my-first-env
```

#### Deactivate an environment

```bash
conda deactivate
```

#### Clone an environment

```bash
conda create -n my-first-clone-env --clone my-first-env
```

#### List available environment

```bash
conda env list
```

#### Remove an environment

```bash
conda env remove -n my-env-name
```

<br>

### Manage Conda Packages

<br>

#### Search for a package

To search a package, you can search directly on [anaconda.org](https://anaconda.org/) and use the search bar to find your package. But the Anaconda search tool is sometimes not working correctly if you don't have the exact name of the package. This is why **the best way to search for a package is to Google it**. Simply Google `conda <your package name>` and the first result should be page of the page of the package on [anaconda.org](https://anaconda.org/). You can also search for packages using the following command:

```bash
conda search package
```

<br>

#### Install a package

Install the default version of a package in your active environment

```bash
conda install package
```

Install a specific version of a package in your active environment

```bash
conda install package=2.4.3
```

Install a package in a specific environment

```bash
conda install package -n my-env-name
```

Install multiple packages

```bash
conda install package1 package2 package3
```

<br>

#### List installed packages

For the active environment

```bash
conda list
```

For a specific environment

```bash
conda list -n my-env-name
```

<br>

#### Update a package

```bash
conda update package
```

<br>

#### Remove a package

```bash
conda remove package
```

<br>

### Export and import Conda environment

#### Export environment

To best way to export a conda environmnet is in a [YAML](https://en.wikipedia.org/wiki/YAML) file. You can create the `.yml` file of your active environment with the following command:

```bash
# yml file with all packages dependencies and versions
conda env export > my_env.yml

```

You can also modify your `.yml` file or create one from scratch. More details on this in the [conda user-guide](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually)

<br>

#### Import environment

You can import an environment from a `.yml` file with the following command:

```bash
# The name of your environment is defined in the yml first line
conda env create --file my_env.yml
```

To change the name of the environment, use this command instead

```bash
conda env create -n new-env-name --file my_env.yml
```

<br>

### Use conda environment in a script

To use conda environment from a shell script, you need to run the conda source script. Like you did in your *bashrc* file (see [Installation step 3](#installation)). Then you will be able to activate your environment from your script.

```bash
#!/bin/bash

### Template script to enable Conda environment from a script

# Run the conda source script
source ~/miniconda3/etc/profile.d/conda.sh

# Activate your environment
conda activate my_env_name

# shell commands
echo "Hello world"
```

<br>

---

- [Conda home page](/Conda) - Home page of the Conda repository
- [Conda installation guide](/Conda/conda_installation_guide.md) - How to install Conda from a Linux terminal
- [Conda get started](/Conda/conda_get_started.md) - Beginners tutorial for basic Conda commands
