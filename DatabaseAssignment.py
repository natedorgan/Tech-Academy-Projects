
import sqlite3

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT)")
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# loops through fileList to find files ending in .txt
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            # the .txt file names are stored as individual one element tuples
            # and then inserted into col_fname so each has a row its own
            cur.execute("INSERT INTO tbl_files (col_fname) VALUES (?)", (x,))
            print(x)

conn.close()

