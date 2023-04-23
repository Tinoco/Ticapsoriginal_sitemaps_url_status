# IMPORT MATPLOTLIB FOR PLOTTING
import matplotlib.pyplot as plt

# TQDM PROGRESS BAR
from tqdm import tqdm

# IDENTIFY LARGE XML FILE
import advertools as adv

# REQUEST TO GET RESPONSES
import requests

# INDEXING YOUR LARGE SITEMAPS
sitemap = adv.sitemap_to_df("https://ticapsoriginal.com/static/sitemap1.xml")

# TYPE CASTING URL TO LIST
urls = sitemap["loc"].to_list()

# START LINKS HTTP RESPONSE COUNTER
sucess = 0
error = 0
redirect = 0


# LINK DIVISION FUNCTION
def linkdivision(status):
    global sucess
    global error
    global redirect
    finder = str(status)
    # RESPONSE CODE FROM URL
    print(finder[1:-1])
    if finder.find(str('200')):
        sucess += 1
    elif finder.find(str('404')):
        error += 1
    elif finder.find(str('302')):
        error += 1


# WALK ON ALL URLS
for item in tqdm(urls):
    status = str(requests.get(item))
    linkdivision(status)

# PLOT CATEGORICAL BAR INERFACE
linkmetrics = ['ERROR ', 'REDIRECT ', 'SUCESS ', 'TOTAL ']
httpscodes = [error, redirect, sucess, len(urls)]

plt.figure(figsize=(10, 5))

plt.plot(len(urls))
plt.bar(linkmetrics, httpscodes)

plt.suptitle('SITE MAP OVERVIEW ')
plt.show()
