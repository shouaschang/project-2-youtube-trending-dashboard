import psycopg2 as p


con = p.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database="Youtube_data")
cur = con.cursor()
cur.execute("select video_id, likes from \"Youtube_videos\"")
rows = cur.fetchall()

for r in rows:
       print(f"video_id {r[0]} likes {r[1]}")
#    postgreSQL_select_Query = "select * from Youtube_videos"
#    cursor.execute(postgreSQL_select_Query)
con.close()