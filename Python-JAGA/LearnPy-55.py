print()
print("|========================================|"
      "| Connecting to a Database in Python "
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
    cmd.execute("SELECT * FROM student")
    rs = cmd.fetchall()
    for row in rs:
        print(row[0], "|", row[1], "|", row[2], "|", row[3], "|", row[4])
except Exception as e:
    print("Error :", e)
finally:
    con.close()
