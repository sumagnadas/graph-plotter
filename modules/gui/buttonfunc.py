from modules import geometry


def draw(self):
    """Draw a line using the coordinates of the points provided by the user"""

    self.check()
    self.p1 = geometry.Point(int(self.x_coord1.text()),
                             int(self.y_coord1.text()))
    self.p2 = geometry.Point(int(self.x_coord2.text()),
                             int(self.y_coord2.text()))
    self.draw_call = True
    self.image.repaint()


def clear(self):
    '''Not to be called by the program
    Resets the input boxes and clear the line(s) on the grid
    When the user presses 'Reset' button'''

    self.x_coord1.setText("0")
    self.y_coord1.setText("0")
    self.x_coord2.setText("0")
    self.y_coord2.setText("0")
    self.image.setPixmap("resources/graph.png")


def save(self):
    self.save_call = True
    self.image.update()


def check(self):
    self.x_coord1.setzero()
    self.y_coord1.setzero()
    self.x_coord2.setzero()
    self.y_coord2.setzero()


def setSaveFiledir(self, filedir):
    self.fileDir = filedir
