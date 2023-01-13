from imageai.Detection import ObjectDetection
from tkinter import *
import os
import tkinter.filedialog as fd

execution_path = os.getcwd()
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(execution_path, "retinanet_resnet50_fpn_coco-eeacb38b.pth"))
detector.loadModel()
objects = detector.CustomObjects(cat=True, dog=True)


def start_prog():
    btn_file = Button(text="Выбрать картинку", command=File)
    btn_file.pack()
    btn_file.place(x=20, y=20)
    btn_dir = Button(text="Сохранить в:", command=Dir)
    btn_dir.pack()
    btn_dir.place(x=20, y=60)
    btn_start = Button(text="Start", command=Compile)
    btn_start.pack()
    btn_start.place(x=20, y=200)


class Main():
    def __init__(self):
        """Запуск программы."""
        start_prog()


class File():
    def __init__(self):
        """Выбор пути к картинке"""

        self.filetypes = (("Изображение", "*.jpg *.gif *.png"), ("Любой", "*"))
        self.filepath = fd.askopenfilename(title="Открыть файл", initialdir="/", filetypes=self.filetypes)
        global filepath1
        filepath1 = self.filepath
        if self.filepath:
            self.LabelPath = Label(text=(self.filepath, "                                                        "))
            self.LabelPath.pack()
            self.LabelPath.place(x=140, y=20)
            print("File:", filepath1)


class Dir():
    def __init__(self):
        """Выбор пути для сохранения результата работы"""

        self.dir = fd.askdirectory(title="Открыть папку", initialdir="/")
        global filepath2
        filepath2 = self.dir
        if self.dir:
            self.LabelDir = Label(text=(self.dir, "                                                              "))
            self.LabelDir.pack()
            self.LabelDir.place(x=110, y=60)
            print("Saving path:", self.dir)


class Compile():
    def __init__(self):
        """Процесс распознавания животных на картинке"""

        list = detector.detectObjectsFromImage(minimum_percentage_probability=30, custom_objects=objects,
                                               input_image=filepath1,
                                               output_image_path=os.path.join(filepath2, "output.jpg"))

        self.LabelSuccess1 = Label(text="Выполнено!")
        self.LabelSuccess1.pack()
        self.LabelSuccess1.place(x=100, y=200)
        print("Success. Saved as output.jpg.")


root = Tk()
root.title("Animal finder")
root.wm_geometry("500x250+300+300")
app = Main()
root.mainloop()