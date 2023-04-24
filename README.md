# Ticapsoriginal Sitemaps Url Status Overview
large xml sitemaps overview plotting result from http response codes

* show status 200 Sucess requests
* show status 404 Error pages requests
* show status 302 Redirects requests
* show total sitemaps urls


# make python environment:
* Install pip first:
<pre><code>sudo apt-get install python3-pip
</code></pre>
* Then install virtualenv using pip3
<pre><code>sudo pip3 install virtualenv 
</code></pre>
* Now create a virtual environment
<pre><code>virtualenv venv
</code></pre>
* Active your virtual environment:
<pre><code>source venv/bin/activate
</code></pre>
* Enter on environment:
<pre><code>cd venv
</code></pre>

## Install tqdm to see progress bar: 
<pre><code>pip install tqdm
</code></pre>

## Install requests to get responses and make requests: 
<pre><code>pip install requests
</code></pre>

## Install matplotlib to plotting categorical chart: 
<pre><code>pip install matplotlib
</code></pre>

## Install advertools to read large url data: 
<pre><code>pip install advertools
</code></pre>

## Clone ticapsoriginaltweepy repository:
<pre><code> git clone https://github.com/Tinoco/Ticapsoriginal_sitemaps_url_status.git
</code></pre>

* Change the sitemapoverview.py file with your sitemap url 

## Make sitemap links status overview :
<pre><code>python sitemap_overview.py
</code></pre>

![](https://ticapsoriginal.com/static/sitemapoverview.png)

## quality:
* [`100% pycodestyle coverage`](https://pypi.org/project/pycodestyle/)

* [`0% code plagiarism detected`](https://github.com/blingenf/copydetect)
