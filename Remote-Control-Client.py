import socket
import time
tcp_client = socket.socket()
ip = input("ip")
port = input("port")
wait_time = 5
print('将要连接：%s:%s' % (ip, port))
start_time = time.time()
while True:
    if (time.time() - start_time) >= wait_time:
        raise Exception('对面不想连！或者是ip错误！\n ip: %s:%s' % (ip, port))
    try:
        print('正在连接····· %s ' % (time.time() - start_time))
        tcp_client.connect((ip,int(port)))
        print('已连接')
        break
    except:
        continue
while True:
    command=input(">")
    tcp_client.send(command.encode())
    if command=="exit":
        break
tcp_client.close()