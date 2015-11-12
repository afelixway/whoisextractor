from bs4 import BeautifulSoup 
from urllib2 import urlopen 
import gdata.spreadsheet.service 
import datetime 
rowdict = {} 
rowdict['date'] = str(datetime.date.today()) 
spread_sheet_id = '1zE8Qe8wmC271hG2uW4XE68btUks79xX0OG-O4KDl_Mo' 
worksheet_id = 'od6' 
client = gdata.spreadsheet.service.SpreadsheetsService() 
client.debug = True 
client.email = "email@domain.com" 
client.password = 'password' 
client.source = 'whoisinfo' 
client.ProgrammaticLogin() 
with open('websitesforwhois.txt') as f: 
    for line in f: 
    soup = BeautifulSoup(urlopen("http://www.checkdomain.com/cgi-bin/checkdomain.pl?domain=" + str(line)).read()) 
    for pre in soup.find_all("pre"): 
        whois_info = str(pre.string) 
        #print whois_info 
    rowdict['website'] = str(line) 
    rowdict['whoisinformation'] = whois_info
    client.InsertRow(rowdict,spread_sheet_id, worksheet_id)

