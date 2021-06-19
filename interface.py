from tkinter import *
from PIL import ImageTk, Image
from face_detector import main

class Application:
    def __init__(self,root):
        self.root = root
        self.root.geometry("600x600")
        self.root.title('Face Authentication')
        self.fontePadrao = ("Arial", "10")

        self.img = ImageTk.PhotoImage(Image.open("assets/face.png"))

        self.imgContainer = Frame(root)
        self.imgContainer["pady"] = 20
        self.imgContainer.pack()

        self.primeiroContainer = Frame(root)
        self.primeiroContainer["pady"] = 20
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(root)
        self.segundoContainer["pady"] = 20
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.imgLabel = Label(self.imgContainer, image=self.img)
        self.imgLabel.pack()

        self.bntAuthenticate = Button(self.primeiroContainer, text="Autenticar",
        font=self.fontePadrao, width=12)
        self.bntAuthenticate["command"] = main
        self.bntAuthenticate.pack (side=LEFT)

        self.bntExit = Button(self.segundoContainer, text="Sair",
        font=self.fontePadrao, width=12)
        self.bntExit["command"] = self.root.destroy
        self.bntExit.pack (side=LEFT)

if __name__ == '__main__':

    root = Tk()
    app = Application(root)
    root.mainloop()