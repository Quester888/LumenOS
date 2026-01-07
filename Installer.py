import os
import sys
import platform
import tkinter as tk

basedir = os.getcwd()

accessdev = ["Windows", "Linux"]
filetointdir = ["L;", "Drivers", "System", "Lumeninate"]

print(f"BaseDir Set as {basedir}")

root = tk.Tk()
root.title("Install LumenOS")
root.geometry("450x450")

def installs1():
    delfile = []
    for file in os.listdir():
        if file.lower().endswith(".txt"):
            print(file)
            delfile.append(file)
        else:
            continue

    for widget in root.winfo_children():
        widget.destroy()

    welt = tk.Label(root, text=f"The following files will be eradicated: {delfile} | {len(delfile)} File(s) will be eradicated.")
    welt.pack(pady=10)

if platform.system() in accessdev:
    print("Install allowed")
    welt = tk.Label(root, text="Welcome to the LumenOS Installer.")
    welt.pack(pady=10)
    welt2 = tk.Label(root, text=f"Ensure the installer is in the desired installation folder. This folder must be empty, as all contents will be erased during installation.\n Current location: {basedir}" )
    welt2.pack(pady=10)

    welt3 = tk.Button(root, text="Install.", command=installs1)
    welt3.pack(pady=10)

else:
    print("Install disallowed")
    welt = tk.Label(root, text="Your device is incompatible with LumenOS, THe installer will close shortly.")
    welt.pack(pady=10)

    root.after(3000, root.destroy)  # closes after 3 seconds
