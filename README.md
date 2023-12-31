## Installation:

1. Create a Virtual Environment using pipenv, where
* pipenv is composed of pip + venv
* pip: Used for installing additional packages.
* venv: Creates isolated environments for each project.

2. To install pipenv:
* cd to the desired working folder.
* pip install pipenv
* Use pipenv to install packages: pipenv install pyspark, python=3.9
* command: pipenv install pyspark:
	- creates a virtual environment automatically
	- all installations are managed in the 'Pipfile'
	- Pipfile.lock: has the information about exact version of installed packages
	
	
3. Activating the Environment:
* Activate the environment with: pipenv shell

4. To destroy the virtual environment:
* First, exit the environment if it's active.
* Then, in the project directory, run pipenv --rm.
* This command will remove the specific virtual environment associated with the project.

## Problem Statement and process

1. Find the number of closed orders for each state
2. Data files ( in the data folder):
	* orders.csv
	* customers.csv
3. 	create orders dataframe
4. create customers dataframe
5. Filter the orders dataframe using pyspark based on order status
6. Join the orders filtered with customers (using customer_id as the primary key)
7. do a groupby on state and then aggregate

## Project Structuring:

### Project Folder Name
	
	1. configs folder
	
		- application.conf 

		customers.file.path = /users/Desktop/…. 
		(to keep the project level configurations, like keep file path etc.)
		
		- pyspark.conf ( to give spark level configs, like executor cores, executor memory, 							application, name etc..).. 
		

	2. lib folder

		- ConfigReader.py (all the .conf files can be read) from the config folder. 
		- DataReader.py (to create spark dataframes)
		- DataManipulation.py (all the pyspark transformations)
		- Utils.py (creating Spark session). 


	3. data folder

		- orders.csv
		- customers.csv

	4. application_main.py (main method, entry point for the spark application). 

	5. Pipfile (automatically generated when doing pipenv install pyspark)

	6. Pipfile.lock (automatically generated, along with pipfile)


