from bottle import route, run, response, request

#@route('/')
#def index():
#    return f'<b>Hello elevéo</b>!'

@route('/')
def counter():
    count = int( request.cookies.get('counter', '0') )
    count += 1
    response.set_cookie('counter', str(count))
    return 'You visited this page %d times' % count

run(host='0.0.0.0', port=8000,debug=True)
