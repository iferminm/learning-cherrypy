import string
import random

import cherrypy


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return '''<html>
            <head></head>
            <body>
                <form method="get" action="generate">
                    <input type="text" value="8" />
                    <button type="submit">Dale ya!</button>
                </form>
            </body>'''

    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))


if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())
