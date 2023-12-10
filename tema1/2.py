import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd

class PlotApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pulse Graphs")

        self.file_path = 'tema1/data.csv'

        self.data = pd.read_csv(self.file_path)

        self.plot_windows = []

        self.create_widgets()

    def create_widgets(self):
        btn_all_values = ttk.Button(self.master, text="Show all values", command=self.plot_all_columns)
        btn_all_values.pack(pady=10)

        btn_first_x_values = ttk.Button(self.master, text="Show first values", command=lambda: self.plot_first_x_values(9))
        btn_first_x_values.pack(pady=10)

        btn_last_y_values = ttk.Button(self.master, text="Show last values", command=lambda: self.plot_last_y_values(16))
        btn_last_y_values.pack(pady=10)

        btn_reset = ttk.Button(self.master, text="Reset", command=self.reset_plots)
        btn_reset.pack(pady=10)

    def plot_all_columns(self):
        self.close_plot_windows()  
        plt.figure(figsize=(6, 4))
        for col in self.data.columns:
            plt.plot(self.data.index, self.data[col], label=col)
        plt.legend()
        plt.title('Toate Coloanele')
        self.show_plot()

    def plot_first_x_values(self, x):
        self.close_plot_windows()  
        plt.figure(figsize=(6, 4))
        for col in self.data.columns:
            plt.plot(self.data.index[:x], self.data[col][:x], label=col)
        plt.legend()
        plt.title(f'Primele {x} Valori')
        self.show_plot()

    def plot_last_y_values(self, y):
        self.close_plot_windows() 
        plt.figure(figsize=(6, 4))
        for col in ['Durata', 'Puls']:  
            plt.plot(self.data.index[-y:], self.data[col][-y:], label=col)
        plt.legend()
        plt.title(f'Ultimele {y} Valori pentru Durata și Puls')
        self.show_plot()

    def reset_plots(self):
        self.close_plot_windows()  

    def show_plot(self):
        canvas = FigureCanvasTkAgg(plt.gcf(), master=self.master)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.plot_windows.append(canvas.get_tk_widget())

    def close_plot_windows(self):
        for window in self.plot_windows:
            window.destroy()
        self.plot_windows = []

if __name__ == "__main__":
    root = tk.Tk()
    app = PlotApp(root)
    root.mainloop()