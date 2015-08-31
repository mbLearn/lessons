# The web crawler we built at the end of Unit 3 has some serious
# flaws if we were going to use it in a real crawler. One
# problem is if we start with a good seed page, it might
# run for an extremely long time (even forever, since the
# number of URLS on the web is not actually finite). This
# question and the following one explore two different ways
# to limit the pages that it can crawl.

# Modify the crawl_web procedure to take a second parameter,
# max_pages, that limits the number of pages to crawl.
# Your procedure should terminate the crawl after
# max_pages different pages have been crawled, or when
# there are no more pages to crawl.

# The following definition of get_page provides an interface
# to the website found at http://www.udacity.com/cs101x/index.html

def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return ('<html><body> This is a test page for learning to crawl!'
                    '<p> It is a good idea to  '
                    '<a href="http://www.udacity.com/cs101x/crawling.html"> learn to '
                    'crawl</a> before you try to '
                    '<a href="http://www.udacity.com/cs101x/walking.html">walk</a>. '
                    '</p> </body> </html> ')
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return ('<html> <body> I have not learned to crawl yet, but I '
            'am quite good at '
            '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return ('<html> <body> I cant get enough '
            '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return ('<html> <body> The magic words are Squeamish Ossifrage! '
            '</body> </html>')
    except:
        return ""
    return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos: ]
        else:
            break
    return links

index2 = []

def add_to_index(index2,keyword,url):
    for entry in index2:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index2.append([keyword,[url]])
    
def add_page_to_index(index2,url,content):
    keyword = content.split()
    for word in keyword:
        add_to_index(index2,word,url)


def crawl_web(seed, max_pages):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled and len(crawled) < max_pages:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return crawled

print crawl_web("http://www.udacity.com/cs101x/index.html",1)
print crawl_web("http://www.udacity.com/cs101x/index.html",3)
print crawl_web("http://www.udacity.com/cs101x/index.html",500)

print '\n'

add_page_to_index(index2,'fake.text',"This is a test")
add_page_to_index(index2, 'http://dilbert.com',
                  """
                  Another strategy is to ignore the fact that you
                  are slowly killing yourself by not sleeping and
                  excercising enough. That frees up several hours
                  a day. The only downside is that you get fat and
                  die. --- Scott Adams on Time Management
                  """)
print index2                    
