#By: Justin Chase
#Find Test Development/QA job parsing the postings on Coinality
import json
import urllib2

keywords = ['test', 'Test', 'QA', 'qa', 'Qa']
coinalityurl = 'https://coinality.com/api/jobs'

def getCoinalityPostings():
    print 'Querying Coinality Job Data...'
    data = json.load(urllib2.urlopen(coinalityurl))
    data = str(data)
    return data

def parsePostings(data):
    found = 0
    for word in keywords:
        print "Searching for Jobs with: " + word
        if word in data:
            print "!!!Posting with " + word + " found!!!"
            found += 1
        else:
            print "No Job postings with " + word + ' found'
    if found == 0:
        print 'No Jobs Found'
    else:
        print '!!!Job posting found!!!'

def main():
    data = getCoinalityPostings()
    parsePostings(data)

if __name__ == "__main__":
    main()

