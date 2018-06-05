# Module to resolve a DOI via cross reference and turn it into json data
# or format as a bibtex reference
#
# October 2016 Robert Shaw

import requests
import json
import bibtexEntry as be

def doiToJson(doi):
    """Returns metadata associated with given DOI string in JSON format
    
    :param doi: a string of the DOI
    :returns: -- JSON metadata for reference
    """
    url = 'http://data.crossref.org/' + doi
    headers = {'Accept': 'application/citeproc+json'}
    r = requests.get(url, headers=headers)
    meta = json.loads(r.content)
    return meta

def doiToBib(doi):
    """Turns metadata from given DOI string into a bibtex object

    :param doi: a string of the DOI
    :returns: -- bibtex object of metadata
    """
    meta = doiToJson(doi)
    data = meta.items()
    journal = getField("container-title", data)
    author = getAuthor(data)
    year, month =  getYearMonth( data)
    title = getField("title", data)
    volume = getField("volume", data)
    entry = be.BibEntry(author = author, year = year, journal = journal, title = title, volume = volume)
    entry.number = getField("is-referenced-by-count", data)
    entry.pages = getField("page", data)
    entry.month = month
    return entry
    
def getField(field, data):
    """Returns the value of the given field name from the given data

    :param field: the name of the field needed
    :param data: the JSON.items() object containing the field
    :returns: -- the value of the field if found, or "" otherwise
    """
    output = ""
    for key, value in data:
        if key == field:
            output = value
    return output

def getAuthor(data):
    """Returns the authors in the correct format for bibtex from the data.

    :param data: the JSON.items() object containing the author data
    :returns: -- a string of the authors in suitable format for bibtex entry
    """
    output = ""
    for key, value in data:
        if key == "author":
            authors = value
            # Parse each author in turn
            for aval in authors:
                firstname = aval['given']
                lastname = aval['family']
                output += "%s, %s and " % (lastname, firstname)  
            output = output.strip(" and ")
    return output

def getYearMonth(data):
    """Returns the year and month from given json data in format for bibtex entry

    :param data: the JSON.items() object containing the data
    :returns: a value pair (year, month)
    """
    year = ""
    month = ""
    verbose_date = getField("published-print", data)
    
    if verbose_date == "":
        verbose_date = getField("published-online", data)

    if verbose_date == "":
        verbose_date = getField("issued", data)

    if verbose_date != "":
        date_parts = verbose_date.get('date-parts')
        if (len(date_parts) > 0):
            if (len(date_parts[0]) > 1):
                year = "%i" % date_parts[0][0]
                month = "%i" % date_parts[0][1]
            else:
                year = "%i" % date_parts[0][0]
    return year, month
