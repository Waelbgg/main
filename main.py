import tkinter as tk
import os
from PIL import Image, ImageTk

# ---------- RUTA BASE ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------- Medidas ----------
FINESTRA_X = 1024
FINESTRA_Y = 768
CANVAS_X = FINESTRA_X // 2
CANVAS_Y = FINESTRA_Y // 2

# ---------- Variables de juego ----------
escena = 1
diners = 0
reputacio = 0
risc = 0
influencia = 0

# ---------- Textos y decisiones ----------
textos = {
    1: {"text": "Haider, 17 anys, regenta un petit kebab.\nLa seva salsa blanca és famosa al barri.\nMassa famosa…\n\nOpcions:\n- investigar\n- ignorar\n- parlar amb clients\n- tancar el local\n- trucar a un amic"},
    2: {"text": "Homes amb cotxes negres observen el local.\nHaider et diu que la salsa no és només menjar.\n\nOpcions:\n- acceptar\n- rebutjar\n- amagar proves\n- buscar informació\n- fugir del barri"},
    3: {"text": "El negoci explota.\nParadisos fiscals, cotxes de luxe, mansions.\n\nOpcions:\n- invertir més diners\n- gastar en luxe\n- traicionar aliats\n- donar part a la caritat\n- retirar-se del negoci"},
    4: {"text": "Redada policial.\nEt detenen amb Haider.\nA la presó, la policia et pressiona.\n\nOpcions:\n- xivar\n- callar\n- manipular\n- amagar evidències\n- buscar un còmplice"},
    5: {"text": "Descobreixes un magatzem secret darrere el kebab.\nHi ha caixes tancades amb símbols estranys.\n\nOpcions:\n- obrir caixes\n- avisar haider\n- fer fotos\n- marxar\n- trucar policia"},
    6: {"text": "Reunió nocturna en un aparcament.\nUn home elegant ofereix expandir el negoci.\n\nOpcions:\n- acceptar tracte\n- rebutjar\n- negociar\n- espiar conversa\n- gravar reunió"},
    7: {"text": "El negoci creix ràpidament.\nDiners fàcils, però el risc augmenta.\n\nOpcions:\n- invertir diners\n- blanquejar diners\n- comprar silenci\n- retirar-se\n- confiar en haider"},
    8: {"text": "Un periodista sap massa coses.\nVol publicar un article.\n\nOpcions:\n- subornar\n- amenaçar\n- explicar veritat\n- ignorar\n- culpar haider"},
    9: {"text": "La policia prepara una redada final.\nTot està a punt d’explotar.\n\nOpcions:\n- fugir\n- xivar\n- callar\n- destruir proves\n- assumir culpa"}
}

finals = {
    "chivato": "Has parlat. Haider cau.\nFINAL: Chivato",
    "heroe": "No has dit res i tot surt bé.\nFINAL: Héroe",
    "mercenario": "Has traït a tots.\nFINAL: Mercenario",
    "presoner": "Tot ha anat malament.\nFINAL: Presoner",
    "imperio": "Domineu el barri.\nFINAL: Imperi criminal",
    "riqueza": "Vius còmodament sense problemes.\nFINAL: Riquesa silenciosa"
}

# ---------- Finestra ----------
finestra = tk.Tk()
finestra.title("HAIDER – El secret de la salsa blanca")
finestra.geometry(f"{FINESTRA_X}x{FINESTRA_Y}")
finestra.resizable(False, False)

# ---------- Canvas ----------
canvas = tk.Canvas(finestra, width=CANVAS_X, height=CANVAS_Y, bg="black")
canvas.place(x=(FINESTRA_X - CANVAS_X)//2, y=80)

# ---------- Cargar imágenes ----------
def cargar_imagen(filename):
    ruta = os.path.join(BASE_DIR, "img", filename)
    imagen = Image.open(ruta)
    imagen = imagen.resize((CANVAS_X, CANVAS_Y), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(imagen)

imatges = {
    1: cargar_imagen("escena1_ke" \
    "bab.png"),
    2: cargar_imagen("escena2_kebab.png"),
    3: cargar_imagen("escena3_lujo.png"),
    4: cargar_imagen("escena4_prision.png"),
    5: cargar_imagen("escena5_magatzem.png"),
    6: cargar_imagen("escena6_reunio.png"),
    7: cargar_imagen("escena7_expansio.png"),
    8: cargar_imagen("escena8_periodista.png"),
    9: cargar_imagen("escena9_redada.png")
}

img_canvas = canvas.create_image(CANVAS_X//2, CANVAS_Y//2, image=imatges[1])

# ---------- Labels ----------
label_text = tk.Label(finestra, text=textos[1]["text"], font=("Arial", 14), wraplength=900, justify="left")
label_text.place(x=60, y=CANVAS_Y + 100)

label_accio = tk.Label(finestra, text="Acció:", font=("Arial", 16))
label_accio.place(x=60, y=FINESTRA_Y - 60)

entrada = tk.Entry(finestra, font=("Arial", 14), width=25)
entrada.place(x=140, y=FINESTRA_Y - 60)

barra_estado = tk.Label(finestra, text="", font=("Arial", 12), bg="lightgrey")
barra_estado.place(x=0, y=0, width=FINESTRA_X)

def actualitza_barra():
    barra_estado.config(text=f"Diners: {diners} | Reputació: {reputacio} | Risc: {risc} | Influència: {influencia}")

# ---------- Funciones ----------
def canvia_escena(nova):
    global escena
    escena = nova
    canvas.itemconfig(img_canvas, image=imatges[nova])
    label_text.config(text=textos[nova]["text"])
    entrada.delete(0, tk.END)
    actualitza_barra()

def acaba(final):
    label_text.config(text=finals[final])
    entrada.delete(0, tk.END)
    actualitza_barra()

# ---------- Lógica ----------
def capta_text(event=None):
    global escena, diners, reputacio, risc, influencia
    accio = entrada.get().lower().strip()

    if escena == 1:
        if accio == "investigar":
            reputacio +=1; risc +=1; influencia +=1
            canvia_escena(2)
        elif accio == "ignorar":
            risc -=1
            canvia_escena(4)
        elif accio == "parlar amb clients":
            diners +=1; reputacio +=2
            canvia_escena(2)
        elif accio == "tancar el local":
            risc -=2
            acaba("riqueza")
        elif accio == "trucar a un amic":
            influencia +=1
            canvia_escena(2)

    elif escena == 2:
        if accio == "acceptar":
            diners +=2; risc +=2
            canvia_escena(3)
        elif accio == "rebutjar":
            risc -=1
            canvia_escena(4)
        elif accio == "amagar proves":
            risc -=1; influencia +=1
            canvia_escena(3)
        elif accio == "buscar informació":
            reputacio +=1
            canvia_escena(4)
        elif accio == "fugir del barri":
            risc -=2
            acaba("riqueza")

    elif escena == 3:
        canvia_escena(4)

    elif escena == 4:
        if accio == "xivar":
            acaba("chivato")
        else:
            canvia_escena(5)

    elif escena == 5:
        canvia_escena(6)

    elif escena == 6:
        canvia_escena(7)

    elif escena == 7:
        canvia_escena(8)

    elif escena == 8:
        canvia_escena(9)

    elif escena == 9:
        if accio == "fugir":
            acaba("riqueza")
        elif accio == "xivar":
            acaba("chivato")
        elif accio == "callar":
            acaba("heroe")
        elif accio == "destruir proves":
            acaba("heroe")
        elif accio == "assumir culpa":
            acaba("presoner")

entrada.bind("<Return>", capta_text)
actualitza_barra()
finestra.mainloop()