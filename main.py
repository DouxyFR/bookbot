def main():
    path_to_file = "books/frankenstein.txt"

def openlivre(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return (file_contents)

def countwords(txtlivre):
    words = txtlivre.split()
    return (len(words))

def countchr(txtlivre):
    txtlivre = txtlivre.lower()
    txtinletter = list(txtlivre)    
    dicochar = {"a":0}
    lettreautorise = "abcdefghijklmnopqrstuvwxyz"
    listlettreautorise = list(lettreautorise)
    for i in range (len(txtinletter)):
        char = (txtinletter[i:i+1]) 
        char = char[0]
        if char in dicochar:
            dicochar[char] += 1
        else:
            dicochar[char] = 1
        
    return rapport(dicochar)

def rapport(dicochar):
    #print(dicochar)
    stringlettreautorise = "abcdefghijklmnopqrstuvwxyz"
    listlettreautorise = list(stringlettreautorise)
    #print(listlettreautorise)
    #print(dicochar)
    sorted_dico = sorted(dicochar, key=lambda x: dicochar[x], reverse=True)
    #print(sorted_dico)
    rapport = "--- Begin report of books/frankenstein.txt ---\n"
    rapport += f"{countwords (openlivre("books/frankenstein.txt"))} words found in the document\n\n"
    """
    for d in dicochar:
        #rapport += f"{dicochar[i]}The 'e' character was found 46043 times\n"
        test = dicochar[d]
        if d in listlettreautorise:
            rapport += f"The '{d}' character was found {test} times\n"
    """
    for d in sorted_dico:
        #rapport += f"{dicochar[i]}The 'e' character was found 46043 times\n"
        test = dicochar[d]
        if d in listlettreautorise:
            rapport += f"The '{d}' character was found {test} times\n"
    rapport += "--- End report ---\n"
    return rapport

def book_statistique(url):
    print (countchr (openlivre("books/frankenstein.txt")))

main()
book_statistique("books/frankenstein.txt")