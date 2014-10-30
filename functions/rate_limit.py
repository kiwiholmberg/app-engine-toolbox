import webapp2
from functools import wraps
from google.appengine.api import memcache
from config import exceptions

def rate_limit(seconds_per_request=1):
    def rate_limiter(function):
        @wraps(function)
        def wrapper(self, *args, **kwargs):
            added = memcache.add('%s:%s' % (self.__class__.__name__, self.request.remote_addr or ''), 1,
                               time=seconds_per_request, namespace='rate_limiting')
            if not added:
                raise exceptions.TooManyRequestsError()
            return function(self, *args, **kwargs)
        return wrapper
    return rate_limiter


# class ExampleHandler(webapp2.RequestHandler):
#   @rate_limit(seconds_per_request=2)
#   def get(self):
#     self.response.write('Hello, webapp2!')
