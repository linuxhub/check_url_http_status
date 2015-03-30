#!/usr/bin/env python
#encoding:utf8
#author: linuxhub.org
#chekc_url_status.py
#检查网页连接url状态

import requests, time

#加载邮件发送器
import mail_send


#当前时间
def current_time():
              return time.strftime('%Y-%m-%d %H:%m:%S',time.localtime())



#检查url的http状态
def check_http_status(url_file):
              
              #取出文件内容
              url_list = []
              with open(url_file) as f:
                            for line in f.readlines():  
                                          url_list.append(line.strip())
              
              
              #检测url返回的http状态
              url_status = {}
              for url in url_list:
                            r = requests.get(url)
                            status = r.status_code 
                            if not url_status.has_key(url):
                                          url_status[url] = {}
                                          url_status[url] = status
                                          
              return url_status

 
#判断http状态
def if_status(url_status):                           
              for url,status in url_status.iteritems():
                            #print status,url
                            if status == 200:
                                          #info = u'提示: OK\n状态: %s\n时间: %s\n地址: %s\n' %(status, current_time(), url)
                                          #mail_send.send_mail(u'检测ULR链接【正常】', info)
                                          pass

                            elif status == 404:
                                          info = u'提示: Error\n状态: %s\n时间: %s\n地址: %s\n' %(status, current_time(), url)
                                          mail_send.send_mail(u'检测ULR链接【出错】', info)

                            else:
                                          info = u'提示: Warning\n状态: %s\n时间: %s\n地址: %s\n' %(status, current_time(), url) 
                                          mail_send.send_mail(u'检测ULR链接【异常】', info)



if __name__ == '__main__':                                          
              url_file = 'url.txt'
              url_status = check_http_status(url_file) 
              if_status(url_status)
