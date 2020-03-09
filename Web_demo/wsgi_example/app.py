def simple_app(environ, start_response):
    """simplest possible application object"""
    status = '200 OK'
    response_headers = [
        ('content-type', 'text/html'),
    ]
    start_response(status, response_headers)
    return [b'hello world by haosuozhong \n']

