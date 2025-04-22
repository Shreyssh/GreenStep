import tkinter as tk
from tkinter import messagebox
import threading
import time

class AnimatedCanvas(tk.Canvas):
    def __init__(self, parent, width, height, bg_color, fg_color, *args, **kwargs):
        super().__init__(parent, width=width, height=height, bg=bg_color, *args, **kwargs)
        self.fg_color = fg_color
        self.width = width
        self.height = height
        self.circle = self.create_oval(10, 10, 60, 60, fill=self.fg_color, outline="")
        self.dx = 2
        self.animate()

    def animate(self):
        self.move(self.circle, self.dx, 0)
        pos = self.coords(self.circle)
        if pos[2] >= self.width or pos[0] <= 0:
            self.dx = -self.dx
        self.after(30, self.animate)

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.config(bg="#d0f0c0")

        title = tk.Label(self, text="Login Portal", font=("Helvetica", 24, "bold"), bg="#d0f0c0")
        title.pack(pady=20)

        self.username_label = tk.Label(self, text="Username:", font=("Helvetica", 14), bg="#d0f0c0")
        self.username_label.pack(pady=(10,0))
        self.username_entry = tk.Entry(self, font=("Helvetica", 14))
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self, text="Password:", font=("Helvetica", 14), bg="#d0f0c0")
        self.password_label.pack(pady=(10,0))
        self.password_entry = tk.Entry(self, font=("Helvetica", 14), show="*")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(self, text="Login", font=("Helvetica", 14), command=self.check_login)
        self.login_button.pack(pady=20)

        # Show actual username and password at bottom
        self.info_label = tk.Label(self, text="Username: user123 | Password: pass123", font=("Helvetica", 12, "italic"), bg="#d0f0c0")
        self.info_label.pack(side="bottom", pady=10)

        # Background animation canvas
        self.bg_canvas = AnimatedCanvas(self, width=400, height=100, bg_color="#a0d8a0", fg_color="#4caf50")
        self.bg_canvas.pack(side="bottom", fill="x")

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "user123" and password == "pass123":
            self.controller.show_frame("PageOne")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#e0f7fa")

        title = tk.Label(self, text="Importance of Environment", font=("Helvetica", 20, "bold"), bg="#e0f7fa")
        title.pack(pady=10)

        text = (
            "The environment is vital to our survival. It provides us with clean air, water, and food.\n"
            "However, human activities have caused significant damage to the environment,\n"
            "including pollution, deforestation, and climate change."
        )
        self.text_label = tk.Label(self, text=text, font=("Helvetica", 14), bg="#e0f7fa", justify="center")
        self.text_label.pack(pady=10)

        # Foreground animation canvas
        self.fg_canvas = AnimatedCanvas(self, width=300, height=80, bg_color="#e0f7fa", fg_color="#00796b")
        self.fg_canvas.pack(pady=10)

        self.next_button = tk.Button(self, text="Go to Sustainable Ways", font=("Helvetica", 14),
                                     command=lambda: controller.show_frame("PageTwo"))
        self.next_button.pack(pady=20)

        # Background animation canvas
        self.bg_canvas = AnimatedCanvas(self, width=400, height=100, bg_color="#b2dfdb", fg_color="#004d40")
        self.bg_canvas.pack(side="bottom", fill="x")

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#fff3e0")

        title = tk.Label(self, text="Sustainable Ways to Conserve Environment", font=("Helvetica", 20, "bold"), bg="#fff3e0")
        title.pack(pady=10)

        text = (
            "We can conserve the environment by adopting sustainable practices such as:\n"
            "- Reducing waste and recycling\n"
            "- Using renewable energy sources\n"
            "- Conserving water\n"
            "- Planting trees\n"
            "- Supporting eco-friendly products"
        )
        self.text_label = tk.Label(self, text=text, font=("Helvetica", 14), bg="#fff3e0", justify="left")
        self.text_label.pack(pady=10)

        # Foreground animation canvas
        self.fg_canvas = AnimatedCanvas(self, width=300, height=80, bg_color="#fff3e0", fg_color="#f57c00")
        self.fg_canvas.pack(pady=10)

        self.back_button = tk.Button(self, text="Back to Importance", font=("Helvetica", 14),
                                     command=lambda: controller.show_frame("PageOne"))
        self.back_button.pack(pady=20)

        # Background animation canvas
        self.bg_canvas = AnimatedCanvas(self, width=400, height=100, bg_color="#ffe0b2", fg_color="#e65100")
        self.bg_canvas.pack(side="bottom", fill="x")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Environment Awareness App")
        self.attributes("-fullscreen", True)
        self.resizable(True, True)

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (LoginPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
