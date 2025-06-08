import smtplib as s
ob= s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('tiyashah313@gmail.com','dxzt arne omha prfz')
subject = "test python"
body = "I Love Python"
message = "subject:{}\n\n{}".format(subject,body)
listadd=['biren007tea@gmail.com', "sonal71116@gmail.com"]
ob.sendmail('tiyashah313@gmail.com',listadd,message)
print("Mail has been send")
ob.quit()