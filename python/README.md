# [Name]
Project description

## Prerequisites
All required packages are provided in [requirements.txt](src/requirements.txt) and can be installed using `pip`
````sh
pip install -r requirements.txt
````

## Configuration
An example configuration is provided as [app.conf](app.conf).

**[Logging]** is provided to the logger configuration as keyword arguments

## Run the code

````sh
python3 main.py [arguments] 
````

**Command Line Arguments**

Argument                 | Description
-------------------------|------------
-h, --help               | shows help message and exits
-c `path`, --conf `path` | provides path to config file
