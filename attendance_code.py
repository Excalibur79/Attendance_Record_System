import sqlite3

def record():
    conn=sqlite3.connect("attendance_record.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS attendance(id INTEGER PRIMARY KEY,name TEXT,section TEXT,enroll INTEGER,status TEXT)")
    conn.commit()
    conn.close()

def insert(name,section,enroll,status):
    conn = sqlite3.connect("attendance_record.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO attendance VALUES(NULL,?,?,?,?)",(name,section,enroll,status))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("attendance_record.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM attendance")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(name="",section="",enroll="",status=""):
    conn = sqlite3.connect("attendance_record.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM attendance WHERE name=? OR section=? OR enroll=? OR status=?",(name,section,enroll,status))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("attendance_record.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM attendance WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,name,section,enroll,status):
    conn = sqlite3.connect("attendance_record.db")
    cur = conn.cursor()
    cur.execute("UPDATE attendance SET name=?,section=?,enroll=?,status=? WHERE id=?",(name,section,enroll,status,id))
    conn.commit()
    conn.close()


record()
#insert("Bihan ChakraBorty","I",1120190009023068,"present")
#delete(5)
update(4,"Spandita Banerjee","I",124124234,"absent")
print(view())



