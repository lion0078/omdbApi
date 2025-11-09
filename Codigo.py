from tkinter import *
from tkinter import ttk
import requests

def buscar_pelicula():
    titulo = entrytitulo.get()
    api = "" # Holaaa, aqui va tu api, simplemente inicia sesion en omdb y obten la api, ej: 1a23bcde
    url = f"http://www.omdbapi.com/?t={titulo}&apikey={api}"

    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()

        if datos['Response'] == 'True':
            resultado = f"Titulo: {datos['Title']} \nAño: {datos['Year']} \nGenero: {datos['Genre']} \nCalificacion: {datos['imdbRating']}"
        else:
            resultado = f"Error: {datos['Error']}"
    else:
        resultado = f"Error en la solicitud: {respuesta.status_code}"

    labelResultado.config(text=resultado)

app = Tk()
app.title("Buscador de peliculas")
app.geometry("500x400")
app.configure(bg="#011627")

frame = Frame(app, bg="#011627")
frame.pack(pady=20, padx=20)

labelTitulo = Label(frame, text="Titulo de la pelicula:", bg="#011627", fg="#ffffff")
labelTitulo.grid(row=0, column=0, padx=10, pady=5, sticky=W)
entrytitulo = ttk.Entry(frame, width=30)
entrytitulo.grid(row=1, column=0, padx=10, pady=5)

btnBuscar = Button(frame, text="Buscar", command=buscar_pelicula, bg="#002341", fg="white", font=("Arial", 10, "bold"), relief="raised", bd=1, activebackground="#002341", activeforeground="#ffffff")
btnBuscar.grid(row=2, columnspan=2, pady=20)

labelResultado = ttk.Label(app, text="", background="#011627", foreground="#ffffff", font=('Helvetica', 10))
labelResultado.pack(pady=20)

app.mainloop()
