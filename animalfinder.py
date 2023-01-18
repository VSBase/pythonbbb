from imageai.Detection import ObjectDetection
from tkinter import *
import os
import tkinter.filedialog as fd
import tkinter as tk

execution_path = os.getcwd()
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(execution_path, "retinanet_resnet50_fpn_coco-eeacb38b.pth"))
detector.loadModel()
objects = detector.CustomObjects(cat=True, dog=True, bird=True, horse=True,
                                 sheep=True, cow=True, elephant=True,
                                 bear=True, zebra=True, giraffe=True)


class AboutRE(tk.Toplevel):
    def __init__(self):
        super().__init__()

        """Вывод окна с ошибкой RunTimeError"""

        self.title("RuntimeError!")
        self.wm_geometry("400x100")
        self.label = Label(self, text="Ошибка!\n Некорректный формат изображения!\n")
        self.button = Button(self, text="Закрыть", command=self.destroy)
        self.label.pack()
        self.button.pack()


class AboutNE(tk.Toplevel):
    def __init__(self):
        super().__init__()

        """Вывод окна с ошибкой NameError"""

        self.title("NameError!")
        self.wm_geometry("400x100")
        self.label = Label(self, text="Ошибка!\n Не выбрано изображение!\n Либо выбран некорректный формат!\n")
        self.button = Button(self, text="Закрыть", command=self.destroy)
        self.label.pack()
        self.button.pack()


class Main(tk.Frame):
    def __init__(self):
        super().__init__()
        """Запуск программы."""
        self.start_prog()

    def start_prog(self):
        """Кнопки в основном меню"""
        btn_file = Button(text="Выбрать изображение", command=File)
        btn_file.pack()
        btn_file.place(x=20, y=20)
        btn_dir = Button(text="Папка сохранения", command=Dir)
        btn_dir.pack()
        btn_dir.place(x=20, y=60)
        self.LabelDirEx = Label(text=(execution_path + " (По умолчанию)                                              "))
        self.LabelDirEx.pack()
        self.LabelDirEx.place(x=140, y=60)
        btn_start = Button(text="Выполнить", command=Compile)
        btn_start.pack()
        btn_start.place(x=20, y=140)
        btn_close = Button(text="Завершить", command=root.destroy)
        btn_close.pack()
        btn_close.place(x=400, y=200)


class File(tk.Frame):
    def __init__(self):
        super().__init__()
        """Выбор пути к картинке"""

        self.filetypes = (("Изображение", "*.jpg *.gif *.png *.bmp *.tiff"), ("Любой", "*"))
        self.filepath = fd.askopenfilename(title="Открыть файл", initialdir="/", filetypes=self.filetypes)
        global filepath1
        filepath1 = self.filepath
        if self.filepath:
            self.LabelPath = Label(
                text=(self.filepath + "                                                            "))
            self.LabelPath.pack()
            self.LabelPath.place(x=160, y=20)
            print("File:", filepath1)


class Dir(tk.Frame):
    def __init__(self):
        super().__init__()
        """Выбор пути для сохранения результата работы"""

        self.dir = fd.askdirectory(title="Открыть папку", initialdir="/")
        global filepath2
        filepath2 = self.dir
        if self.dir:
            self.LabelDir = Label(
                text=(self.dir + "                                                                  "))
            self.LabelDir.pack()
            self.LabelDir.place(x=140, y=60)
            print("Saving path:", self.dir)


class Compile(tk.Frame):
    def __init__(self):
        super().__init__()
        """Процесс распознавания животных на картинке"""
        try:
            list = detector.detectObjectsFromImage(minimum_percentage_probability=30, custom_objects=objects,
                                                   input_image=filepath1,
                                                   output_image_path=os.path.join(filepath2, "output.jpg"))
            self.LabelSuccessOut = Label(text="Успешно выполнено!                                                     ")
            self.LabelSuccessOut.pack()
            self.LabelSuccessOut.place(x=100, y=140)
            print("Success. Saved as output.jpg.")
        except RuntimeError:
            about = AboutRE()
            about.grab_set()
            self.LabelErrorOut = Label(text="Ошибка!                                                                  ")
            self.LabelErrorOut.pack()
            self.LabelErrorOut.place(x=100, y=140)
        except NameError:
            about = AboutNE()
            about.grab_set()
            self.LabelErrorOut = Label(text="Ошибка!                                                                  ")
            self.LabelErrorOut.pack()
            self.LabelErrorOut.place(x=100, y=140)


if __name__ == "__main__":
    root = Tk()
    root.title("Animal finder")
    root.wm_geometry("500x250+300+300")
    app = Main()
    root.mainloop()
