import requests
import tkinter as tk
from PIL import ImageTk, Image 
root=tk.Tk()
def dowloader(url):
    print(url)
    response = requests.get(url)
    image1=Image.open(requests.get(url, stream=True).raw)
    image1 = image1.resize((100,100), Image. ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(image=test)
    label1.image = test
    label1.place(x=250, y=200)
    file = open("ImageDownloader/image.jpg", "wb")
    file.write(response.content)
    file.close()
root.geometry('600x400')
var = tk.StringVar()
label =tk.Label( root, textvariable=var,font = "Helvetica 14 bold" )

var.set("past your image url")
label.pack()
txt =tk.Entry(root,width=50,justify='center',font = "Helvetica 14 bold")
txt.pack()
B = tk.Button(root, text ="Dowload",activeforeground = "blue",activebackground = "pink",pady=10,padx=20, command =lambda:dowloader(txt.get()))
B.pack()



root.mainloop()
    