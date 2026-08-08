student = {
    "name": "Jaga Rabari",
    "roll_no": "101",
    "course": "Web Development",
    "email": "jaga@example.com"
}

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Table</title>
</head>
<body>

<h2>Student Details</h2>

<table border="1" cellpadding="10">
    <tr>
        <th>Name</th>
        <th>Roll No</th>
        <th>Course</th>
        <th>Email</th>
    </tr>
    <tr>
        <td>{name}</td>
        <td>{roll_no}</td>
        <td>{course}</td>
        <td>{email}</td>
    </tr>
</table>

</body>
</html>
""".format(**student)

print(html)