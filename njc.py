import cx_Oracle

connection = cx_Oracle.connect(
    user="system",
    password="root",
    dsn="localhost/xe")

print("Successfully connected to Oracle Database")

cursor = connection.cursor()


cursor.execute("""
    begin
        execute immediate 'drop table movie';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;""")

cursor.execute("""
    create table movie (movie_name varchar(20),
                      lead_actor varchar(20),
                      lead_actress varchar(20),
                      year_of_relase number,director varchar(20))""")
    
data = [['uri','vicky kaushal','yami',2019,'aditya dhar'], ['the call','nil','park shin hye',2020,'lee chung-hyun'],['the witch:part1','choi woo-shik','kim da-mi',2018,'park hoon-jung']]
cursor.executemany('insert into employee values(:1,:2,:3)', data)
connection.commit()
print('Multiple records are inserted successfully')
if cursor:
    cursor.close()
if connection:
    connection.close()

 
 
    

