print("Halo, selamat datang di Mathbot")

import random

def pilih_kuis():
    print("""Pilih kuis:
1. Kuis Lepas
2. Kuis 5
3. Ganti mode
4. Akhiri program""")
    print("")

while True:
    print("""Pilih mode:
1. Penjumlahan
2. Pengurangan
3. Campur
4. Akhiri Program""")
    print("")
    perintah = input("Masukkan perintah: ")
    print("")

    a = ""
    if perintah == "1" or perintah == "2" or perintah == "3" or perintah == "4":
        if perintah == "4":
            print("Terima kasih telah bermain kuis ini. Sampai jumpa lagi!")
            exit()
        elif perintah == "1":
            a += "penjumlahan"
        elif perintah == "2":
            a += "pengurangan"
        elif perintah == "3":
            a += "campur"
        print(f"Baik, pilih mode {a} ya, sekarang pilih jenis kuis apa?")
        pilih_kuis()
        y = input("Masukkan jenis kuis: ")
        print("")

        while perintah == "1" and y == "1":
            b = random.randint(0,10)
            c = random.randint(0,10)
            z = b + c
            print("Berapa",b,"+",c,end="")
            print("?")
            j = input("Jawab: ")
            if j.isdigit():
                if j == str(z):
                    print("Hore benar!")
                    print("")
                elif j != str(z):
                    print("Masih kurang tepat, ya. Jawabannya adalah",z)
                    print("")
            else:
                print("")
                pilih_kuis()
                y = input("Masukkan jenis kuis: ")
                print("")
            
        while perintah == "1" and y == "2":
            skor = 0
            for _ in range (1,6):
                b = random.randint(0,10)
                c = random.randint(0,10)
                z = b + c
                print("Berapa",b,"+",c,end="")
                print("?")
                j = input("Jawab: ")
                if j.isdigit():
                    if j == str(z):
                        skor += 20
                        print("Hore benar!")
                        print("")
                    elif j != str(z):
                        print("Masih kurang tepat, ya. Jawabannya adalah",z)
                        print("")
                else:
                    print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                    print("")
            print("Score:",skor)
            print("")
            pilih_kuis()
            y = input("Masukkan jenis kuis: ")
            print("")

        while perintah == "2" and y == "1":
            b = random.randint(0,10)
            c = random.randint(0,10)
            if b>c:
                v = b - c
                print("Berapa",b,"-",c,end="")
                print("?")
                k = input("Jawab: ")
                if k.isdigit():
                    if k == str(v):
                        print("Hore benar!")
                        print("")
                    elif k != str(v):
                        print("Masih kurang tepat, ya. Jawabannya adalah",v)
                        print("")
                else:
                    print("")
                    pilih_kuis()
                    y = input("Masukkan jenis kuis: ")
                    print("")
            elif b<c:
                v = c - b
                print("Berapa",c,"-",b,end="")
                print("?")
                k = input("Jawab: ")
                if k.isdigit():
                    if k == str(v):
                        print("Hore benar!")
                        print("")
                    elif k != str(v):
                        print("Masih kurang tepat, ya. Jawabannya adalah",v)
                        print("")
                else:
                    print("")
                    pilih_kuis()
                    y = input("Masukkan jenis kuis: ")
                    print("")

        while perintah == "2" and y == "2":
            skor = 0
            for _ in range (1,6):
                b = random.randint(0,10)
                c = random.randint(0,10)
                if b>c:
                    v = b - c
                    print("Berapa",b,"-",c,end="")
                    print("?")
                    k = input("Jawab: ")
                    if k.isdigit():
                        if k == str(v):
                            skor += 20
                            print("Hore benar!")
                            print("")
                        elif k != str(v):
                            print("Masih kurang tepat, ya. Jawabannya adalah",v)
                            print("")
                    else:
                        print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                        print("")
                elif b<c:
                    v = c - b
                    print("Berapa",c,"-",b,end="")
                    print("?")
                    k = input("Jawab: ")
                    if k.isdigit():
                        if k == str(v):
                            skor += 20
                            print("Hore benar!")
                            print("")
                        elif k != str(v):
                            print("Masih kurang tepat, ya. Jawabannya adalah",v)
                            print("")
                    else:
                        print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                        print("")
            print("Score:",skor)
            print("")
            pilih_kuis()
            y = input("Masukkan jenis kuis: ")
            print("")

        while perintah == "3" and y == "1":
            l = ["+","-"]
            m = random.choice(l)
            b = random.randint(0,10)
            c = random.randint(0,10)
            if m == "+":
                z = b + c
                print("Berapa",b,"+",c,end="")
                print("?")
                j = input("Jawab: ")
                if j.isdigit():
                    if j == str(z):
                        print("Hore benar!")
                        print("")
                    elif j != str(z):
                        print("Masih kurang tepat, ya. Jawabannya adalah",z)
                        print("")
                else:
                    print("")
                    pilih_kuis()
                    y = input("Masukkan jenis kuis: ")
                    print("")
            elif m == "-":
                if b>c:
                    v = b - c
                    print("Berapa",b,"-",c,end="")
                    print("?")
                    k = input("Jawab: ")
                    if k.isdigit():
                        if k == str(v):
                            print("Hore benar!")
                            print("")
                        elif k != str(v):
                            print("Masih kurang tepat, ya. Jawabannya adalah",v)
                            print("")
                    else:
                        print("")
                        pilih_kuis()
                        y = input("Masukkan jenis kuis: ")
                        print("")
                elif b<c:
                    v = c - b
                    print("Berapa",c,"-",b,end="")
                    print("?")
                    k = input("Jawab: ")
                    if k.isdigit():
                        if k == str(v):
                            print("Hore benar!")
                            print("")
                        elif k != str(v):
                            print("Masih kurang tepat, ya. Jawabannya adalah",v)
                            print("")
                    else:
                        print("")
                        pilih_kuis()
                        y = input("Masukkan jenis kuis: ")
                        print("")

        _ = 0
        while perintah == "3" and y == "2" and _<6:
            skor = 0
            l = ["+","-"]
            for _ in range (1,6):
                m = random.choice(l)
                b = random.randint(0,10)
                c = random.randint(0,10)
                if m == "+":
                    z = b + c
                    print("Berapa",b,"+",c,end="")
                    print("?")
                    j = input("Jawab: ")
                    if j.isdigit():
                        if j == str(z):
                            skor += 20
                            print("Hore benar!")
                            print("")
                        elif j != str(z):
                            print("Masih kurang tepat, ya. Jawabannya adalah",z)
                            print("")
                    else:
                        print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                        print("")
                elif m == "-":
                    if b>c:
                        v = b - c
                        print("Berapa",b,"-",c,end="")
                        print("?")
                        k = input("Jawab: ")
                        if k.isdigit():
                            if k == str(v):
                                skor += 20
                                print("Hore benar!")
                                print("")
                            elif k != str(v):
                                print("Masih kurang tepat, ya. Jawabannya adalah",v)
                                print("")
                        else:
                            print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                            print("")
                    elif b<c:
                        v = c - b
                        print("Berapa",c,"-",b,end="")
                        print("?")
                        k = input("Jawab: ")
                        if k.isdigit():
                            if k == str(v):
                                skor += 20
                                print("Hore benar!")
                                print("")
                            elif k != str(v):
                                print("Masih kurang tepat, ya. Jawabannya adalah",v)
                                print("")
                        else:
                            print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                            print("")
            print("Score:",skor)
            print("")
            pilih_kuis()
            y = input("Masukkan jenis kuis: ")
            print("")

        if y == "3":
            continue

        if y == "4":
            print("Terima kasih telah bermain kuis ini. Sampai jumpa lagi!")
            exit()

    else:
        print("Program tidak mengenali perintah yang dimasukkan. Silahkan memilih dari perintah yang tersedia.")
        print("")

#TP1 ini didiskusikan dengan Stelline Claudia - 2106700933

