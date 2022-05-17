import time

# open a file
fname = input("Enter file:")
if len(fname) < 1:
    fname = "weeks.txt"
fhand = open(fname)

# list for temp urls
web_url = list()

# countries dictionary
countries = ['global','se','us','gb','ae','ar','at','au','be','bg','bo',\
             'br','ca','ch','cl','co','cr','cz','de','dk','do','ec','ee',\
             'eg','es','fi','fr','gr','gt','hk','hn','hu','id','ie','il',\
             'in','is','it','jp','kr','lt','lu','lv','ma','mx','my','ni',\
             'nl','no','nz','pa','pe','ph','pl','pt','py','ro','ru','sa',\
             'sg','sk','sv','th','tr','tw','ua','uy','un','za']

#Select the country
country = input ("Enter the country: ")
x  = countries.__contains__(country)
if x == True:
    print ("Proceeding......")
    time.sleep(3)
else:
    country = 'global'
    print ("Invalid. Default country: global")
    print ("Proceeding......")
    time.sleep(3)

print ('Your selected country:', country)

#n = input("How many weeks do you want to retrieve? (max 246): ")
n = input ("No. of weeks: (281max) ")
n = int(n)

for line in fhand:
    if n > 0:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        date_s = ''.join(line_list) #string
        url = "https://spotifycharts.com/regional/"+ country + "/" + "weekly" + "/" + date_s
        print(url)
        web_url.append(url)
        n = n - 1

print ("=====Writing to TXT=====")
time.sleep(3)

filename = input ("Export Url Filename: ")
textfile = open('%s.txt' % filename,'w')
for url in web_url:
    textfile.write(url + "\n")
textfile.close()

print ("Done.")
