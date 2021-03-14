# String Matching
Modulprojekt PRO1 WiSe2020/21

This is a command line string matching tool.  
Users can search for a search term in direct input texts, single .txt files or directories with multiple .txt files.  
The tool prints out the first index of each found search term occurrence (per file if directory is searched).

## Installation
This project was developed with Python 3.8.

Clone this directory and navigate to it in your CLI.
If you want to create a virtual environment for installing the requirements run ```python3 -m venv env``` and activate it either by running ```./env/bin/activate``` or ```source ./env/bin/activate``` depending on your operating system.

Use pip to install the requirements by running ```pip install requirements.txt```.

## Usage
### Parameter
Print help to see all command-line options:
```bash
python3 search.py --help
```  
#### Required
```--patter``` and ```--text``` for simply matching the pattern to the text using a finite-state matching algorithm by default:
```bash
python3 search.py -p 'example' -t 'example text'
```  
#### Optional
```--case-insensitive``` to disable case sensitivity:
```bash
python3 search.py -i -p 'example' -t 'example text'
```
```--method``` to choose which matching method (either ```'naive'``` or ```'finite-state'```) is used for the search:
```bash
python3 search.py -p 'example' -t 'example text' -m 'naive'
```
### Examples
