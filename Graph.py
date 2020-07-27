from tkinter import*
class Bars:
    """This module allows you to normalize an array or list, which is going to be
        passed as a parameter and then drawn in a bar graph.
        Note: This module only works on tkinter Canvas.

        For more info go to https://stackoverflow.com/questions/26785354/normalizing-a-list-of-numbers-in-python."""
    
    def __init__(self, canvas, data):
        """Canvas has to be a tkinter canvas, else this module won't work
            Data can be an array or a list."""
        self.canvas = canvas
        self.data = data
        self.canvas_dimensions = (self.canvas.winfo_reqheight(), self.canvas.winfo_reqwidth())


    def drawData(self, colors):
        """drawData has a color parameter that has to be list of colors,
            the rectangles are going to be filled by those colors on the list.
            Note: if the parameter is not a list it will throw an error."""
        self.canvas.delete("all")
        xWidth = self.canvas_dimensions[1] * 2 / (len(self.data) + 1)
        offcanvas, space = 20, 5
        normalizedData = [i / max(self.data) for i in self.data]
        for index, height in enumerate(normalizedData):
            xi = index * xWidth + offcanvas + space
            yi = self.canvas_dimensions[0] - (height * self.canvas_dimensions[0] / 1.10)
            xf = (index + 1) * xWidth + offcanvas
            yf = 425
            self.canvas.create_rectangle(xi, yi, xf, yf, fill=colors[index])
            if len(self.data) <= 50:
                self.canvas.create_text(xi,yi+2,anchor=SW,text=self.data[index],fill='white')

 
