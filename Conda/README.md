# Conda - Package management tool

- [Home page of the Linux Resources repository](../README.md)

## Links to other Conda pages in this repository

- [Conda installation guide](/Conda/conda_installation_guide.md) - How to install Conda from a Linux terminal
- [Conda get started](/Conda/conda_get_started.md) - Beginners tutorial for basic Conda commands
- [Conda usage](/Conda/conda_usage.md) - List of useful Conda commands

## Table of contents


## Introduction to Conda

This is a summary page for basic usage of Conda. For more details or more advanced commands, please refer to the 
[Conda user guide](https://conda.io/projects/conda/en/latest/user-guide/index.html)

### What is Conda

Conda is an open source package and environment manager. It provides an easy way for users to install packages in 
isolated environments without worrying about dependencies and conflicting requirements.

### Why I need to use Conda

- Conda can be installed by any user into their own userspace (**you don't need admin rights**). This provides maximum 
control to users over their Conda installation.
- You can quickly install any version of a software without worrying about dependencies conflict with other software 
and/or other users' configurations
- You can have multiple environments. *e.g.* One for each of your projects or pipelines.
- You can easily export and import Conda environments from other users to replicate an environment.

### How can I use Conda

Conda can be installed on all platforms (Windows, macOS, Linux), but most bioinformatics and data analysis packages are 
only available on Linux and macOS. **If you have a Windows computer we recommend using the Windows Subsystem for Linux 
(WSL). See [WSL Installation Guide](/WSL_Workshop/WSL_installation.md) for more info.** 
[The Conda installation guide page](/Conda/conda_installation_guide.md) focuses on the Linux installation of Miniconda,
but its installation and the usage is almost identical for other platforms.

<br>

### Terms and definition

Conda has a simple syntax. There is only a short list of commands to know for basic Conda users. Before getting to the 
list of commands, here is a terminology table of the most common terms used with `conda`:

| Term | Definition |
| --- | --- |
| Conda package | An [archive](https://en.wikipedia.org/wiki/Archive_file) containing all of the executable files and 
configuration files necessary for a specific software tool or library, as well as metadata about the external 
dependencies of that software |
| Conda Environment | A directory into which Conda packages can be installed |
| Install | When a Conda package is installed, it is downloaded from Conda's online package repository, and unpacked 
into a given Conda environment |
| Activate | When a Conda environment is activated, it means that Conda has modified the user's system environment in 
such a way that the software and libraries in the Conda environment are now accessible to the user |
| Base Environment | The default Conda environment that is created when Conda is installed. It should initially only 
contain the Conda package and its dependencies. Installing packages directly into the base environment is not recommended |
| Conda Channels | Location where packages are stored. Conda packages are downloaded from remote channels which are 
URLs to directories containing conda packages. You can search for channels and packages at 
[Anaconda Cloud](https://anaconda.org/). Some of these channels are managed by communities of users who collaborate on 
packaging software |

<br>

## Tips and best practices

- **Build multiple small environments**  
   Conda environments can become too complex if you install too many packages in a single environment. In some cases, 
   the package manager becomes unable to resolve the dependencies which will creates problems with your environment. To avoid this:
  - Do not install all your packages in your base environment
  - Create one environment for each pipeline/projects
- Use meaningful name for your environments
- Add your environment file (`.yml`) to your Git project. Your environment will change while you are working on your pipeline or project.

<br>

## Acknowledgements 

This tutorial was originally created by AAFC's Bioinformatics Research Support Network [(BRSN)](mailto:aafc.bioinfosupport.aac@agr.gc.ca) 
in their repository and was cloned and adapted for the purposes of GenARCC with the BRSN's permission.

<br>

---

- [Conda installation guide](/Conda/conda_installation_guide.md) - How to install Conda from a Linux terminal
- [Conda get started](/Conda/conda_get_started.md) - Beginners tutorial for basic Conda commands
- [Conda usage](/Conda/conda_usage.md) - List of useful Conda commands
