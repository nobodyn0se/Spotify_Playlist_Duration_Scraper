# Spotify_Playlist_Duration_Scraper

This web scraper takes a Spotify Playlist URL as user input and returns: 1. Total duration of all songs in the playlist; 2. Average duration of songs; 3. Total number of songs in the playlist

Pre-requisites before running this script: 
The following packages must be installed - selenium, bs4, re, html5lib (parser). 

The script returns HTML source code of the playlist webpage (using selenium to retrieve dynamic JS elements), parse it with html5lib and create a list of duration of every song. 
The sum of these list elements is finally displayed in hh:mm:ss format along with average duration which is calculated using total number of list items (songs). 

After you enter the open.spotify playlist URL, add at least one space before pressing the Enter button to allow console input. 
Be patient, the script will return the results in a few seconds :) 
