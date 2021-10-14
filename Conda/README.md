# Conda - Package management tool

- [Home page of the repository](../README.md)
- [WSL Workshop](/WSL_Workshop)

## Links to other Conda pages in this repository

- [Conda installation guide](conda_installation_guide) - How to install Conda from a Linux terminal
- [Conda get started](conda_get_started) - Beginners tutorial for basic Conda commands
- [Conda usage](conda_usage) - List of useful Conda commands

[[_TOC_]]

## Introduction to Conda

This is a summary page for basic usage of Conda. For more details or more advanced command, please refer to the [Conda user guide](https://conda.io/projects/conda/en/latest/user-guide/index.html)

**Part of this document was taken from the [Biocluster documentation](https://redmine.biodiversity.agr.gc.ca/projects/biocluster/wiki/Installing_Conda)**

<br>

### What is Conda

The Conda package management tool provides an easy way for users to manage their environments.

### Why I need to use Conda

- Conda can be install by any user into their own userspace (**you don't need admin rights**). This provides maximum control to users over their Conda installation.
- You can quickly install any version of a software without worrying about dependencies and avoid dependencies conflict between your software other users' configurations
- You can have multiple environments, for each of your project or pipeline.
- You can easily export and import Conda environment from other users to replicate environment.

### How can I use Conda

Conda can be install on all platforms (Windows, macOS, Linux). But most of bioinformatics and data analysis packages are only available on Linux and macOS. **If you have a Windows computer we recommend using the Windows Subsystem for Linux. See [WSL Installation Guide](/WSL_Workshop/WSL_installation.md) for more info.** This page focus on the Linux installation of Miniconda but the installation and the usage is almost identical for other platform.

<br>

### Terms and definition

Conda has a simple syntax. There is only a short list of commands to know for basic Conda users. Before getting to the list of commands, here is a terminology table of the most common terms used with `conda`:

| Term | Definition |
| --- | --- |
| Conda package | An [archive](https://en.wikipedia.org/wiki/Archive_file) containing all of the executable files and configuration files necessary for a specific software tool or library, as well as metadata about the external dependencies of that software |
| Conda Environment | A directory into which Conda packages can be installed |
| Activate | When a Conda environment is activated, it means that Conda has modified the user's system environment in such a way that the software and libraries in the Conda environment are now accessible to the user |
| Install | When a Conda package is installed, it is downloaded from Conda's online package repository, and unpacked into a given Conda environment |
| Base Environment | The default Conda environment that is created when Conda is installed. It should initially only contain the Conda package and its dependencies. Installing packages directly into the base environment is not recommended |
| Conda Channels | Different users who upload conda packages to the [Anaconda Cloud](https://anaconda.org/). Some of these channels are actually communities of users who collaborate on packaging software |

<br>

## Tips and best practices

- **Build multiple small environments**  
   Conda environments can become too complex if you install too many packages in a single environment. In some cases, the package manager won't be able to resolved the dependencies which will creates problems with your environment. To avoid this:
  - Do not install all your packages in your base environment
  - Create one environment for each pipeline/projects

- Use meaningful name for your environments
- Add your environment file (`.yml`) to your Git project. Your environment will change while you are working on your pipeline or project.
