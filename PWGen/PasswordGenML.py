import customtkinter as ctk
import random
import string
from tkinter import messagebox

translations = {
    "es": {
        "title": "Generador de Contraseñas", "length": "Longitud:",
        "generate": "🎲 Generar", "copy": "📋 Copiar",
        "copied": "¡Contraseña copiada!", "copied_title": "Copiado",
        "warning": "Selecciona al menos un tipo de carácter.", "warning_title": "Advertencia",
        "dark_mode": "Modo Oscuro", "letters": "Letras (a-z, A-Z)",
        "numbers": "Números (0-9)", "symbols": "Símbolos (!@#...)"
    },
    "en": {
        "title": "Password Generator", "length": "Length:",
        "generate": "🎲 Generate", "copy": "📋 Copy",
        "copied": "Password copied!", "copied_title": "Copied",
        "warning": "Select at least one character type.", "warning_title": "Warning",
        "dark_mode": "Dark Mode", "letters": "Letters (a-z, A-Z)",
        "numbers": "Numbers (0-9)", "symbols": "Symbols (!@#...)"
    }
}

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app, lang = ctk.CTk(), "es"
app.geometry("430x460")
app.resizable(False, False)

password_var = ctk.StringVar()
length_var = ctk.IntVar(value=12)
dark_mode_var = ctk.BooleanVar(value=False)
types = {
    "letters": (ctk.BooleanVar(value=True), string.ascii_letters),
    "numbers": (ctk.BooleanVar(value=True), string.digits),
    "symbols": (ctk.BooleanVar(value=True), string.punctuation)
}


def generate_password():
    pool = ''.join(chars for var, chars in types.values() if var.get())
    if not pool:
        t = translations[lang]
        return messagebox.showwarning(t["warning_title"], t["warning"])
    password_var.set(''.join(random.choice(pool)
                     for _ in range(length_var.get())))


def copy_password():
    if password_var.get():
        app.clipboard_clear()
        app.clipboard_append(password_var.get())
        t = translations[lang]
        messagebox.showinfo(t["copied_title"], t["copied"])


def toggle_theme():
    ctk.set_appearance_mode("dark" if dark_mode_var.get() else "light")


def toggle_lang():
    global lang
    lang = "en" if lang == "es" else "es"
    update_texts()


widgets, checkboxes = {}, {}

widgets["title"] = ctk.CTkLabel(app, font=("Helvetica", 20, "bold"))
widgets["title"].pack(pady=20)

frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(padx=20, pady=10, fill="both", expand=True)

widgets["length"] = ctk.CTkLabel(frame, font=("Helvetica", 13))
widgets["length"].pack(pady=(15, 5))
ctk.CTkSlider(frame, from_=4, to=64, variable=length_var,
              number_of_steps=60).pack()
ctk.CTkLabel(frame, textvariable=length_var).pack(pady=5)

for key in types:
    checkboxes[key] = ctk.CTkCheckBox(frame, variable=types[key][0])
    checkboxes[key].pack(anchor="w", padx=30, pady=2)

widgets["generate"] = ctk.CTkButton(frame, command=generate_password)
widgets["generate"].pack(pady=10)

ctk.CTkEntry(frame, textvariable=password_var, font=(
    "Consolas", 14), width=260).pack(pady=8)

widgets["copy"] = ctk.CTkButton(frame, command=copy_password)
widgets["copy"].pack(pady=5)

widgets["dark_mode"] = ctk.CTkSwitch(
    frame, variable=dark_mode_var, command=toggle_theme)
widgets["dark_mode"].pack(pady=10)

ctk.CTkButton(app, text="🌐", width=30, command=toggle_lang).place(x=10, y=10)


def update_texts():
    t = translations[lang]
    app.title(t["title"])
    widgets["title"].configure(text="🔐 " + t["title"])
    widgets["length"].configure(text=t["length"])
    widgets["generate"].configure(text=t["generate"])
    widgets["copy"].configure(text=t["copy"])
    widgets["dark_mode"].configure(text=t["dark_mode"])
    checkboxes["letters"].configure(text=t["letters"])
    checkboxes["numbers"].configure(text=t["numbers"])
    checkboxes["symbols"].configure(text=t["symbols"])


update_texts()
app.mainloop()
