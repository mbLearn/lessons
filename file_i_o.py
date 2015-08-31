import sys, re

def Cat(filename):
    f = open(filename)
    text = f.read()
    print '-----', filename
    return text
    

def match_words(filename):
    full_text = Cat(filename)
    #print full_text
    word = "the"
    match_word = re.findall(r'(the [A-Z A-z]+\.)', full_text)
    for i in match_word:
        print i


# Define a main() function that prints a little greeting.
def main():
    args = sys.argv[1:]
    for arg in args:
        match_words(arg)
        

# This is the standard boilerplate that calls the main() funciton
if __name__ == '__main__':
    main()
    
