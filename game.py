from tkinter import Button, Canvas, Label, Frame, Radiobutton, StringVar, PhotoImage, ttk
import random
from PIL import Image, ImageTk

class Game:
    def __init__(self, master):
        self.master = master
        #dictionary for image sources because of resizing of images
        self.img_sources = {"paper":"./images/paper.png", "rock":"./images/rock.png", "scissors":"./images/scissors.png"}
        #dictionary for choices, easy to switch based on key, key values are same as values of buttons
        self.choices = {"paper":ImageTk.PhotoImage(Image.open(self.img_sources.get("paper"))), "rock":ImageTk.PhotoImage(Image.open(self.img_sources.get("rock"))), "scissors":ImageTk.PhotoImage(Image.open(self.img_sources.get("scissors")))}
        self.choice = StringVar()
        self.game_gui()
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(3, weight=1)
        self.master.grid_columnconfigure(4, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.computer_choice = random.choice(list(self.choices.keys()))
        self.choice.set(random.choice(list(self.choices.keys())))
        self.score.set("SCORE")
        self.player_img = self.player_canvas.create_image(0, 0, image=self.choices.get(self.choice.get()), anchor="nw")
        self.computer_img = self.computer_canvas.create_image(0, 0, image=self.choices.get(self.computer_choice), anchor="nw")
        #event binds for canvases, resize images to match canvas sizes when window size changes
        self.player_canvas.bind("<Configure>", self.change_img_size)
        self.computer_canvas.bind("<Configure>", self.change_img_size)
        style = ttk.Style()
        style.configure("P.TButton", padding=10, foreground="#152a38", font=("Helvetica", 34))
        style.map("P.TButton",
            foreground=[("pressed", "#152a38"), ("active", "#152a38")])

        style.configure("TRadiobutton", padding=10, background="#556e53", foreground="#152a38", font="Helvetica")
        style.map("TRadiobutton",
            foreground=[("pressed", "#d1d4c9"), ("active", "#d1d4c9")],
            background=[("pressed", "!disabled", "#152a38"), ("active", "#556e53")])

        style.configure("TLabel", anchor="center", background="#556e53", foreground="#d1d4c9", font=("Helvetica", 34))

    def game_gui(self):

        #create widgets
        self.play_button = ttk.Button(self.master, text="PLAY", style="P.TButton", command=self.play)
        self.player_canvas = Canvas(self.master)
        self.computer_canvas = Canvas(self.master)
        self.vs_label = ttk.Label(self.master, text="VS")
        self.rock_button = ttk.Radiobutton(self.master, variable=self.choice, value="rock", text="ROCK", style="TRadiobutton", command=self.change_choice)
        self.paper_button = ttk.Radiobutton(self.master, variable=self.choice, value="paper", text="PAPER", style="TRadiobutton", command=self.change_choice)
        self.scissors_button = ttk.Radiobutton(self.master, variable=self.choice, value="scissors", text="SCISSOR", style="TRadiobutton", command=self.change_choice)
        self.score = StringVar()
        self.score_label = ttk.Label(self.master, textvariable=self.score)

        #place widgets using grid
        self.play_button.grid(row=0, column=3, pady=40)
        self.player_canvas.grid(row=0, column=0, padx=20, pady=20, rowspan=2, columnspan=3, sticky="NESW")
        self.vs_label.grid(row=1, column=3, sticky="EW")
        self.computer_canvas.grid(row=0, column=4, rowspan=2, padx=20, pady=20, sticky="NESW")
        self.rock_button.grid(row=2, column=0, padx=20, sticky="E")
        self.paper_button.grid(row=2, column=1, padx=20, sticky="W")
        self.scissors_button.grid(row=2, column=2, padx=20, sticky="W")
        self.score_label.grid(row=3, column=0, columnspan=5, pady=20, sticky="NESW")

    def play(self):   
        self.computer_choice = random.choice(list(self.choices.keys()))
        self.computer_canvas.itemconfig(self.computer_img, image=self.choices.get(self.computer_choice))
        player_choice = self.choice.get()
        if self.computer_choice == player_choice:
            self.score.set("IT IS A TIE")
        else:
            if (player_choice=="paper" and self.computer_choice=="rock") or (player_choice=="scissors" and self.computer_choice=="paper") or (player_choice=="rock" and self.computer_choice=="scissors"):
                self.score.set("YOU WIN")

            else:
                self.score.set("YOU LOSE")

    def change_choice(self):
        self.player_canvas.itemconfig(self.player_img, image=self.choices.get(self.choice.get()))

    def change_img_size(self, event):
        for key in self.choices:
            img_src = self.img_sources.get(key)
            img = Image.open(img_src).resize((event.width, event.height), Image.ANTIALIAS)
            self.choices[key] = ImageTk.PhotoImage(img)
        
        self.player_canvas.itemconfig(self.player_img, image=self.choices.get(self.choice.get()))
        self.computer_canvas.itemconfig(self.computer_img, image=self.choices.get(self.computer_choice))