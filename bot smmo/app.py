import tkinter as tk
import subprocess
import threading

root = tk.Tk()
root.title("SIMPLEMMO Bot")
process = None

def stop_bot():
    global process

    if process and process.poll() is None:
            print("Proces już jest uruchomiony.")
    return

    try:
        process = subprocess.Popen(["python", filepath], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, errors = process.communicate()
        exit_code = process.returncode

        
        file_window = tk.Toplevel(root)
        file_window.title(filepath)
        text_area = tk.Text(file_window)
        text_area.pack(fill="both", expand=True)
        
        
        if exit_code == 0:
            text_area.insert("1.0", output)
        else:
            text_area.insert("1.0", errors)
    except FileNotFoundError:
        print("Plik nie został odnaleziony.")


    if process and process.poll() is None:
        process.terminate()
        print("Proces zatrzymany.")
    else:
        print("Brak działającego procesu.")

def open_bot(filepath):
    try:
        result = subprocess.run(["python", filepath], capture_output=True, text=True)
        output = result.stdout
        file_window = tk.Toplevel(root)
        file_window.title(filepath)
        text_area = tk.Text(file_window)
        text_area.pack(fill="both", expand=True)
        text_area.insert("1.0", output)
    except FileNotFoundError:
        print("Plik nie został odnaleziony.")

def start_bot():
    file_path = "C:/Users/fabia/Desktop/bot smmo/bot.py"

    # Uruchamianie zadania w tle za pomocą wątku
    thread = threading.Thread(target=open_bot, args=(file_path,))
    thread.start()

canvas = tk.Canvas(root, height=700, width=700, bg='#263D42')
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

start_button = tk.Button(root, text="Start", padx=10, pady=5, fg="white", bg="#253D42", command=start_bot)
start_button.pack()

Stop_button = tk.Button(root, text="Stop", padx=10, pady=5, fg="white", bg="#253D42", command=stop_bot)
Stop_button.pack()


quests_button = tk.Button(root, text="Quests", padx=10, pady=5, fg="white", bg="#253D42")
quests_button.pack()

battles_button = tk.Button(root, text="Battles", padx=10, pady=5, fg="white", bg="#253D42")
battles_button.pack()

root.mainloop()