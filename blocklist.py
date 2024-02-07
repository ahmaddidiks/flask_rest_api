'''
blocklist.py

This file is just contain the blocklist of the JWT tokens. It will be imported by  app and the logout resources so that token can be added to the blocklist when the user logs out.
'''

BLOCKLIST = set()