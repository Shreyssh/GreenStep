# GreenSteps - Enhanced GUI Python App with Tkinter

import tkinter as tk
from tkinter import messagebox, ttk, PhotoImage
import random
import datetime
import os

# Eco-friendly tips
tips = [
    "Turn off lights when not in use.",
    "Carry your own water bottle.",
    "Use both sides of paper.",
    "Unplug devices when not charging.",
    "Compost your food scraps."
]

# Point values for actions
actions = {
    "Walked or Cycled": 5,
    "Plant-Based Meal": 5,
    "Recycled": 5,
    "Saved Electricity": 5
}

# Achievements thresholds
achievements = {
    20: "Eco Novice 🌿",
    50: "Green Warrior 🌱",
    100: "Planet Protector 🌎"
}

# App data
total_points = 0
log = []
achieved = set()

# Functions
def log_action(action):
    global total_points
    points = actions[action]
    total_points += points
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f"[{timestamp}] {action} (+{points} pts)"
    log.insert(0, entry)
    update_points()
    update_log()
    check_achievements()
    messagebox.showinfo("Logged!", f"✅ {action} added! (+{points} pts)")

def update_points():
    points_label.config(text=f"🌟 Total Points: {total_points}")

def update_log():
    log_list.delete(0, tk.END)
    for entry in log:
        log_list.insert(tk.END, entry)

def check_achievements():
    for threshold, title in achievements.items():
        if total_points >= threshold and threshold not in achieved:
            achieved.add(threshold)
            messagebox.showinfo("🎉 Achievement Unlocked!", f"You earned the '{title}' badge!")
            achievements_list.insert(tk.END, f"{title}")

def show_tip():
    tip_label.config(text=f"🌍 Eco Tip: {random.choice(tips)}")

# GUI Setup
root = tk.Tk()
root.title("GreenSteps - Earth Day App")
root.geometry("750x600")
root.configure(bg="#e6f2e6")

# Load and set app icon
icon_path = "leaf.png"
if os.path.exists(icon_path):
    icon = PhotoImage(file=icon_path)
    root.iconphoto(False, icon)

header_frame = tk.Frame(root, bg="#4caf50")
header_frame.pack(fill=tk.X)

header = tk.Label(header_frame, text="🌿 GreenSteps - Save the Earth 🌿", font=("Arial", 24, "bold"), bg="#4caf50", fg="white", pady=10)
header.pack()

points_label = tk.Label(root, text="🌟 Total Points: 0", font=("Arial", 16), bg="#e6f2e6", fg="#2e4d2e")
points_label.pack(pady=10)

buttons_frame = tk.LabelFrame(root, text="Log Your Action", bg="#e6f2e6", font=("Arial", 12, "bold"), fg="#2e4d2e")
buttons_frame.pack(pady=10)

for action in actions:
    btn = tk.Button(buttons_frame, text=action, font=("Arial", 12), width=25, bg="#66bb6a", fg="white",
                    command=lambda a=action: log_action(a))
    btn.pack(pady=5)

log_frame = tk.LabelFrame(root, text="📜 Action Log", bg="#e6f2e6", font=("Arial", 12, "bold"), fg="#2e4d2e")
log_frame.pack(fill="both", expand=True, padx=20, pady=10)

log_list = tk.Listbox(log_frame, font=("Arial", 10), height=8)
log_list.pack(fill="both", expand=True, padx=10, pady=10)

achievements_frame = tk.LabelFrame(root, text="🏅 Achievements", bg="#e6f2e6", font=("Arial", 12, "bold"), fg="#2e4d2e")
achievements_frame.pack(fill="x", padx=20, pady=10)

achievements_list = tk.Listbox(achievements_frame, font=("Arial", 10), height=3)
achievements_list.pack(fill="both", expand=True, padx=10, pady=5)

tip_label = tk.Label(root, text="", font=("Arial", 12, "italic"), bg="#e6f2e6", fg="#2e4d2e")
tip_label.pack(pady=10)

show_tip()

root.mainloop()
