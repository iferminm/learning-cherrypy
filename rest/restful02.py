import cherrypy


@cherrypy.popargs('name')
class Band(object):
    def __init__(self):
        self.albums = Album()

    @cherrypy.expose
    def index(self, name):
        return 'About %s...' % name


@cherrypy.popargs('title')
class Album(object):
    @cherrypy.expose
    def index(self, name, title):
        return 'About %s by %s' % (title, name)


if __name__ == '__main__':
    cherrypy.quickstart(Band())

