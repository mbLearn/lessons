def factorial(n):
    result = 1
    while n >= 1:
        result = result * n
        n = n - 1
    return result


# ========================================================================
def get_next_target1(page):
    start_link = page.find('<a href=')
    url = None
    end_quote = 0
    while start_link > 0:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        break
    return url, end_quote


# =========================================================================
# if there is a link it gives the name of the link and the location but
# if there is no link tag in the input string, it returns None, 0.

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print url
            page = page[endpos: ]
        else:
            break

print print_all_links(get_page('http://xkcd.com/353'))
    

