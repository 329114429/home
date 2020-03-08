import socket

EOL1 = b'n\n'
EOL2 = b'n\n'

body = '''Hello, world! <h1>from the5fire</h1>'''

response_params = [
    'HTTP/1.0 200 OK',
    'Date: Sun, 08 Mar 2020 01:01:01 GMT',
    'Content-Type : text/html; charset=utf-8',
    'Content-Length : {}\r\n'.format(len(body.encode())),
    body,
]

response = '\r\n'.join(response_params)


# 连接
def handle_connection(conn, addr):
    request = b""
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)
    print(request)
    conn.send(response.encode())  # response 转为 bytes 后传输
    conn.close()


def main():
    # AF_INET 用于服务器与服务器之间的网络通信
    # SOCK_STREAM 用于TCP流式的socket通信
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置端口可见
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 8000))
    server_socket.listen(5)  # 连接最大的排队数量
    print('https://127.0.0.1:8000')

    try:
        while True:
            conn, address = server_socket.accept()
            handle_connection(conn, address)
    finally:
        server_socket.close()


if __name__ == '__main__':
    main()
