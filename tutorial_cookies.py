import cherrypy


class MyCookieApp(object):
    @cherrypy.expose
    def set(self):
        cookie = cherrypy.response.cookie
        cookie['cookie_name'] = 'cookie_value'
        cookie['cookie_name']['path'] = '/'
        cookie['cookie_name']['max-age'] = 3600
        cookie['cookie_name']['version'] = 1
        return '<html><body>Hello, I\'ve sent you a cookie!'

    @cherrypy.expose
    def read(self):
        cookie = cherrypy.request.cookie
        res = """<html><body>Hi, you sent me %s cookies.<br />
                Here is a list of cookie names/values:<br />""" % len(cookie)
        for name in cookie.keys():
            res += "name: %s, value: %s<br>" % (name, cookie[name].value)
        return res + "</body></html>"

if __name__ == '__main__':
    cherrypy.quickstart(MyCookieApp(), '/cookie')
