
# import libraries
import os
from tkinter import *
from tkinter import messagebox
from PyPDF2 import PdfReader
import pyttsx3
# from PIL import Image, Imagetk

class PdfAudioConverter:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #============Variables==========================================
        self.input_file = StringVar()
        self.output_file = StringVar()
        self.start_page = StringVar()
        self.end_page = StringVar()
        
        # -------------title---------------------------------------------
        self.title = Label(self.root, text="PDF to Audio Converter", font=("goudy old style", 20, "bold"), bg="#0f4d7d", fg="white")
        self.title.place(x=10, y=10, width=1075, height=40)
        
        # =========== image frame==============================
        img_frame = Frame(self.root, bd=3, relief=RIDGE)
        img_frame.place(x=10,y=55,height=400,width=500,)
        
        # ======================= images =======================
        # self.img1 = Image.open("images/home.jpg")
        # self.img1 = self.img1.resize((400, 200), Image.ANTIALIAS)
        # self.img1 = ImageTk.PhotoImage(self.img1)
        # self.lbl_img1 = Label(self.root, image=self.img1, bd=3, relief=RAISED)
        # self.lbl_img1.place(x=10, y=55)
        
        # -------------Main section---------------------------------------------
        self.lbl1 = Label(self.root, text="Please upload or paste the path of the pdf file you want to convert:", 
                            font=("goudy old style", 14, "italic"), bg="white", fg="#0f4d7d")
        self.lbl1.place(x=515, y=55)
        
        btn_browse = Button(self.root, text="Browse", relief=RIDGE, cursor="hand2", font=("goudy old style", 15),
                            bg="#2196f3", fg="white").place(x=520, y=100, width=110, height=28)
        self.txt_input_file = Entry(self.root,textvariable=self.input_file, font=("goudy old style", 14, "bold"),
                          bg="lightyellow")
        self.txt_input_file.place(x=650, y=100, width=360)
        
        self.pages = Label(self.root, text="Page range:", font=("goudy old style", 14, "italic"), bg="white", fg="#0f4d7d")
        self.pages.place(x=515, y=140)
        
        self.lbl_start = Label(self.root, text="From:", font=("goudy old style", 14), bg="white", fg="#0f4d7d")
        self.lbl_start.place(x=630, y=140)
        self.txt_startPage = Entry(self.root,textvariable=self.start_page, font=("goudy old style", 14, "bold"),
                          bg="lightyellow").place(x=690, y=140, width=80)
        
        self.lbl_end = Label(self.root, text="To:", font=("goudy old style", 14), bg="white", fg="#0f4d7d")
        self.lbl_end.place(x=795, y=140)
        self.txt_endPage = Entry(self.root,textvariable=self.end_page, font=("goudy old style", 14, "bold"), 
                          bg="lightyellow").place(x=840, y=140, width=80)
        
        self.lbl_output = Label(self.root, text="Output file name:", font=("goudy old style", 14), bg="white", fg="#0f4d7d")
        self.lbl_output.place(x=515, y=200)
        self.txt_output = Entry(self.root,textvariable=self.output_file, font=("goudy old style", 14, "bold"), 
                          bg="lightyellow").place(x=690, y=200, width=230)
        
       
        btn_clear = Button(self.root, text="Clear",command=self.clear, relief=RIDGE, cursor="hand2", font=("goudy old style", 15),
                         bg="#9400D3", fg="white").place(x=665, y=260, width=110, height=38)
        btn_update = Button(self.root, text="Convert",command=self.convert, relief=RIDGE, cursor="hand2", font=("goudy old style", 15),
                         bg="#32CD32", fg="white").place(x=825, y=260, width=110, height=38)
        # btn_delete = Button(self.root, text="Exit", relief=RIDGE, cursor="hand2", font=("goudy old style", 15),
        #                  bg="#8B0000", fg="white").place(x=825, y=260, width=110, height=28)
        
        self.lbl_note = Label(self.root, text="Note: \n1. The document file to be uploaded should be in PDF format.\n2. The audio file is automatically downloaded to your Downloads folder.", 
                              font=("goudy old style", 14, "italic"), bg="white", fg="red", justify="left")
        self.lbl_note.place(x=515, y=320)
        
         # -------------footer---------------------------------------------
        self.footer = Label(self.root, text="Developed by High Tides Tech Solutions Ltd.\nEmail:stoneymorris98@gmail.com, contact: 0799211182", 
                            font=("goudy old style", 14, "italic"), bg="#0f4d7d", fg="white")
        self.footer.place(x=10, y=455, width=1075, height=40)
        
        #========== call method====================
        # self.printVar()
        
    # =====================Backend functionality=================================================
    # def upload(self):
    #     try:
    #         pass
    #     except:
    #         pass
            
    def clear(self):
        try:
            self.input_file.set("")
            self.output_file.set("")
            self.start_page.set("")
            self.end_page.set("")
        except Exception as e:
            print("Error occurred", e)
        
    def convert(self):
        try:
            file_path = self.input_file.get()
            startPage = int(self.start_page.get())
            endPage = int(self.end_page.get())
            output_name = self.output_file.get()
            
            speaker = pyttsx3.init()

            pdfReader = PdfReader(open(file_path,"rb"))
            # print(f"The book has {len(pdfReader.pages)} pages")
            # # print(pdfReader.pages[0].extract_text(0))
            text =""
            for page_num in range(startPage-1, endPage):
                text += pdfReader.pages[page_num].extract_text()
                # speaker.say(text)
                # speaker.runAndWait()

            # speaker.stop()

            speaker.save_to_file(text, output_name+".mp3")
            speaker.runAndWait()
            messagebox.showinfo("Success","The conversion process is successful!", parent=self.root)
        except Exception as e:
            print("Error occurred:", e)
            
        

if __name__ == "__main__":
    root = Tk()
    obj = PdfAudioConverter(root)
    root.mainloop()

