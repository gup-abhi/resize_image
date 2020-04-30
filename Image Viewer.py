# importing tkinter module
import tkinter as tk
# importing image from PIL module
from PIL import Image,ImageTk
# importing resizeimage from resizeimage module
from resizeimage import resizeimage

# creating window
win = tk.Tk()
# giving title to our window
win.title("image Viewer")
# specifying the window size
win.geometry("300x300")

# providing image path
path = "minion.jpg"
# resizing tne image after opening from the path provided (resize value should be less than the original size)
resize_image = resizeimage.resize_cover(Image.open(path), [100, 200])
# rendering the image
render_pic = ImageTk.PhotoImage(resize_image)
# putting the image in the window
img = tk.Label(win, image=render_pic)
img.pack()

# creating window loop
win.mainloop()
