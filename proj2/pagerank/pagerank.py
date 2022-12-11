import os
from random import choice, choices
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    
    PD = {}

    if len(corpus[page]) > 0:
        # set P for linked pages 
        P = damping_factor/len(corpus[page])
        for site in corpus[page]:
            PD[site] = P

        # set P for any page
        P = (1 - damping_factor)/len(corpus)
        for site in corpus:
            PD[site] = P
    else:
        P = 1/len(corpus)
        for site in corpus[page]:
            PD[site] = P

    return PD


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    count = {}
    for page in corpus:
        count[page] = 0
    
    sample = choice(list(count.keys()))

    for _ in range(n):
        D = transition_model(corpus, sample, damping_factor)
        population = []
        weight = []
        for key, value in D.items():
            population.append(key)
            weight.append(value)
        sample = choices(population=population, weights=weight)[0]
        count[sample] += 1
    
    for page in count:
        count[page] /= n

    return count

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    
    count = {}
    N = len(corpus)
    for page in corpus:
        count[page] = 1/ N
        if len(corpus[page]) == 0:
            all_page = set()
            for pages in corpus:
                all_page.add(pages)
            corpus[page] = all_page

    delta = 1

    while delta > 0.001:
        for key in count.keys():
            s = 0
            for key2 in corpus:
                if key in corpus[key2]:
                    s += count[key2]/len(corpus[key2])
            R = (1 - damping_factor)/N + damping_factor * s
            delta = abs(R- count[key])
            count[key] = R





if __name__ == "__main__":
    main()
