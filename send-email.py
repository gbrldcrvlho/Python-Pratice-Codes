import smtlib

my_email = "testing@gmail.com"
password = "mypw123"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)

connection.sendmail()(from_addr=my_email,
    to_addrs="receipentemail@yahoo.com", msg="Hello World")

connection.close()