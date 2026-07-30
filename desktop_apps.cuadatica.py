import math
import os
from tkinter import *
from tkinter import messagebox

# Intentar importar Pillow para asegurar compatibilidad universal con PNG/JPG
try:
    from PIL import Image, ImageTk

    USAR_PIL = True
except ImportError:
    USAR_PIL = False


# ------------------------------------------
# Funciones de la app
# ------------------------------------------
def salir():
    messagebox.showinfo(
        "Resolutor 1.0", "Hizo clic en el botón Salir. ¡Hasta luego!"
    )
    ventana_principal.destroy()


def borrar():
    messagebox.showinfo(
        "Resolutor 1.0", "Los datos de la ecuación serán borrados"
    )
    a.set("")
    b.set("")
    c.set("")
    t_resultados.delete("1.0", END)


def resolver():
    # 1. Validar que no dejen campos vacíos
    if entry_a.get() == "" or entry_b.get() == "" or entry_c.get() == "":
        messagebox.showwarning(
            "Advertencia", "Por favor ingrese todos los coeficientes (a, b, c)."
        )
        return

    # 2. Intentar convertir a números
    try:
        val_a = float(entry_a.get())
        val_b = float(entry_b.get())
        val_c = float(entry_c.get())
    except ValueError:
        messagebox.showerror(
            "Error de entrada", "Por favor ingrese únicamente números válidos."
        )
        return

    # 3. La variable 'a' no puede ser 0 en una ecuación cuadrática
    if val_a == 0:
        messagebox.showerror(
            "Error", "El valor de 'a' no puede ser 0 en una ecuación cuadrática."
        )
        return

    # 4. Calcular el discriminante (b^2 - 4ac)
    d = (val_b**2) - (4 * val_a * val_c)

    # Limpiar caja de resultados antes de escribir
    t_resultados.delete("1.0", END)

    # 5. Mostrar resultados según el valor del discriminante
    if d > 0:
        x1 = (-val_b + math.sqrt(d)) / (2 * val_a)
        x2 = (-val_b - math.sqrt(d)) / (2 * val_a)
        t_resultados.insert(
            INSERT,
            f"Ecuación: {val_a}x² + {val_b}x + {val_c} = 0\n\n"
            f"Dos soluciones reales:\n"
            f"  • x1 = {round(x1, 2)}\n"
            f"  • x2 = {round(x2, 2)}\n",
        )
    elif d == 0:
        x = -val_b / (2 * val_a)
        t_resultados.insert(
            INSERT,
            f"Ecuación: {val_a}x² + {val_b}x + {val_c} = 0\n\n"
            f"Una solución real única:\n"
            f"  • x = {round(x, 2)}\n",
        )
    else:
        # Raíces complejas (imaginarias)
        parte_real = -val_b / (2 * val_a)
        parte_imag = math.sqrt(-d) / (2 * val_a)
        t_resultados.insert(
            INSERT,
            f"Ecuación: {val_a}x² + {val_b}x + {val_c} = 0\n\n"
            f"Soluciones complejas (imaginarias):\n"
            f"  • x1 = {round(parte_real, 2)} + {round(abs(parte_imag), 2)}i\n"
            f"  • x2 = {round(parte_real, 2)} - {round(abs(parte_imag), 2)}i\n",
        )


# ------------------------------------------
# Configuración ventana principal
# ------------------------------------------
ventana_principal = Tk()
ventana_principal.title("Sistemas Guanentá - Ecuación Cuadrática")
ventana_principal.geometry("500x520")
ventana_principal.config(bg="#1e1e1e")  # Fondo modo oscuro profundo
ventana_principal.resizable(0, 0)

# Cargar icono (.ico) de la ventana si existe
ruta_icono = "icono.ico"
if os.path.exists(ruta_icono):
    try:
        ventana_principal.iconbitmap(ruta_icono)
    except Exception as e:
        print(f"No se pudo cargar el icono: {e}")

# ------------------------------------------
# Variables globales de la app
# ------------------------------------------
a = StringVar()
b = StringVar()
c = StringVar()

# ------------------------------------------
# Frame 1: Entrada de datos
# ------------------------------------------
frame_entrada = Frame(
    ventana_principal, bg="#2d2d2d", bd=1, relief="solid", width=480, height=240
)
frame_entrada.place(x=10, y=10)

# Título de la app
titulo = Label(
    frame_entrada,
    text="Ecuación: ax² + bx + c = 0",
    bg="#2d2d2d",
    fg="#60a5fa",
    font=("Segoe UI", 15, "bold"),
)
titulo.place(x=100, y=15)

aviso = Label(
    frame_entrada,
    text="Ingrese los coeficientes a, b y c:",
    bg="#2d2d2d",
    fg="#a1a1aa",
    font=("Segoe UI", 10),
)
aviso.place(x=120, y=50)

# Entrada Coeficiente A
lb_a = Label(
    frame_entrada,
    text="a =",
    bg="#2d2d2d",
    fg="#ffffff",
    font=("Segoe UI", 12, "bold"),
)
lb_a.place(x=60, y=90)

entry_a = Entry(
    frame_entrada,
    textvariable=a,
    bg="#3f3f46",
    fg="#ffffff",
    insertbackground="white",
    font=("Segoe UI", 12),
    bd=1,
    relief="solid",
)
entry_a.focus_set()
entry_a.place(x=110, y=90, width=120, height=30)

# Entrada Coeficiente B
lb_b = Label(
    frame_entrada,
    text="b =",
    bg="#2d2d2d",
    fg="#ffffff",
    font=("Segoe UI", 12, "bold"),
)
lb_b.place(x=60, y=135)

entry_b = Entry(
    frame_entrada,
    textvariable=b,
    bg="#3f3f46",
    fg="#ffffff",
    insertbackground="white",
    font=("Segoe UI", 12),
    bd=1,
    relief="solid",
)
entry_b.place(x=110, y=135, width=120, height=30)

# Entrada Coeficiente C
lb_c = Label(
    frame_entrada,
    text="c =",
    bg="#2d2d2d",
    fg="#ffffff",
    font=("Segoe UI", 12, "bold"),
)
lb_c.place(x=60, y=180)

entry_c = Entry(
    frame_entrada,
    textvariable=c,
    bg="#3f3f46",
    fg="#ffffff",
    insertbackground="white",
    font=("Segoe UI", 12),
    bd=1,
    relief="solid",
)
entry_c.place(x=110, y=180, width=120, height=30)

# ------------------------------------------
# Cargar e Integrar la Imagen "screen.png"
# ------------------------------------------
ruta_imagen = "screen.png"

if os.path.exists(ruta_imagen):
    try:
        if USAR_PIL:
            img_obj = Image.open(ruta_imagen)
            img_obj = img_obj.resize(
                (180, 120)
            )  # Redimensionar para encajar perfectamente
            img_logo = ImageTk.PhotoImage(img_obj)
        else:
            img_logo = PhotoImage(file=ruta_imagen)

        # Mostrar la imagen a la derecha de las entradas de texto
        lb_imagen = Label(frame_entrada, image=img_logo, bg="#2d2d2d")
        lb_imagen.place(x=260, y=90)
    except Exception as e:
        print(f"Error cargando la imagen: {e}")

# ------------------------------------------
# Frame 2: Operaciones (Botones)
# ------------------------------------------
frame_operaciones = Frame(
    ventana_principal, bg="#2d2d2d", bd=1, relief="solid", width=480, height=90
)
frame_operaciones.place(x=10, y=260)

# Botón para Resolver
bt_resolver = Button(
    frame_operaciones,
    text="Resolver",
    command=resolver,
    bg="#2563eb",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    bd=0,
    cursor="hand2",
    activebackground="#1d4ed8",
    activeforeground="white",
)
bt_resolver.place(x=45, y=30, width=100, height=32)

# Botón para Borrar
bt_borrar = Button(
    frame_operaciones,
    text="Borrar",
    command=borrar,
    bg="#4b5563",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    bd=0,
    cursor="hand2",
    activebackground="#374151",
    activeforeground="white",
)
bt_borrar.place(x=180, y=30, width=100, height=32)

# Botón para Salir
bt_salir = Button(
    frame_operaciones,
    text="Salir",
    command=salir,
    bg="#dc2626",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    bd=0,
    cursor="hand2",
    activebackground="#b91c1c",
    activeforeground="white",
)
bt_salir.place(x=315, y=30, width=100, height=32)

# ------------------------------------------
# Frame 3: Resultados
# ------------------------------------------
frame_resultados = Frame(
    ventana_principal, bg="#2d2d2d", bd=1, relief="solid", width=480, height=140
)
frame_resultados.place(x=10, y=360)

# Área de texto para mostrar las raíces x1 y x2
t_resultados = Text(
    frame_resultados,
    bg="#18181b",
    fg="#38bdf8",
    insertbackground="white",
    font=("Consolas", 11),
    bd=0,
    padx=10,
    pady=10,
)
t_resultados.place(x=10, y=10, width=460, height=120)

# Bucle principal
ventana_principal.mainloop()