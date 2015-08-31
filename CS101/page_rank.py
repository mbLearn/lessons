def compute_ranks(graph):
        d = 0.8 # damping factor
        numloops = 10

        ranks = {} # make an empty dict to store ranks
        npages = len(graph) # This gives a value for N
        for page in graph:
            ranks[page] = 1.0 / npages
            '''
            This goes through each page in the graph
            using that to create key:value pair in the
            ranks dictionary where each key is a page
            and the value is 1/N. This gives each page
            the same rank.
            '''  
        for i in range(0, numloops):
            # each time through the loop an
            # empty dictionary is created
            newranks = {} 
            for page in graph:
                '''
                The following code is the first part
                of the PageRank algorithm, the part that
                is (1-d) * 1/N. The probability of typing
                in the url in the address bar. 
                '''
                newrank = (1 - d) / npages

                '''
                The quiz asks us to implement the second
                part of the algorithm, the part that
                calculates the probability of clicking a link
                to our target webpage from another webpage. Which is:
                sum(PageRank_p/Outlinks_p) where is "p" is a page that links
                to our target page.
                The first time through the loop the value for
                PageRank is 1/N from the first for loop then each time
                after we use the values for PageRank that are
                assigned with the code "ranks=newranks".
                '''

                for page in graph:
                    newrank = (1-d) / npages
                    for node in graph: ##  the key is - how to get the "inlinks" for a page... 
                        if page in graph[node]:
                            newrank = newrank + d *(ranks[node] / len(graph[nodes]))
                newranks[page] = newrank

                '''
                This takes the newrank for the page 
                that was just calculated with the
                algorithm and assigns it to the newranks
                dictionary created at the top of the loop
                '''

        ranks = newranks
         '''
        After going through every page in the graph
        we have a fully filled newranks dictionary
        and we take that and assign all the values to the
        ranks dictionary we created above. This gives
        us prior PageRank that we use for the next time
        through the loop.
        '''
    return ranks

index, graph = crawl_web("http://cs101.udactiy.com/urank/index.html")
ranks = compute_ranks(graph)
