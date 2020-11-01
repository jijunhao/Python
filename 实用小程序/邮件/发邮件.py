import smtplib
import pandas as pd
import numpy as np
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

if __name__ == '__main__':
    data = pd.read_excel("E:/大数据二班花名册.xlsx")
    #data = pd.read_excel("E:/测试.xlsx")
    sender = '2818657803@qq.com'
    receiver_list = list(data['QQ'])
    smtpserver = 'smtp.qq.com'
    username = '2818657803@qq.com'
    password = ''
    mail_title = ''
    service = smtplib.SMTP_SSL(host='smtp.qq.com')
    service.connect(host='smtp.qq.com', port=465)
    service.login(username, password)
    for receiver in receiver_list:
        # 创建一个带附件的实例
        receiver_eml = str(receiver) + "@qq.com"
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver_eml
        message['Subject'] = Header(mail_title, 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText('收到后不用回复！', 'plain', 'utf-8'))

        index = receiver_list.index(receiver)
        try:
            # 构造附件
            docx = 'E:/第12章/' + str(data["学号"][index]) + "_" + data["姓名"][index] + ".docx"
            att = MIMEApplication(open(docx, 'rb').read(), 'utf-8')
            att['Content-Type'] = 'application/octet-stream'
            att.add_header('Content-Disposition', 'attachment', filename=('gbk', '', '%s.docx' %(str(data["学号"][index])+"_"+data["姓名"][index]+"_10")))
            #att["Content-Disposition"] = 'attachment; filename=%s.docx' % str(data["学号"][index])
            message.attach(att)
            service.sendmail(sender, receiver_eml, message.as_string())
            print(receiver_eml, "邮件发送成功！")
        except Exception as e:
            print(e)
            print(receiver_eml, "邮件发送失败！", data["姓名"][index], "文件缺失")

    service.quit()