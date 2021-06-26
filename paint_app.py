from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from tkinter.ttk import Scale

import pyscreenshot as ImageGrab



class main:
    def __init__(self, master):
        self.root = master
        self.root.title("PAINT"
                        )
        self.root.geometry("800x520")
        self.color_fg = 'black'#Colour of pen
        self.color_bg = 'white'#Background colour
        self.root.configure(background='white')
        self.root.resizable(0,0)
        self.color_frame=LabelFrame(self.root,relief=RIDGE,bg='white')
        self.color_frame.place(x=0,y=0,width=40,height=210)

        #making colour buttons

        colors=['blue','black','red','#00a5f9','#682cbf','#009888']
        i=7
        j=0
        for color in colors:
            if color=='blue':
                Button(self.color_frame,bd=3,bg=color,relief=RIDGE,width=1,command=self.change_colorblue).grid(row=i,column=j)
            elif color=='black':
                Button(self.color_frame, bd=3, bg=color, relief=RIDGE, width=1, command=self.change_colorblack).grid(
                    row=i, column=j)
            elif color=='red':
                Button(self.color_frame, bd=3, bg=color, relief=RIDGE, width=1, command=self.change_colorred).grid(
                    row=i, column=j)
            elif color=='#00a5f9':
                Button(self.color_frame, bd=3, bg=color, relief=RIDGE, width=1, command=self.change_colora).grid(
                    row=i, column=j)
            elif color=='#682cbf':
                Button(self.color_frame, bd=3, bg=color, relief=RIDGE, width=1, command=self.change_colorb).grid(
                    row=i, column=j)
            elif color=='#009888':
                Button(self.color_frame, bd=3, bg=color, relief=RIDGE, width=1, command=self.change_colorc).grid(
                    row=i, column=j)
            i=i+1

        #making other buttons and placing them in apprprite place

        self.erazer_button=Button(self.root,text='ERAZE',font=('calibri',10),bd=3, bg= 'white' , command=self.eraze, width=8,relief=RIDGE)
        self.erazer_button.place(x=0,y=215)
        self.clear_button = Button(self.root, text='CLEAR', bd=3, bg='white', command=self.clear, width=8, relief=RIDGE)
        self.clear_button.place(x=0, y=245)
        self.save_button = Button(self.root, text='SAVE', bd=3, bg='white', command=self.save, width=8, relief=RIDGE)
        self.save_button.place(x=0, y=275)

        self.pen_size_scale_frame=LabelFrame(self.root,text='SIZE',bd=3,bg='white',font=('arial',8,'bold'),relief=RIDGE)
        self.pen_size_scale_frame.place(x=0,y=310,height=200,width=40)

        self.pen_size=Scale(self.pen_size_scale_frame,orient=VERTICAL,from_=3,to=25,command=self.changeW,length=170)
        self.pen_size.set(1)
        self.pen_size.grid(row=0,column=1,padx=9)

        #making the canvas and making it recognise movements of the mouse

        self.canvas=Canvas(self.root,bg='white',bd=3,relief=GROOVE,height=505,width=710)
        self.canvas.place(x=80,y=5)

        self.old_x = None
        self.old_y = None
        self.penwidth = 3
        self.canvas.bind('<B1-Motion>', self.paint)  # drawing  line
        self.canvas.bind('<ButtonRelease-1>', self.reset)

    #All functions are defined below



    def paint(self, e):
        '''creates a canvas where you can paint'''
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, e.x, e.y, width=self.penwidth, fill=self.color_fg,
                               capstyle=ROUND, smooth=True)

        self.old_x = e.x
        self.old_y = e.y

    def reset(self, e):
        '''reseting or cleaning the canvas'''
        self.old_x = None
        self.old_y = None

    def changeW(self, e):
        '''change Width of pen through slider'''
        self.penwidth = e

    def clear(self):
        '''clears the canvas'''
        self.canvas.delete(ALL)

    def change_colorblue(self):
        '''change colour to blue'''
        self.color_fg='blue'

    def change_colorblack(self):
        '''change colour to black'''
        self.color_fg='black'

    def change_colorred(self):
        '''change colour to red'''
        self.color_fg='red'

    def change_colora(self):
        self.color_fg='#00a5f9'

    def change_colorb(self):
        self.color_fg='#682cbf'

    def change_colorc(self):
        self.color_fg='#009888'

    def eraze(self):
        '''erazing stuff simply by changing colour of the brush to white'''
        self.color_fg='white'


    def save(self):

        '''Making values for a screenshort'''
        x = self.root.winfo_rootx() + self.canvas.winfo_x()
        #print(x)
        y = self.root.winfo_rooty() + self.canvas.winfo_y()
        #print(y)
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        #print(x1)
        #print(y1)
        screenshort=ImageGrab.grab().crop((x, y, x1, y1))

        filename = asksaveasfilename(initialdir = "/home",title = "Select file",filetypes = (('JPEG', ('*.jpg','*.jpeg','*.jpe','*.jfif')),('PNG', '*.png'),('BMP', ('*.bmp','*.jdib')),('GIF', '*.gif')))
        #print(filename)

        screenshort.save(filename)
        messagebox.showinfo('File saved : ', str(filename))

if __name__ == '__main__':
    root = Tk()
    main(root)
    root.title('Paint')
    root.mainloop()

