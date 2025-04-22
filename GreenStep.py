import tkinter as tk
from tkinter import messagebox, PhotoImage
import random
import datetime
import os

# ----------- Animated Canvas Class -----------
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

# ----------- Login Page -----------
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#d0f0c0")

        tk.Label(self, text="Login Portal", font=("Helvetica", 24, "bold"), bg="#d0f0c0").pack(pady=20)

        tk.Label(self, text="Username:", font=("Helvetica", 14), bg="#d0f0c0").pack(pady=(10, 0))
        self.username_entry = tk.Entry(self, font=("Helvetica", 14))
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Password:", font=("Helvetica", 14), bg="#d0f0c0").pack(pady=(10, 0))
        self.password_entry = tk.Entry(self, font=("Helvetica", 14), show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Login", font=("Helvetica", 14), command=self.check_login).pack(pady=20)

        tk.Label(self, text="Username: user123 | Password: pass123", font=("Helvetica", 12, "italic"), bg="#d0f0c0").pack(side="bottom", pady=10)
        self.bg_canvas = AnimatedCanvas(self, width=400, height=100, bg_color="#a0d8a0", fg_color="#4caf50")
        self.bg_canvas.pack(side="bottom", fill="x")

    def check_login(self):
        if self.username_entry.get() == "user123" and self.password_entry.get() == "pass123":
            self.controller.show_frame("PageOne")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

# ----------- Page One -----------
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#e0f7fa")

        tk.Label(self, text="Importance of Environment", font=("Helvetica", 20, "bold"), bg="#e0f7fa").pack(pady=10)
        tk.Label(
            self,
            text="The environment is vital to our survival. It provides us with clean air, water, and food.\n"
                 "However, human activities have caused significant damage to the environment,\n"
                 "including pollution, deforestation, and climate change.",
            font=("Helvetica", 14), bg="#e0f7fa", justify="center").pack(pady=10)

        AnimatedCanvas(self, width=300, height=80, bg_color="#e0f7fa", fg_color="#00796b").pack(pady=10)
        tk.Button(self, text="Go to Sustainable Ways", font=("Helvetica", 14),
                  command=lambda: controller.show_frame("PageTwo")).pack(pady=20)

        AnimatedCanvas(self, width=400, height=100, bg_color="#b2dfdb", fg_color="#004d40").pack(side="bottom", fill="x")

# ----------- Page Two -----------
class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#fff3e0")

        tk.Label(self, text="Sustainable Ways to Conserve Environment", font=("Helvetica", 20, "bold"), bg="#fff3e0").pack(pady=10)
        tk.Label(
            self,
            text="- Reducing waste and recycling\n"
                 "- Using renewable energy sources\n"
                 "- Conserving water\n"
                 "- Planting trees\n"
                 "- Supporting eco-friendly products",
            font=("Helvetica", 14), bg="#fff3e0", justify="left").pack(pady=10)

        AnimatedCanvas(self, width=300, height=80, bg_color="#fff3e0", fg_color="#f57c00").pack(pady=10)
        tk.Button(self, text="Go to GreenSteps Tracker", font=("Helvetica", 14),
                  command=lambda: controller.show_frame("PageThree")).pack(pady=10)
        tk.Button(self, text="Back to Importance", font=("Helvetica", 14),
                  command=lambda: controller.show_frame("PageOne")).pack()

        AnimatedCanvas(self, width=400, height=100, bg_color="#ffe0b2", fg_color="#e65100").pack(side="bottom", fill="x")

# ----------- Page Three (GreenSteps App) -----------
class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#e6f2e6")

        self.total_points = 0
        self.log = []
        self.achieved = set()
        self.tips = [
            "Turn off lights when not in use.",
            "Carry your own water bottle.",
            "Use both sides of paper.",
            "Unplug devices when not charging.",
            "Compost your food scraps."
        ]
        self.actions = {
            "Walked or Cycled": 5,
            "Plant-Based Meal": 5,
            "Recycled": 5,
            "Saved Electricity": 5
        }
        self.achievements = {
            20: "Eco Novice 🌿",
            50: "Green Warrior 🌱",
            100: "Planet Protector 🌎"
        }

        tk.Label(self, text="🌿 GreenSteps - Save the Earth 🌿", font=("Arial", 24, "bold"), bg="#4caf50", fg="white").pack(fill="x")

        self.points_label = tk.Label(self, text="🌟 Total Points: 0", font=("Arial", 16), bg="#e6f2e6", fg="#2e4d2e")
        self.points_label.pack(pady=10)

        button_frame = tk.LabelFrame(self, text="Log Your Action", bg="#e6f2e6", font=("Arial", 12, "bold"), fg="#2e4d2e")
        button_frame.pack(pady=10)
        for action in self.actions:
            tk.Button(button_frame, text=action, font=("Arial", 12), width=25, bg="#66bb6a", fg="white",
                      command=lambda a=action: self.log_action(a)).pack(pady=5)

        log_frame = tk.LabelFrame(self, text="📜 Action Log", bg="#e6f2e6", font=("Arial", 12, "bold"), fg="#2e4d2e")
        log_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.log_list = tk.Listbox(log_frame, font=("Arial", 10), height=8)
        self.log_list.pack(fill="both", expand=True, padx=10, pady=10)

        ach_frame = tk.LabelFrame(self, text="🏅 Achievements", bg="#e6f2e6", font=("Arial", 12, "bold"), fg="#2e4d2e")
        ach_frame.pack(fill="x", padx=20, pady=10)

        self.achievements_list = tk.Listbox(ach_frame, font=("Arial", 10), height=3)
        self.achievements_list.pack(fill="both", expand=True, padx=10, pady=5)

        self.tip_label = tk.Label(self, text="", font=("Arial", 12, "italic"), bg="#e6f2e6", fg="#2e4d2e")
        self.tip_label.pack(pady=10)
        self.show_tip()

        tk.Button(self, text="⬅ Back to Sustainable Ways", font=("Arial", 12),
                  command=lambda: controller.show_frame("PageTwo")).pack(pady=10)

    def log_action(self, action):
        points = self.actions[action]
        self.total_points += points
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        entry = f"[{timestamp}] {action} (+{points} pts)"
        self.log.insert(0, entry)
        self.update_points()
        self.update_log()
        self.check_achievements()
        messagebox.showinfo("Logged!", f"✅ {action} added! (+{points} pts)")

    def update_points(self):
        self.points_label.config(text=f"🌟 Total Points: {self.total_points}")

    def update_log(self):
        self.log_list.delete(0, tk.END)
        for entry in self.log:
            self.log_list.insert(tk.END, entry)

    def check_achievements(self):
        for threshold, title in self.achievements.items():
            if self.total_points >= threshold and threshold not in self.achieved:
                self.achieved.add(threshold)
                self.achievements_list.insert(tk.END, f"{title}")
                messagebox.showinfo("🎉 Achievement Unlocked!", f"You earned the '{title}' badge!")

    def show_tip(self):
        self.tip_label.config(text=f"🌍 Eco Tip: {random.choice(self.tips)}")

# ----------- Main App Controller -----------
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Environment Awareness + GreenSteps Tracker")
        self.attributes("-fullscreen", True)

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (LoginPage, PageOne, PageTwo, PageThree):
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
