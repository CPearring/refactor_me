#!/usr/bin/env python
# command line program to download a user's avatar from github. usage: `python GET_AVATAR.PY <github_username>`. 

import sys
import json
import argparse
import requests
import shutil

# parse command line arguments
PARSER = argparse.ArgumentParser()
PARSER.add_argument(  'username')
ARGS = PARSER.parse_args()
# call the github api and get user info
RequestUrl = 'https://api.github.com/users/' + ARGS.username
RESULT = requests.get( RequestUrl )
if RESULT.ok :
    user_info = json.loads(RESULT.content)
    avatarURL = user_info['avatar_url']
else:
    sys.stderr.write( "Error fetching user information for {0}; exiting now, sorry...\n".format(ARGS.username) )
    sys.exit()
# download and save image file
I = requests.get(avatarURL , stream=True)
if I.ok:
    with open(ARGS.username + '.png' , 'wb') as OuTfIle:
        shutil.copyfileobj( I.raw,  OuTfIle )
