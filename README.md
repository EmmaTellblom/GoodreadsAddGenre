
## Hi!

I created this script because I wanted to create some statistics and noticed that genres was not included in the regular export from Goodreads. So I wanted to create a script that went through the export and gathered the information from Goodreads without requiring login credentials or anything else. Simply add your export file to this folder (make sure your file is named `goodreads_library_export.csv` and when the script is finished you will have a new file called `goodreads_export_with_genres.csv`
Depending on how many books you have in your export file, this might take a few minutes to run through.

Please note that I'm a junior python programmer and did this for myself for another project I'm working on. Constructive criticism is appreciated.

To use this script you need to have the following modules installed:

    pandas
    re
    requests
    BeautifulSoup

### Information
The genres added are the 7 "top" genres from Goodreads. Please not that these may not be correct since they are from users bookshelves. If you have a complaints about this, go to Goodreads. 

I noticed that the export from Goodreads sometimes throws in extra spaces in the author column, so I cleaned that. And since I'm European I like regular date formats, so that is corrected as well. For some weird reason the file from Goodreads throws in "= in the ISBN/ISBN13 column, cleaned that too. If you find more weird crap in the export file, let me know and I can fix that too. 

### Usage
Put your Goodreads export in this folder. Run the main file `python main.py` 

Use, change, do whatever you want.