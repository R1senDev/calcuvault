from loader import config, storage_description

import pyglet

WINDOW_HEIGHT = 600

window = pyglet.window.Window(620, WINDOW_HEIGHT, caption = 'Calculator')

expression = '0'

class Button:
	def __init__(self, x, y, width, height, border, text):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.border = border
		self.text = text

	def draw(self):
		pyglet.shapes.Rectangle(self.x, self.y, self.width, self.height, (255, 255, 255, 255)).draw()
		pyglet.shapes.Rectangle(self.x + self.border, self.y + self.border, self.width - 2 * self.border, self.height - 2 * self.border, config['appearance']['bg_color']).draw()
		pyglet.text.Label(self.text, 'Consolas', 60, bold = True, color = (255, 255, 255, 255), x = self.x + self.width // 2, y = self.y + self.height // 2, anchor_x = 'center', anchor_y = 'center').draw()

	def is_clicked(self, x, y):
		return self.x < x < self.x + self.width and self.y < y < self.y + self.height

@window.event
def on_mouse_press(x, y, button, modifiers):
	global expression

	for i in buttons:
		if not buttons[i].is_clicked(x, y):
			continue

		match i:
		
			case '=':

				if expression == config['passkey']:
					expression = 'PASSKEY!'
				else:
					try:
						expression = str(eval(expression))
					except SyntaxError:
						expression = 'ERROR'

			case 'C':

				expression = '0'
			
			case _:

				if expression == 'ERROR':
					expression = ''
				expression += i
				if expression[0] == '0':
					expression = expression.lstrip('0')

@window.event
def on_resize(w, h):
	bg_rect.width  = w
	bg_rect.height = h

@window.event
def on_draw():
	window.clear()

	window.set_size(max(620, len(expression) * 48), WINDOW_HEIGHT)

	bg_rect.draw()

	for i in buttons:
		buttons[i].draw()
	
	pyglet.text.Label(expression, 'Consolas', 60, True, x = 20, y = 550, anchor_y = 'center', color = (255, 255, 255, 255)).draw()

buttons = {
	'.':     Button(20,  20,  100, 100, 5, '.'),
	'0':     Button(140, 20,  100, 100, 5, '0'),
	'=':     Button(260, 20,  100, 100, 5, '='),
	'+':     Button(380, 20,  100, 100, 5, '+'),
	'1':     Button(20,  140, 100, 100, 5, '1'),
	'2':     Button(140, 140, 100, 100, 5, '2'),
	'3':     Button(260, 140, 100, 100, 5, '3'),
	'-':     Button(380, 140, 100, 100, 5, '-'),
	'**0.5': Button(500, 140, 100, 100, 5, '√'),
	'4':     Button(20,  260, 100, 100, 5, '4'),
	'5':     Button(140, 260, 100, 100, 5, '5'),
	'6':     Button(260, 260, 100, 100, 5, '6'),
	'/':     Button(380, 260, 100, 100, 5, '/'),
	'**':    Button(500, 260, 100, 100, 5, '^'),
	'7':     Button(20,  380, 100, 100, 5, '7'),
	'8':     Button(140, 380, 100, 100, 5, '8'),
	'9':     Button(260, 380, 100, 100, 5, '9'),
	'*':     Button(380, 380, 100, 100, 5, '*'),
	'C':     Button(500, 380, 100, 100, 5, 'C'),
}

bg_rect = pyglet.shapes.Rectangle(0, 0, window.width, window.height, config['appearance']['bg_color'])

pyglet.app.run()