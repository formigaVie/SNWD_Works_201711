#!/usr/bin/env python
import os
import jinja2
import webapp2
import random
import datetime

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)

class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))

class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")



class BlogHandler(BaseHandler):
    def get(self):
        current_datetime = datetime.datetime.now()
        my_number = random.randint(0,9)
        readable_date2 = current_datetime.isoformat()
        return self.render_template("blog.html",params={"site_mynumber": my_number,
                                                        "site_date2": readable_date2})

MY_HISTORY=[]

class LottoHandler(BaseHandler):
    def get(self):
        global MY_HISTORY
        current_datetime = datetime.datetime.now()
        # current_datetime += datetime.timedelta(hours=1)
        readable_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        my_lotto = random.sample(range(0,45),6)
        # append date and my_lotto to MY_HISTORY
        MY_HISTORY.append( (readable_date,my_lotto) )
        return self.render_template("lotto.html", params={"mylotto": my_lotto,
                                                          "site_date": readable_date,
                                                          "site_history": MY_HISTORY})


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/blog', BlogHandler),
    webapp2.Route('/lotto', LottoHandler),
], debug=True)
