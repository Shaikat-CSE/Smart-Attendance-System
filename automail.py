import yagmail
import os

receiver = "Shaikat143@gmail.com"  # receiver email address
body = "Attendence File"  # email body
filename = "Attendance"+os.sep+"Attendance_2024-11-07_23-48-02.csv" 

yag = yagmail.SMTP("shaikat.sk@yahoo.com", "ghetgsert")

yag.send(
    to=receiver,
    subject="Attendance Report", 
    contents=body, 
    attachments=filename, 
)

