import sqlite3

class Video:

    def __init__(self):
        self.conn = sqlite3.connect('test.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.creat_tale()

    def creat_tale(self):
        #self.curor.execute(""" DROP TABLE products """)
        self.cursor.execute("""
        Create TABLE IF NOT EXISTS videos(
            id INTEGER NOT NULL PRIMARY KEY,
            Name Text NOT NULL,
            Category Text NOT NULL,
            Likes Text NOT NULL,
            Views Real NOT NULL,
            Link Text NOT NULL
        )""")


    def insert_values(self,Name,Category,Likes,Views, Link):
        self.cursor.execute(""" INSERT OR IGNORE INTO videos(Name, Category, Likes, Views, Link) Values(?,?,?,?,?) """, (Name, Category, Likes, Views, Link) )
        self.conn.commit()
        msg = "record commited"

    def delete_video(self,video_id):
        self.cursor.execute(""" DELETE FROM videos WHERE id = (?) """,  (video_id,))
        self.conn.commit()
        msg = "record commited"

    def get_video_by_name(self, name):
        self.cursor.execute(""" SELECT * FROM videos WHERE Name = (?) """,(name,))
        results = self.cursor.fetchall()
        return results

    def get_video_by_id(self, video_id):
            self.cursor.execute(""" SELECT * FROM videos WHERE id = (?) """,(video_id,))
            results = self.cursor.fetchone
            return results

    def get_all_videos(self):
        self.cursor.execute(""" SELECT * FROM videos """)
        rows = self.cursor.fetchall()
        return rows
