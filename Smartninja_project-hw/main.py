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
        return self.render_template("index.html")

class BlogHandler(BaseHandler):
    def get(self):
        current_datetime2 = datetime.datetime.now()
        readable_date2 = current_datetime2.strftime("%Y-%m-%d %H:%M")
        return self.render_template("blog.html", params={"site_date2": readable_date2})

class ContactHandler(BaseHandler):
    def get(self):
        current_datetime4 = datetime.datetime.now()
        readable_date4 = current_datetime4.strftime("%Y-%m-%d %H:%M")
        return self.render_template("contact.html",params={"site_date4": readable_date4})

MY_HISTORY=[]

class LottoHandler(BaseHandler):
    def get(self):
        global MY_HISTORY
        current_datetime = datetime.datetime.now()
        readable_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        my_lotto = random.sample(range(0,45),6)
        # append date and my_lotto to MY_HISTORY
        MY_HISTORY.append( (readable_date,my_lotto) )
        return self.render_template("lotto.html", params={"mylotto": my_lotto,
                                                          "site_history": MY_HISTORY})

class CGHandler(BaseHandler):
    def get(self):
            return self.render_template("capitalsgame.html")

    def post(self):
            has_guessed = True
            guess = self.request.get("guess")
            # secretnumber = random.sample((0,5),1)
            #  "site_date": readable_date,

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
        return self.render_template("sng.html", params={"is_guessed": is_guessed,
                                                        "has_guessed": has_guessed})

class RBlHandler(BaseHandler):
    def get(self):
        messages = model.Message.query().fetch()
        return self.render_template("realblog.html", params={"messages": messages})
    def post(self):
        uname = self.request.get("username")
        uname = str(uname or "Anonymous")
        message_t = self.request.get("message_text")
        message = model.Message(message_text=message_t, name=uname)
        message.put()
        return self.redirect_to("realblog")

class CalcHandler(BaseHandler):
    def get(self):
        return self.render_template("calculator.html")

    def post(self):
        has_guessed = True
        x = self.request.get("x")
        ops = self.request.get("operation_symbol")
        y = self.request.get("y")

        a = float(x or 0)
        b = float(y or 0)

        if ops == "+" or ops == "-" or ops == "*" or ops == "/":
            is_ok = True
            if ops == "+":
                solution = a + b
            elif ops == "-":
                solution = a - b
            elif ops == "/":
                solution = a / b
            elif ops == "*":
                solution = a * b
        else:
            is_ok = False

        return self.render_template("calculator.html", params={"opsy": is_ok,
                                                               "sols": solution})

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/blog', BlogHandler),
    webapp2.Route('/contact', ContactHandler),
    webapp2.Route('/lotto', LottoHandler),
    webapp2.Route('/capital', CGHandler),
    webapp2.Route('/sng',SNGHandler),
    webapp2.Route('/realblog', RBlHandler, name="realblog"),
    webapp2.Route('/calculator', CalcHandler),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='0.0.0.0', port='8090')

if __name__ == '__main__':
    main()