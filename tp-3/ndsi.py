# -*- coding: utf-8 -*-
import string
import matplotlib.pyplot as plt

def load_stop_words(filename):
    """
    Parameters
    ----------
    filename : string
        nama file yang menyimpan daftar stopwords.
        Di soal, nama default-nya adalah stopwords.txt

    Returns
    -------
    stop_words : set
        himpunan stopwords (unik)

    Fungsi menerima nama file yang berisi daftar stopwords,
    kemudian memuat semua stopwords ke dalam struktur data
    set. Perhatikan bahwa semua stopwords yang ada di dalam
    file sudah dalam bentuk huruf kecil semua.
    """
    stopwords = open(filename,"r")
    stop_words = set()
    for line in stopwords:
        for word in line.split():
            stop_words.add(word)
    return stop_words

def count_words(filepath, stop_words):
    """
    Parameters
    ----------
    filepath : string
        path atau lokasi dari file yang berisi sekumpulan
        kalimat-kalimat yang memiliki polaritas sentiment,
        yaitu rt-polarity.neg atau rt-polarity.pos

    stop_words : set
        himpunan stopwords

    Returns
    -------
    word_freq : dictionary
        sebuah dictionary, dimana key adalah kata (string)
        dan value adalah frekuensi (int) dari kemunculan
        kata tersebut.

    Fungsi ini akan scan semua baris (semua kalimat) yang
    ada di file dan kemudian mengakumulasikan frekuensi dari
    setiap kata yang muncul pada file tersebut.

    Contoh
    ------
    Jika isi dari file adalah:

        I just watched a good movie
        wow! a good movie
        a good one

    Fungsi akan mengembalikan dictionary:
        {'i':1, 'just':1, 'watched':1, 'a':3, 'good':3,
         'movie':2, 'wow!':1, 'one':1}

    Notes
    -----
    1. stopwords diabaikan
    2. karakter tanda baca seperti , . / dan sebagainya juga
       diabaikan (gunakan string.punctuation di library string)
    """
    polarity = open(filepath, "r")
    resultwords = []
    for line in polarity:
        for punctuation in line:
            if punctuation in string.punctuation:
                line = line.replace(punctuation,"")
        for word in line.split():
            if word not in stop_words:
                resultwords.append(word)
    word_freq = {}
    for element in resultwords:
        word_freq[element] = resultwords.count(element)
    return word_freq

def compute_ndsi(word_freq_pos, word_freq_neg):
    """
    Parameters
    ----------
    word_freq_pos : dictionary
        sebuah dictionary, dimana key adalah kata (string)
        dan value adalah frekuensi (int) dari kemunculan
        kata tersebut. Frekuensi dari kata dihitung dari
        file rt-polarity.pos
    word_freq_neg : dictionary
        sebuah dictionary, dimana key adalah kata (string)
        dan value adalah frekuensi (int) dari kemunculan
        kata tersebut. Frekuensi dari kata dihitung dari
        file rt-polarity.neg

    Returns
    -------
    word_ndsi : dictionary
        sebuah dictionary, dimana key merupakan kata (string)
        dan value adalah NDSI score (float)

    Notes
    -----
    NDSI dari sebuah kata dihitung dengan:

              word_freq_pos[word] - word_freq_neg[word]
              -----------------------------------------
              word_freq_pos[word] + word_freq_neg[word]

    Jika kata tidak ditemukan pada salah satu dictionary,
    frekuensi kata tersebut adalah 0.

    Contoh
    ------
    Jika word_freq_neg = {'bad':10, 'worst':5, 'good':1} dan
         word_freq_pos = {'good':20, 'nice':5, 'bad':2},

    maka word_ndsi = {'bad':-0.67, 'worst':-1, 'good':0.90, 'nice':1}

    """
    word_ndsi = {}
    for word in word_freq_neg:
        if word in word_freq_pos:
            ndsi = ((word_freq_pos[word] - word_freq_neg[word])/(word_freq_pos[word] + word_freq_neg[word]))
            word_ndsi[word] = ndsi
        elif word not in word_freq_pos:
            ndsi = ((0 - word_freq_neg[word])/(0 + word_freq_neg[word]))
            word_ndsi[word] = ndsi
    for word in word_freq_pos:
        if word not in word_freq_neg:
            ndsi = ((word_freq_pos[word] - 0)/(word_freq_pos[word] + 0))
            word_ndsi[word] = ndsi
    return word_ndsi

def show_ndsi_histogram(word_ndsi):
    """
    Parameters
    ----------
    word_ndsi : dictionary
        sebuah dictionary, dimana key adalah kata (string)
        dan value adalah NDSI score (float) dari kata tersebut.

    Returns
    -------
    None.

    Plot histogram dari semua NDSI scores yang dihasilkan

    """
    ndsi_scores = [score for _, score in word_ndsi.items()]
    plt.hist(ndsi_scores, 100, facecolor = 'g', alpha = 0.75)
    plt.yscale("log")
    plt.xlabel('NDSI score')
    plt.ylabel('Frekuensi')
    plt.savefig("ndsi-hist.pdf")

if __name__ == "__main__":

    # memuat stop words ke sebuah set
    stop_words = load_stop_words("stopwords.txt")

    # menghitung word frequency untuk file berisi kalimat-kalimat sentiment positif
    word_freq_pos = count_words("./sent-polarity-data/rt-polarity.pos", stop_words)

    # menghitung word frequency untuk file berisi kalimat-kalimat sentiment negatif
    word_freq_neg = count_words("./sent-polarity-data/rt-polarity.neg", stop_words)

    # hitung NDSI untuk semua kata-kata pada kedua jenis dictionary berisi
    # word frequency
    word_freq_ndsi = compute_ndsi(word_freq_pos, word_freq_neg)

    # tampilkan histogram dari nilai-nilai NDSI yang dihasilkan
    show_ndsi_histogram(word_freq_ndsi)

    # mengurutkan pasangan kata dan skor ndsi yang ada
    # di word_freq_ndsi berdasarkan nilai ndsi saja, dari terkecil
    # ke yang terbesar

    word_freq_ndsi_list = sorted(word_freq_ndsi.items(), key=lambda sort: sort[1])
    print(word_freq_ndsi_list)
    sorted_word_freq_ndsi = dict(word_freq_ndsi_list)

    # menyimpan daftar kata-kata dan nilai ndsi yang sudah diurutkan tadi ke
    # file ndsi.txt

    ndsi_filename = "ndsi.txt"
    ndsi_txt = open(ndsi_filename, "w")
    for word in sorted_word_freq_ndsi:
        print(f"{word} {sorted_word_freq_ndsi[word]}", file=ndsi_txt)
    ndsi_txt.close()