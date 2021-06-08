# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays CASCADE"
user_table_drop = "DROP TABLE IF EXISTS users CASCADE"
song_table_drop = "DROP TABLE IF EXISTS songs CASCADE"
artist_table_drop = "DROP TABLE IF EXISTS artists CASCADE"
time_table_drop = "DROP TABLE IF EXISTS time CASCADE"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(
    songplay_id SERIAL PRIMARY KEY,
    start_time TIMESTAMP NOT NULL,
    user_id INT NOT NULL,
    level INT NOT NULL,
    song_id VARCHAR(50),
    artist_id VARCHAR(50),
    session_id INT NOT NULL,
    location VARCHAR(255) NOT NULL,
    user_agent VARCHAR(255) NOT NULL,
    FOREIGN KEY (start_time)
        REFERENCES time (start_time),
    FOREIGN KEY (user_id)
        REFERENCES users (user_id),
    FOREIGN KEY (song_id)
        REFERENCES songs (song_id),
    FOREIGN KEY (artist_id)
        REFERENCES artists (artist_id)
);
""")

user_table_create = ("""
CREATE TYPE current_gender AS ENUM ('M', 'F');

CREATE TABLE IF NOT EXISTS users(
    user_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender current_gender NOT NULL,
    level INT
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(
    song_id VARCHAR(50) PRIMARY KEY,
    title VARCHAR(255),
    artist_id VARCHAR(50),
    year INT,
    duration NUMERIC,
    FOREIGN KEY(artist_id)
        REFERENCES artists (artist_id)
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(
    artist_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255) NOT NULL,
    latitude NUMERIC,
    longitude NUMERIC
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
    start_time TIMESTAMP UNIQUE,
    hour INT,
    day INT,
    week INT,
    month INT,
    year INT,
    weekday INT
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

create_table_queries = [artist_table_create, user_table_create, song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]