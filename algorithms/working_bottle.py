from bottle import route, run, template, static_file,request, get, post
import json



class Login:
    def register_routes(self):
        route("/login", method='GET', callback=self.login())
        route("/login", method='POST', callback=self.do_login())

    @get('/login') # or @route('/login')
    def login(self):
        return '''
        <form action="/login" method="post">
        Username: <input name="username" type="text" />
        Password: <input name="password" type="password" />
        <input value="Login" type="submit" />
        </form>
        '''
    @post('/login') # or @route('/login', method='POST')
    def do_login(self):
        username = request.forms.get('username')
        password = request.forms.get('password')
        if username and password:
            return "<p>Your login information was correct.</p>"
        else:
            return "<p>Login failed.</p>"


run(host='localhost', port=8080)