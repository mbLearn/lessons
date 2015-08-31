## =========================== Problem 1 ===============================
# Define a procedure, add_to_index, that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already in the index, add the url to the list of
# urls associated with that keyword.
# If the keyword is not in the index, add an entry to the index: [keyword,[url]]

index = []
def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])
    return index

add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index
print '\n'
## ======================= Alternate ========================================
index = []

def add_to_index1(index,keyword,url):
    for key, value in index:
        if key == keyword:
            value.append(url)
            return
    index.append([keyword,[url]])
    return index

## ========================== Problem 2 =======================================
# Define a procedure, lookup, that takes two inputs:
# - an index
# - keyword

# The procedure should return a list of the urls associated with the keyword.
# If the keyword is not in the index, the procedure should return an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]

def lookup(index,keyword):
    for key, values in index:
        if key == keyword:
            return values

print lookup(index,'udacity')
print "\n"
## ============================ Problem 3 =======================================
# Define a procedure, add_page_to_index, that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include all of the word occurences found in the
# page content by adding the url to the word's associated url list.
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
