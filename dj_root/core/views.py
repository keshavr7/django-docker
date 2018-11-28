import redis
from django.conf import settings
from django.http import HttpResponse


def hello(request):
    r = redis.StrictRedis(connection_pool=settings.REDIS_CONNECTION_POOL)
    visits = r.incr("counter")
    html = "<h3>hello there!</h3>" \
           "<b>Visits:</b> {visits}"
    return HttpResponse(html.format(visits=visits))
