from googletrans import Translator
import wikipedia

translator = Translator()

__sysName = "Alice"
name = "Alice"
usrLang = "eng"

def OnSystemLang(s):
    try:
        return translator.translate(s, dest = "eng").text
    except:
        return s
def WriteOnUserLang(s):
    try:
        print(translator.translate(s, dest = usrLang).text)
    except:
        print(s)

def OnUserLang(s):
    try:
        return translator.translate(s, dest = usrLang).text
    except:
        return s

def ClearFromSymbols(s):
    s = ''.join(s)
    s = s.split('!')
    s = ''.join(s)
    s = s.split('?')
    s = ''.join(s)
    s = s.split('.')
    s = ''.join(s)
    s = s.split(',')
    s = ''.join(s)
    return s

data = {"Hi": "Hello)"}
def Answer(s):
    try:
        WriteOnUserLang(data[s])
    except:
        data[s] = input("<")

def FindAnswer(s):
    try:
        return wikipedia.summary(s)
    except:
        return "No answer."

def SetLanguage(l):
    try:
        wikipedia.set_lang(l)
        global usrLang
        usrLang = l
    except:
        print("Error. ", l, "To change language just type \"Change language \" and language(like \"eng\"). For more information write \"help\"")

def FindAnswer(s, c):
    try:
        return wikipedia.summary(s, sentences = c)
    except:
        return OnUserLang("No answer.")

def FindPage(s):
    try:
        return wikipedia.page(s)
    except:
        return OnUserLang("No answer.")

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

try:
    assistant = wikipedia.summary("Assistant (software)", sentences = 1)
    print(OnUserLang("Hello! This assistant name is " + name + ". " + assistant))
except Exception as e:
    print("To work good " + __sysName + " needs internet. Please check your connection.", e)

while True:
    s = input(">")
    if s.upper() == "QUIT" or s.upper() == "EXIT" or s.upper() == OnUserLang("QUIT") or s.upper() == OnUserLang("EXIT"):
        WriteOnUserLang("Bye!")
        #quit() raise translation

    if "WHAT IS" in s.upper() or OnUserLang("what is").upper() in s.upper():
        a = 0
        s = s.split(' ')
        while a < len(s):
            if s[a].upper() == "WHAT" or s[a].upper() == "IS" or s[a].upper() == OnUserLang("WHAT").upper() or s[a].upper() == OnUserLang("IS").upper():
                s[a] = ''
                b = 0
                while b < a:
                    s[b] = ''
                    b += 1
            a += 1
        
        s = ' '.join(s)

        s = ClearFromSymbols(s)

        WriteDefinition(s)
    elif "HELP" in s.upper() or OnUserLang("HELP").upper() in s.upper() or "INFO" in s.upper() or "HELP" in OnSystemLang(s).upper() or "INFO" in OnSystemLang(s).upper():
        if usrLang != "eng":
            WriteOnUserLang("You can write \"What is \" and word you want to get definition of. Also you can change language by typing \"Change language \" or \"Set lang\" and language(like eng)")
        print("You can write \"What is \" and word you want to get definition of. Also you can change language by typing \"Change language \" or \"Set lang\" and language(like eng)")
    elif "CHANGE LANGUAGE" in s.upper() or "SET LANG" in s.upper() or OnUserLang("CHANGE LANGUAGE").upper() in s.upper() or OnUserLang("SET LANG").upper() in s.upper():
        a = 0
        s = s.split(' ')
        while a < len(s):
            #if s[a].upper() == "CHANGE" or s[a].upper() == "LANGUAGE" or s[a].upper() == "SET" or s[a].upper() == "LANG" or s[a].upper() == OnUserLang("CHANGE").upper() or s[a].upper() == OnUserLang("LANGUAGE").upper() or s[a].upper() == OnUserLang("SET").upper() or s[a].upper() == OnUserLang("LANG").upper():
            if  "CHANGE" in s[a].upper() or "LANGUAGE" in s[a].upper() or "SET" in s[a].upper() or "LANG" in s[a].upper() or OnUserLang("CHANGE").upper() in s[a].upper() or OnUserLang("LANGUAGE").upper() in s[a].upper() or OnUserLang("SET").upper() in s[a].upper() or OnUserLang("LANG").upper() in s[a].upper():
                s[a] = ''
                b = 0
                while b < a:
                    s[b] = ''
                    b += 1
            a += 1
        
        s = ''.join(s)
        s = s.split('!')
        s = ''.join(s)
        s = s.split('?')
        s = ''.join(s)
        s = s.split('.')
        s = ''.join(s)
        s = s.split(',')
        s = ''.join(s)
        s = s.split('`')
        s = ''.join(s)
        s = s.split('<')
        s = ''.join(s)
        s = s.split('>')

        s = ''.join(s)
        SetLanguage(s)
    else:
        Answer(s)
