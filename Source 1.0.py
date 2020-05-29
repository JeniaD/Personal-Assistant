import wikipedia

def FindAnswer(s):
    try:
        return wikipedia.summary(s)
    except:
        return "No answer."


def FindAnswer(s, c):
    try:
        return wikipedia.summary(s, sentences = c)
    except:
        return No answer.

def FindPage(s):
    try:
        return wikipedia.page(s)
    except:
        return No answer.
        
def Search(s):
    return wikipedia.search(s)

def WriteDefinition(q):
    try:
        res = FindPage(q)
        print(FindAnswer(q, 3))
        print("\nUrl: ", res.url)
        print("\nDid you mean: ", res.links, "\b?\n\n")
    except:
        print("\nError!\n")

while True:
    s = input(">")
    WriteDefinition(s)
