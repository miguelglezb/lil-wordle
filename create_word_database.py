import collections
from pathlib import Path

forbidden_chr_list = [ chr(i) for i in range(33,94) ]
forbidden_chr_list.extend([chr(95), chr(8212), chr(8216), chr(8217), chr(8220)])  


book_path = Path("./book-database")

book_collection = [ book for book in book_path.iterdir() ]            
counter = collections.Counter()

def filter_by_length(wordlist):
    filtered_list = [ word for word in wordlist if len(word) == 5 ] 
    return filtered_list

def remove_forbidden_chr_lists(wordlist):
    for fc in forbidden_chr_list:
        for word in enumerate(wordlist):
            wordlist[word[0]] = word[1].replace(fc,'')
    return wordlist


for book in book_collection:

    data = open(book)
    word_list = []

    for line in data.readlines():
        word_list.extend(line.split())


    #Filter for non-5-character length strings
    five_length_string = filter_by_length(word_list)

    #Filter for forbidden characters (capital letters included)  
    five_all_word_list = remove_forbidden_chr_lists(five_length_string)

    #Filter again for non-5-character length strings
    filtered_wordlist =  filter_by_length(five_all_word_list)
    foo = collections.Counter(filtered_wordlist)
    counter.update(filtered_wordlist)

word_database = [ word[0] for word in counter.most_common(200) ] 
