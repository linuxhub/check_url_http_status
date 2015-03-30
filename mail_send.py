#!/usr/bin/env python
#encoding:utf8
#author: linuxhub.org
#邮件发送
#导入smtplib和MIMEText

import smtplib,sys 
from email.mime.text import MIMEText 


def send_mail(sub,content): 


              #要发给谁
              mailto_list=["root@linuxhub.org"] 

              #设置服务器，用户名、口令以及邮箱的后缀
              mail_host="smtp.163.com"
              mail_user="xxxx@163.com"
              mail_pass="xxxxxx"
              mail_postfix="163.com"

              '''
              to_list:发给谁
              sub:主题
              content:内容
              send_mail("xxxx@163.com","sub","content")
              '''
              
              me= mail_user+"<"+mail_user+"@"+mail_postfix+">"
              msg = MIMEText(content,_charset='gbk') 
              msg['Subject'] = sub 
              msg['From'] = me 
              msg['To'] = ";".join(mailto_list)
              
              try: 
                            s = smtplib.SMTP() 
                            s.connect(mail_host) 
                            s.login(mail_user,mail_pass) 
                            s.sendmail(me, mailto_list, msg.as_string()) 
                            s.close() 
                            return True
              
              
              except Exception, e: 
                            print str(e) 
                            return False
                            
              
if __name__ == '__main__': 
              if send_mail(u'这是python测试邮件标题',u'python发送邮件内容'): 
                            print u'发送成功'
              else: 
                            print u'发送失败'