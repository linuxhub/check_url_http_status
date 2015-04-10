#!/usr/bin/env python
#encoding:utf8
#author: linuxhub.org
#chekc_url_status.py
#检查网页连接url状态

import requests, time, socket, requests

#加载邮件发送器
import mail_send


#当前时间
def current_time():
              return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())


#根据URL获取IP地址
def url_find_ip(url):
              domain = url.split('/')[2]
              ip = socket.gethostbyname(domain)              
              return ip




#根据ip地址查询出IP所在的地理位置
def get_ip_info(ip):
              r = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=%s' %ip)
              if  r.json()['code'] == 0 :
                            i = r.json()['data']
                            country = i['country']  #国家 
                            area = i['area']        #区域
                            region = i['region']    #地区
                            city = i['city']        #城市
                            isp = i['isp']          #运营商 
                            ip_info = u'%s,%s地区,%s%s,%s' %(country, area, region, city, isp)
                            return ip_info



def main(url_file):
              #取出文件内容
              url_list = []
              with open(url_file) as f:
                            for line in f.readlines():  
                                          url_list.append(line.strip())
                            
                            
              #检测url返回的http状态
              for url in url_list:
                            ip = url_find_ip(url)     #ip
                            ip_info = get_ip_info(ip) #ip所在地
                            curr_time = current_time() #当前时间
                            r = requests.get(url) 
                            status = r.status_code #http状态 
                            
                            #print status,ip,ip_info,url
                            #print u"状态代码: %s\n服务器IP地址: %s\nIP的地理位置: %s\nURL链接: %s\n" % (status, ip, ip_info, url)
                            
                            if status == 200:
                                          #info = u"链接地址: 正常\n\n状态代码: %s\n\n当前时间: %s\n\n服务器IP地址: %s\n\nIP的地理位置: %s\n\nURL链接: %s\n" % (status, curr_time, ip, ip_info, url)
                                          #mail_send.send_mail(u'检测ULR链接【正常】', info)                                          
                                          #print info 
                                          pass
                            elif status == 404:
                                          info = u"链接地址: 错误\n状态代码: %s\n当前时间: %s\n服务器IP地址: %s\nIP的地理位置: %s\nURL链接: %s\n" % (status, curr_time, ip, ip_info, url)
                                          mail_send.send_mail(u'检测ULR链接【错误】', info)
                                          #print info
                            else:
                                          info = u"链接地址: 异常\n状态代码: %s\n当前时间: %s\n服务器IP地址: %s\nIP的地理位置: %s\nURL链接: %s\n" % (status, curr_time, ip, ip_info, url)
                                          title = u'检测ULR链接【异常 %s】' %status
                                          mail_send.send_mail(title, info)
                                          #print info
                                          

if __name__ == '__main__':                                          
              url_file = 'url.txt'
              main(url_file)


