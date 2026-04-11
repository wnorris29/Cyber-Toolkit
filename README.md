# Cyber-Toolkit
Python Project acting as a cybersecurity toolkit, goal is to develop and consolidate the python skills I have already learned. Please note this is a CLI tool


## Features 

- Hashing tools, including generating file and string hashes as well as comparing two hashes

- password tools for generating and rating passwords

- portscanner which can conduct full, popular and custom scans 

- WHois lookup 

- DNS enumeration

- rich formatting

- multithreading for more performant scans



## Installation 
clone the repo using the following:

```git clone https://github.com/wnorris29/cyber-toolkit.git```

cd into the folder and install the dependancy with the following:

```pip install pyfiglet```

## Usage 

run the command ```python main.py``` 

The programme can be run with an interactive menu or through CLI arguments

Here are the CLI arguments:

- ``` --scan``` - this is for the portscanner functionality it has tree options:
    - ```full``` - full scan
    - ```popular``` - for the popular ports 
    - ```custom``` - to run a scan on a custom port range
the scan argument requires a ```--host``` argument alongisde it, and if running a custom scan, ```--port-range``` must be used as well. 

- ```--hash``` - three options:
    - ``` string```
    - ```file```
    - ```compare```

- ```--pwd``` - Two options:
    - ```generate``
    - ```rate```

please note for the hash and password arguments this will be used as normal after the arguments are parsed. 

## Planned Features

- GUI front end 
- VirusTotal Integration
- phishing analyser
- log parser


