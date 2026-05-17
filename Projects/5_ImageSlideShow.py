import tkinter as tk
import time
from PIL import Image , ImageTk


root = tk.Tk()
root.title("Image SlideShow")
root.geometry("900x900")



imagePaths = [
    r"C:\Users\prith\Downloads\ViratKohlii.jpg",
    r"C:\Users\prith\Downloads\SidhuMoosewalaa.jpg",
    r"C:\Users\prith\Downloads\Abdevillers.jfif"

]


images = []

for path in imagePaths:
    img = Image.open(path)
    img = img.resize((500,500))
    images.append(img)


finalImages = []

for img in images:
    photo = ImageTk.PhotoImage(img)
    finalImages.append(photo)

imageLabel = tk.Label(root)
imageLabel.pack(pady=30)



def startSlideshow():
    for photo in finalImages:
        imageLabel.config(image = photo)
        imageLabel.image = photo
        root.update()
        time.sleep(3)


playButton = tk.Button(
    root,
    text= "Play the slideshow",
    font =("Arial",17),
    command= startSlideshow
)

playButton.pack(pady=20)

root.mainloop()
