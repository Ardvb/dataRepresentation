# GMIT Data Representation Big Project

### Author: Arnoud van Balkom
- Lecturer: Andrew Beatty
- Email: G00376518@gmit.ie

## Getting started
- Download [Anaconda](https://www.anaconda.com/)

- Follow these steps to download this repository:

1. Go to my repository on Github: https://github.com/Ardvb/dataRepresentation
2. Click the clone or download button.
3. Save the repository to your device.
4. Run the sql files to create the necessary databases
4. Connect to server by running 'rest_server.py' and follow the on screen instructions

## Contents of this repository

- Two Python DAO files that will connect to the MYSQL databases
- Static html pages that allow the user to communicate with the databases in a nice way
- dbconfig.py and dbconfigs.py are files to enter credentials that will subsquently be read by the DAO files and then can be used to connect to the database
- requirements.txt contains a list of required packages that should be installed in a virtual environment in order for this server to run.
- Two mysql files that can be ran to create the necessary databases
- a python server rest_server.py that uses flask for allowing to make CRUD operations to the databases.
