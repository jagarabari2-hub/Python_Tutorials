print()
print("|========================================|"
      "| Deleting Data from table "
      "||========================================|")
print()
import pymysql
con = pymysql.connect(
    host="localhost",
    user="Jaga",
    password="jaga@123",
    database="python"
)

print("Connected Successfully")
cmd = con.cursor()
try:
    cmd.execute("delete from student where id=11")
    con.commit()
    print("Data Deleted Successfully")
except Exception as e:
    print("Error: ", e)
    con.rollback()
