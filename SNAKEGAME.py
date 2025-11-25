import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk  # For background image


class LoginPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game - Login")
        self.master.geometry("800x600")
        self.master.resizable(False, False)

        # Load and set background image
        self.bg_image = Image.open("snake-game-bg-image.jpg")
        self.bg_image = self.bg_image.resize((800, 600))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.background_label = tk.Label(master, image=self.bg_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(master, text="WELCOME TO SNAKE GAME !!!", font=("Arial", 30, "bold"), fg="white", bg="teal").pack(pady=10)
        tk.Label(master, text="Please enter your login and password", font=("Arial", 15), fg="white", bg="teal").pack(pady=5)

        tk.Label(master, text="Username:", font=("Arial", 20), fg="white", bg="teal").pack(pady=(10, 0))
        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        tk.Label(master, text="Password:", font=("Arial", 20), fg="white", bg="teal").pack(pady=(10, 0))
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        tk.Button(master, text="Login", command=self.authenticate).pack(pady=20)

        self.users = {
            "admin": "123",
            "player": "snake"
        }

    def authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.users and self.users[username] == password:
            self.master.destroy()
            root = tk.Tk()
            SnakeGame(root, username)
            root.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")


class SnakeGame:
    def __init__(self, master, username):
        self.master = master
        self.master.title(f"Snake Game - {username}")
        self.master.geometry("600x400")
        self.master.resizable(False, False)

        self.master.configure(bg="darkolivegreen")

        self.canvas = tk.Canvas(master, bg="darkolivegreen", width=1200, height=800)
        self.canvas.pack()

        self.cell_size = 20
        self.snake = [(5, 10), (4, 10), (3, 10)]
        self.direction = "Right"
        self.username = username
        self.score = 0

        self.food = None
        self.place_food()

        self.master.bind("<KeyPress>", self.change_direction)
        self.update_game()

    def place_food(self):
        while True:
            x = random.randint(0, 29)
            y = random.randint(0, 19)
            if (x, y) not in self.snake:
                self.food = (x, y)
                break

    def change_direction(self, event):
        key = event.keysym
        opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if key in ["Up", "Down", "Left", "Right"] and opposites.get(key) != self.direction:
            self.direction = key

    def update_game(self):
        head_x, head_y = self.snake[0]

        if self.direction == "Up":
            new_head = (head_x, head_y - 1)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 1)
        elif self.direction == "Left":
            new_head = (head_x - 1, head_y)
        elif self.direction == "Right":
            new_head = (head_x + 1, head_y)

        if (new_head in self.snake or
            new_head[0] < 0 or new_head[1] < 0 or
            new_head[0] >= 30 or new_head[1] >= 20):
            self.game_over()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.place_food()
        else:
            self.snake.pop()

        self.draw()
        self.master.after(150, self.update_game)

    def draw(self):
        self.canvas.delete("all")

        for (x, y) in self.snake:
            self.canvas.create_oval(
                x * self.cell_size,
                y * self.cell_size,
                (x + 1) * self.cell_size,
                (y + 1) * self.cell_size,
                fill="lime"
            )

        food_x, food_y = self.food
        self.canvas.create_oval(
            food_x * self.cell_size,
            food_y * self.cell_size,
            (food_x + 1) * self.cell_size,
            (food_y + 1) * self.cell_size,
            fill="red"
        )

    def game_over(self):
        self.canvas.create_text(300, 200, text=f"Game Over!\nScore: {self.score}", fill="white", font=("Arial", 20, "bold"))
        self.canvas.create_text(300, 250, text="Press 'R' to Restart", fill="white", font=("Arial", 12))
        self.master.bind("<KeyPress-r>", self.restart_game)
        self.master.bind("<KeyPress-q>", self.quit_game)

    def restart_game(self, event):
        self.snake = [(5, 10), (4, 10), (3, 10)]
        self.direction = "Right"
        self.score = 0
        self.place_food()
        self.update_game()


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginPage(root)
    root.mainloop()
