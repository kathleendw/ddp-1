import tkinter as tk
import tkinter.messagebox as tkmsg

class MainWindow(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.configure(bg='#dcdcdc')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.lbl_file = tk.Label(self, text='Save barcode to PS file [eg: EAN13.eps]', bg='#dcdcdc').grid(row=0, column=1)
        self.ent_file = tk.Entry(self)
        self.ent_file.grid(row=1, column=1)
        self.lbl_code = tk.Label(self, text='Enter code (first 12 decimal digits):', bg='#dcdcdc').grid(row=2, column=1)
        self.ent_code = tk.Entry(self)
        self.ent_code.grid(row=3, column=1)
        self.ent_code.bind('<Return>', self.error)
        self.canvas = tk.Canvas(self, width=250, height=300)
        self.canvas.grid(row=5, column=1, padx=20, pady=20)
        self.canvas.create_text(125, 35, text='EAN-13 Barcode:', font='Helvetica 20 bold')

    def error(self, file):
        file = self.ent_file.get()
        code = self.ent_code.get()

        if len(code) == 12 and file[-4:] == '.eps':
            return self.barcode()
        elif file[-4:] != '.eps':
            tkmsg.showerror('Wrong Input!', 'Please enter correct type of file.')
        elif len(code) != 12:
            tkmsg.showerror('Wrong Input!', 'Please enter correct input code.')

    def barcode(self):
        code = self.ent_code.get()
        even_chars = []
        odd_chars = []
        for i in range(len(code)):
            if i % 2 == 0:
                odd_chars.append(code[i])
            else:
                even_chars.append(code[i])

        sum_even_chars = 0
        sum_odd_chars = 0
        for i in even_chars:
            sum_even_chars += int(i)
        for j in odd_chars:
            sum_odd_chars += int(j)

        check_sum = sum_even_chars * 3 + sum_odd_chars
        check_digit = 0
        if (check_sum % 10) != 0:
            check_digit += 10 - (check_sum % 10)
        else:
            check_digit += check_sum % 10
        check_digit_str = str(check_digit)
        code_ean_13 = code + check_digit_str

        structure = {'0': 'LLLLLLRRRRRR',
                    '1': 'LLGLGGRRRRRR',
                    '2': 'LLGGLGRRRRRR',
                    '3': 'LLGGGLRRRRRR',
                    '4': 'LGLLGGRRRRRR',
                    '5': 'LGGLLGRRRRRR',
                    '6': 'LGGGLLRRRRRR',
                    '7': 'LGLGLGRRRRRR',
                    '8': 'LGLGGLRRRRRR',
                    '9': 'LGGLGLRRRRRR'}

        L_code = {'0L': '0001101',
                '1L': '0011001',
                '2L': '0010011',
                '3L': '0111101',
                '4L': '0100011',
                '5L': '0110001',
                '6L': '0101111',
                '7L': '0111011',
                '8L': '0110111',
                '9L': '0001011'}

        G_code = {'0G': '0100111',
                '1G': '0110011',
                '2G': '0011011',
                '3G': '0100001',
                '4G': '0011101',
                '5G': '0111001',
                '6G': '0000101',
                '7G': '0010001',
                '8G': '0001001',
                '9G': '0010111'}

        R_code = {'0R': '1110010',
                '1R': '1100110',
                '2R': '1101100',
                '3R': '1000010',
                '4R': '1011100',
                '5R': '1001110',
                '6R': '1010000',
                '7R': '1000100',
                '8R': '1001000',
                '9R': '1110100'}

        structure_code = list(structure[code_ean_13[0]])
        twelve_digits_list = list(code_ean_13[1:])
        twelve_digits_code = [j[i] for i in range (len(twelve_digits_list)) for j in [twelve_digits_list, structure_code]]
        code_str = ''.join(twelve_digits_code)
        code_list = [code_str[i:i + 2] for i in range(0, len(code_str), 2)]

        twelve_digits_bit = ''
        for i in code_list:
            if i[1] == "L":
                twelve_digits_bit += L_code[i]
            elif i[1] == "G":
                twelve_digits_bit += G_code[i]
            elif i[1] == "R":
                twelve_digits_bit += R_code[i]

        S_bit = '101'
        M_bit = '01010'
        E_bit = '101'
        for i in range(len(S_bit)):
            if S_bit[i] == "0":
                continue
            self.canvas.create_line(35+i*2, 75, 35+i*2, 205, width=2, fill="blue")
        for i in range(len(twelve_digits_bit[:43])):
            if twelve_digits_bit[:43][i] == "0":
                continue
            self.canvas.create_line(41+i*2, 75, 41+i*2, 200, width=2, fill="green")
        for i in range(len(M_bit)):
            if M_bit[i] == "0":
                continue
            self.canvas.create_line(127+i*2, 75, 127+i*2, 205, width=2, fill="blue")
        for i in range(len(twelve_digits_bit[43:])):
            if twelve_digits_bit[43:][i] == "0":
                continue
            self.canvas.create_line(137+i*2, 75, 137+i*2, 200, width=2, fill="green")
        for i in range(len(E_bit)):
            if E_bit[i] == "0":
                continue
            self.canvas.create_line(219+i*2, 75, 219+i*2, 205, width=2, fill="blue")
        
        self.canvas.create_text(25, 220, text=code_ean_13[0], font="Helvetica 16 bold")
        for i, c in enumerate(code_ean_13[1:7]):
            self.canvas.create_text(50+i*13, 220, text=c, font="Helvetica 16 bold")
        for i, c in enumerate(code_ean_13[7:]):
            self.canvas.create_text(145+i*13, 220, text=c, font="Helvetica 16 bold")

        self.canvas.create_text(125, 265, text=f"Check digit: {check_digit}", font="Helvetica 18 bold", fill="orange")

        file = self.ent_file.get()
        self.canvas.postscript(file=file)
    
if __name__ == '__main__':
    main_window = MainWindow()
    main_window.master.title('EAN-13')
    main_window.master.mainloop()