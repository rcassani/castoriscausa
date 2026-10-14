Title: Github actions and Matlab, multiple OS
Date: 2023-08-14 17:00
Tags: GitHub, Matlab, Linux, macOS, Windows
Author: Raymundo Cassani
Slug: github_actions_matlab
Thumbnail: github_actions_matlab.png

[GitHub actions](https://docs.github.com/actions) are an amazing tool to automate different stages on in the software development workflow, and they can be used in Matlab projects!

By using [Matlab GitHub actions](https://github.com/matlab-actions), it is possible to set up Matlab, and run Matlab code on [GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners) with different OS (**Linux**, **macOS** and **Windows**). This allows painless testing of your code on different Matlab versions on different OS.

### Toy example
A working toy example of using Matlab with GitHub actions can be found [here](https://github.com/rcassani/github_actions_matlab). The repo consists of two main parts: a yaml file and a Matlab script:

#### 1. yaml file
The yaml file `./github/workflows/github-actions.yaml` defines:

* When the GitHub action will run
* The OS versions: Linux (Ubuntu 20.04), macOS (12 Monterey) and Windows (Server 2019) for the runners
* The Matlab version (R2021b) that will be used
* The Matlab script (`wonder_script.m`) in the repo to be executed
* Other task (display results)

**Code:**

    :::yaml
    {!> https://raw.githubusercontent.com/rcassani/github_actions_matlab/main/.github/workflows/github-actions.yaml !}

#### 2. Matlab script
The `wonder_script.m` Matlab script gets information of the computer where the code is running and writes such information on a text file
**Code:**

    :::matlab
    {!> https://raw.githubusercontent.com/rcassani/github_actions_matlab/main/wonder_script.m !}
