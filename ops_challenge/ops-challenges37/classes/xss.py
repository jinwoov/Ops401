
#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description:  To check if the website is vulnerable to cross site scripting.  
# Date:        11/25/2020
# Modified by: Jin Kim


# Import libraries

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

### This is getting the content of the html. The url is passed in as an argument.
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

### It is looking through the HTML scaffold and checkinf where the form starts and storing its action, method and input fields in the form.
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

### form details is the the detail of the forms that is created through above function. This then grabs inputs from the object and check if the input type is text or search then the value will be what it is passed in. If the method is post method it iwll call request post method and if it is get method it will call get method.
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value
    print(data, "this is for data")
    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

### Using the given url it will first get all of the form then save it in the object variable call forms. Then it will run the javascript script to check if is XSS vulnerable.if the content returns what the js script user have passed in then it will change is_vulnerable boolean to true otherwise it will stay as false.
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<script>alert('Mochi')</script>"
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        print(f"{content} this is content")
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            print(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main

###C Prompting user with a input of what URL they want to scan then run the function stack through using `scan_xss` function.
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))

### TODO: When you have finished annotating this script with your own comments, copy it to Web Security Dojo
### TODO: Test this script against one XSS-positive target and one XSS-negative target
### TODO: Paste the outputs here as comments in this script, clearling indicating which is positive detection and negative detection

# Enter a URL to test for XSS:https://xss-game.appspot.com/level1/frame
# [+] Detected 1 forms on https://xss-game.appspot.com/level1/frame.
# {'query': "<script>alert('Mochi')</script>"} this is for data

# <!doctype html>
# <html>
#   <head>
#     <!-- Internal game scripts/styles, mostly boring stuff -->
#     <script src="/static/game-frame.js"></script>
#     <link rel="stylesheet" href="/static/game-frame-styles.css" />
#   </head>

#   <body id="level1">
#     <img src="/static/logos/level1.png">
#       <div>
# Sorry, no results were found for <b><script>alert('Mochi')</script></b>. <a href='?'>Try again</a>.
#     </div>
#   </body>
# </html>
#  this is content
# [+] XSS Detected on https://xss-game.appspot.com/level1/frame
# [*] Form details:
# {'action': '', 'method': 'get', 'inputs': [{'type': 'text', 'name': 'query', 'value': "<script>alert('Mochi')</script>"}, {'type': 'submit', 'name': None}]}True