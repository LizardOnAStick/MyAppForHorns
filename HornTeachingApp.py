import tkinter as tk
from tkinter import messagebox
import pyaudio
import numpy as np
import webbrowser

class FrenchHornApp:
    def __init__(self, master):
        self.master = master
        master.title("French Horn Teacher")
        
        # Set the color scheme
        self.bg_color = "#000000"  # Black
        self.text_color = "#4B9CD3"  # Blue
        self.button_bg = "#1E3F66"  # Darker blue for buttons
        self.button_fg = "#FFFFFF"  # White text for buttons
        
        master.configure(bg=self.bg_color)
        
        self.current_frame = None
        self.current_lesson = 1  # Track the current lesson
        self.all_lessons_completed = False  # Track if all lessons are completed
        
        # Audio setup for tuner
        self.CHUNK = 1024
        self.RATE = 44100
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paFloat32,
                                  channels=1,
                                  rate=self.RATE,
                                  input=True,
                                  frames_per_buffer=self.CHUNK)
        self.video_urls = {
            "Intro": "https://www.youtube.com/watch?v=XA6jumI7cw0",
            "Lesson 1": "https://www.youtube.com/watch?v=3alV6peUo60",
            "Lesson 2": "https://www.youtube.com/watch?v=evcttJdPu_I",
            "Lesson 3": "https://www.youtube.com/watch?v=dOLpUCR4iSM"
        }
        self.play_intro_video()

        self.show_menu()
    def play_video(self, video_key):
        video_url = self.video_urls.get(video_key)
        if not video_url:
            messagebox.showwarning("Video Not Found", f"No Video found for {video_key}")
            return
        webbrowser.open(video_url)
    def play_intro_video(self):
        self.play_video("Intro")
    def show_menu(self):
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = tk.Frame(self.master, bg=self.bg_color)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(self.current_frame, text="Welcome to French Horn Teacher", 
                 bg=self.bg_color, fg=self.text_color, font=("Arial", 18, "bold")).pack(pady=20)
        
        tk.Label(self.current_frame, text="Learn to play the French Horn with interactive lessons", 
                 bg=self.bg_color, fg=self.text_color, font=("Arial", 14)).pack(pady=10)
        
        # Display current lesson number or completion status
        status_text = "All lessons completed!" if self.all_lessons_completed else f"Current Lesson: {self.current_lesson}"
        tk.Label(self.current_frame, text=status_text, 
                 bg=self.bg_color, fg=self.text_color, font=("Arial", 12)).pack(pady=10)
        
        tk.Button(self.current_frame, text="Continue Lesson", command=self.continue_lesson,
                  bg=self.button_bg, fg=self.button_fg, font=("Arial", 12)).pack(pady=20)
        
        if self.all_lessons_completed:
            tk.Button(self.current_frame, text="Open Tuner", command=self.show_advanced_tuner,
                      bg=self.button_bg, fg=self.button_fg, font=("Arial", 12)).pack(pady=20)
        
        tk.Button(self.current_frame, text="Quit", command=self.master.quit,
                  bg=self.button_bg, fg=self.button_fg, font=("Arial", 12)).pack(pady=10)

    def continue_lesson(self):
        if self.current_lesson == 1:
            self.start_lesson1()
        elif self.current_lesson == 2:
            self.start_lesson2()
        elif self.current_lesson == 3:
            self.start_lesson3()
        # Add more elif statements for future lessons
    
    def start_lesson1(self):
        self.play_video("Lesson 1")
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = tk.Frame(self.master, bg=self.bg_color)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(self.current_frame, text="Lesson 1: Proper Breathing and Embouchure for French Horn",
                 bg=self.bg_color, fg=self.text_color, font=("Arial", 14, "bold")).pack(pady=10)
        
        instructions = [
            "1. Take a deep breath, expanding your diaphragm.",
            "2. Form your embouchure: Make a small 'o' shape with your lips.",
            "3. Buzz your lips as if saying 'mm'."
        ]
        
        for instruction in instructions:
            tk.Label(self.current_frame, text=instruction, bg=self.bg_color, fg=self.text_color, 
                     font=("Arial", 12)).pack(anchor='w', padx=10, pady=5)
        
        tk.Button(self.current_frame, text="I've practiced these steps", command=self.check_practice_lesson1,
                  bg=self.button_bg, fg=self.button_fg, font=("Arial", 12)).pack(pady=20)
        
        self.attempts = 0
    
    def check_practice_lesson1(self):
        self.attempts += 1
        if self.attempts < 3:
            messagebox.showinfo("Keep Practicing", "Great job! Now try again, focusing on keeping your embouchure relaxed.")
        else:
            messagebox.showinfo("Well Done!", "Excellent! You've completed the first French horn breathing and embouchure exercise.")
            self.current_lesson = 2  # Progress to next lesson
            self.show_completion_lesson1()
    
    def show_completion_lesson1(self):
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = tk.Frame(self.master, bg=self.bg_color)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(self.current_frame, text="Congratulations on completing Lesson 1!", 
                 bg=self.bg_color, fg=self.text_color, font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(self.current_frame, text="In the next lesson, we'll cover how to hold the French horn.", 
                 bg=self.bg_color, fg=self.text_color, font=("Arial", 12)).pack()
        
        tk.Button(self.current_frame, text="Next Lesson", command=self.start_lesson2,
                  bg=self.button_bg, fg=self.button_fg, font=("Arial", 12)).pack(pady=20)
        
        tk.Button(self.current_frame, text="Back to Menu", command=self.show_menu,
                  bg=self.button_bg, fg=self.button_fg, font=("Arial", 12)).pack(pady=20)
    
    def start_lesson2(self):
        self.play_video("Lesson 2")
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = tk.Frame(self.master, bg=self.bg_color)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(self.current_frame, text="Lesson 2: How to properly hold a French Horn",
                 bg=self.bg_color, fg=self.text_color, font=("Arial", 14, "bold")).pack(pady=10)
        
        instructions = [
            "1. Stick the farthest edge of the bell (where the sound comes out) from your instrument on your leg",
            "2. Put the mouthpiece to your lips",
            "3. Take your left hand and put it on the buttons with your hand wrapped around the tube",
            "4. Put your pinky finger on the metal piece sticking up to hold your horn, then place your thumb on the other piece of metal on the other side",
            "5. Put your hand inside the bell and have it flat against the metal facing you",
            "6. Move your right hand to the middle of the inside of the bell where it sharply drops inward and the very outward edge"
        ]
        
        for instruction in instructions:
            tk.Label(self.current_frame, text=instruction, bg=self.bg_color, fg=self.text_color, 
                     font=("Arial", 12)).pack(anchor='w', padx=10, pady=5)
        
        tk.Button(self.current_frame, text="I've practiced these steps", command=self.check_practice_lesson2,
                  bg=self.button_bg, fg=self.button_fg, font=("Arial", 12)).pack(pady=20)
        
        self.attempts = 0
    
    def check_practice_lesson2(self):
        self.attempts += 1
        if self.attempts < 3:
            messagebox.showinfo("Keep Practicing", "Great job! Now reset, focusing on your hand placements.")
        else:
            messagebox.showinfo("Well Done!", "Excellent! You've completed the second lesson")
            self.current_lesson = 3  # Progress to next lesson (if implemented)
            self.show_completion_lesson2()
    
    def show_completion_lesson2(self):
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = tk.Frame(self.master, bg=self.bg_color)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(self.current_frame, text="Congratulations on completing Lesson 2!", 
                 bg=self.bg_color, fg=self.text_color, font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(self.current_frame, text="You've learned the basics of holding a French horn.", 
                 bg=self.bg_color, fg=self.text_color, font=("Arial", 12)).pack()
        
        tk.Button(self.current_frame, text="Next Lesson", command=self.start_lesson3,
                  bg=self.button_bg, fg=self.button_fg, font=("Arial", 12)).pack(pady=20)
        tk.Button(self.current_frame, text="Back to Menu", command=self.show_menu,
                  bg=self.button_bg, fg=self.button_fg, font=("Arial", 12)).pack(pady=20)
    def start_lesson3(self):
        self.play_video("Lesson 3")
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = tk.Frame(self.master, bg=self.bg_color)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(self.current_frame, text="Lesson 3: Playing a C on the French Horn",
                 bg=self.bg_color, fg=self.text_color, font=("Arial", 14, "bold")).pack(pady=10)
        
        instructions = [
            "1. Form the embouchure as learned in Lesson 1",
            "2. Hold the French Horn as practiced in Lesson 2",
            "3. Take a deep breath",
            "4. Blow steadily into the mouthpiece, aiming for a C note (261.6 Hz)",
            "5. Use the tuner below to check if you're hitting the right note"
        ]
        
        for instruction in instructions:
            tk.Label(self.current_frame, text=instruction, bg=self.bg_color, fg=self.text_color, 
                    font=("Arial", 12)).pack(anchor='w', padx=10, pady=5)
        
        self.tuner_label = tk.Label(self.current_frame, text="Tuner: Not playing", 
                                    bg=self.bg_color, fg=self.text_color, font=("Arial", 14))
        self.tuner_label.pack(pady=20)
        
        tk.Button(self.current_frame, text="Start Tuner", command=self.start_tuner,
                  bg=self.button_bg, fg=self.button_fg, font=("Arial", 12)).pack(pady=10)
        
        tk.Button(self.current_frame, text="Stop Tuner", command=self.stop_tuner,
                  bg=self.button_bg, fg=self.button_fg, font=("Arial", 12)).pack(pady=10)
        
        tk.Button(self.current_frame, text="I've practiced playing C", command=self.check_practice_lesson3,
                  bg=self.button_bg, fg=self.button_fg, font=("Arial", 12)).pack(pady=20)
        
        self.attempts = 0
        self.is_tuner_running = False
    
    def start_tuner(self):
        self.is_tuner_running = True
        self.update_tuner()
    
    def stop_tuner(self):
        self.is_tuner_running = False
        self.tuner_label.config(text="Tuner: Not playing")
    
    def update_tuner(self):
        if self.is_tuner_running:
            data = np.frombuffer(self.stream.read(self.CHUNK), dtype=np.float32)
            fft = np.fft.fft(data)
            frequencies = np.fft.fftfreq(len(fft), 1.0/self.RATE)
            peak_frequency = frequencies[np.argmax(np.abs(fft))]
            
            if 250 < peak_frequency < 270:  # Allow some wiggle room around 261.6 Hz
                self.tuner_label.config(text="Tuner: C detected! Great job!", fg="#00FF00")
            else:
                self.tuner_label.config(text=f"Tuner: Not C (detected {peak_frequency:.2f} Hz)", fg=self.text_color)
            
            self.master.after(100, self.update_tuner)
    
    def check_practice_lesson3(self):
        self.attempts += 1
        if self.attempts < 3:
            messagebox.showinfo("Keep Practicing", "Great effort! Keep trying to hit that C note.")
        else:
            messagebox.showinfo("Well Done!", "Excellent! You've completed the third lesson on playing C.")
            self.current_lesson = 4  # Progress to next lesson (if implemented)
            self.show_completion_lesson3()
    
    
    def show_completion_lesson3(self):
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = tk.Frame(self.master, bg=self.bg_color)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(self.current_frame, text="Congratulations on completing Lesson 3!", 
                 bg=self.bg_color, fg=self.text_color, font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(self.current_frame, text="You've learned to play a C note on the French horn.", 
                 bg=self.bg_color, fg=self.text_color, font=("Arial", 12)).pack()
        tk.Label(self.current_frame, text="You've completed all available lessons!", 
                 bg=self.bg_color, fg=self.text_color, font=("Arial", 12)).pack(pady=10)
        
        self.all_lessons_completed = True  # Mark all lessons as completed
        
        tk.Button(self.current_frame, text="Back to Menu", command=self.show_menu,
                  bg=self.button_bg, fg=self.button_fg, font=("Arial", 12)).pack(pady=20)

    def show_advanced_tuner(self):
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = tk.Frame(self.master, bg=self.bg_color)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(self.current_frame, text="Advanced Tuner", 
                 bg=self.bg_color, fg=self.text_color, font=("Arial", 18, "bold")).pack(pady=20)
        
        self.tuner_label = tk.Label(self.current_frame, text="Play a note...", 
                                    bg=self.bg_color, fg=self.text_color, font=("Arial", 14))
        self.tuner_label.pack(pady=20)
        
        tk.Button(self.current_frame, text="Start Tuner", command=self.start_advanced_tuner,
                  bg=self.button_bg, fg=self.button_fg, font=("Arial", 12)).pack(pady=10)
        
        tk.Button(self.current_frame, text="Stop Tuner", command=self.stop_advanced_tuner,
                  bg=self.button_bg, fg=self.button_fg, font=("Arial", 12)).pack(pady=10)
        
        tk.Button(self.current_frame, text="Back to Menu", command=self.show_menu,
                  bg=self.button_bg, fg=self.button_fg, font=("Arial", 12)).pack(pady=20)
        
        self.is_tuner_running = False

    def start_advanced_tuner(self):
        self.is_tuner_running = True
        self.update_advanced_tuner()

    def stop_advanced_tuner(self):
        self.is_tuner_running = False
        self.tuner_label.config(text="Play a note...")

    def update_advanced_tuner(self):
        if self.is_tuner_running:
            data = np.frombuffer(self.stream.read(self.CHUNK), dtype=np.float32)
            fft = np.fft.fft(data)
            frequencies = np.fft.fftfreq(len(fft), 1.0/self.RATE)
            magnitude = np.abs(fft)
            
            # Check if there's a clear peak
            if np.max(magnitude) > 10 * np.mean(magnitude):  # Adjust this threshold as needed
                peak_frequency = frequencies[np.argmax(magnitude)]
                note = self.frequency_to_note(peak_frequency)
                self.tuner_label.config(text=f"Detected Note: {note} ({peak_frequency:.2f} Hz)")
            else:
                self.tuner_label.config(text="No clear note detected. Please play louder.")
            
            self.master.after(100, self.update_advanced_tuner)

    def frequency_to_note(self, frequency):
        # A4 = 440 Hz
        note_names = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
        a4_freq = 440
        if frequency <= 0:
            return "Invalid frequency"
        try:
            half_steps = round(12 * np.log2(frequency / a4_freq))
            octave = 4 + half_steps // 12
            note_index = half_steps % 12
            return f"{note_names[note_index]}{octave}"
        except ValueError:
            return "Error in note calculation"

    # ... (rest of the code remains the same) ...
if __name__ == "__main__":
    root = tk.Tk()
    app = FrenchHornApp(root)
    root.mainloop()