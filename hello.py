#!/usr/bin/env python

import os
from pprint import pprint
import json
import urlparse
import sys

from templates import *

username = 'user'
password = 'password'

#Headers
'''
print "Content-Type: text/html"
print "Set-Cookie: loggedin=True"
print #New line
'''

#Body
#print json.dumps((dict(os.environ)))
'''
#pprint(dict(os.environ))
if os.environ.get("QUERY_STRING"):
	print "Queries:\n<br />"
	queries = os.environ.get("QUERY_STRING").split('&')
	print '\n<br />'.join(queries)
	
	print '\n<br />'
	print '\n<br />'
	#params = urlparse.parse_qs(os.environ['QUERY_STRING'])
	#print params


if os.environ.get("HTTP_USER_AGENT"):
	agent = os.environ.get("HTTP_USER_AGENT")
	if 'Firefox' in agent:
		print "You're using Firefox!"
	
	elif 'Chrome' in agent:
		print "You're using Chrome!"
	
	elif 'Curl' in agent:
		print "You're using Curl!"
	
	else:
		print "I don't know what you are using."
		
	print "\n<br />"	
'''


#print login_page()

content_length = os.environ['CONTENT_LENGTH']
cookie = os.environ['HTTP_COOKIE']

logged_in = False



if 'logged-in=True' in cookie:
	logged_in = True
	print
	print "Logged in"

elif content_length:
	bytes_to_read = int(content_length)
	content = sys.stdin.read(bytes_to_read)
	params = urlparse.parse_qs(content)
	
	if (params['username'][0] == username
		and params['password'][0] == password):
			print "Set-Cookie: logged-in=True"
			
			print
			logged_in = True
			#print "Hi,", username
	else:
		
		print "<pre>"
		print "Invalid User/Pass:",content
		print "</pre>"

if not logged_in:
	print r"""
   	 <h1> Welcome! </h1>

   	 <form method="POST" action="hello.py">
   	     <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
   	     <label> <span>Password:</span> <input type="password" name="password"></label>

   	     <button type="submit"> Login! </button>
  	  </form>
  	  """
else:
	print "This is a secret message for ", username


