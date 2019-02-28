from tornado.web import RequestHandler
from database_interface import Table
from .utils import js_in, js_out


RULES = []

class PowerTest(RequestHandler):
    def get(self):
        table = Table("thetwodottest", host="mbconnect.net")
        table.drop()
        table.create()
        table.insert(name="gay")
        table.insert(name="pay")
        r = table.find(name="gay")
        table.update(r[0]['id'], name="may")
        self.write(js_out(table.select()))


RULES.append(("/power/test", PowerTest))
