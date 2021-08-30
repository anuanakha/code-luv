import cx_Oracle

try:
	con = cx_Oracle.connect('system,/root@localhost:1521/xe')

except cx_Oracle.DatabaseError as er:
	print('There is an error in the Oracle database:', er)

else:
	try:
		cur = con.cursor()
		cur.execute('select * from movie')
		rows = cur.fetchall()
		print(rows)
except cx_Oracle.DatabaseError as er:
		print('There is an error in the Oracle database:', er)

	except Exception as er:
		print('Error:'+str(er))

