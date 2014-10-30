#!/usr/bin/env python

import logging

from google.appengine.ext import ndb
# from google.appengine.api import files
# from google.appengine.api import images
# from google.appengine.api import search
# from google.appengine.ext import blobstore
# from google.appengine.api import memcache
# from google.appengine.api import taskqueue


MC_ALL_THE_MODELS = 'MC_ALL_THE_MODELS'

class The_model(ndb.Model):
    # the_blob = ndb.BlobKeyProperty()
    # the_string = ndb.StringProperty()
    # the_bool = ndb.BooleanProperty(default=False)
    # the_key = ndb.KeyProperty(repeated=True)
    # the_int = ndb.IntegerProperty(default=0)

    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty(auto_now=True)

    # @property
    # def image_url(self):
    #    if self.image:
    #        return images.get_serving_url(self.image)

    def create():
        pass

    def validate():
        pass

    def serialize(self):
        return {
            # 'the_blob'      : str(self.the_blob),
            # 'the_string'    : self.the_string,
            # 'the_bool'      : str(self.the_bool),
            # 'the_id'        : str(self.the_key),
            # 'the_int'       : self.the_int
        }

    @classmethod
    def get_all(cls):
        r = memcache.get(MC_ALL_THE_MODELS)
        if not r:
            r = cls.query().fetch()
            if r:
                memcache.set(MC_ALL_THE_MODELS, r)
        return r

    # @classmethod
    # def delete_by_id(cls, the_id):
    #     r = cls.get_by_id( int(the_id) )
    #     if not r:
    #         raise Exception()
    #     fut = r.key.delete_async()
    #     fut.get_result()
