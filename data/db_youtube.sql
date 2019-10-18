-- Database: Youtube_project

-- DROP DATABASE "Youtube_project";

CREATE DATABASE "Youtube_project"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

drop table youtube_video
create table youtube_video
(
video_id VARCHAR(30),
trending_date VARCHAR(30),
category_id VARCHAR(30),
views bigint,
category VARCHAR(50),
likes bigint,
dislikes bigint,
comments_count bigint
)

select * from youtube_video