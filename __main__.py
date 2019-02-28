import tornado.ioloop
import tornado.web

import user_interface
import application_interface


RULES = [
    *user_interface.RULES,
    *application_interface.RULES,
]

def make_app():
    return tornado.web.Application(RULES)

if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.instance().start()