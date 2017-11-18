from icalendar import *
import urllib.request
import datetime

def start_time(event):
    return event['DTSTART'].dt


def lecturize(event):
    return event['SUMMARY'].encode('utf-8')

def location(event):
    return event['LOCATION'].encode('utf-8')

def get_latest_session(sessions):
    right_now = datetime.datetime.now()
    smallest_diff = sessions[0][1] - right_now
    print('smallest diff %d', smallest_diff)
    s = sessions[0]
    for session in sessions:
        current_diff = session[1] - right_now
        if right_now < session[1] and smallest_diff > current_diff: # and smallest_diff < right_now - right_now:
            s = session
            smallest_diff = session[1] - right_now
    return s

def get_stuff(url):
    file = urllib.request.urlopen(url)
    g = file.read()
    gcal = Calendar.from_ical(g)

    sessions = [(lecturize(e), start_time(e), location(e)) for e in gcal.walk('vevent')]

    session = get_latest_session(sessions)
    return str(session[0]) + '\n' + str(session[1]) + '\n' + str(session[2])
    #return str(sessions[0][0]) + '\n' + str(sessions[0][1]) + '\n' + str(sessions[0][2])

#print get_stuff('https://se.timeedit.net/web/uu/db1/schema/s.ics?i=yQ99053X5Z69Q096546X6Z690544400259053Q9561Y59Y504YX5953556Z0XW90nQY255')
