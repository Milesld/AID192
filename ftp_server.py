from socket import *
import os,sys
import signal

def client_handle(c):
    while True:
        data = c.recv(1024)
        file_list = os.listdir('file')
        files = []
        for file in file_list:
            if os.path.isfile(file):
                files.append(file)
        if data.decode() == 'list':
            msg = ','.join(files)
            c.send(b'服务端文件为：%s'%msg)
        elif data.decode() == 'get file':
            
        elif data.decode() == 'put file':
            c.send(b'the server is ready to receieve...')
            data = c.recv(1024)

        print(data)
        c.send(b'ok')
    c.close()


def main():
    #创建监听套接字
    HOST = '0.0.0.0'
    PORT = 9999
    ADDR = (HOST,PORT)
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    #处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    print('listen the port 9999...')
    #循环等待客户端连接
    while True:
        try:
            c,addr = s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit('服务器退出')
        except Exception as e:
            print(e)
            continue
        #创建子进程
        pid = os.fork()
        if pid == 0:
            s.close()
            client_handle(c) #处理客户端请求
            os._exit(0)
        else:
            c.close()


if if __name__ == "__main__":
    main()