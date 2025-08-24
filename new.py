import cv2  # for image processing
import easygui  # to open the filebox
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import *
from PIL import Image

w1= tk.Tk()
w1.geometry('700x850')
w1.title('select your option!')
w1.configure(background ="#D3D3D3",
              bd="30")

label = Label(w1,text="select any of these option to convert an image to cartoon",background='grey', foreground='white', font=('calibri',20 , 'bold'))

label.pack()
varList = tk.StringVar(w1)
varList.set("Select-Option")
options_menu = ["Select-Image", "Capture-Image"]

class menu:
    def __init__(self,w1,varList,options_menu):
        self.w1=w1
        self.varList=varList
        self.options_menu=options_menu
    #select any option from optionmenu
    def option(self):
        om = tk.OptionMenu(self.w1,self.varList,*self.options_menu)
        om.config(bg='yellow',font=('calibri', 20, 'bold'))
        om.pack()
        button1 =Button(self.w1,text="submit", command=lambda:self.select(self.varList,self.options_menu,button1,om),padx=20, pady=15,background='black',foreground='white', activebackground='green',bd='4',justify='center',font=('calibri', 20, 'bold'))
        button1.pack(side=TOP)

#what option is selected retrival using get method and appropriate action to be taken
    def select(self,varList,options_menu,button1,om):
        t=tk.messagebox.askyesno("Are you sure", "Do you want to continue?")
        m = menu(w1,varList,options_menu)

        # if clicked ok
        if t and varList.get() in options_menu:
               options_menu = options_menu
               select = varList.get()
               if select == options_menu[0]:
                  t1 = tk.messagebox.askyesno("Are you sure", "Do you want to select an image?")
                  if t1:
                    p = select_image(w1)
                    p.upload()
                  else:
                    t1 = tk.messagebox.askyesno("warning", "Please select any image?",icon="error")
                    if t1:
                       self.select(varList,options_menu,button1,om)
                    else:
                        sys.exit()
               elif select== options_menu[1]:
                  t1 = tk.messagebox.askyesno("Are you sure", "Do you want to capture an image?")
                  if t1:
                      p = image_capture(w1)
                      p.cam()
                  else:
                       t1= tk.messagebox.askyesno("warning", "Please click ok to capture image?", icon="error")
                       if t1:

                         self.select(varList, options_menu)
                       else:
                          sys.exit()

        #if clicked no
        elif varList not in options_menu:
            t=tk.messagebox.askretrycancel("warning", "please select any of the option?",icon="error")

            if t:
                om.destroy()
                button1.destroy()
                self.option()
            else:
                sys.exit()
        else:
            t = tk.messagebox.askretrycancel("warning", "please retry?")
            if t:

                om.destroy()
                button1.destroy()
                self.option()
            else:
                sys.exit()




class capture_save:

    def __init__(self,image,w2):
        self.image=image
        self.w2=w2



    def filename_c(self):
        w3 = tk.Tk()
        w3.geometry('700x850')
        w3.title('Save-Capture')
        w3.configure(background="#ADD8E6", bd="30")


        L2 = Label(w3, text="Enter filename to be saved", bg='black', foreground='white',
                   font=('calibri', 20, 'bold')).grid(row=0, column=0)

        E1 = Entry(w3, bd=5,font=('calibri', 20, 'bold'))
        E1.grid(row=0, column=1)
        button3 = Button(w3, text="Save", font=('calibri', 15, 'bold'), bd='6', foreground='black', bg='white',
                         command=lambda: self.capture_save(E1, w3), padx=20,
                         pady=5).grid(row=1, columnspan=1, column=1)

    def capture_save(self, E1, w3):
        if E1.get() == "":
            t = tk.messagebox.askyesno("warning", "file name cannot be empty!", icon="error")
            if t=="yes":
                w3.destroy()
                self.filename()
            else:
                sys.exit()
        else:
            path1 = "capture-saves"
            extension = '.jpg'
            # c = select_image(top2)
            x = E1.get()
            path = os.path.join(path1, E1.get() + extension)

            cv2.imwrite(path,self.image)
            I = "Image saved by name " + E1.get() + " at " + path
            tk.messagebox.showinfo(title="saved_info", message=I)
            t=tk.messagebox.askquestion("Question","Do you want to continue?")
            w3.destroy()
            s=select_image(self.w2)
            if t=="yes":
                x=1
                l1 = Label(self.w2, text="Click on Cartoonify.", foreground='black',
                           font=('calibri', 20, 'bold'))
                l1.pack(side=TOP, pady=50)
                button2 = Button(self.w2, text="Cartoonify Image Captured", bd='6',
                                 command=lambda:s.cartoonify(path,x),
                                 padx=20, pady=5, background='black', foreground='white', font=('calibri', 15, 'bold'))
                button2.pack(side=TOP, pady=50)
            else:
                self.capture_save()
            # to cartoonify the image-selected



class select_image:
    def __init__(self,w1):
        self.w1=w1

    #to upload the image from local system
    def upload(self):
        ImagePath = easygui.fileopenbox()
        try:
            if Image.open(ImagePath):
                if Image.open(ImagePath).format.lower() in ['png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif']:
                    tk.messagebox.showinfo(title='image_selected', message="your image is choosen")
                    self.w2= tk.Tk()
                    self.w2.geometry('700x850')
                    self.w2.title('cartoonify image')
                    self.w2.configure(background="pink",
                                        bd="30")
                    l1 = Label(self.w2, text="Click on Cartoonify.", foreground='black',
                               font=('calibri', 20, 'bold'))
                    l1.pack(side=TOP, pady=50)
                    x=0
                    button2 = Button(self.w2, text="Cartoonify Image selected", bd='6',
                                     command=lambda: self.cartoonify(ImagePath,x), padx=20, pady=5, background='black',
                                     foreground='white', font=('calibri', 15, 'bold'))
                    button2.pack(side=TOP, pady=50)
        except:
            t=tk.messagebox.askquestion("Retry","Cannot find appropriate image. Choose appropriate file",icon="error")
            if t=='yes':
                ImagePath=""
                self.upload()
            else:
                sys.exit()
#to cartoonify the image-selected
    def cartoonify(self,ImagePath,x):

            m = image_capture(w1)
            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            originalmage = cv2.imread(ImagePath)

            g= cv2.cvtColor(originalmage, cv2.COLOR_RGB2BGR)

            # Detect faces in the image
            faces = faceCascade.detectMultiScale(
                g,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30,30),
                #flags=cv2.CV_HAAR_SCALE_IMAGE
            )
            print(format(len(faces)))
            if int(format(len(faces))) == 1:

                gray1 = cv2.cvtColor(g, cv2.COLOR_BGR2RGB)

                R1 = cv2.resize(g, (960, 540))
                # converting an image to grayscale
                grayScaleImage = cv2.cvtColor(g, cv2.COLOR_BGR2GRAY)
                R2 = cv2.resize(grayScaleImage, (960, 540))

                # applying median blur to smoothen an image

                smoothGrayScale = cv2.medianBlur(grayScaleImage, 3)
                R3 = cv2.resize(smoothGrayScale, (960, 540))

                # retrieving the edges for cartoon effect
                # by using thresholding technique
                getEdge = cv2.adaptiveThreshold(smoothGrayScale, 255,
                                                cv2.ADAPTIVE_THRESH_MEAN_C,
                                                cv2.THRESH_BINARY, 13, 5)

                R4 = cv2.resize(getEdge, (960, 540))

                # applying bilateral filter to remove noise
                # and keep edge sharp as required
                colorImage = cv2.bilateralFilter(gray1, 8, 75, 75)
                R5 = cv2.resize(colorImage, (960, 540))

                # masking edged image with our "BEAUTIFY" image
                cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)
                R6 = cv2.resize(cartoonImage, (960, 540))

                # Plotting the whole transition
                images = [R1, R2, R3, R4, R5, R6]
                cv2.imshow("Sketch",R4)


                t=tk.messagebox.showinfo(title='Cartoon_Converted', message="your image is converted to cartoon")
                if t:
                  t=tk.messagebox.askyesno(title='Save Cartoon Converted', message="Do you really want to save the cartooned image?")
                  if t:
                      fig, axes = plt.subplots(3, 2, figsize=(8, 8), subplot_kw={'xticks': [], 'yticks': []},
                                               gridspec_kw=dict(hspace=0.1, wspace=0.1))
                      for i, ax in enumerate(axes.flat):
                          ax.imshow(images[i], cmap='gray')
                      #plt.show()
                      save=save_cartoon(R4,self.w1)
                      w2= tk.Tk()
                      w2.geometry('700x850')
                      w2.title('cartoonify image')
                      w2.configure(background="pink",
                                          bd="30")
                      l2 = Label(w2, text="click on save cartoon.", foreground='black',
                                 font=('calibri', 20, 'bold'))
                      l2.pack(side=TOP, pady=50)

                      button3 = Button(w2, text="Save Cartooned Image", bd='6', command=save.filename,
                                       padx=20, pady=5, background='black', foreground='white',
                                       font=('calibri', 15, 'bold'))
                      button3.pack(side=TOP, pady=50)
                      plt.show()
                  else:
                      sys.exit()


            elif int(format(len(faces))) == 0:

                t = tk.messagebox.askyesno("Warning", "No faces detected. Do you wanna retry?", icon="error")
                if t:
                    if x==0:
                        self.upload()
                    elif x==1:
                        m.cam()


                else:
                    sys.exit()
            elif int(format(len(faces))) > 1:
                t = tk.messagebox.askyesno("Warning", "more than one face detected. Try again with single face?",
                                           icon="error")
                if t:
                    if x==0:
                        self.upload()
                    elif x==1:
                        m.cam()
                else:
                    sys.exit()


class save_cartoon:
    def __init__(self,R4,w2):
        self.R4=R4
        self.w2=w2
    def filename(self):
        #self.top1.destroy()

        w3 = tk.Tk()
        w3.geometry('700x850')
        w3.title('Save-Cartoon')
        w3.configure(background="#F5F5F5",bd="30")
        L3 = Label(w3, text="Enter filename to be saved", bg='black', foreground='white',
                   font=('calibri', 20, 'bold')).grid(row=0,column=0)

        E1 = Entry(w3, bd=5,font=('calibri', 20, 'bold'))
        E1.grid(row=0,column=1)
        button4= Button(w3, text="save", font=('calibri', 15, 'bold'),bd='6', foreground='black',bg='white',command=lambda:self.cartoon_save(E1,w3), padx=20,
                       pady=5).grid(row=1,columnspan=1,column=1)


    def cartoon_save(self,E1,w3):
        if E1.get()=="":
            t = tk.messagebox.askyesno("warning", "file name cannot be empty!", icon="error")
            if t=='yes':
                w3.destroy()
                self.filename()
            else:
                sys.exit()

        else:
            path1 = "cartoon-saves"
            extension = '.jpg'
            path = os.path.join(path1, E1.get() + extension)
            cv2.imwrite(path, cv2.cvtColor(self.R4, cv2.COLOR_RGB2BGR))
            I = "Image saved by name " + str(E1.get()) + " at " + path
            tk.messagebox.showinfo(title="saved_info", message=I)
            w3.destroy()


class image_capture:
    def __init__(self,w1):
        self.w1=w1


    def cam(self):
        t=tk.messagebox.showinfo("Instructions","Click 'a' to capture image or Click 'q' to quit")
        if t:
          cam = cv2.VideoCapture(0)

          while True:
            result, image = cam.read()
            cv2.imshow('capture-image', image)
            if cv2.waitKey(1) & 0xFF == ord('a'):
                if result==True:

                   t=tk.messagebox.askyesno("opinion", "do you want to save?")
                   if t:
                       cv2.waitKey(2000)
                       #cam.release()
                       cv2.destroyAllWindows()
                       break
                #break
                   else:
                       t=tk.messagebox.askyesno("opinion", "do you want to recapture image?")
                       #print(t)
                       if t:
                           #image_capture(top)
                           cam.destroy()
                           cv2.destroyAllWindows()

                           self.cam()
                        #self.cam()
                       else:
                           sys.exit()

                else:
                    cam.release()
                    break

            if cv2.waitKey(1) & 0xFF == ord('q'):
                t=tk.messagebox.askyesno("Retry", "Cannot capture any image.want to try again?", icon="error")
                if t:
                    #cam.destroy()
                    cv2.destroyAllWindows()

                    self.cam()
                else:
                    sys.exit()

        # cv2.destroyWindow('cartoon-image')
        if cam.isOpened():
            cv2.destroyAllWindows()
            cam.release()
           # cv2.VideoCapture(0).release()


        tk.messagebox.showinfo(title='Image_Captured', message="Your Image is Captured")
        #cv2.imshow("capture-image", image)
        self.w2 = tk.Tk()
        self.w2.geometry('700x850')
        self.w2.title('Save Capture')
        self.w2.configure(background="#FFFFE0",
                            bd="30")
        l1 = Label(self.w2, text="Click to Save Captured Image.", foreground='black',
                   font=('calibri', 20, 'bold'))
        l1.pack(side=TOP, pady=50)
        save = capture_save(image, self.w2)
        button2 = Button(self.w2, text="Save-Captured-Image", bd='6', command=save.filename_c, padx=20, pady=5,
                         background='black', foreground='white', font=('calibri', 15, 'bold'))
        button2.pack(side=TOP, pady=50)
def cartoonify(self, image):
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        gray1 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            image,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )

        if len(faces) == 1:
            # Converting the image to grayscale and applying filters
            grayScaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            smoothGrayScale = cv2.medianBlur(grayScaleImage, 3)
            getEdge = cv2.adaptiveThreshold(smoothGrayScale, 255,
                                            cv2.ADAPTIVE_THRESH_MEAN_C,
                                            cv2.THRESH_BINARY, 13, 5)

            # Applying bilateral filter
            colorImage = cv2.bilateralFilter(gray1, 8, 75, 75)

            # Masking edge image with "cartooned" image
            cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)

            # Showing the cartoonified image
            cv2.imshow("Cartoon Image", cartoonImage)

            t = tk.messagebox.showinfo(title='Cartoon Converted', message="Your image is converted to a cartoon.")
            if t:
                save = save_cartoon(cartoonImage, self.w2)
                button3 = Button(self.w2, text="Save Cartooned Image", bd='6', command=save.filename,
                                 padx=20, pady=5, background='black', foreground='white',
                                 font=('calibri', 15, 'bold'))
                button3.pack(side=TOP, pady=50)

        elif len(faces) == 0:
            tk.messagebox.showwarning("No Faces Detected", "No faces were detected in the image.")
        else:
            tk.messagebox.showwarning("Multiple Faces Detected", "More than one face was detected.")





s=menu(w1,varList,options_menu)
s.option()

w1.mainloop()

