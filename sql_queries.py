# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

# This is the fact table that contains the primary keys from the below 4 Dimension tables so that JOINs can be made between the fact table and dimension tables
songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (
                                songplay_id int PRIMARY KEY, 
                                start_time timestamp, 
                                user_id int, 
                                level varchar, 
                                song_id varchar, 
                                artist_id varchar, 
                                session_id int,
                                location varchar,
                                user_agent varchar
                                );
""")

# This is the dimension table containing the information about users of the app
user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
                                user_id int PRIMARY KEY,
                                first_name varchar,
                                last_name varchar,
                                gender varchar,
                                level varchar
                                );
""")

# This is the dimension table containing information about the songs in the database. artist_id is a primary key of another dimension table so must be declared as not null to
#ensure that there are no issues during joining, there must be a corresponding artist_id for a particular song_id
song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
                                song_id varchar PRIMARY KEY,
                                title varchar,
                                artist_id varchar NOT NULL, 
                                year int,
                                duration float
                                );
""")

# This is the dimension table containing information about the artists in the database
artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
                                artist_id varchar PRIMARY KEY,
                                name varchar,
                                location varchar,
                                latitude float,
                                longitude float
                                );
""")

# This is the dimension table containing information about timestamps of records in songplays table
time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
                                start_time timestamp PRIMARY KEY,
                                hour int,
                                day int,
                                week int,
                                month int,
                                year int,
                                weekday varchar
                                );
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]