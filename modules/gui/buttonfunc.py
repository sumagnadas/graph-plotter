from modules import geometry

def draw(self):
    """Draw a line using the coordinates of the points provided by the user"""

    self.check()
    self.p1 = geometry.Point(int(self.x_coord1.text()), int(self.y_coord1.text()))
    self.p2 = geometry.Point(int(self.x_coord2.text()), int(self.y_coord2.text()))
    self.draw_call = True
    self.image.repaint()


def clear(self):
    """Clear the text boxes if the user presses "Clear" button and also the grid"""

    self.x_coord1.setText("0")
    self.y_coord1.setText("0")
    self.x_coord2.setText("0")
    self.y_coord2.setText("0")
    self.image.setPixmap("graph.png")

def save(self):
    self.save_call = True
    self.image.update()

def check(self):
    self.x_coord1.setzero()
    self.y_coord1.setzero()
    self.x_coord2.setzero()
    self.y_coord2.setzero()
