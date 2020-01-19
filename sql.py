import cx_Oracle
import os
os.putenv('NLS_LANG', 'KOREAN_KOREA.KO16MSWIN949')

conn  =  cx_Oracle.connect("scott/oracle@127.0.0.1:1521/orcl")

#pandas.read_sql("sql문장", con = conn)
curs = conn.cursor()
curs.execute("select * from emp")

for row in curs:
    print(row)
    
curs.close()
conn.close()
