Export-privatepics
==================

Export images from privatepics app iTunes backup.


Why
==================
I lost my images saved in the app privatepics (com.dreamingphone.privatepics) after installing an iOS beta.

Using iPhone backup extractor (http://supercrazyawesome.com/) i exported the PPStorage.private.
Turns out that it's just a SQLite Db, so I wrote this small script to export the images.

Leaving it here if someone else needs it :)

Usage
==================
1. Export the app data using iPhone backup extractor (http://supercrazyawesome.com/)
![](https://raw.githubusercontent.com/endast/Export-privatepics/master/docs/extractor.png)
2. run the script on the PPStorage.private file: $python export_privatepics.py PPStorage.private (exports to current dir)
3. Enjoy your files :)
