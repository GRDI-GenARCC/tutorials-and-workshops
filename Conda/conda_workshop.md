# Conda Workshop

- [Home page of the repository](../README.md)
- [Conda Documentation](README)
- [WSL Workshop](/WSL_Workshop)

[[_TOC_]]

## Summary

This workshop covers the basic usage of Conda. At the end of the workshop you will be able to:

- Install Conda from any Linux terminal (WSL, Biocluster, Ubuntu, etc.)
- Create Conda environment
- Install packages on a specific Conda environment
- Use a Conda environment in a script

**Part of this document was taken from the [Biocluster documentation](https://redmine.biodiversity.agr.gc.ca/projects/biocluster/wiki/Installing_Conda)**

### What is Conda

The Conda package management tool provides an easy way for users to manage their environments.

### Why I need to use Conda

- Conda can be install by any user into their own userspace (**you don't need admin rights**). This provides maximum control to users over their Conda installation.
- You can quickly install any version of a software without worrying about dependencies and avoid dependencies conflict between your software other users' configurations
- You can have multiple environments, for each of your project or pipeline.
- You can easily export and import Conda environment from other users to replicate environment.

### How can I use Conda

Conda can be install on all platforms (Windows, macOS, Linux). But most of bioinformatics and data analysis packages are only available on Linux and macOS. **If you have a Windows computer we recommend using the Windows Subsystem for Linux. See [WSL Installation Guide](/WSL_Workshop/WSL_installation.md) for more info.** This page focus on the Linux installation of Miniconda but the installation and the usage is almost identical for other platform.

### Terms and definitions

Here is a terminology table of the most common terms used with `conda`:

| Term | Definition |
| --- | --- |
| Conda package | An [archive](https://en.wikipedia.org/wiki/Archive_file) containing all of the executable files and configuration files necessary for a specific software tool or library, as well as metadata about the external dependencies of that software |
| Conda Environment | A directory into which Conda packages can be installed |
| Activate | When a Conda environment is activated, it means that Conda has modified the user's system environment in such a way that the software and libraries in the Conda environment are now accessible to the user |
| Install | When a Conda package is installed, it is downloaded from Conda's online package repository, and unpacked into a given Conda environment |
| Base Environment | The default Conda environment that is created when Conda is installed. It should initially only contain the Conda package and its dependencies. Installing packages directly into the base environment is not recommended |
| Conda Channels | Different users who upload conda packages to the [Anaconda Cloud](https://anaconda.org/). Some of these channels are actually communities of users who collaborate on packaging software |

<br>

### 1. Install Conda

1.1. **Download and run the install script**

   Open a Linux terminal and enter the following command:

   ```{bash}
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    sh Miniconda3-latest-Linux-x86_64.sh
   ```

1.2. **Installation procedure**

   You will be guided through a command line based installation wizard:
   1. Press `<Enter>` to continue
   2. Press `q` to close the license or `<enter>` to scroll through it until you've read it all
   3. Type `"yes"` to accept the license, then press `<enter>`
   4. The default install location of `~/miniconda3/` is fine, so press `<enter>
   5. Prepending the miniconda install location is no longer the recommended way to enable Conda, so type `"no"` and press `<enter>`

1.3. **Enable the `conda` command**

   At this point, Conda is installed in your home directory, but if you try running it now, you'll get an error. This is because you have not told the command line interpreter that you want Conda enabled in your path. You can do this by running the following command:

   ```{bash}
    source ~/miniconda3/etc/profile.d/conda.sh
   ```

    This command tells the command line interpreter to run the Conda source script, which enables the conda command for your environment. You will likely want to run this command every time you connect to the Biocluster, so you are encouraged to edit your ~/.bashrc file, and add that command to the end of the file.

1.4. **Activate The Base environment**

   Once Conda is installed and enabled in your home directory, you will find some functionality is available right away. You should be able to run conda info to print some information about your installation. Some other Conda commands are available without activating the base environment, however Conda's behaviour is less predictable when used while not activated. Therefore, it is recommended that the only Conda command you run when no Conda environments are activated is to activate the base environment:

   ```{bash}
    conda activate
   ```

   **You'll note that your shell prompt becomes prepended with "(base)". This is how Conda tells you which environment is currently active.**

1.5. **Configure Conda**

   Conda comes mostly pre-configured out of the box, but there are some minor configuration tweaks we recommend for bioinformatics users. We recommend adding the conda-forge and bioconda channels to your configuration. These channels are both run by free community initiatives, and are backed by a set of guidelines for the packagers that ensure that the software packages are secure and usable. The conda-forge channel provides more general purpose software tools and libraries, while the bioconda channel focuses on bioinformatics software. To add these channels, run the following commands:

   ```{bash}
    conda config --add channels bioconda
    conda config --add channels conda-forge
   ```

You are now all set to start using Conda.

<br>

### 2. Manage conda environment

#### 2.1. Create an environment

Now that Conda is set up, you can create your first environment with the command:

```{bash}
conda create -n my_first_env
```

<br>

#### 2.2. Install packages

The best way to search for a package is to go to [anaconda.org](https://anaconda.org/) and use the search bar to find your package. Let's install the Blast package in the environment we just created.

```{bash}
# Activate the environment
conda activate my_first_env

# Install the blast package
conda install blast
```

Now let's see if Blast is installed and which version you installed.

```{bash}
blastn -version
```

You can specify the version of the package you want to install using `conda install blast=2.12.0`**

<br>

#### 2.3. Clone an environment

A good practice is to use meaningful environment name. We did a poor job naming our first environment (my_first_env). Let's duplicate and rename this environment to fix this.

```{bash}
# Clone the environment
conda create -n blast_env --clone my_first_env
```

<br>

#### 2.4. List available environments

You created a new environment, let's see the list of available Conda environments.

```{bash}
conda env list
```

<br>

#### 2.5. Remove an environment

Now that we created a clone of our first environment with a meaningful name, let's clean and remove our first environment.

```{bash}
# Remove the environment
conda env remove -n my_first_env

# List environment to verify it is correctly removed
conda env list
```

<br>

### 3. Use a conda environment in a script

I
