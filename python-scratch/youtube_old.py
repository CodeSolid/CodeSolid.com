"""
Given the URL of a Playlist on YouTube as a command-line 
argument outputs a markdown-formatted list of videos links.
It's recommended to quote the playlist name to avoid 
issues with the shell parsing it incorrectly.

Dependencies:
	BeautifulSoup
	Requests
"""

import sys
from bs4 import BeautifulSoup
import requests


if len(sys.argv) != 2:
    print("Usage:  python {0} playlist_url".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]
response = requests.get(url)

if not response.ok:
    print("Error retrieving url:", url)
    sys.exit(1)

soup = BeautifulSoup(response.text, 'html.parser')
# titles  = soup.find_all(attrs={'id':'video-title'})
titles  = soup.find_all("a")
print(len(titles))
#for title in titles:
#    print(title)
print(response.text)