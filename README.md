# Unauthorized
可快速检测各类未授权漏洞,支持批量和单个。

查看帮助：python3 xxx.py  -h 

批量：python3  xxx.py  -f  <target.txt>
     <target.txt> 为目标IP+端口集合
     例：
     x.x.x.x:1234
      
     运行后会在脚本同级目录生成两个文件，Success储存检测成功的地址，Fail储存检测失败的地址。
     
     
单个：python3 xxx.py -i <target ip> -p <target port>

