import requests, webbrowser,os
from .progress import *

def get_html():
    targetsite = input("Enter target site: ") # Uncomment this to accept user input target site
    if(targetsite == ""):
        targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
    session = create_session()
    response = session.get(targetsite)
    cookies_jar = response.cookies
    rc = get_cookies(targetsite,cookies_jar)
    write_to_file(rc)
    path = os.path.abspath("./index.html")
    animated_marker()
    webbrowser.open(path)

def get_cookies(tg, cj):
    response = requests.get(tg, cookies=cj)
    response_content = response.content.decode(encoding="UTF-8")
    return response_content

def create_session():
    session = requests.session()
    return session

def write_to_file(rc):
    files = open("./index.html", "w")
    for line in rc:
        files.writelines(line)
    files.close()


def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

