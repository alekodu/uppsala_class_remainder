from icalendar import *
import urllib.request

def start_time(event):
    return event['DTSTART'].dt


def lecturize(event):
    return event['SUMMARY'].encode('utf-8')

def location(event):
    return event['LOCATION'].encode('utf-8')

def get_stuff(url):
    file = urllib.request.urlopen(url)
    g = file.read()
    gcal = Calendar.from_ical(g)

    sessions = [(lecturize(e), start_time(e), location(e)) for e in gcal.walk('vevent')]

    return str(sessions[0][0]) + '\n' + str(sessions[0][1]) + '\n' + str(sessions[0][2])

#print get_stuff('https://se.timeedit.net/web/uu/db1/schema/s.ics?i=yQ99053X5Z69Q096546X6Z690544400259053Q9561Y59Y504YX5953556Z0XW90nQY255')
