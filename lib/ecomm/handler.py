import webapp2
import jinja2
import os
import logging


template_dir = os.path.join(os.path.dirname(__file__),'..','..','templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape=True)
                                #extensions=['jinja2.ext.autoescape'])

class Handler(webapp2.RequestHandler):
    def write(self,*a,**kw):
        self.response.out.write(*a,**kw)
    def render_str(self,template,**params):
        t=jinja_env.get_template(template)
        return t.render(params)
    def render(self, template,**kw):
        self.write(self.render_str(template,**kw))

 #    def initialize(self, *a, **kw):
	# webapp2.RequestHandler.initialize(self,*a,**kw)
 #        uid = self.request.cookies.get('uid')
 #        self.user = None
 #        if(uid):
 #            userid = int(uid.split("||")[0])
 #            if(util.verifyLoginUser(uid)):
 #                self.user = User.get_by_id(userid)