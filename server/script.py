from bottle import route, run, template, static_file


@route('/Hello')
def Hello():
    return template('index')


if __name__=='__main__':
    run(host= 'localhost', port=8080)
