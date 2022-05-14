import csv

# open a file
fname = input("Enter file:")
if len(fname) < 1:
    fname = "weekday.txt"
fhand = open(fname)

#n = 10   #initialize the counter

week_lst = list()

for line in fhand:
    line = line.rstrip()    #split the line to words
    try:
        line = line.split()[1]
        line = line.split('"')[1]
        week_lst.append(line)
        #date = re.findall('^data-value="', line)
        #n = n - 1
    except:
        continue
        #email = words [1]       #extract the index 1 : email address
        #count = count + 1

print ("=====Writing to TXT=====")
# print (dataset)

# Use file to refer to the file object
textfile = open("weeks.txt", "w")
for data in week_lst:
    textfile.write(data + "\n")
textfile.close()

print ("Done")
