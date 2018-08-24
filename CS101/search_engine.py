from urllib import urlopen

def get_page(url):
    try:
        return str(urlopen(url).read())
    except:
        return ""


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1 : end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(pages):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos: ]
        else:
            break
    return links

def crawl_wed(seed):
    tocrawl = [seed]
    crawled = []
    index = {}
    graph = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_tp_index(index, page, content)
            outlinks =  get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph

def add_page_to_index(index, url, content): 
    words = content.split() 
    for word in words: 
        add_to_index(index, word, url) 

def add_to_index(index, keyword, url): 
    if keyword in index: 
        index[keyword].append(url)
    else:
        # not found, add new keyword to index 
        index[keyword] = [url]

def lookup(index, keyword): 
    if keyword in index: 
         return index[keyword] 
    else: return None


def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10

    ranks = {} # make an empty dict to store ranks
    npages = len(graph) # This gives a value for N

    for page in graph:
        ranks[page] = 1.0 / npages
    for i in range(0, numloops):
        # each time through the loop an empty dict is created
        newranks = {}
        for page in graph:
            newrank = (1-d) / npages
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d*(ranks[node] / (len(graph[node])))
            newranks[page] = newrank
        ranks = newranks
    return ranks
