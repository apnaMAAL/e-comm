#!/usr/bin/env python

import webapp2
import os
import logging
import sys
sys.path.insert(0, 'lib')

from ecomm.handler import Handler

class HomeHandler(Handler):
    def get(self):
        self.render('hello.html')


app = webapp2.WSGIApplication([
    ('/', HomeHandler)
], debug=False)