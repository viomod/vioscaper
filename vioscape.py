# pyinstaller --onefile --icon=violet.ico --name=vioscaper.exe vioscape.py

import os
import pyperclip

vioscape_dict = {
    "a": "vx99",
    "b": "v6xz",
    "c": "zv8x",
    "d": "vv92",
    "e": "0x9v",
    "f": "00vx",
    "g": "zx0v",
    "h": "v9x0",
    "i": "x9v0",
    "j": "9vx0",
    "k": "v0x9",
    "l": "x90v",
    "m": "9xv0",
    "n": "v09x",
    "o": "x0v9",
    "p": "90vx",
    "q": "v900",
    "r": "59v0",
    "s": "9vx5",
    "t": "vtx9",
    "u": "x95v",
    "v": "9vx2",
    "w": "v59x",
    "x": "x3v9",
    "y": "96vx",
    "z": "v9x5",

    "0": "azst",
    "1": "xxas",
    "2": "scox",
    "3": "azsx",
    "4": "astr",
    "5": "alzx",
    "6": "rome",
    "7": "zaos",
    "8": "xxv0",
    "9": "oovj",

    " ": "spao",
}

started = False

def main():
    os.system('title Vioscaper')
    global started
    if started == False:
        print("starting program")
        started = True
    else:
        print("restarting program")
    unvioscape_dict = {v: k for k, v in vioscape_dict.items()}

    which = input("would you like to vioscape or unvioscape? (un, v or exit): ").strip().lower()

    if which == "v":
        text = input("enter text to vioscape: ").lower()
        
        vioscaped_text = "".join(vioscape_dict.get(char, char) for char in text)

        question = input("would you like to see your vioscaped text or log it to a file? (txt or see): ").strip().lower()

        if question == "txt":
            with open("vioscape.txt", "w") as f:
                f.write(vioscaped_text)
            print("text saved to vioscape.txt")
            open_file = input("would you like to open the file? (y/n): ").strip().lower()
            if open_file == "y":
                with open("vioscape.txt", "r") as f:
                    os.system("notepad vioscape.txt")
            elif open_file != "n":
                print("invalid option")
                main()
        elif question == "see":
            print("ur vioscaped text is:", vioscaped_text)
        else:
            print("invalid input")
    elif which == "exit":
        exit()
    elif which == "un":
        text = input("enter text to unvioscape: ").strip()
        
        decoded_text = ""
        i = 0
        while i < len(text):
            chunk = text[i:i+4]
            if chunk in unvioscape_dict:
                decoded_text += unvioscape_dict[chunk]
                i += 4
            else:
                decoded_text += chunk[0] 
                i += 1

        print("ur unvioscaped text is:", decoded_text)
        
    else:
        print("invalid option")
    if input("would you like to copy this to clipboard? (y/n): ").strip().lower() == "y":
        pyperclip.copy(decoded_text if which == "un" else vioscaped_text)
        print("copied to clipboard")
    main()

main()
