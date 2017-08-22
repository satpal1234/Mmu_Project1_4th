# import statements
from spy_detail import spy_name,spy_age,spy_rating,spy_salutation
from start_chat import start_chat
print "Let's get started"
question="Do you want to continue as"+spy_salutation+" "+spy_name+" "
existing=raw_input(question)
if existing=='y'or existing=='Y':
    start_chat()
    # Logic here

elif existing=='N'or existing=='n':
    raw_input("enter your name")
    spy_name = raw_input()
    if len(spy_name)>0:
        spy_age=0
        spy_rating=0.0
        spy_is_online=False
        spy_salutation=raw_input("what should we all you ?")



