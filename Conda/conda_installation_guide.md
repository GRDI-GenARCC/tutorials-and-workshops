# Conda Installation Guide

## Links to other Conda pages in this repository

- [Conda home page](/Conda) - Home page of the Conda repository
- [Conda get started](/Conda/conda_get_started.md) - Beginners tutorial for basic Conda commands
- [Conda usage](/Conda/conda_usage.md) - List of useful Conda commands

## Table of contents

[[_TOC_]]

## Installation

### 1. Download and run the install script

   Open a Linux terminal and enter the following command:

   ```bash
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    sh Miniconda3-latest-Linux-x86_64.sh
   ```

### 2. Installation procedure

   You will be guided through a command line based installation wizard:

   1. Press `<Enter>` to continue
   2. Press `q` to close the license or `<enter>` to scroll through it until you've read it all
   3. Type `"yes"` to accept the license, then press `<enter>`
   4. The default install location of `~/miniconda3/` is fine, so press `<enter>`
   5. Running `conda init` is no longer the recommended way to enable Conda, so type `"no"` and press `<enter>`

### 3. Enable the `conda` command

   At this point, Conda is installed in your home directory, but if you try running it now, you'll get an error. This is because you have not told the command line interpreter that you want Conda enabled in your path. You can do this by running the following command:

   ```bash
    source ~/miniconda3/etc/profile.d/conda.sh
   ```

   This command tells the command line interpreter to run the Conda source script, which enables the conda command for your environment. You will likely want to run this command every time you connect to the Biocluster, so you are encouraged to edit your ~/.bashrc file, and add that command to the end of the file.

### 4. Activate The Base environment

   Once Conda is installed and enabled in your home directory, you will find some functionality is available right away. You should be able to run conda info to print some information about your installation. Some other Conda commands are available without activating the base environment, however Conda's behaviour is less predictable when used while not activated. Therefore, it is recommended that the only Conda command you run when no Conda environments are activated is to activate the base environment:

   ```bash
    conda activate
   ```

   **You'll note that your shell prompt becomes prepended with "(base)". This is how Conda tells you which environment is currently active.**

### 5. Configure Conda

   Conda comes mostly pre-configured out of the box, but there are some minor configuration tweaks we recommend for bioinformatics users. We recommend adding the conda-forge and bioconda channels to your configuration. These channels are both run by free community initiatives, and are backed by a set of guidelines for the packagers that ensure that the software packages are secure and usable. The conda-forge channel provides more general purpose software tools and libraries, while the bioconda channel focuses on bioinformatics software. To add these channels, run the following commands:

   ```bash
    conda config --add channels bioconda
    conda config --add channels conda-forge
   ```

You are now all set to start using Conda.

<br>

## Update Conda

Once you've installed Conda, you should ensure that it is up to the latest version. You can do this by running:

```bash
conda update conda
```

<br>

---

- [Conda home page](/Conda) - Home page of the Conda repository
- [Conda get started](/Conda/conda_get_started.md) - Beginners tutorial for basic Conda commands
- [Conda usage](/Conda/conda_usage.md) - List of useful Conda commands
