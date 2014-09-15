#!/usr/bin/env python

import webapp2
import os
import logging
import sys
sys.path.insert(0, 'lib')


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello wrold,')


app = webapp2.WSGIApplication([
    ('/', HomeHandler)
], debug=False)