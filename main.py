import tkinter as tk
from tkinter import messagebox
import random
import time


class TypingSpeedTest:
    def __init__(self, master):
        self.master = master
        master.title("Typing Speed Test")
        master.geometry("600x500")
        master.configure(bg='#f0f0f0')

        # Sample paragraphs for typing test
        self.paragraphs = [
            "The quick brown fox jumps over the lazy dog. This classic pangram contains every letter of the English alphabet.",
            "Programming is not about what you know, it's about what you can figure out when you don't know something.",
            "Success is not final, failure is not fatal: it is the courage to continue that counts.",
            "In the world of technology, learning never stops. Every day brings new challenges and opportunities.",
            "Artificial intelligence is transforming the way we live, work, and interact with the world around us."
        ]

        self.setup_ui()
        self.reset_test()

    def setup_ui(self):
        # Sample Text Display
        self.sample_text_label = tk.Label(
            self.master,
            text="",
            wraplength=500,
            font=('Courier', 12),
            bg='#f0f0f0',
            justify=tk.LEFT
        )
        self.sample_text_label.pack(pady=10)

        # Entry Field
        self.entry = tk.Text(
            self.master,
            height=6,
            width=70,
            font=('Courier', 12)
        )
        self.entry.pack(pady=10)
        self.entry.bind('<KeyRelease>', self.start_test)

        # Results Frame
        self.results_frame = tk.Frame(self.master, bg='#f0f0f0')
        self.results_frame.pack(pady=10)

        # Speed Label
        self.speed_label = tk.Label(
            self.results_frame,
            text="WPM: 0",
            font=('Arial', 12, 'bold'),
            bg='#f0f0f0'
        )
        self.speed_label.grid(row=0, column=0, padx=10)

        # Accuracy Label
        self.accuracy_label = tk.Label(
            self.results_frame,
            text="Accuracy: 0%",
            font=('Arial', 12, 'bold'),
            bg='#f0f0f0'
        )
        self.accuracy_label.grid(row=0, column=1, padx=10)

        # Reset Button
        self.reset_button = tk.Button(
            self.master,
            text="Reset Test",
            command=self.reset_test,
            font=('Arial', 10)
        )
        self.reset_button.pack(pady=10)

    def reset_test(self):
        # Choose a random paragraph
        self.current_text = random.choice(self.paragraphs)
        self.sample_text_label.config(text=self.current_text)

        # Reset entry and results
        self.entry.delete(1.0, tk.END)
        self.speed_label.config(text="WPM: 0")
        self.accuracy_label.config(text="Accuracy: 0%")

        # Reset test variables
        self.start_time = None
        self.test_started = False

    def start_test(self, event):
        if not self.test_started:
            self.start_time = time.time()
            self.test_started = True

        self.calculate_results()

    def calculate_results(self):
        if not self.test_started:
            return

        typed_text = self.entry.get(1.0, tk.END).strip()

        # Calculate time elapsed
        time_elapsed = max(time.time() - self.start_time, 1)  # Prevent division by zero

        # Calculate Words Per Minute (WPM)
        words = typed_text.split()
        wpm = int((len(words) / time_elapsed) * 60)

        # Calculate Accuracy
        correct_chars = sum(1 for a, b in zip(typed_text, self.current_text) if a == b)
        accuracy = (correct_chars / len(self.current_text)) * 100 if self.current_text else 0

        # Update labels
        self.speed_label.config(text=f"WPM: {wpm}")
        self.accuracy_label.config(text=f"Accuracy: {accuracy:.2f}%")


def main():
    root = tk.Tk()
    typing_test = TypingSpeedTest(root)
    root.mainloop()


if __name__ == "__main__":
    main()