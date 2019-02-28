from .pager import Builder
from tornado.web import RequestHandler


RULES = []

class Page(RequestHandler):
    def get(self):
        page = Builder()
        page.add("test")
        page.render()
        self.write(page.page)

RULES.append(("/", Page))