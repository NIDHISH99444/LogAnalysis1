# LogAnalysis

The third project  of Udacity FSN.This project include large database with million rows ,explored by SQL queries to extract  the desired data.
This project is a blueprint of reporting tool for a newpaper site to discover what kind of articles the site's readers like .
The database contains newspaper articles along with the web server logs.

## Requirements 
- Python3
- Vagrant
- VirtualBox

## Setup
1. Installing  vagrant and virtualBox 
2. Cloning  repository

## Steps 

1. **vagrant up** is used to launching vagrant VM
2. Typing **vagrant ssh** 
3. **psql -d news -f newsdata.sql** commaned is used to load the data,connect the database and runnning the necessary SQL statements.

### Database Tables :
- Authors table
- Articles table
- Log table

4. **python3 newsdata.py**  is used to execute command from command line 	
