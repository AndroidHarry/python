
https://kivy.org/doc/stable/gettingstarted/intro.html


Checking the demo
python kivy_venv/share/kivy-examples/demo/showcase/main.py


self.x = self.y = 0
self.top = self.height





##########################################################################

.kv file

keyword: root, self.parent
-------------------------------
eg, pong.kv
center_x: root.width * 3 / 4
center: self.parent.center

##########################################################################

(layout) 布局
/examples/demo/kivycatalog


(coordinate)坐标: x, y, top, right
-----------------------------------
eg, 
 # bounce off top and bottom
 if (self.ball.y < 0) or (self.ball.top > self.height):
	self.ball.velocity_y *= -1

 # bounce off left and right
 if (self.ball.x < 0) or (self.ball.right > self.width):
	self.ball.velocity_x *= -1

##########################################################################

touch.ud
------------
touch.ud is a Python dictionary (type <dict>) that allows us to store custom attributes for a touch.
By creating the line inside the with block, the canvas automatically knows about the line and will draw it.

eg,
	def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 1, 0)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

##########################################################################

