#!/bin/bash

/usr/bin/python /home/durrr/LacrosseAI/downloadScheduleHTMLRPI.py
echo "Finished downloading schedule HTML."

/usr/bin/python /home/durrr/LacrosseAI/downloadStatsHTMLRPI.py
echo "Finished downloading stats HTML."

/usr/bin/python /home/durrr/LacrosseAI/downloadTeamsHTMLRPI.py
echo "Finished downloading teams HTML."

/usr/bin/python3 /home/durrr/LacrosseAI/scrapeSchedule.py
echo "Finished scraping schedule data."

/usr/bin/python3 /home/durrr/LacrosseAI/scrapeStats.py
echo "Finished scraping stats data."

/usr/bin/python3 /home/durrr/LacrosseAI/scrapeTeams.py
echo "Finished scraping teams data."

