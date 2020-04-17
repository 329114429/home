# 网关

import os
import sys

from Web_demo.wsgi_example.app import simple_app


def wsgi_to_bytes(s):
    return s.encode()


def run_with_cgi(application):
    environ = dict(os.environ.items())
    environ['wsgi.input'] = sys.stdin.buffer
    environ['wsgi.errors'] = sys.stderr
    environ['wsgi.version'] = (1, 0)
    environ['wsgi.multithread'] = False
    environ['wsgi.multiprocess'] = True
    environ['wsgi.run_once'] = True

    if environ.get('HTTPS', 'off') in ('on', '1'):
        environ['wsgi.url_scheme'] = 'https'
    else:
        environ['wsgi.url_scheme'] = 'http'

    headers_set = []
    headers_sent = []

    def write(data):
        out = sys.stdout.buffer
        if not headers_set:
            raise AssertionError("write() before start_response()")
        elif not headers_sent:
            # 在输入一行数据之前,先发送响应头
            status, response_headers = headers_sent[:] = headers_set
            out.write(wsgi_to_bytes('status:%s\r\n' % status))

            for header in response_headers:
                out.write(wsgi_to_bytes('%s:%s\r\n' % header))

        out.write(data)
        out.flush()

    def start_response(status, response_headers, exc_info=None):
        if exc_info:
            try:
                if headers_sent:
                    # 如果已经发送了header ,则重新抛出异常信息
                    raise (exc_info[0], exc_info[1], exc_info[2])
            finally:
                exc_info = None
        elif headers_set:
            raise AssertionError("Headers already set!")

        headers_set[:] = [status, response_headers]

    result = application(environ, start_response)

    try:
        for data in result:
            if data:
                write(data)
        if not headers_set:
            write("")
    finally:
        if hasattr(result, 'close'):
            result.close()


if __name__ == '__main__':
    run_with_cgi(simple_app)
