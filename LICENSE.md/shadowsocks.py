#/usr/bin/env python
#-*- coding:utf-8 -*-
import os
from multiprocessing import Process

ssl_command = 'sslocal -c /etc/shadowsocks.json'  # 加载配置文件
shadow_command = 'proxychains firefox'   # 启动火狐浏览器

def run_shadowSocks(shadow):
        os.system(shadow_command)

def run_proxychains(proxychains):
        os.system(ssl_command)

def run():
    p = Process(target=run_shadowSocks,args=(shadow_command,)) # 多进程
    p2 = Process(target=run_proxychains,args=(ssl_command,))
    p.start()
    p2.start()
    p2.join()
if __name__ == "__main__":
	run()
