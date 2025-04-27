file_input = input("Silahkan masukkan nama file: ")
print()
print(file_input,":")
print()

import string
import random

#mengecek apakah file ada atau tidak dan handle eror apabila file ternyata tidak ada
try:
    input = open(file_input)
except FileNotFoundError:
    print("File input tidak ada:(")
else: 
    #memeriksa apakah file kosong atau tidak
    with open(file_input,"r") as read_char:
        first_char = read_char.read(1)
    #apabila tidak ada karakter yang ditemukan, maka file kosong
    if not first_char:
        print("File input ada tapi kosong:(")
    else:
        #menghilangkan punctuations pada stopwords.txt dan memasukkan setiap stop words pada list stopwords
        with open("stopwords.txt","r") as stop_words:
            stopwords = []
            for baris in stop_words:
                for kata in baris.split():
                    for punctuations in kata:
                        if punctuations in string.punctuation:
                            kata = kata.replace(punctuations,"")
                    stopwords.append(kata)
                    
            with open(file_input,"r") as input:
                #semua huruf dijadikan lowercase serta semua punctuations dan stopwords dihilangkan pada file input
                #lalu setiap kata dimasukkan pada list resultwords
                resultwords = []
                for line in input:
                    line = line.lower()
                    for punctuation in line:
                        if punctuation in string.punctuation:
                            line = line.replace(punctuation,"")
                    for word in line.split():
                        if word not in stopwords:
                            resultwords.append(word)
                            
                #menghitung jumlah kemunculan setiap kata pada list resultwords dan memasukkannya pada list count
                count = []
                for elemen in set(resultwords):
                    count.append([elemen,resultwords.count(elemen)])
                #list count diatur berdasarkan jumlah kemunculan terlebih dahulu, lalu berdasarkan alfabet
                count.sort(key=lambda sort: (sort[1],sort[0]),reverse=True)
                count = count[0:56] #mengambil 56 sublist pertama dalam list count
                
                #memprint list count dengan format 14x4
                i = 0
                for list in count:
                    format = f"{list[1]}:{list[0]}"
                    if i%4 == 3:
                        print(f"{format:<20}")
                    else:
                        print(f"{format:<20}",end=" ")
                    i+=1
                
                #mengambil jumlah kemunculan kata tertinggi
                high = []
                for list in count[0]:
                    high.append(list)
                high = high[1]
                
                #mengambil jumlah kemunculan kata terendah
                low = []
                for list in count[-1]:
                    low.append(list)
                low = low[1]
                
                #membuat list baru untuk mengatur berdasarkan alfabet
                pair = []
                for list in count:
                    pair.append(list)
                pair.sort(key=lambda sort: sort[0])

                def make_HTML_word(word, cnt, high, low):
                    '''
                    Make a word with a font size and a random color.
                    Font size is scaled between html_big and html_little (to be user set).
                    high and low represent the high and low counts in the document.
                    cnt is the count of the word. 
                    Required -- word (string) to be formatted
                            -- cnt (int) count of occurrences of word
                            -- high (int) highest word count in the document
                            -- low (int) lowest word count in the document
                    Return -- a string formatted for HTML that is scaled with respect to cnt
                    '''
                    html_big = 96
                    html_little = 14
                    if high != low:
                        ratio = (cnt-low)/float(high-low)
                    else:
                        ratio = 0
                    font_size = html_big*ratio + (1-ratio)*html_little
                    font_size = int(font_size)
                    rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    word_str = '<span style=\"color: rgb{}; font-size:{:s}px;\">{:s}</span>'
                    return word_str.format(rgb, str(font_size), word)

                def make_HTML_box(body):
                    '''
                    Take one long string of words and put them in an HTML box.
                    If desired, width, background color & border can be changed in the function
                    This function stuffs the "body" string into the the HTML formatting string.

                    Required -- body (string), a string of words
                    Return -- a string that specifies an HTML box containing the body
                    '''
                    box_str = """<div style=\"
        width: 560px;
        background-color: rgb(250,250,250);
        border: 1px grey solid;
        text-align: center\" >{:s}</div>
                    """
                    return box_str.format(body)

                def print_HTML_file(body, title):
                    '''
                    Create a standard html page (file) with titles, header etc.
                    and add the body (an html box) to that page. File created is title+'.html'
                    Required -- body (string), a string that specifies an HTML box
                    Return -- nothing
                    '''
                    fd = open(title+'.html', 'w')
                    the_str = """
        <html> <head>
        <title>"""+title+"""</title>
        </head>

        <body>
        <h1>"""+'A Word Cloud of '+title+'</h1>'+'\n'+body+'\n'+"""<hr>
        </body> </html>
                    """
                    fd.write(the_str)
                    fd.close()

                def main():
                    pairs = pair
                    high_count = high
                    low_count = low
                    body = ''
                    for word, cnt in pairs:
                        body = body + " " + make_HTML_word(word, cnt, high_count, low_count) + "\n"
                    box = make_HTML_box(body)  #creates HTML in a box
                    #writes HTML to file input
                    print_HTML_file(box, file_input)

                if __name__ == '__main__':
                    main()

                    

