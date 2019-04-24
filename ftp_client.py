from socket import *
import sys
import time

ADDR = ('127.0.0.1',9999)

class FtpClient(object):
    def __init__(self,sockfd):
        self.sockfd = sockfd
    
    def do_list():
        self.sockfd.send(b'L')
        data = self.sockfd.recv(128).decode()
        if data == 'ok':
            while True:
                file = self.sockfd.recv(1024).decode()
                if file == '##':
                    break
                print(file)
            data = self.sockfd.recv()
        else:
            print(data.decode())
        


def main():
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print(e)
        return
    ftp = FtpClient(sockfd)) #创建类实例
    while True:
        print('\n===========命令选项===========')
        print('***          list           ***')
        print('***        get file         ***')
        print('***        put file         ***')
        print('***          quit           ***')
        print('*******************************')
        cmd = input('请输入命令：')
        if cmd.strip() == 'list':
            do_list()

if __name__ == "__main__":
    main()
    