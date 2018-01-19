#!/usr/bin/env python
import os
import jinja2
import webapp2
import random
import datetime
import model

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

MY_BLOG=[]
class BlogHandler(BaseHandler):
    def get(self):
        my_number = random.randint(0, 9)
        current_datetime2 = datetime.datetime.now()
        readable_date2 = current_datetime2.isoformat()
        return self.render_template("blog.html",params={"site_mynumber": my_number,
                                                        "site_date2": readable_date2})
    def post(self):
        message = self.request.get("message")
        global MY_BLOG
        current_datetime = datetime.datetime.now()
        readable_date3 = current_datetime.strftime("%Y-%m-%d %H:%M")
        MY_BLOG.append( (readable_date3, message) )
        return self.render_template("blog.html", params={"page_history": MY_BLOG})

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

class SNGHandler(BaseHandler):
    def get(self):
        return self.render_template("sng.html")

    def post(self):
        has_guessed = True
        guess = self.request.get("guess")
        # secretnumber = random.sample((0,5),1)
        secretnumber = 4
        number=int(guess or 0)
        # wenn guess keinen Wert hat oder leer ist
        is_guessed = secretnumber == number
        #is_guessed wird ein Bool
        #check auf Html oder im Backend moeglich
        #if secretnumber == guess:
        #    answer="Congratulations you have found the secret number {}" .format(secretnumber)
        #else:
        #    answer="sorry please try again"
        #return self.render_template("sng.html", params={"answers": answer})

        #return self.request("answer")

        return self.render_template("sng.html", params={"is_guessed": is_guessed,
                                                        "has_guessed": has_guessed})

class SLHandler(BaseHandler):
    def get(self):
        return self.render_template("shoppinglist.html")

class CGHandler(BaseHandler):
    def get(self):
        return self.render_template("capitalsgame.html")

class RBlHandler(BaseHandler):
    def get(self):
        messages = model.Message.query().fetch()
        return self.render_template("realblog.html", params={"messages": messages})
    def post(self):
        uname = self.request.get("username")
        message_t = self.request.get("message_text")
        message = model.Message(message_text=message_t, name=uname)
        message.put()
        return self.redirect_to("realblog")

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/blog', BlogHandler),
    webapp2.Route('/lotto', LottoHandler),
    webapp2.Route('/sng', SNGHandler),
    webapp2.Route('/shoppinglist', SLHandler),
    webapp2.Route('/capitals',CGHandler),
    webapp2.Route('/realblog',RBlHandler, name="realblog"),

], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='0.0.0.0', port='8080')

if __name__ == '__main__':
    main()