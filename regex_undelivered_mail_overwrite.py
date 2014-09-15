# email extract from text file from thunderbird.
# github 
import os
import re
import csv


# vars for filenames
filename = 'Bounced Email.txt'
newfilename = 'bounced_cleaned.csv'
#re.sub('^.*\b(gsend.state.ut.us)\b.*$', "--", f.rstrip())

# read file
if os.path.exists(filename):
	data = open(filename,'r')
	bulkemails = data.read()
else:
	print "File not found."
	raise SystemExit

# regex = email extract
r = re.compile(r'[\w\.-]+@[\w\.-]+')
t = re.compile ('(?<=from the\s).*(?=\sParent)')
re.sub('^.*\b(gsend.state.ut.us)\b.*$', "--", filename)
results = r.findall(bulkemails)
results1 = t.findall(bulkemails)
clean_up = results + results1
emails = ""
for x in clean_up:
	emails +="'"+ str(x)+"'"+","+"\n"

# function to write file
def writefile():
	f = open(newfilename, 'w')
	f.write(emails)
	f.close()

#function to handle overwrite
def overwrite_ok():
	response = raw_input("Are you sure you want to overwrite "+str(newfilename)+"? Yes or No\n")
	if response == "Yes":
		writefile()
	elif response == "No":
		print "Aborted."
	else:
		print "Please enter Yes or No."
		overwrite_ok()
#write/overwrite
if os.path.exists(newfilename):
	overwrite_ok()		
else: 
	writefile()

# csv clean
# find duplicates
rows = csv.reader(open("bounced_cleaned.csv", "rb"))
newrows = []
for row in rows:
    if row not in newrows:
        newrows.append(row)
writer = csv.writer(open("bounced_cleaned.csv", "wb"),delimiter=',')
writer.writerows(newrows)
del writer
print "Complete"





