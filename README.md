# Data-Modeling-with-PostgreSQL
This repository contains the code to define fact and dimension tables of a PostgreSQL database of star schema designed for particular analytic focus. The repo also contains code for the ETL pipeline that transfers data from files in two local directories into the tables in the database using Python and SQL

## Project Description

A startup wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. Their analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As a data engineer I created a Postgres database schema with tables and ETL pipeline designed to optimize queries on their song play analysis.

## Project Structure

* `data` -  folder containing all the JSON logs that contain data about user activity on app and metadata about songs.
* `sql_queries.py` - contains all sql queries that are used to Create, Insert data and Drop tables.
* `create_tables.py` - Run this file to reset tables before each time you run your ETL scripts.
* `test.ipynb` - displays the first few rows of each table within the database to test the output.
* `etl.ipynb` - reads and processes a single JSON log containing data about user activity and a single JSON log containing song metadata and loads the data into appropriate tables. This was used to develop the initial ETL pipeline with small amount of data.
* `etl.py` - reads and processes all JSON logs and loads the data into the tables.
* `README.md` - Provides a summary of the project and discussions on the data modelling.

## Choice of Database

The reason that I chose a relational database management system for this project are as follows:

* The volume of data the startup is dealing with is quite a small dataset.
* The data from the music streaming app is structured as we know how the key-value pairs are stored inside the JSON logs and what are their data types. 
* Easier to change to business requirements and flexibility in queries as the analytics team would want to perform ad-hoc queries to get a better understanding of the songs that different users are listening to.
* The analytics team would want to be able to do aggregations and analytics on the data.
* The ability to do JOINs would be very useful here due to the way data is getting logged in JSON files. Please see Entity relationship diagram below. Even though JOINs are slow, due to the small size of the dataset this shouldn't be a problem.

## Entity Relationship Diagram (ERD)

![alt text](https://raw.githubusercontent.com/username/projectname/branch/path/to/img.png)

The above represents the entity relationship diagram which shows how the different keys within the JSON logs can be connected together in a star schema. **songplays** is the fact table showing foreign keys that connect this table to all the other dimension tables. **users, time, songs, artists** are all dimension tables, each containing a primary key unique to each table. A star schema was chosen for this database design because of the following reasons:

* Star schema supports denormalization of the data, which would be quite useful in this analytics case as this will allow the analytics team to execute simple queries and fast aggregations on the data. Even though, denormalizing the data may lead to Data integrity issues, this has been tackled through the upsert query clauses in `sql_queries.py`.
* Star schema supports one to one mapping, which is easy to implement and works very well in this case due to the small number of keys within the JSON logs. 

## ETL Pipeline

Once the database and tables has been created a ETL Pipeline is applied to the user activity data and the song metadata. Please see list of key steps that happens in the Pipeline below:

* A list of all the JSON files that exist within a specified directory containing information about the song metadata is created.
* All of these JSON files are then transformed into a Pandas Dataframe.
* All the values that exist in the Dataframe for each of the column within the **songs** table is then selected and inserted into the table.
* All the values that exist in the Dataframe for each of the column within the **artists** table is then selected and inserted into the table.
* A list of all the JSON files that exist within a specified directory containing information about the user activity on the app is created.
* All of these JSON files are then transformed into a Pandas Dataframe.
* A filter is then applied on the Dataframe to only select the rows that contain the column page within the Dataframe as `NextSong`.
* The epoch timestamps which are in `ms` is converted to a datetime format and data extracted from them for all the columns that exist within the **time** table and inserted into the table.
* All the values that exist in the Dataframe for each of the column within the **users** table is then selected and inserted into the table.
* Since the log file does not specify an ID for either the song or the artist, a join was performed to get the song ID and artist ID by querying the **songs and artists** tables to find matches based on song. The result of this query was then inserted into the **songplays** table alongwith all the other values that existed in the Dataframe for each of the column within the table.

## Running the scripts

### Udacity Workspace

To run the project in Udacity workspace, copy the contents of the repo in the workspace and ensure you have a version of python3 running. Then execute the below commands in the terminal in order:

```python
python create_tables.py
```
```python
python etl.py
```
Then, open `test.ipynb` and execute the SQL queries in the notebook to see the output from the Database.

### Locally in Ubuntu

Ensure you are working with Ubuntu 16.04 or 18.04.

* Firstly, install postgre in Ubuntu if it doesn't exist already by following this [link](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04). **Only follow the installation section otherwise you may mess it up for running this Project**.
* You will need to configure postgre to have a user named `student` with password `student` and create a database called `studentdb`. Follow this [video](https://www.youtube.com/watch?v=-LwI4HMR_Eg) to do this. You can skip the installation section in the video.
* Setup Jupyter Notebook to run on your local machine if there isn't one already running by following until Step 3 of this [link](https://www.digitalocean.com/community/tutorials/how-to-set-up-jupyter-notebook-with-python-3-on-ubuntu-18-04). Copy the contents of this repo in the folder that you will create in Step 2.
* Then execute the below commands in the virtualenv terminal in order (You will probably have to install some python modules to get it working):
```python
python create_tables.py
```
```python
python etl.py
```
* Execute the below command in virtualenv terminal
```python
jupyter notebook
```
* Open `test.ipynb` from Jupyter notebook in browser and execute the SQL queries in the notebook to see the output from the Database.
