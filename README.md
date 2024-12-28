# Chrome Dino Game  <!-- -Sth. funny as intern titel -->

![GitHub Repo stars](https://img.shields.io/github/stars/RedLion8399/Dino)
![GitHub forks](https://img.shields.io/github/forks/RedLion8399/Dino)
![Schulprojekt](https://img.shields.io/badge/School_project-green?link=gymnasium-warstein.de)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/RedLion8399/Dino)
![GitHub last commit](https://img.shields.io/github/last-commit/RedLion8399/Dino)
[![GitHub commits](https://badgen.net/github/commits/RedLion8399/Dino)](https://GitHub.com/RedLion8399/Dino/commit/)
[![GitHub branches](https://badgen.net/github/branches/RedLion8399/Dino)](https://github.com/RedLion8399/Dino/)
![GitHub repo size](https://img.shields.io/github/repo-size/RedLion8399/Dino)
![GitHub language count](https://img.shields.io/github/languages/count/RedLion8399/Dino)
![GitHub top language](https://img.shields.io/github/languages/top/RedLion8399/Dino)
![Tests status](https://img.shields.io/github/actions/workflow/status/RedLion8399/Dino/run_tests.yml?label=Tests)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/RedLion8399/Dino/run_linter.yml?label=Style)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/RedLion8399/Dino)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues-closed/RedLion8399/Dino)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues-pr/RedLion8399/Dino)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues-pr-closed/RedLion8399/Dino)
![GitHub License](https://img.shields.io/github/license/RedLion8399/Dino)
![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/RedLion8399/Dino/total)


## :cactus: About the project
This project is a recreation of the iconic Chrome Dino game, designed as a school project in a computer science class. The primary purpose is to introduce 10th graders to the fundamentals of Python programming through a fun and engaging hands-on project. The task is to break down the concepts included in the project to ensure they are understandable to our schoolmates.


## :books: Table of content
- [Chrome Dino Game  ](#chrome-dino-game--)
  - [:cactus: About the project](#cactus-about-the-project)
  - [:books: Table of content](#books-table-of-content)
  - [:star: Project Overview and Features](#star-project-overview-and-features)
  - [:rocket: Getting started](#rocket-getting-started)
    - [:snake: Installing python](#snake-installing-python)
    - [:hammer: Installing git](#hammer-installing-git)
    - [:package: Clone repository](#package-clone-repository)
    - [:gear: Install dependencies](#gear-install-dependencies)
    - [:video\_game: Ececuting](#video_game-ececuting)
  - [:bug: How to Contribute and Report Issues](#bug-how-to-contribute-and-report-issues)
  - [:handshake: Acknowledgement](#handshake-acknowledgement)
  - [:scroll: Conclusion and License](#scroll-conclusion-and-license)
  - [:speech\_balloon: Contact](#speech_balloon-contact)


## :star: Project Overview and Features

## :rocket: Getting started
As mentioned earlier this project is intendet to explane students basic programming concepts so the explanations how to install and use the programm are much more detailed than you are used to read here o GitHub.

### :snake: Installing python
First ensure that you have python installed on your programm. To test the following command in your terminal:

- On Windows
```bash
python --version
```
- On Mac or Linux
```shell
python3 --version
```
If python is installed on you mashine the output should be something like
```shell
Python 3.13.0
```

If the version is higher that 3.8 everything should work totaly fine. Otherwise you have to install python. On windows you can simply use the installer from [python.org](https://www.python.org/downloads/) On MaxOS and Linux xou can use an installer as well but you have also tho option to install python usiing your terminal.

### :hammer: Installing git
To get this project on your local pc you also need another tool called git. It is used to create a version history of your project. Similar to above you can check if it is installed using:

```shell
git --version
```

If no version number is shown you must git as well. In windows you have to use the installer from the [website](https://git-scm.com/) again. Meanwhile on Linux and MacOS it is the best option to use the terminal again althought it would be possible to get an installer.

### :package: Clone repository
After installing python and git you can clone thin project onto your local mashine. That means more or less copying the whole project to your pc. To do this navigat to the folder you would like the project to be stored and run the following command in your terminal:
```shell
git clone https://github.com/RedLion8399/Dino.git
```

### :gear: Install dependencies
Althought it is not neceserry to use the programm it is recommend to set up a virtual enviroment. To do this you only need two command:
- On windows:
```bash
python -m venv .venv
.venv\Scripts\activate.bat
```
- On Mac and Linux
```shell
python3 -m venv .venv
source .venv/bin/activate
```

Because the programm uses recorces that are not available iin the default python installation you must install them now seperatly. To only play the game run:
- On Windows
```bash
pip install -e .
```
- On Mac and Linux
```shell
pip3 install -e .
```

If you would like to contribute on the project install the developement dependencies to by riuning a secound command:
```bash
pip install .[lint]
```
- On Mac and Linux
```shell
pip3 install .[lint]
```

### :video_game: Ececuting
To play the game only search for the main file in the scr folder, run it ad have fun while playing.

## :bug: How to Contribute and Report Issues
If you like the project and want to take part in the projekt you are welcom. Just fork the repo and try out what you want. As mentioned earlier this repo is intendet to students beginning with programming to understand basic concepts of programming and contribution using git and GitHub.

To suggest new features or reporting bugs aou can open an [issue](https://github.com/RedLion8399/Dino/issues) directly here on GitHub. There are already pre-formatted issuetemplates to help you writing a consistent issue that is hopefully easy to understand and process. These templates should cover most possible cases. Althought if they do not fit to your needs feel free to open an issue without a template.


## :handshake: Acknowledgement
The graphics used in this project are sourced from the [Runn Gesture Gaming](https://github.com/TusharAMD/Runn) GitHub repository by Tushar Amdoskar (TusharAMD), licensed under the [MIT License](https://github.com/TusharAMD/Runn/blob/master/LICENSE). Special thanks to the original author for providing these resources.


## :scroll: Conclusion and License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details


## :speech_balloon: Contact
If you ever eed to cantact us exept those things outlined in the [Contributions chapter](#bug-how-to-contribute-and-report-issues) you can open a [discussion](https://github.com/RedLion8399/Dino/discussions) directly here on GitHub. Most things about the project can be discussed there. In case this option does not fit to your needs you can also write an email. Our contacts are available in the [pyproject.toml file.](./pyproject.toml)
