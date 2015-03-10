# Bitcoin Job Checker

### Feature List:

 * Given a list of Keywords scans Coinality open postings for matches


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

 * More sites to get Job Postings from
 * Result Parsing into Objects, instead of a Big String
 * E-mail Alerts
 * Running at all time
