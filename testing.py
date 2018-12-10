import smtplib
from email.mime.text import MIMEText
from email.header import Header

HISTORY = 'LOL'

# Настройки
mail_sender = 'biostat18@mail.ru'
mail_receiver = 'biostat18@mail.ru'
username = 'biostat18@mail.ru'
password = 'qwerty3301'
server = smtplib.SMTP('smtp.mail.ru:587')

# Формируем тело письма
subject = 'Привет всем Маркам!'
# subject = 'Приветик ' + mail_sender + '!' # + mail_sender
body = HISTORY
msg = MIMEText(body, 'plain', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')

# Отпавляем письмо
server.starttls()
server.ehlo()
server.login(username, password)
server.sendmail(mail_sender, mail_receiver, msg.as_string())
server.quit()
