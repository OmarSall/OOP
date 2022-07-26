import sqlite3


#integer primary key - auto increment value
class Database:

    def __init__(self,db):     #constructor - cunstruct/initiate the object
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        conn.commit()
        
#we have open connection in a class
        def insert(self, title, author, year, isbn):
            cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
            conn.commit()
            conn.close()
            
        def view(self):
            cur.execute("SELECT * FROM book")
            # conn.commit() we will not perform any changes thus commit is not needed
            rows = cur.fetchall()
            conn.close()
            return rows

        def search(self, title="", author="", year="", isbn=""):
            cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
            # conn.commit() we will not perform any changes thus commit is not needed
            rows = cur.fetchall()
            conn.close()
            return rows 

        def delete(self, id):
            cur.execute("DELETE FROM book WHERE id=?", (id,))
            conn.commit()
            conn.close()
            
        def update(self, id, title, author, year, isbn):
            cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
            conn.commit()
            conn.close()
        
        def __del__():
            conn.close()



# connect()
# insert("The Sun", "John Smith", 1959, 992234992)
# delete(2)
# update(3, "The moon","John Smooth", 1917, 99999 )
# print(view())
# print(search(author ="John Smith"))
