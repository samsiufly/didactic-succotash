# Generate all required urls at once

# open a file
fname = input("Enter Week data filename:")
if len(fname) < 1:
    fname = "week_one.txt"
try:
    fhand = open(fname)
except:
    print('week data is invalid. Please try again.')
    quit()

# list for temp urls
web_url = list()
ls_countries = list()
ls_date = list()

# countries dictionary
countries = ['global','se','us','gb','ae','ar','at','au','be','bg','bo',\
             'br','ca','ch','cl','co','cr','cz','de','dk','do','ec','ee',\
             'eg','es','fi','fr','gr','gt','hk','hn','hu','id','ie','il',\
             'in','is','it','jp','kr','lt','lu','lv','ma','mx','my','ni',\
             'nl','no','nz','pa','pe','ph','pl','pt','py','ro','ru','sa',\
             'sg','sk','sv','th','tr','tw','ua','uy','un','za']

market = input ('Please input country code or input 0 for all countries: ')

h = 1
while h > 0 :
    if market == 0:
        for country in countries:
            url_a = "https://spotifycharts.com/regional/" + market + "/"
            ls_countries.append(url_a)
    if market in countries:
        print ('Correct.', market)
        url_a = "https://spotifycharts.com/regional/" + market + "/"
        ls_countries.append(url_a)
        h = h - 1
    else:
        print ('<<<<<country code invalid! Please start the app again>>>>>')
        quit()

for line in fhand:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    date_s = ''.join(line_list) #string
    ls_date.append(date_s)
print ('All Dates Valid')


n = input ("No. of weeks to be retrieved: (281max) ")
n = int(n)

ls_url = list()

for link in ls_countries:
    for i in ls_date:
        if n > 0:
            url = link + "weekly" + "/" + i
            ls_url.append(url)
            n = n - 1
        else: continue


print ("=====Writing to TXT=====")

filename = input ("Export Url Filename: ")
textfile = open('%s.txt' % filename,'w')
for i in ls_url:
    textfile.write(i + "\n")
textfile.close()

print ("Done.")
print ('Use data_crawl.py to sprawl data')
