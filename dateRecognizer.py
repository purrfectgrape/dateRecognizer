# Author: Giang Ha Le
import re
import os
import sys 

YEAR = r"\d{4}"
MONTH = r"january|february|march|april|may|june|july|august|" \
"september|october|november|december|jan|feb|mar|apr|" \
"jun|jul|aug|sep|oct|nov|dec|jan\.|feb\.|mar\.|apr\.|may\." \
"jun\.|jul\.|aug\.|sep\.|oct\.|nov\.|dec\."
DAYNUM = r"\d{1,2}"
TIMENUM = r"\d{1,2}"
MONTHNUM = r"\d{1,2}"
DAYSUF = r"st|nd|rd|th"
DAYOFTHEWEEK = r"monday|tuesday|wednesday|thursday|friday|saturday|sunday"
AMPM = r"am|pm|AM|PM|a\.m\.|p\.m\."
SEP = r"-|\/|."
PUNC = r",|, | "
PREP = r"of"
FUZZYRANGE = r"morning|afternoon|evening|night|midnight"
HOLS = r"new year(?:\'s)? day|martin luther king,?(?: jr.)? day|george washington(?:\'s)? birthday|memorial day|independence day|labor day|columbus day|veterans day|thanksgiving day|christmas day"

# This regex captures patterns like
# January 15th, 2019
# Jan 15, 2018
# Feb 3rd, 1999
# jan 2nd 1828 where only the date is obligatory.
re1 = re.compile('(%s)?(%s)?(%s)(%s)?(%s)(%s)?(%s)?(%s)?' % (DAYOFTHEWEEK, PUNC, MONTH, PUNC, DAYNUM, DAYSUF, PUNC, YEAR), re.I)

# This regex captures patterns like
# 01/31/1990
re2 = re.compile('(%s)(%s)(%s)(%s)(%s)' % (MONTHNUM, SEP, DAYNUM, SEP, YEAR), re.I)

# This regex captures patterns like
# Monday morning, Monday
re3 = re.compile('(%s)(%s)?(%s)' % (DAYOFTHEWEEK, PUNC, FUZZYRANGE), re.I)

# This regex captures patterns like
# Monday 2PM
re4 = re.compile('(%s)( ?)(%s)?( ?)(%s)?' % (DAYOFTHEWEEK, TIMENUM, AMPM), re.I)

# Holidays
re5 = re.compile('(%s)' % HOLS, re.I)

# This regex captures patterns like
# Tuesday, Oct 2018
# where only the month and year are obligatory.
re6 = re.compile('(%s)?(%s)?(%s)(%s)?(%s)' % (DAYOFTHEWEEK, PUNC, MONTH, PUNC, YEAR), re.I)

# This regex captures patterns like "4th of July"
re7 = re.compile('(%s)(%s)?( )(%s)( )(%s)' % (DAYNUM, DAYSUF, PREP, MONTH), re.I)

# This regex captures patterns like "Monday the 24th"
re8 = re.compile('(%s)( the? )(%s)(%s)?' % (DAYOFTHEWEEK, DAYNUM, DAYSUF), re.I)

all_regexes = [re1, re2, re3, re4, re5, re6, re7, re8]

# Recognizer of dates.
def searchDates(regex, text):
    matches = re.findall(regex, text)
    return matches

if len(sys.argv) < 2:
    print("Please supply two arguments to the script! Usage python3 dateRecognizer.py infile outfile")
    sys.exit()

inputfile = sys.argv[1]
outputfile = sys.argv[2]
    
with open(inputfile, 'r') as infile:
    text = infile.read()

results = list()
for regex in all_regexes:
    results.append(searchDates(regex, text))

with open(outputfile, 'w') as outfile:
    for result in results:
        for item in result:
            outfile.write("".join(item) + "\n")
            
