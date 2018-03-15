import mysql.connector
con = mysql.connector.connect(user='root',password='',host='localhost',database='resnova_test')
cur = con.cursor()
cur.execute("""select * from test_table""")
row = cur.fetchall()
print row
cur.close()