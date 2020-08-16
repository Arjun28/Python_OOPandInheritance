import datetime as dt

class Member:

    free_days = 100

    def __init__(self, uname, fname):
        self.username = uname
        self.fullname = fname
        self.date_joined = dt.date.today()
        self.is_active = True
        self.free_expires = dt.date.today() + dt.timedelta(Member.free_days)
        self.secret_code = ''

    def show_datejoined(self):
        return f"{self.fullname} joined on {self.date_joined:%m/%d/%y}"

    def activate(self, yesno):
        self.is_active = yesno

    def showexpiry(self):
        return f"{self.fullname} expires on {self.free_expires}"  

    def get_status(self):
        return f"{self.fullname} is a regular Member."

    @classmethod
    def setfreedays(cls,days):
        cls.free_days = days

    @staticmethod
    def currenttime():
        return dt.datetime.now()


class Admin(Member):
    def __init__(self, uname, fname, secret_code):
        super().__init__(uname, fname)
        self.secret_code = secret_code
    
    def get_status(self):
        return f"{self.fullname} is an Admin."

      
    
class User(Member):
    def get_status(self):
        return f"{self.fullname} is an User."



"""
new_guy = Member('Arjun','Mallikarjun')
print(new_guy.show_datejoined())
print(new_guy.is_active)
new_guy.activate(True)
print(new_guy.is_active)


Member.setfreedays(10)
print(Member.currenttime())
aru = Member('MJ','MLKRJN-J')
print(aru.show_datejoined())
print(Member.show_datejoined(aru))
print(aru.free_expires) 
"""


Arjun = Admin('Aru','Mallikarjun','DEVO')
print(Arjun.fullname, Arjun.free_expires, Arjun.secret_code, Arjun.date_joined)
print(Arjun.showexpiry())
print(Arjun.get_status())

Ron = User('Ronny','RandyRon')
print(Ron.fullname, Ron.free_expires, Ron.secret_code)
print(Ron.showexpiry())
print(Ron.get_status())