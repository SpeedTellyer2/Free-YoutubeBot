import tkinter as tk
import tkinter.font as tkfont

class YouTubeBotGUI:
    def __init__(self, master):
        self.master = master
        master.title("𝖄𝖔𝖚𝖙𝖚𝖇𝖊𝕭𝖔𝖙")
        master.configure(background="#000000")

        # Create custom font for title
        title_font = tkfont.Font(family="Arial", size=24, weight="bold")
        title_label = tk.Label(master, text="𝖄𝖔𝖚𝖙𝖚𝖇𝖊𝕭𝖔𝖙", font=title_font, fg="#FF0000", bg="#000000")
        title_label.pack(pady=20)

        # Create input fields for video link and amount
        self.link_label = tk.Label(master, text="Video Link:", fg="#FF0000", bg="#000000")
        self.link_label.pack()
        self.link_entry = tk.Entry(master, width=40, fg="#FF0000", bg="#000000")
        self.link_entry.pack()

        self.amount_label = tk.Label(master, text="Amount:", fg="#FF0000", bg="#000000")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(master, width=40, fg="#FF0000", bg="#000000")
        self.amount_entry.pack()

        # Create buttons for each interaction type
        self.subscription_button = tk.Button(master, text="Send Subscribers", command=self.send_subscribers, fg="#FF0000", bg="#000000")
        self.subscription_button.pack(pady=10)

        self.view_button = tk.Button(master, text="Send Views", command=self.send_views, fg="#FF0000", bg="#000000")
        self.view_button.pack(pady=10)

        self.like_button = tk.Button(master, text="Send Likes", command=self.send_likes, fg="#FF0000", bg="#000000")
        self.like_button.pack(pady=10)

        self.comment_button = tk.Button(master, text="Send Comments", command=self.send_comments, fg="#FF0000", bg="#000000")
        self.comment_button.pack(pady=10)

        self.watch_hours_button = tk.Button(master, text="Send Watch Hours", command=self.send_watch_hours, fg="#FF0000", bg="#000000")
        self.watch_hours_button.pack(pady=10)

    def send_subscribers(self):
        self.show_message("Subscribers sent successfully!")

    def send_views(self):
        self.show_message("Views sent successfully!")

    def send_likes(self):
        self.show_message("Likes sent successfully!")

    def send_comments(self):
        self.show_message("Comments sent successfully!")

    def send_watch_hours(self):
        self.show_message("Watch hours sent successfully!")

    def show_message(self, message):
        print(message)

root = tk.Tk()
my_gui = YouTubeBotGUI(root)
root.mainloop()