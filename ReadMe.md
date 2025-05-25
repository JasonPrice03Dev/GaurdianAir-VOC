Step 1: 

I have attatched the following files to the upload:

- MyProject(Virtual Env)
- ProjectFiles (Project Code)
- python (Contains ServiceAccountKey)

(WARNING - if you do not download the python and MyProject file it will not run)

(WARNING - This project must be tested on a Raspberry Pi 5 due to virtual environment dependencies)

These are all the files needed to run the project so please download all and implement them into your files

Step 2:

Put these files in a folder, for example I chose my user folder so these are the locations I stored each file (Replace YOUR_USERNAME with your actual Pi username, e.g., k00268716):

- /home/YOUR_USERNAME/MyProject
- /home/YOUR_USERNAME/Documents/ProjectFiles
- /home/YOUR_USERNAME/python

Step 3:

Run the following to activate the virtual environment:

- source /home/YOUR_USERNAME/MyProject/my_venv/bin/activate (Replace YOUR_USERNAME with your actual Pi username, e.g., k00268716)

Step 4:

Run the following to enter the project files while in the virtual environment

- cd /home/YOUR_USERNAME/Documents/ProjectFiles (Replace YOUR_USERNAME with your actual Pi username, e.g., k00268716)


Step 5:

Run the following code to run the application:

- python webserver.py (Ensure SenseHat is attacthed in order to work)

Step 6:

You may now go to http://localhost:5000/ to view the dashboard
