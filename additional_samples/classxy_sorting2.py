import datetime

class Message(object):
    def __init__(self, text, author, date):
        self.text = text
        self.author = author
        self.date = date

    def __str__(self):
        return "{} {} {}".format(self.text, self.author, self.date)

messages = [
    Message("super eintrag", "jochina", datetime.datetime(2018,1,1,18,0,0)),
    Message("kochrezepte fuer alle", "berndi", datetime.datetime(2018,2,1,18,0,0)),
    Message("feiner sportbuecher", "alfred", datetime.datetime(2018,1,19,18,0,0)),
]

if __name__ == '__main__':
    print [str(m) for m in messages]
    print [str(m) for m in sorted(messages,key=lambda x: x.date)][::-1]
    print [str(m) for m in sorted(messages, key=lambda x: x.author)]