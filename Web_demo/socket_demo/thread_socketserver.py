# 多线程服务器
import socket
import errno
import threading
import time

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'

body = """hello, world <h1>django 企业开发</h1> - from {thread_name}"""

response_params = [
    'HTTP/1.0 200 OK',
    'date: Sun, 08 Mar 2020 09:33:15 GMT',
    'content-type: text/html; charset=utf-8',
    'content-length : {length}\r\n',
    body,
]

response = '\r\n'.join(response_params)


def handle_connect(conn, address):
    print(conn, address)
    time.sleep(1)  # 自行调试,设置睡眠时间

    request = b""
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)

    print(request)

    current_thread = threading.currentThread()
    content_length = len(body.format(thread_name=current_thread.name).encode())
    print(current_thread.name)

    conn.send(response.format(thread_name=current_thread.name, length=content_length).encode())
    conn.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置端口可复用,保证我们每次ctrl+c组合键之后,快速重启
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 8000))

    server_socket.listen(10)
    print('http://127.0.0.1:8000')

    server_socket.setblocking(False)  # 设置 socket 为非阻塞模式

    try:
        i = 0
        while True:
            try:
                conn, address = server_socket.accept()
            except socket.error as e:
                if e.args[0] != errno.EAGAIN:
                    raise
                continue
            i += 1
            print(i)
            t = threading.Thread(target=handle_connect, args=(conn, address), name='thread-%s' % i)
            t.start()
    finally:
        server_socket.close()


if __name__ == '__main__':
    main()
