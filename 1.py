from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    title = "Tic Tac Toe!"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(
"""MDFloatLayout:
	MDGridLayout:
		size_hint: .5, .5
		pos_hint: {'center_x': .5, 'center_y': .7}
		cols: 3
		rows: 3

		Button:
			id: btn1
			text: ""
			font_size: "45sp"
			on_release: app.press(btn1)

		Button:
			id: btn2
			text: ""
			font_size: "45sp"
			on_release: app.press(btn2)

		Button:
			id: btn3
			text: ""
			font_size: "45sp"
			on_release: app.press(btn3)

		Button:
			id: btn4
			text: ""
			font_size: "45sp"
			on_release: app.press(btn4)

		Button:
			id: btn5
			text: ""
			font_size: "45sp"
			on_release: app.press(btn5)

		Button:
			id: btn6
			text: ""
			font_size: "45sp"
			on_release: app.press(btn6)

		Button:
			id: btn7
			text: ""
			font_size: "45sp"
			on_release: app.press(btn7)

		Button:
			id: btn8
			text: ""
			font_size: "45sp"
			on_release: app.press(btn8)

		Button:
			id: btn9
			text: ""
			font_size: "45sp"
			on_release: app.press(btn9)

	MDLabel:
		id: score
		font_size: "32sp"
		text: ""
		halign: "center"
		pos_hint: {"center_y": .3}""")

    turn = "X"

    winner = False

    def no_winner(self):
        if self.winner == False and \
                self.root.ids.btn1.disabled == True and \
                self.root.ids.btn2.disabled == True and \
                self.root.ids.btn3.disabled == True and \
                self.root.ids.btn4.disabled == True and \
                self.root.ids.btn5.disabled == True and \
                self.root.ids.btn6.disabled == True and \
                self.root.ids.btn7.disabled == True and \
                self.root.ids.btn8.disabled == True and \
                self.root.ids.btn9.disabled == True:
            self.root.ids.score.text = "Izjednačeno"

    def end_game(self, a, b, c):
        self.winner = True
        a.color = "red"
        b.color = "red"
        c.color = "red"

        self.disable()

        self.root.ids.score.text = f"{a.text} Pobjeđuje"

    def disable(self):
        self.root.ids.btn1.disabled = True
        self.root.ids.btn2.disabled = True
        self.root.ids.btn3.disabled = True
        self.root.ids.btn4.disabled = True
        self.root.ids.btn5.disabled = True
        self.root.ids.btn6.disabled = True
        self.root.ids.btn7.disabled = True
        self.root.ids.btn8.disabled = True
        self.root.ids.btn9.disabled = True

    def check(self):
        if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn2.text and self.root.ids.btn2.text == self.root.ids.btn3.text:
            self.end_game(self.root.ids.btn1, self.root.ids.btn2, self.root.ids.btn3)

        if self.root.ids.btn4.text != "" and self.root.ids.btn4.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn6.text:
            self.end_game(self.root.ids.btn4, self.root.ids.btn5, self.root.ids.btn6)

        if self.root.ids.btn7.text != "" and self.root.ids.btn7.text == self.root.ids.btn8.text and self.root.ids.btn8.text == self.root.ids.btn9.text:
            self.end_game(self.root.ids.btn7, self.root.ids.btn8, self.root.ids.btn9)

        if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn4.text and self.root.ids.btn4.text == self.root.ids.btn7.text:
            self.end_game(self.root.ids.btn1, self.root.ids.btn4, self.root.ids.btn7)

        if self.root.ids.btn2.text != "" and self.root.ids.btn2.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn8.text:
            self.end_game(self.root.ids.btn2, self.root.ids.btn5, self.root.ids.btn8)

        if self.root.ids.btn3.text != "" and self.root.ids.btn3.text == self.root.ids.btn6.text and self.root.ids.btn6.text == self.root.ids.btn9.text:
            self.end_game(self.root.ids.btn3, self.root.ids.btn6, self.root.ids.btn9)

        if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn9.text:
            self.end_game(self.root.ids.btn1, self.root.ids.btn5, self.root.ids.btn9)

        if self.root.ids.btn3.text != "" and self.root.ids.btn3.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn7.text:
            self.end_game(self.root.ids.btn3, self.root.ids.btn5, self.root.ids.btn7)

        self.no_winner()

    def press(self, btn):
        if self.turn == 'X':
            btn.text = "X"
            btn.disabled = True
            self.root.ids.score.text = ""
            self.turn = "O"
        else:
            btn.text = "O"
            btn.disabled = True
            self.root.ids.score.text = ""
            self.turn = "X"

        self.check()

MainApp().run()