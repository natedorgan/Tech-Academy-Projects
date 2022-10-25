import datetime
import pytz

utc_now = pytz.utc.localize(datetime.datetime.utcnow())
pst_now = utc_now.astimezone(pytz.timezone("America/Los_Angeles"))
est_now = utc_now.astimezone(pytz.timezone("America/New_York"))
bst_now = utc_now.astimezone(pytz.timezone("Europe/London"))

pst_now == utc_now == est_now == bst_now


por=pst_now.strftime("%H")
new=est_now.strftime("%H")
lon=bst_now.strftime("%H")

port=int(por)
newy=int(new)
lond=int(lon)

if port <= 17 and port >= 9:
    print("Portland: Open")
else:
    print("Portland: Closed")

if newy <= 17 and port >= 9:
    print("New York: Open")
else:
    print("New York: Closed")

if lond <= 17 and port >= 9:
    print("London: Open")
else:
    print("London: Closed")


