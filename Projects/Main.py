import tkinter as tk
from tkinter import font
from StoryGenerator import StoryGenerator
from Teams import Teams
from Characters import Players
from NarrativeSchemas import Schemas


class Main:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("600x600")
        self.window.title("The Football Fiction Forger")
        self.window.configure(background='#1B1B1B')
        
        # Set font styles
        title_font = font.Font(family='Helvetica', size=40, weight='bold')
        button_font = font.Font(family='Helvetica', size=20, weight='bold')

        # Add title label
        title_label = tk.Label(self.window, text="The Football Fiction Forger", font=title_font, fg="#FFFFFF", bg="#1B1B1B")
        title_label.pack(pady=50)

        # Add button to generate story
        generate_button = tk.Button(self.window, text="Generate Story", font=button_font, fg="#FFFFFF", bg="#4B4B4B", command=self.generate_story)
        generate_button.place(relx=0.5, rely=0.5, anchor='center')
        
        self.window.mainloop()
        
    def generate_story(self):
        # Call the StoryGenerator class to generate a football story
        story_generator = StoryGenerator('used_names.json')
        story = story_generator.generate_story()
        
        # Display the story in a popup window
        popup_window = tk.Toplevel(self.window)
        popup_window.geometry("600x600")
        popup_window.configure(background='#1B1B1B')
        story_label = tk.Label(popup_window, text=story, font=font.Font(family='Helvetica', size=16), fg="#FFFFFF", bg="#1B1B1B", wraplength=500, justify='left')
        story_label.pack(padx=50, pady=50)

if __name__ == '__main__':
    app = Main()


teams = Teams()
defenders = Players()
scorers = Players()
goalkeepers = Players()
