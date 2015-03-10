# Bitcoin Job Checker

### Feature List:

 * Given a list of Keywords scans Coinality open postings for matches

I'm no good at writing sample / filler text, so go write something yourself.

### Technology:

 * Python
 
### Code:

```python
import tb.py

#Set the Keywords to look for, Could be Programming, Python, Management
tb.keywords = ['test', 'Test', 'QA', 'qa', 'Qa']

#Get all the Coinality Postings
data = tb.getCoinalityPostings()

#Parse out the keywords
tb.parsePostings(data)
```
```python
>> python tb.py
>> Querying Coinality Job Data...
>> Searching for Jobs with: test
>> No Job postings with test found
>> Searching for Jobs with: Test
>> No Job postings with Test found
>> Searching for Jobs with: QA
>> No Job postings with QA found
>> Searching for Jobs with: qa
>> No Job postings with qa found
>> Searching for Jobs with: Qa
>> No Job postings with Qa found
>> No Jobs Found
```
This is [Coinality API](https://coinality.com/api-documentation/) to derive job postings.


### Future Improvements:

 * [marked](https://github.com/chjj) for Markdown parsing
 * [CodeMirror](http://codemirror.net/) for the awesome syntax-highlighted editor
 * [highlight.js](http://softwaremaniacs.org/soft/highlight/en/) for syntax highlighting in output code blocks
 * [js-deflate](https://github.com/dankogai/js-deflate) for gzipping of data to make it fit in URLs
