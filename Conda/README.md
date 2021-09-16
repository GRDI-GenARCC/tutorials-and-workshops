# Conda - Package management tool

- [Home page of the repository](../README.md)
- [WSL Workshop](/WSL_Workshop)

[[_TOC_]]

## Introduction to Conda

**Part of this document was taken from the [Biocluster documentation](https://redmine.biodiversity.agr.gc.ca/projects/biocluster/wiki/Installing_Conda)**

### What is Conda

The Conda package management tool provides an easy way for users to manage their own software environments. Conda can be install by any user into their own userspace (you don't need admin rights). This provides maximum control to users over their Conda installation.

### What I need to use Conda

Conda can be install on all platforms (Windows, macOS, Linux). Install procedure and usage is similar on all platforms but here we will focus on the Linux installation of Miniconda. If you have a Windows computer we recommend using the Windows Subsystem for Linux ([WSL Installation Guide](/WSL_Workshop/WSL_installation.md)).

<br>

## Getting started

### Installation

1. **Download and run the install script**

   Open a Linux terminal and enter the following command:

   ```{bash}
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    sh Miniconda3-latest-Linux-x86_64.sh
   ```

2. **Installation procedure**

   You will be guided through a command line based installation wizard:
   1. Press `<Enter>` to continue
   2. Press `q` to close the license or `<enter>` to scroll through it until you've read it all
   3. Type `"yes"` to accept the license, then press `<enter>`
   4. The default install location of `~/miniconda3/` is fine, so press `<enter>
   5. Prepending the miniconda install location is no longer the recommended way to enable Conda, so type `"no"` and press `<enter>`
3. **Enable the `conda` command**

   At this point, Conda is installed in your home directory, but if you try running it now, you'll get an error. This is because you have not told the command line interpreter that you want Conda enabled in your path. You can do this by running the following command:

   ```{bash}
    source ~/miniconda3/etc/profile.d/conda.sh
   ```

    This command tells the command line interpreter to run the Conda source script, which enables the conda command for your environment. You will likely want to run this command every time you connect to the Biocluster, so you are encouraged to edit your ~/.bashrc file, and add that command to the end of the file.

4. **Activating The Base environment**

   Once Conda is installed and enabled in your home directory, you will find some functionality is available right away. You should be able to run conda info to print some information about your installation. Some other Conda commands are available without activating the base environment, however Conda's behaviour is less predictable when used while not activated. Therefore, it is recommended that the only Conda command you run when no Conda environments are activated is to activate the base environment:

   ```{bash}
    conda activate
   ```

   **You'll note that your shell prompt becomes prepended with "(base)". This is how Conda tells you which environment is currently active.**

5. **Configuring Conda**

   Conda comes mostly pre-configured out of the box, but there are some minor configuration tweaks we recommend for bioinformatics users. We recommend adding the conda-forge and bioconda channels to your configuration. These channels are both run by free community initiatives, and are backed by a set of guidelines for the packagers that ensure that the software packages are secure and usable. The conda-forge channel provides more general purpose software tools and libraries, while the bioconda channel focuses on bioinformatics software. To add these channels, run the following commands:

   ```{bash}
    conda config --add channels bioconda
    conda config --add channels conda-forge
   ```

You are now all set to start using Conda.

<br>

### Updating Conda

Once you've installed Conda, you should ensure that it is up to the latest version. You can do this by running:

```{bash}
conda update conda
```

---

<br>

## Usage

Conda has a simple syntax. There is only a short list of commands to know for basic Conda users. Before getting to the list of basic commands, here is a terminology table of the most common terms used with `conda`:

| Term | Definition |
| --- | --- |
| Conda package | An [archive](https://en.wikipedia.org/wiki/Archive_file) containing all of the executable files and configuration files necessary for a specific software tool or library, as well as metadata about the external dependencies of that software |
| Conda Environment | A directory into which Conda packages can be installed |
| Activate | When a Conda environment is activated, it means that Conda has modified the user's system environment in such a way that the software and libraries in the Conda environment are now accessible to the user |
| Install | When a Conda package is installed, it is downloaded from Conda's online package repository, and unpacked into a given Conda environment |
| Base Environment | The default Conda environment that is created when Conda is installed. It should initially only contain the Conda package and its dependencies. Installing packages directly into the base environment is not recommended |
| Conda Channels | Different users who upload conda packages to the [Anaconda Cloud](https://anaconda.org/). Some of these channels are actually communities of users who collaborate on packaging software |

### Create and manipulate Conda environment

#### Create a new environment

```{bash}
conda create -n my-first-env
```

#### Activate an environment

```{bash}
conda activate my-first-env
```

#### Deactivate an environment

```{bash}
conda deactivate
```

#### Clone an environment

```{bash}
conda create -n my-first-clone-env --clone my-first-env
```

#### List available env

```{bash}
conda env list
```

#### Remove an environment

```{bash}
conda env remove -n my-first-env
```

### Software management

### Import and export environment

### Use conda environment in a script

## Tips and best practices
