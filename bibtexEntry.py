# Defines a class for containing and outputting a bibtex entry for an article
#
# October 2016 Robert Shaw
import sys
import importlib
import re

class BibEntry:
    """A bibtex entry object for an article"""
    type = "article"
    number = ""
    pages = ""
    month = ""
    note = ""
    key = ""
    
    def __init__(self, author="", title="", journal="", year="", volume=""):
        self.author = author
        self.title = title
        self.title = self.title.replace(',','')
        self.title = self.title.replace(':','')
        self.title = self.title.replace('-','')
        self.journal = journal
        self.journal = self.journal.replace(',','')
        self.journal = self.journal.replace(':','')
        self.journal = self.journal.replace('-','')
        self.year = year[0:4]
        self.reference = author.split( )[0] + year + title.split( )[0]
        self.reference = self.reference.replace(',','')
        self.reference = self.reference.replace(':','')
        self.reference = self.reference.replace('-','')
        self.volume = volume
    
    def ToString(self):
        importlib.reload(sys)
        # sys.setdefaultencoding("utf-8")
        output = "@Article{" + self.reference + ",\n"
        output += "author = {" + self.author + "},\n"
        output += "title = {" + self.title + "},\n"
        output += "journal = {" + self.journal + "},\n"
        output += "year = " + self.year + ",\n"
        
        if self.number != "":
            output += "number = " + str(self.number) + ",\n"
        
        if self.pages != "":
            output += "pages = {" + self.pages + "},\n"
        
        if self.month != "":
            output += "month = " + self.month + ",\n"
        
        if self.note != "":
            output += "note = {" + self.note + "},\n"
        
        output += "volume = " + self.volume + "\n}"
        ######################################
        output_csv = self.title + ","
        output_csv += self.journal + ","
        output_csv += self.year + ","
        
        if self.number != "":
            output_csv += str(self.number) + ","
        else :
             output_csv += ","
        
        # if self.month != "":
        #     output_csv += self.month + ","
        # else :
        #      output_csv += ","

        return output,output_csv
    
    def ToCSV(self):
        importlib.reload(sys)
        # sys.setdefaultencoding("utf-8")
        # output = "@Article{" + self.reference + ",\n"
        # output += "author = {" + self.author + "},\n"

    