import sqlite3

def main():
    db=sqlite3.connect('db/sample.db')
    cur=db.cursor()

    #creating the table
    cur.execute('DROP TABLE IF EXISTS tmp')
    cur.execute('CREATE TABLE IF NOT EXISTS tmp(a TEXT, b TEXT, c TEXT)')
    cur.execute("INSERT INTO tmp VALUES ('ONE', 'TWO','THREE')")
    cur.execute("INSERT INTO tmp VALUES ('ONE', 'TWO','THREE')")
    cur.execute("INSERT INTO tmp VALUES ('ONE', 'TWO','THREE')")
    db.commit()

    cur.execute('SELECT * FROM tmp')
    row=cur.fetchone()
    while row:
        print(row)
        row=cur.fetchone()

    cur.close()
    db.close()

if __name__=="__main__":
    main()
