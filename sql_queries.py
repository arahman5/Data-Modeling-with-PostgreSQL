# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

# This is the fact table that contains the primary keys from the below 4 Dimension tables so that JOINs can be made between the fact table and dimension tables. 
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

# Adding a upsert statement to tackle Data Integrity issue in case of duplicated data
songplay_table_insert = ("""INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
                           
""")

# Adding a upsert statement to tackle Data Integrity issue in case of duplicated data, it maybe possible for a user to chnage their level from free to paid or vice versa
user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) 
                        VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) 
                        DO UPDATE
                             SET level = EXCLUDED.level
""")

# Adding a upsert statement to tackle Data Integrity issue in case of duplicated data
song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) 
                        VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING                            
                            
""")

# Adding a upsert statement to tackle Data Integrity issue in case of duplicated data
artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude) 
                        VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")

# Adding a upsert statement to tackle Data Integrity issue in case of duplicated data
time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("""SELECT songs.song_id, songs.artist_id FROM songs 
                    JOIN artists on songs.artist_id = artists.artist_id
                    WHERE title = %s
                    AND name = %s
                    AND duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]