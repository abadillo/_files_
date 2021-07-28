# Setup guide

This is kinda of a guide for setting up two conky scripts. One is a system montitor and the other one is a calendar for assignments

1. Install this fonts:
    * https://www.dafont.com/vermin-vibes-1989.font
    * https://managore.itch.io/m6x11

2. Put the content of this folder on ~/.config/conky/

3. Make a login script with the following:

    #!/bin/sh

    conky -d -q -c ~/.config/conky/conky1.conf &

    conky -d -q -c ~/.config/conky/conky2.conf &

4. For setting up automation of the reloadconky. sh for changing the calendar in conky2.conf:

    1. Make the file reloadconky. sh executable with chmod -x
    2. Add this line to your aliases:

        alias uplan='cd && killall conky && cd .config/conky/conky2-script && kwrite Plan.txt && wait && sh reloadconky.sh && cd && sh .config/old-autostart-scripts/conky.sh'

    Tip: Use the file editor of your choice, in my case that is kwrite; and put it in the alias
    Tip 2: Only change the files Plan.txt and conkyheader.txt; the conky2 file is created by the reloadconky. sh script
#
## Notation on the Plan.txt file:


|Syb| Meaning        | Color       |
|---|----------------|-------------|
| # | Title          | Light Blue  |
| ! | Important      | Red         |
| * | Done           | Light Blue  |
|   | Incoming       | Blue        |
