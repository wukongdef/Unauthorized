#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:Wukongdef
# Time:20220419
import socket
from sys import argv
import optparse

def banner():
    print("""
  _____            _  _        _    _          
 |  __ \          | |(_)      | |  | |   /\    
 | |__) | ___   __| | _  ___  | |  | |  /  \   
 |  _  / / _ \ / _` || |/ __| | |  | | / /\ \  
 | | \ \|  __/| (_| || |\__ \ | |__| |/ ____ \  
 |_|  \_\\\___| \__,_||_||___/  \____//_/    \_\\
                                                
                                                --by:wukongdef v1.0 
                                        """)

def start(file):
    with open(file, "r", encoding='UTF-8') as f,open('Success.txt','w',encoding='utf-8') as f1_object,open('Fail.txt','w',encoding='utf-8') as f2_object:
        for target in f:
            target = target.strip()
            ip = str(target.split(':')[0])
            port = int(target.split(':')[1])
            # print(ip)
            res = redis(ip=ip,port=port)#执行redis()函数，将ip,port传入
            if res[0]: #若为True，则存在未授权，提取位置为1的元素写入success文件对象
                f1_object.write(res[1] + "\n")
            else:
                f2_object.write(res[1] + "\n")

def redis(ip,port):
    try:
        socket.setdefaulttimeout(3)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send(bytes("INFO\r\n", 'UTF-8'))
        result = s.recv(1024).decode()
        if "redis_version" in result:
            data = "\033[31m"+ip + ":"+str(port)+ "存在redis未授权"+"\033[0m"
            print(data)
            data1 = ip + ":"+str(port)
        judge = [1,data1] #做判断，返回一个列表给res
        s.close()
    except:
        data = "\033[36m"+ip + ":"+str(port)+ "不存在redis未授权"+"\033[0m"
        print(data)
        data1 = ip + ":"+ str(port)
        judge = [0,data1]
    
    return judge

def single(ip,port):
    try:
        socket.setdefaulttimeout(3)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send(bytes("INFO\r\n", 'UTF-8'))
        result = s.recv(1024).decode()
        if "redis_version" in result:
            print("\033[31m"+ip + ":"+str(port)+ "存在redis未授权"+"\033[0m")
        s.close()
    except:
        print("\033[36m"+ip + ":"+str(port)+ "不存在redis未授权"+"\033[0m")

if __name__== '__main__':
        banner()
        usage = ("Usage: 批量：%prog -f <target file>\n       单个：%prog -i <target ip> -p <target port>\n\n"
                "Example: python3 %prog -f ip.txt\n         python3 %prog -i 1.1.1.1 -p 6379")
        parse = optparse.OptionParser(usage)
        parse.add_option('-f', dest='filename', type='string', help='target file')
        parse.add_option('-i',dest='ip',help='target ip')
        parse.add_option('-p',dest='port',help='target port')
        (options, args) = parse.parse_args()
        try:
            if argv[1] == '-i':
                single(ip=str(options.ip),port=int(options.port))#将实参传入形参
            else:
                start(file=options.filename)#将实参传入形参
        except:
            print("输入有误！-h 显示帮助信息。")