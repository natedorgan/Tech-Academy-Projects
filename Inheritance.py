
class User:
    name = ''
    email = ''
    password = ''
    account_number = 0

# the child class Subscriber inherits the attributes from User and
# their mailing address and also how long they've been subscribed
# though I was unable to sort out how to do that in Python so this is a theoretical
class Subscriber(User):
    address = ''
    subscriber_since = ''

# Guest is also a child of User and so inherits the same attributes
# They also can be on or off the email list and it saves their age in case
# there is age-restricted content I guess
class Guest(User):
    email_list = True
    age = ''
    
    
    
