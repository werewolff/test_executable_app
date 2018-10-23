import datetime
import dateutils


class App:
    def response(offset=0):
        print((datetime.datetime.now().date() + dateutils.relativedelta(days=offset)).isoformat())
ex=App
def now():
    ex.response()
def tomorrow():
    ex.response(1)
def yesterday():
    ex.response(-1)