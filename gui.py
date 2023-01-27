from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from huffman import HuffmanCoding

class HuffmanCodingGUI:
    def __init__(self, master):
        self.master = master
        master.title("Huffman Coding")
        master.geometry("300x200")
        master.resizable(False, False)
        master.configure(background="#E1B74F")
        self.compress_button = Button(master, text="Compress", command=self.compress)
        self.compress_button.place(x=100, y=40)
        

        self.decompress_button = Button(master, text="Decompress", command=self.decompress)
        self.decompress_button.place(x=100, y=80)
        
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.place(x=100, y=120)
        

    def compress(self):
        file_path = filedialog.askopenfilename()
        h = HuffmanCoding(file_path)
        output_path = h.compress()
        messagebox.showinfo("Compress", "Compressed file is saved as " + output_path)

    def decompress(self):
        file_path = filedialog.askopenfilename()
        h = HuffmanCoding(file_path)
        output_path = h.decompress()
        messagebox.showinfo("Decompress", "Decompressed file is saved as " + output_path)

root = Tk()
my_gui = HuffmanCodingGUI(root)
root.mainloop()