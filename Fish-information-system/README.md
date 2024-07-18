# Fish-Project 
This project is designed to serve as a comprehensive platform for searching and exploring various fish species, their habitats, behavior, and other relevant information. The application is built using Python's Django framework and utilizes MySQL as the database for storing and retrieving fish-related data.

## Installation
To set up the Fish-Project on your local machine, follow these steps:
Dependencies: Install the required dependencies using pip:
Database Setup: Create a MySQL database and import the provided fish_data.sql file for populating the tables with sample data:
Configure Settings: Update the app.config['SQLALCHEMY_DATABASE_URI'] variable in app.py with your MySQL database credentials.
Running the Application
After completing the installation steps, you can run the Fish-AI-Project using the following command:
## Linux/Mac
```bash
gh clone  https://github.com/shim24sa/Fish-information-sysgtem
cd Fish-information-system
python -m venv .venv 
source .venv/bin/activate
pip install -r requirements.txt
python mange.py runserver
```
## Windows
```bat
gh clone  https://github.com/shim24sa/Fish-information-system
cd Fish-information-system
python -m venv .venv 
.\.venv\Scripts\Activate.ps1
.\load_csv.bat
pip install -r requirements.txt
python mange.py runserver
```
The application will be available at http://localhost:5000.
Usage
Once the application is running, users can search for specific fish species and retrieve information about their habitats, behavior, and other relevant data. The application provides a user-friendly interface for navigating and exploring the various fish species in the database.
## Authors
## License
MIT License
## Acknowledgments
Special thanks to the Flask and MySQL communities for providing the tools and resources necessary for making this project a reality.
