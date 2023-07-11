import random
import csv
import sys
import os
import pandas as pd
import tkinter as tk
from tkinter import ttk, PhotoImage, Label, font, messagebox
from PIL import Image, ImageTk
from pygame import mixer

directorio_proyecto = os.getcwd()
ruta_partidosCSV = os.path.join(directorio_proyecto, 'Recursos', 'CSV', 'partidos.csv')
ruta_resultadosCSV = os.path.join(directorio_proyecto, 'Recursos', 'CSV', 'resultados.csv')
ruta_victoriasCSV = os.path.join(directorio_proyecto, 'Recursos', 'CSV', 'victorias.csv')
ruta_gamesCSV = os.path.join(directorio_proyecto, 'Recursos', 'CSV', 'games.csv')
ruta_resultsCSV = os.path.join(directorio_proyecto, 'Recursos', 'CSV', 'results.csv')
ruta_victoriesCSV = os.path.join(directorio_proyecto, 'Recursos', 'CSV', 'victories.csv')
ruta_borrar = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'borrar_datos.png')
ruta_estadisticas_equipos = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'estadisticas_equipos.png')
ruta_estadisticas_partidos = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'estadisticas_partidos.png')
ruta_estadisticas_torneos = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'estadisticas_torneos.png')
ruta_salir = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'salir.png')
ruta_simular_torneo = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'simular_torneo.png')
ruta_volver = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'volver.png')
ruta_ayuda = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'ayuda.png')
ruta_ingles = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'ingles.png')
ruta_español = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'español.png')
ruta_simular1 = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'simular1.png')
ruta_simular5 = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'simular5.png')
ruta_simular10 = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'simular10.png')
ruta_simular100 = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'simular100.png')
ruta_buscador = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'buscador.png')
ruta_volumenON = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'volumen_on.png')
ruta_volumenOFF = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'volumen_off.png')
ruta_escudo_filtrar = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'escudo_filtrar.png')
ruta_set_filtrar = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'set_filtrar.png')
ruta_ganador_filtrar = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'ganador_filtrar.png')
ruta_filtroayuda = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'filtro_ayuda.PNG')
ruta_filtrar_datos= os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'filtrar_datos.png')
ruta_limpiar_filtros = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'limpiar_filtros.png')
ruta_trofeo_platino = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'trofeo_platino.png')
ruta_trofeo_plata = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'trofeo_plata.png')
ruta_trofeo_oro = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'trofeo_oro.png')
ruta_trofeo_bronce = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'trofeo_bronce.png')
ruta_trofeo_no_conseguido = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'trofeo_no_conseguido.png')
ruta_trofeo = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'trofeos.png')
ruta_simular_ayuda = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'simular_ayuda.PNG')
ruta_trofeos_ayuda = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'trofeos_ayuda.PNG')
ruta_volumen_ayuda = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'volumen_ayuda.PNG')
ruta_cambio_idioma_ayuda = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'cambio_idioma_ayuda.PNG')
ruta_limpiar_ayuda = os.path.join(directorio_proyecto, 'Recursos', 'Imagenes', 'limpiar_ayuda.PNG')
ruta_maintheme= os.path.join(directorio_proyecto, 'Recursos', 'Audio', 'main_theme.mp3')
ruta_ganar_trofeo= os.path.join(directorio_proyecto, 'Recursos', 'Audio', 'trofeo.mp3')

trofeos_conseguidos = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
simula=[False, False, False, False]
filtros=[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

def generar_partidos(equipos):
    partidos = []
    random.shuffle(equipos)
    for i in range(0, len(equipos), 2):
        partidos.append((equipos[i], equipos[i+1]))
    return partidos

def clasificar_equipo(partido, resultado):
    if resultado == 'W':
        return partido[0]
    else:
        return partido[1]

def simular_partidos(fase, equipos):
    resultados = []
    partidos = generar_partidos(equipos)
    with open(ruta_partidosCSV, mode='a', newline='') as archivo_csv, open(ruta_gamesCSV, mode='a', newline='') as archivo_csv2:
        nombres_columnas = ['Local', 'Visitante', 'Set 1', 'Set 2', 'Set 3', 'Ganador']
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=nombres_columnas)
        nombres_columnas_i = ['Home', 'Visitor', 'Set 1', 'Set 2', 'Set 3', 'Winner']
        escritor_csv2 = csv.DictWriter(archivo_csv2, fieldnames=nombres_columnas_i)

        if archivo_csv.tell() == 0:
            escritor_csv.writeheader()
        if(archivo_csv2.tell()==0):
            escritor_csv2.writeheader()

        for partido in partidos:
            set_Local = 0
            set_Visitante = 0
            fila = {'Local': partido}
            fila['Local'] = partido[0]
            fila['Visitante'] = partido[1]
            fila2 = {'Home': partido}
            fila2['Home'] = partido[0]
            fila2['Visitor'] = partido[1]
            for i in range(3):
                resultado_set = [0, 0]
                if set_Local == 2 or set_Visitante == 2:
                    break
                else:
                    for j in range(12):
                        juego = random.randint(0, 1)
                        if juego == 0:
                            resultado_set[0] += 1
                        else:
                            resultado_set[1] += 1
                        
                        if resultado_set[0] == 6:
                            set_Local += 1
                            if i == 0:
                                fila['Set 1'] = str(resultado_set[0]) + "-" + str(resultado_set[1])
                                fila2['Set 1'] = str(resultado_set[0]) + "-" + str(resultado_set[1])
                            elif i == 1:
                                fila['Set 2'] = str(resultado_set[0]) + "-" + str(resultado_set[1])
                                fila2['Set 2'] = str(resultado_set[0]) + "-" + str(resultado_set[1])
                            else:
                                fila['Set 3'] = str(resultado_set[0]) + "-" + str(resultado_set[1])
                                fila2['Set 3'] = str(resultado_set[0]) + "-" + str(resultado_set[1])
                            break
                        elif resultado_set[0] == 5 and resultado_set[1] == 5:
                            juego = random.randint(0, 1)
                            if juego == 0:
                                resultado_set[0] = 7
                                set_Local += 1
                            else: 
                                resultado_set[1] = 7
                                set_Visitante += 1
                            if i == 0:
                                fila['Set 1'] = str(resultado_set[0]) + "-" + str(resultado_set[1])
                                fila2['Set 1'] = str(resultado_set[0]) + "-" + str(resultado_set[1])
                            elif i == 1:
                                fila['Set 2'] = str(resultado_set[0]) + "-" + str(resultado_set[1])
                                fila2['Set 2'] = str(resultado_set[0]) + "-" + str(resultado_set[1])
                            else:
                                fila['Set 3'] = str(resultado_set[0]) + "-" + str(resultado_set[1])
                                fila2['Set 3'] = str(resultado_set[0]) + "-" + str(resultado_set[1])
                            break
                        elif resultado_set[1] == 6:
                            set_Visitante += 1
                            if i == 0:
                                fila['Set 1'] = str(resultado_set[0]) + "-" + str(resultado_set[1])
                                fila2['Set 1'] = str(resultado_set[0]) + "-" + str(resultado_set[1])
                            elif i == 1:
                                fila['Set 2'] = str(resultado_set[0]) + "-" + str(resultado_set[1])
                                fila2['Set 2'] = str(resultado_set[0]) + "-" + str(resultado_set[1])
                            else:
                                fila['Set 3'] = str(resultado_set[0]) + "-" + str(resultado_set[1])
                                fila2['Set 3'] = str(resultado_set[0]) + "-" + str(resultado_set[1])
                            break
            
            if set_Local > set_Visitante:
                resultado = 'W'
                fila['Ganador'] = partido[0] + " gana"
                fila2['Winner'] = partido[0] + " wins"
            else:
                resultado = 'L'
                fila['Ganador'] = partido[1] + " gana"
                fila2['Winner'] = partido[1] + " wins"
            
            resultados.append((partido, resultado))
            escritor_csv.writerow(fila)
            escritor_csv2.writerow(fila2)

    clasificados = [clasificar_equipo(partido, resultado) for partido, resultado in resultados]
    return clasificados

def calcular_porcentaje_victoria(victorias, partidos_jugados):
    if partidos_jugados == 0:
        return 0
    else:
        return victorias / partidos_jugados * 100

def actualizar_victorias(equipos):
    
    porcentaje_victoria =[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    victorias_totales=0
    victorias = [0, 0, 0, 0, 0, 0, 0, 0]
    porcentaje_derrota =[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    derrotas_totales=0
    derrotas = [0, 0, 0, 0, 0, 0, 0, 0]
    relacionvd=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    with open(ruta_resultadosCSV, mode='r') as archivo_csv:
        csv_reader = csv.reader(archivo_csv)
        next(csv_reader)  
        for row in csv_reader:
            if not any(row):  
                continue  
            if row[0] == 'La Coruna':
                victorias[0] += int(row[4])
                derrotas[0] += 3 - int(row[4])
            elif row[0] == 'Murcia':
                victorias[1] += int(row[4])
                derrotas[1] += 3 - int(row[4])
            elif row[0] == 'Toledo':
                victorias[2] += int(row[4])
                derrotas[2] += 3 - int(row[4])
            elif row[0] == 'Bilbao':
                victorias[3] += int(row[4])
                derrotas[3] += 3 - int(row[4])
            elif row[0] == 'Madrid':
                victorias[4] += int(row[4])
                derrotas[4] += 3 - int(row[4])
            elif row[0] == 'Barcelona':
                victorias[5] += int(row[4])
                derrotas[5] += 3 - int(row[4])
            elif row[0] == 'Sevilla':
                victorias[6] += int(row[4])
                derrotas[6] += 3 - int(row[4])
            elif row[0] == 'Malaga':
                victorias[7] += int(row[4])
                derrotas[7] += 3 - int(row[4])
    
    for victoria in victorias:
        victorias_totales += victoria
    
    for derrota in derrotas:
        derrotas_totales+= derrota
    
    for indice, victoria in enumerate(victorias):
        porcentaje_victoria[indice] = round((victoria / victorias_totales) * 100, 2)

    for indice, derrota in enumerate(derrotas):
        porcentaje_derrota[indice] = round((derrota / derrotas_totales) *100, 2)  

    for indice, victoria in enumerate(victorias):
        if derrotas[indice] == 0:
            relacionvd[indice] = victoria
        else:
            relacionvd[indice] = round((victoria / derrotas[indice]), 2)

    with open(ruta_victoriasCSV, mode='w', newline='') as archivo_csv, open(ruta_victoriesCSV, mode='w', newline='') as archivo_csv2:
        nombres_columnas = ['Equipo', 'Victorias', ' Porcentaje (V)', 'Derrotas', 'Porcentaje (D)', 'Relacion (V/D)']
        nombres_columnas_i = ['Team', 'Victories', 'Percentage (V)', 'Defeats', 'Percentage (D)', 'Relationship(W/L)']
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(nombres_columnas)
        escritor_csv2 = csv.writer(archivo_csv2)
        escritor_csv2.writerow(nombres_columnas_i)
        
        for equipo, victoria, porcentaje_v, derrota, porcentaje_d, relacion in zip(equipos, victorias, porcentaje_victoria, derrotas, porcentaje_derrota, relacionvd):
            fila = [equipo, victoria, porcentaje_v, derrota, porcentaje_d, relacion]
            escritor_csv.writerow(fila)
            escritor_csv2.writerow(fila)

def main():
    
    equipos = ['La Coruna', 'Murcia', 'Toledo', 'Bilbao', 'Madrid', 'Barcelona', 'Sevilla', 'Malaga'] 
    
    with open(ruta_resultadosCSV, mode='a', newline='') as archivo_csv, open(ruta_resultsCSV, mode='a', newline='') as archivo_csv2:
        nombres_columnas = ['Equipo', 'Cuartos','Semifinales', 'Final', 'Victorias']
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=nombres_columnas)
        nombres_columnas_i = ['Team', 'Quarters', 'Semifinals', 'Final', 'Victories']
        escritor_csv2 = csv.DictWriter(archivo_csv2, fieldnames=nombres_columnas_i)
        filas=[]
        filas2=[]
        
        if archivo_csv.tell() == 0:
            escritor_csv.writeheader()
        if(archivo_csv2.tell() == 0):
            escritor_csv2.writeheader()

        clasificados_cuartos = simular_partidos("Cuartos de final", equipos)
        clasificados_semis = simular_partidos("Semifinales", clasificados_cuartos)
        ganador = simular_partidos("Final", clasificados_semis)[0]
        
        with open(ruta_partidosCSV, mode='a', newline='') as archivo_csv, open(ruta_gamesCSV, mode='a', newline='') as archivo_csv2:
            escritor_csv1 = csv.DictWriter(archivo_csv, fieldnames=nombres_columnas)
            escritor_csv1.writerow({})
            escritor_csv3 = csv.DictWriter(archivo_csv2, fieldnames=nombres_columnas_i)
            escritor_csv3.writerow({})
        
        for equipo in equipos:
            fila_equipo = {'Equipo': equipo}
            fila_equipo_i ={'Team': equipo}
            if equipo not in clasificados_cuartos:
                fila_equipo['Cuartos'] = equipo + " cae eliminado"
                fila_equipo['Victorias']=0
                fila_equipo_i['Quarters'] = equipo + " is eliminated"
                fila_equipo_i['Victories']=0
            if equipo in clasificados_cuartos:
                fila_equipo['Cuartos'] = equipo + " pasa de ronda"
                fila_equipo['Victorias']=1
                fila_equipo_i['Quarters'] = equipo + " go throught"
                fila_equipo_i['Victories'] =1
            if equipo in clasificados_semis:
                fila_equipo['Semifinales'] = equipo + " pasa de ronda"
                fila_equipo['Victorias']=2
                fila_equipo_i['Semifinals'] = equipo + " go throught"
                fila_equipo_i["Victories"] = 2
            if equipo not in clasificados_semis and equipo in clasificados_cuartos:
                fila_equipo['Semifinales'] = equipo + " cae eliminado"
                fila_equipo_i["Semifinals"] = equipo + " is eliminated"
            if equipo == ganador:
                fila_equipo['Final'] = equipo + " gana el torneo"
                fila_equipo['Victorias']=3
                fila_equipo_i['Final'] = equipo + " is the winner"
                fila_equipo_i["Victories"] =3
            if equipo != ganador and equipo in clasificados_semis and equipo in clasificados_cuartos:
                fila_equipo['Final'] = equipo + " pierde en la final"
                fila_equipo_i['Final'] = equipo + " loses in the final"
            filas.append(fila_equipo)
            filas2.append(fila_equipo_i)
        
        escritor_csv.writerows(filas)
        escritor_csv2.writerows(filas2)
        escritor_csv.writerow({})
        escritor_csv2.writerow({})
        
    actualizar_victorias(equipos)
        
def generar_interfaz():
    def trofeo():
        ventana_trofeo = tk.Toplevel()
        ventana_trofeo.overrideredirect(True)
        ventana_trofeo.attributes("-topmost", True)
        ventana_trofeo.configure(background='#8A2BE2')
        ventana_trofeo.geometry("+{}+{}".format(ventana_trofeo.winfo_screenwidth() // 2, 0))
        canvas = tk.Canvas(ventana_trofeo, width=75, height=75)  # Ajusta el tamaño según tus necesidades
        canvas.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        canvas.configure(background='#8A2BE2', highlightbackground='#8A2BE2')
        canvas.create_polygon(37.5, 3.75, 15, 74.25, 71.25, 29.25, 3.75, 29.25, 60, 74.25, fill='#FFD700', outline='black', width=2.25)   
        mixer.music.load(ruta_ganar_trofeo)
        mixer.music.play()
        def cerrar_ventana():
            ventana_trofeo.destroy()
            mixer.music.load(ruta_maintheme)
            mixer.music.play()
            mixer.music.play(loops=-1)
            if trofeos_conseguidos[0] == False and all(trofeos_conseguidos[i] for i in range(1, 17)):
                trofeos_conseguidos[0] = True
                trofeo()
        ventana_trofeo.after(2000, cerrar_ventana)
    
    mixer.init()
    mixer.music.load(ruta_maintheme)
    def toggle_mute():
        if mixer.music.get_volume() == 0:
            mixer.music.set_volume(1.0)
            boton_volumen.config(image=imagen_volumenONfinal)
        else:
            if not trofeos_conseguidos[15]:
                trofeos_conseguidos[15] = True
                trofeo()
            mixer.music.set_volume(0)
            boton_volumen.config(image=imagen_volumenOFFfinal)
    mixer.music.play(loops=-1)
    
    ventana = tk.Tk()
    idioma= True

    def mostrar_trofeos():
        ventana_trofeos = tk.Toplevel()
        if idioma:
            texto_titulo_trofeo= "Trofeos"
            texto_trofeo= "Sala de trofeos"
        else: 
            texto_titulo_trofeo = "Trophies"
            texto_trofeo = "Trophy room"
        ventana_trofeos.title(texto_titulo_trofeo)
        ventana_trofeos.attributes("-fullscreen", True)
        ventana_trofeos.configure(bg="#03254c")
        ancho_imagen=200
        alto_imagen=200
        ancho_pantalla = ventana_trofeos.winfo_screenwidth()
        imagen_trofeo_no_conseguido = Image.open(ruta_trofeo_no_conseguido)
        imagen_trofeo_no_conseguido = imagen_trofeo_no_conseguido.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
        imagen_trofeo_no_conseguido_final=ImageTk.PhotoImage(imagen_trofeo_no_conseguido)
        imagen_trofeo_platino = Image.open(ruta_trofeo_platino)
        imagen_trofeo_platino = imagen_trofeo_platino.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
        imagen_trofeo_platino_final=ImageTk.PhotoImage(imagen_trofeo_platino)
        imagen_trofeo_bronce = Image.open(ruta_trofeo_bronce)
        imagen_trofeo_bronce = imagen_trofeo_bronce.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
        imagen_trofeo_bronce_final=ImageTk.PhotoImage(imagen_trofeo_bronce)
        imagen_trofeo_plata = Image.open(ruta_trofeo_plata)
        imagen_trofeo_plata = imagen_trofeo_plata.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
        imagen_trofeo_plata_final=ImageTk.PhotoImage(imagen_trofeo_plata)
        imagen_trofeo_oro = Image.open(ruta_trofeo_oro)
        imagen_trofeo_oro = imagen_trofeo_oro.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
        imagen_trofeo_oro_final=ImageTk.PhotoImage(imagen_trofeo_oro)
        style = ttk.Style()
        style.configure("Flat.TButton",font=('Arial', 22, 'bold') ,relief="flat", background="SystemButtonFace", foreground='deep sky blue')

        imagen_volver = PhotoImage(file=ruta_volver)
        boton_salir = ttk.Button(ventana_trofeos, image=imagen_volver, command=ventana_trofeos.destroy, style="EstiloSalida.TButton")
        boton_salir.image = imagen_volver  # Mantener la referencia a la imagen
        boton_salir.pack(fill='x', padx=10, pady=10)  # Configurar el ancho y alto del botón
        boton_salir.grid(row=0, column=0, padx=10, pady=10, sticky='w')   

        encabezado_trofeos = Label(ventana_trofeos, text=texto_trofeo, font=("Arial", 40, 'bold'),
                    fg='yellow', bg='#007BFF', relief='raised', bd=5)
        encabezado_trofeos.configure(font=font.Font(family='impact', size=60))
        encabezado_trofeos.grid(row=0, column=0, padx=10, pady=(20, 10))

        lista_elementos = [
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_platino_final, "texto": "Experto en PadelDash", "texto2":"¡Has conseguido todos los trofeos!"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_bronce_final, "texto": "El primero de muchos", "texto2": "Tu primer torneo simulado"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_plata_final, "texto": "Toca todos los palos", "texto2": "Has usado todas las opciones de simulación"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_bronce_final, "texto": "Quiero ver los resultados", "texto2": "Has mostrado los datos de los torneos, los datos de los partidos, o las estadísticas de los equipos"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_plata_final, "texto": "Mi equipo favorito es...", "texto2": "Has filtrado los resultados según alguno de los equipos"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_oro_final, "texto": "Los partidos más rápidos", "texto2": "Has filtrado usando la opción 'Terminado en 2 sets'"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_plata_final, "texto": "La próxima vez será", "texto2": "Has utilizado el filtro 'Eliminado en...'"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_plata_final, "texto": "Real hasta el final", "texto2": "Has utilizado el filtro 'Pasa a la siguiente ronda'"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_bronce_final, "texto": "Es mejor la cantidad que la calidad", "texto2": "Has filtrado el número de victorias o de derrotas"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_plata_final, "texto": "Estoy en el montón bueno", "texto2": "Has filtrado algún porcentaje utilizando la relación '51-100'"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_bronce_final, "texto": "¿Es una buena relación?","texto2": "Has filtrado según la relacion victorias/derrotas"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_bronce_final,"texto": "Hay que hacer una limpieza", "texto2": "Tabla restaurada"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_oro_final, "texto": "El rey de la estadística", "texto2": "Has usado todos los filtros posibles"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_plata_final,"texto": "Vuelta a empezar", "texto2": "Has borrado los datos"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_bronce_final,"texto": "No hablo tu idioma", "texto2":"Has cambiado el idioma de la aplicación"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_bronce_final,"texto": "¡No aguanto más ese ruido!", "texto2":"Has silenciado el juego"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_bronce_final,"texto": "Echame un cable por favor", "texto2":"Has entrado en la sección de ayuda"}            
        ]
        lista_elementos_ingles = [
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_platino_final, "texto": "Expert in PadelDash", "texto2":"You have obtained all the trophies!"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_bronce_final, "texto": "The first of many","texto2": "Your first simulated tournament"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_plata_final, "texto": "Touches all areas", "texto2": "You have used all simulation options"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_bronce_final, "texto": "I want to see the results", "texto2": "You have displayed tournament data, match data, or team statistics."},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_plata_final,  "texto": "My favorite team is...", "texto2": "You have filtered the results according to one of the following teams"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_oro_final, "texto": "The fastest matches", "texto2": "You have filtered using the option 'Finished in 2 sets'."},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_plata_final, "texto": "Next time it will be", "texto2": "You have used the filter 'Removed on...'"},
            {"imagen": imagen_trofeo_no_conseguido_final,"imagen2":imagen_trofeo_plata_final, "texto": "Real to the end", "texto2": "You have used the filter 'Go to the next round'"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_bronce_final, "texto": "Quantity is better than quality", "texto2": "You have filtered the number of wins or losses."},
            {"imagen": imagen_trofeo_no_conseguido_final,"imagen2":imagen_trofeo_plata_final, "texto": "I am in the good pile", "texto2": "You have filtered some percentage using the '51-100' ratio."},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_bronce_final, "texto": "Is it a good relationship?", "texto2": "You have filtered by win/loss ratio."},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_bronce_final, "texto": "A cleanup is needed", "texto2": "Restored table"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_oro_final, "texto": "The king of statistics", "texto2": "You have used all possible filters"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_plata_final, "texto": "Starting over", "texto2": "You have deleted the data"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_bronce_final, "texto": "I don't speak your language", "texto2":"You have changed the application language"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_bronce_final, "texto": "I can't stand that noise anymore!", "texto2":"You have muted the game"},
            {"imagen": imagen_trofeo_no_conseguido_final, "imagen2":imagen_trofeo_bronce_final,"texto": "Please give me a hand", "texto2":"You have accessed the help section"}            
        ]
        frame_principal = tk.Frame(ventana_trofeos)
        frame_principal.grid(row=1, column=0, sticky="nsew")
        frame_principal.configure(width=ancho_pantalla, background="#0078D7")
        frame_principal.grid_rowconfigure(0, weight=1)
        frame_principal.grid_columnconfigure(0, weight=1)
        ancho_pantalla = ventana_trofeos.winfo_screenwidth()
        canvas = tk.Canvas(frame_principal)
        canvas.configure(width=ancho_pantalla - 50, height=500, background="#0078D7")
        canvas.grid(row=1, column=0, sticky="nsew")
        scrollbar = ttk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=1, column=1, sticky="nsew")
        canvas.configure(yscrollcommand=scrollbar.set)
        frame_interior = tk.Frame(canvas)
        frame_interior.configure(background="#0078D7")
        canvas.create_window((0, 0), window=frame_interior, anchor="nw", tags="frame_interior")
        frame_interior.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
        
        if idioma:
            for i, elemento in enumerate(lista_elementos):
                frame_elemento = ttk.LabelFrame(frame_interior, width=1000, height=300, style='EstiloAzul.TLabel')
                frame_elemento.grid(row=i, column=0, padx=ancho_pantalla/4, pady=10, sticky="nswe")

                if trofeos_conseguidos[i]: 
                    etiqueta_imagen = tk.Label(frame_elemento, image=elemento["imagen2"])
                    etiqueta_imagen.pack(side="left", padx=10)

                    etiqueta_texto = tk.Label(frame_elemento, text=elemento["texto2"], font=("impact", 30), justify="center",
                                            wraplength=700, padx=20, background="deep sky blue")
                    etiqueta_texto.pack(side="left")
                else: 
                    etiqueta_imagen = tk.Label(frame_elemento, image=elemento["imagen"])
                    etiqueta_imagen.pack(side="left", padx=10)

                    etiqueta_texto = tk.Label(frame_elemento, text=elemento["texto"], font=("impact", 30), justify="center",
                                            wraplength=700, padx=20, background="deep sky blue")
                    etiqueta_texto.pack(side="left")
                frame_elemento.grid_rowconfigure(0, weight=1)
                frame_elemento.grid_columnconfigure(0, weight=1)
                frame_elemento.grid_propagate(False)

        else:
            for i, elemento in enumerate(lista_elementos_ingles):
                frame_elemento = ttk.LabelFrame(frame_interior, width=1000, height=300, style='EstiloAzul.TLabel' )
                frame_elemento.grid(row=i, column=0, padx=ancho_pantalla/4, pady=10, sticky="nsew")

                if trofeos_conseguidos[i]: 
                    etiqueta_imagen = tk.Label(frame_elemento, image=elemento["imagen2"])
                    etiqueta_imagen.pack(side="left", padx=10)

                    etiqueta_texto = tk.Label(frame_elemento, text=elemento["texto2"], font=("impact", 30), justify="center",
                                            wraplength=700, padx=20, background="deep sky blue")
                    etiqueta_texto.pack(side="left")
                else: 
                    etiqueta_imagen = tk.Label(frame_elemento, image=elemento["imagen"])
                    etiqueta_imagen.pack(side="left", padx=10)

                    etiqueta_texto = tk.Label(frame_elemento, text=elemento["texto"], font=("impact", 30), justify="center",
                                            wraplength=700, padx=20, background="deep sky blue")
                    etiqueta_texto.pack(side="left")
                frame_elemento.grid_rowconfigure(0, weight=1)
                frame_elemento.grid_columnconfigure(0, weight=1)
                frame_elemento.grid_propagate(False)

        frame_interior.update_idletasks()  
        canvas.config(scrollregion=canvas.bbox("all"))
        ventana_trofeos.mainloop()
    
    def cambiar_idioma_ingles():
        nonlocal idioma
        if not trofeos_conseguidos[14]:
            trofeos_conseguidos[14]= True
            trofeo()
        boton_ingles.config(state="disabled")  
        boton_español.config(state="normal")  
        idioma = False
        encabezado.config(text="Welcome to PadelDash")
        boton_simular.config(text="Simulate Tournament")
        boton_historial_partidos.config(text="Show Match History")
        boton_historial_torneos.config(text="Show Tournament History")
        boton_estadisticas_equipos.config(text="Show Team Statistics")
        boton_borrar_datos.config(text="Delete Data")
        boton_ayuda.config(text="Help")

    def cambiar_idioma_español():
        nonlocal idioma
        if not trofeos_conseguidos[14]:
            trofeos_conseguidos[14]= True
            trofeo()
        boton_ingles.config(state="normal")  
        boton_español.config(state="disabled")  
        idioma=True
        encabezado.config(text="Bienvenido a PadelDash")
        boton_simular.config(text="Simular Torneo")
        boton_historial_partidos.config(text="Mostrar Historial de Partidos")
        boton_historial_torneos.config(text="Mostrar Historial de Torneos")
        boton_estadisticas_equipos.config(text="Mostrar Estadísticas de Equipos")
        boton_borrar_datos.config(text="Borrar Datos")
        boton_ayuda.config(text="Ayuda")
        
    def abrir_ventana_ayuda():
        nonlocal idioma
        ancho_imagen=200
        alto_imagen=200
        if not trofeos_conseguidos[16]:
            trofeos_conseguidos[16] = True
            trofeo()
        ventana_ayuda = tk.Toplevel()
        if idioma:
            texto_titulo_ayuda= "Ayuda"
        else: texto_titulo_ayuda= "Help"
        ventana_ayuda.title(texto_titulo_ayuda)
        ventana_ayuda.attributes('-fullscreen', True) 
        ventana_ayuda.configure(background="#0078D7")
        ancho_pantalla = ventana_ayuda.winfo_screenwidth()
        imagen_simular_torneo2 = Image.open(ruta_simular_torneo)
        imagen_simular_torneo200x200 = imagen_simular_torneo2.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
        imagen_simular_torneofinal=ImageTk.PhotoImage(imagen_simular_torneo200x200)
        imagen_estadisticas_partidos2 = Image.open(ruta_estadisticas_partidos)
        imagen_estadisticas_partidos200x200 = imagen_estadisticas_partidos2.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
        imagen_estadisticas_partidosfinal=ImageTk.PhotoImage(imagen_estadisticas_partidos200x200)
        imagen_estadisticas_torneos2 = Image.open(ruta_estadisticas_torneos)
        imagen_estadisticas_torneos200x200 = imagen_estadisticas_torneos2.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
        imagen_estadisticas_torneosfinal=ImageTk.PhotoImage(imagen_estadisticas_torneos200x200)
        imagen_estadisticas_equipos2 = Image.open(ruta_estadisticas_equipos)
        imagen_estadisticas_equipos200x200 = imagen_estadisticas_equipos2.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
        imagen_estadisticas_equiposfinal=ImageTk.PhotoImage(imagen_estadisticas_equipos200x200)
        imagenborrar2 = Image.open(ruta_borrar)
        imagenborrar200x200 = imagenborrar2.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
        imagen_borrarfinal=ImageTk.PhotoImage(imagenborrar200x200)
        imagen_salir2 = Image.open(ruta_salir)
        imagen_salir200x200 = imagen_salir2.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
        imagen_salirfinal=ImageTk.PhotoImage(imagen_salir200x200)
        imagen_filtroayuda = Image.open(ruta_filtroayuda)
        imagen_filtroayuda200x200 = imagen_filtroayuda.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
        imagen_filtroayudafinal=ImageTk.PhotoImage(imagen_filtroayuda200x200)
        imagen_simular_ayuda = Image.open(ruta_simular_ayuda)
        imagen_simular_ayuda200x200 = imagen_simular_ayuda.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
        imagen_simular_ayudafinal=ImageTk.PhotoImage(imagen_simular_ayuda200x200)
        imagen_trofeos_ayuda = Image.open(ruta_trofeos_ayuda)
        imagen_trofeos_ayuda200x200 = imagen_trofeos_ayuda.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
        imagen_trofeos_ayudafinal=ImageTk.PhotoImage(imagen_trofeos_ayuda200x200)
        imagen_volumen_ayuda = Image.open(ruta_volumen_ayuda)
        imagen_volumen_ayuda200x200 = imagen_volumen_ayuda.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
        imagen_volumen_ayudafinal=ImageTk.PhotoImage(imagen_volumen_ayuda200x200)
        imagen_cambio_idioma_ayuda = Image.open(ruta_cambio_idioma_ayuda)
        imagen_cambio_idioma_ayuda200x200 = imagen_cambio_idioma_ayuda.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
        imagen_cambio_idioma_ayudafinal=ImageTk.PhotoImage(imagen_cambio_idioma_ayuda200x200)
        imagen_limpiar_ayuda = Image.open(ruta_limpiar_ayuda)
        imagen_limpiar_ayuda200x200 = imagen_limpiar_ayuda.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
        imagen_limpiar_ayudafinal=ImageTk.PhotoImage(imagen_limpiar_ayuda200x200)
        
        style = ttk.Style()
        style.configure("EstiloAzul.TLabel", background="deep sky blue")
        style2 = ttk.Style()
        style2.configure("Vertical.TScrollbar",
                gripcount=0,
                background="deep sky blue",  # Color de fondo
                darkcolor="#005EBF",  # Color oscuro
                troughcolor="#D3EAFD"  # Color del canal
                )
        texto_ayuda=""
        if idioma: 
            texto_ayuda="Toda la ayuda en esta sección"
        else: 
            texto_ayuda="All the help in this section"       
        style2.configure("EstiloSalida.TButton", background="#0078D7")  # Configurar el estilo azul
        imagen_volver = PhotoImage(file=ruta_volver)
        boton_salir = ttk.Button(ventana_ayuda, image=imagen_volver, command=ventana_ayuda.destroy, style="EstiloSalida.TButton")
        boton_salir.image = imagen_volver  # Mantener la referencia a la imagen
        boton_salir.pack(fill='x', padx=10, pady=10)  # Configurar el ancho y alto del botón
        boton_salir.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        encabezado_ayuda = Label(ventana_ayuda, text=texto_ayuda, font=("Arial", 40, 'bold'),
                    fg='yellow', bg='#007BFF', relief='raised', bd=5)

        # Personalizar el estilo del texto
        encabezado_ayuda.configure(font=font.Font(family='impact', size=60))

        encabezado_ayuda.grid(row=0, column=0, columnspan=3, padx=10, pady=(20, 10))
        
        lista_elementos = [
            {"imagen": imagen_trofeos_ayudafinal, "texto": "Muestra los trofeos conseguidos"},
            {"imagen": imagen_volumen_ayudafinal, "texto": "Activa o desactiva el volumen de la aplicación"},
            {"imagen": imagen_cambio_idioma_ayudafinal, "texto": "Cambia el idioma de la aplicación"},
            {"imagen": imagen_simular_torneofinal, "texto": "Este botón simula torneos de padel. Este torneo consta de ocho equipos y juegan 3 fases: cuartos de final, semifinal y final"},
            {"imagen": imagen_simular_ayudafinal, "texto": "Elige el número de torneos que quieres simular"},
            {"imagen": imagen_estadisticas_partidosfinal, "texto": "Muestra las estadísticas de todos los partidos de cada torneo: los equipos local y visitante, los resultados en cada set y el ganador"},
            {"imagen": imagen_estadisticas_torneosfinal, "texto": "Muestra las estadisticas de los torneos de forma que te dice quien gana en cada fase y quien pierde y las victorias de cada equipo para cada torneo"},
            {"imagen": imagen_estadisticas_equiposfinal, "texto": "Muestra las victorias, el porcentaje de victorias de cada equipo, las derrotas, el procentaje de derrotas y la relación victorias/derrotas. Nota: el porcentaje de victorias es calculado de la manera: victorias del equipo / victorias totales. Las derrotas se calculan de igual manera."},
            {"imagen": imagen_limpiar_ayudafinal, "texto": "Limpia los filtros que se han aplicado"},
            {"imagen": imagen_filtroayudafinal, "texto": "Filtra los datos. La lista de la izquierda muestra que columna quieres filtrar y la de la derecha para filtrar el conjunto de valores que quieres observar"},
            {"imagen": imagen_borrarfinal, "texto": "Borra los datos de la base de datos"},
            {"imagen": imagen_salirfinal, "texto": "Salir de la aplicación"}
        ]

        list_elements = [
            {"imagen": imagen_trofeos_ayudafinal, "texto": "Displays trophies won"},
            {"imagen": imagen_volumen_ayudafinal, "texto": "Activates or deactivates the volume of the application"},
            {"imagen": imagen_cambio_idioma_ayudafinal, "texto": "Change the application language"},
            {"imagen": imagen_simular_torneofinal, "texto": "This button simulates padel tournaments. This tournament consists of eight teams and they play 3 phases: quarterfinals, semifinals and finals."},
            {"imagen": imagen_simular_ayudafinal, "texto": "Choose the number of tournaments you want to simulater"},
            {"imagen": imagen_estadisticas_partidosfinal, "texto": "Shows the statistics of all matches in each tournament: the home and away teams, the results in each set and the winner."},
            {"imagen": imagen_estadisticas_torneosfinal, "texto": "Displays tournament statistics in a way that tells you who wins in each phase and who loses and the victories of each team for each tournament."},
            {"imagen": imagen_estadisticas_equiposfinal, "texto": "It shows the wins, the winning percentage of each team, the losses, the losing percentage and the win/loss ratio. Note: the percentage of wins is calculated as follows: team wins / total wins. Losses are calculated in the same way."},
            {"imagen": imagen_limpiar_ayudafinal, "texto": "Cleans filters that have been applied"},
            {"imagen": imagen_filtroayudafinal, "texto": "Filter the data. The list on the left shows which column you want to filter and the one on the right to filter the set of values you want to observe."},
            {"imagen": imagen_borrarfinal, "texto": "Deletes data from the database"},
            {"imagen": imagen_salirfinal, "texto": "Exit the application"}
        ]
        # Crear un frame principal para contener el canvas y el scrollbar
        frame_principal = tk.Frame(ventana_ayuda)
        frame_principal.grid(row=1, column=0, sticky="nsew")
        frame_principal.configure(width=ancho_pantalla, background="#0078D7")
        frame_principal.grid_rowconfigure(0, weight=1)
        frame_principal.grid_columnconfigure(0, weight=1)

        # Obtener el ancho de la pantalla
        ancho_pantalla = ventana_ayuda.winfo_screenwidth()

        # Crear el canvas
        canvas = tk.Canvas(frame_principal)
        canvas.configure(width=ancho_pantalla - 50, height=500, background="#0078D7")
        canvas.grid(row=1, column=0, sticky="nsew")
        
        # Crear el scrollbar y asociarlo al canvas
        scrollbar = ttk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=1, column=1, sticky="nsew")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Crear un frame interior en el canvas
        frame_interior = tk.Frame(canvas)
        frame_interior.configure(background="#0078D7")
        canvas.create_window((0, 0), window=frame_interior, anchor="nw", tags="frame_interior")
        
        frame_interior.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
        if idioma:
            for i, elemento in enumerate(lista_elementos):
                frame_elemento = ttk.LabelFrame(frame_interior, width=1000, height=300, style='EstiloAzul.TLabel')
                frame_elemento.grid(row=i, column=0, padx=ancho_pantalla / 4.5, pady=10, sticky="nswe")

                etiqueta_imagen = tk.Label(frame_elemento, image=elemento["imagen"])
                etiqueta_imagen.pack(side="left", padx=10)

                etiqueta_texto = tk.Label(frame_elemento, text=elemento["texto"], font=("impact", 15),
                                        wraplength=700, background="deep sky blue")
                etiqueta_texto.pack(side="left")
                frame_elemento.grid_rowconfigure(0, weight=1)
                frame_elemento.grid_columnconfigure(0, weight=1)
                frame_elemento.grid_propagate(False)

        else:
            for i, elemento in enumerate(list_elements):
                frame_elemento = ttk.LabelFrame(frame_interior, width=1000, height=300, style='EstiloAzul.TLabel' )
                frame_elemento.grid(row=i, column=0, padx=ancho_pantalla / 4.5, pady=10, sticky="nsew")

                etiqueta_imagen = tk.Label(frame_elemento, image=elemento["imagen"])
                etiqueta_imagen.pack(side="left", padx=10)

                etiqueta_texto = tk.Label(frame_elemento, text=elemento["texto"], font=("impact", 15), justify="center",
                                        wraplength=700, padx=20, background="deep sky blue")
                etiqueta_texto.pack(side="left")
                frame_elemento.grid_rowconfigure(0, weight=1)
                frame_elemento.grid_columnconfigure(0, weight=1)
                frame_elemento.grid_propagate(False)

        # Configurar el canvas para permitir el desplazamiento
        frame_interior.update_idletasks()  # Actualizar el tamaño del frame interior
        canvas.config(scrollregion=canvas.bbox("all"))

        ventana_ayuda.mainloop()

    def simular_torneo():
        def simular(n):
            for _ in range(n):
                if (n==1 or n==5 or n==10 or n==100) and all(not simula[i] for i in range(4)):
                    trofeos_conseguidos[1]= True
                    trofeo()
                    if n==1:
                        simula[0]= True
                    elif n==5:
                        simula[1]=True
                    elif n==10:
                        simula[2]=True
                    elif n==100:
                        simula[3]= True
                if n==1 and simula[0] == False:
                    simula[0] = True
                if n==5 and simula[1] == False:
                    simula[1] = True
                if n==10 and simula[2] == False:
                    simula[2] = True
                if n==100 and simula[3] == False:
                    simula[3] = True
                if all(simula[i] for i in range(4)) and not trofeos_conseguidos[2]:
                    trofeos_conseguidos[2]= True
                    trofeo()
                main()

            if idioma:
                ventana.withdraw()
                messagebox.showinfo("Torneo", f"Torneo finalizado {n} veces")
                ventana_simulacion.deiconify()
            else:
                ventana.withdraw()
                messagebox.showinfo("Tournament", f"Tournament finished {n} times")
                ventana_simulacion.deiconify()

        def volver_atras():
            ventana.deiconify()
            ventana_simulacion.destroy()
            
        nonlocal idioma
        texto_1vez=""
        texto_5veces=""
        texto_10veces=""
        texto_100veces=""
        texto_encabezado=""
        if idioma:
            texto_1vez="SIMULAR 1 VEZ"
            texto_5veces= "SIMULAR 5 VECES"
            texto_10veces= "SIMULAR 10 VECES"
            texto_100veces= "SIMULAR 100 VECES"
            texto_encabezado= "Simula torneos tantas veces como quieras"
        else:
            texto_1vez="SIMULATE 1 TIME"
            texto_5veces= "SIMULATE 5 TIMES"
            texto_10veces= "SIMULATE 10 TIMES"
            texto_100veces= "SIMULATE 100 TIMES"
            texto_encabezado= "Simulate tournaments as many times as you want"
        ancho_imagen= 200
        alto_imagen=200
        imagen_volver = PhotoImage(file=ruta_volver)
        imagen_simular1= Image.open(ruta_simular1)
        imagen_simular5= Image.open(ruta_simular5)
        imagen_simular10= Image.open(ruta_simular10)
        imagen_simular100= Image.open(ruta_simular100)
        imagen_simular1_300x300= imagen_simular1.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
        imagen_simular1_final = ImageTk.PhotoImage(imagen_simular1_300x300)
        imagen_simular5_300x300= imagen_simular5.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
        imagen_simular5_final = ImageTk.PhotoImage(imagen_simular5_300x300)
        imagen_simular10_300x300= imagen_simular10.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
        imagen_simular10_final = ImageTk.PhotoImage(imagen_simular10_300x300)
        imagen_simular100_300x300= imagen_simular100.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
        imagen_simular100_final = ImageTk.PhotoImage(imagen_simular100_300x300)
        
        ventana_simulacion = tk.Toplevel()
        if idioma:
            texto_simulación= "Simular"
        else: texto_simulación = "Simulate"
        ventana_simulacion.title(texto_simulación)
        ventana_simulacion.attributes("-fullscreen", True)
        ventana_simulacion.configure(bg="#03254c")
        ancho_pantalla = ventana.winfo_screenwidth()
        altura_pantalla = ventana.winfo_screenheight()
        ancho_boton = int(ancho_pantalla * 0.1)
        altura_boton = int(altura_pantalla * 0.2)
        ventana_simulacion.grid_columnconfigure(0, weight=1, minsize=ancho_boton)
        ventana_simulacion.grid_columnconfigure(1, weight=1, minsize=ancho_boton)
        ventana_simulacion.grid_rowconfigure(0, weight=1, minsize=altura_boton)
        ventana_simulacion.grid_rowconfigure(1, weight=1, minsize=altura_boton)
        ventana_simulacion.grid_rowconfigure(2, weight=1, minsize=altura_boton)
        ventana_simulacion.style = ttk.Style()
        ventana_simulacion.style.theme_use('default')
        ventana_simulacion.style.configure('PersonalizacionBoton2.TButton',
                            background='#03254c',
                            foreground='#00FF00',
                            font=('impact', 30),
                            relief='flat')
        ventana_simulacion.style.map('PersonalizacionBoton2.TButton',
                    background=[('active', 'light blue')])
        ventana_simulacion.style.configure('PersonalizacionBoton2.TButton:hover',
                            background='light blue',
                            foreground='black',
                            font=('impact', 15),
                            relief='gr',
                            cursor= 'hand2')
        
        encabezado_simulación = Label(ventana_simulacion, text=texto_encabezado, font=("Arial", 40, 'bold'),
                    fg='#00FF00', bg='#007BFF', relief='raised', bd=5)
        encabezado_simulación.configure(font=font.Font(family='impact', size=40))
        encabezado_simulación.grid(row=0, column=0, columnspan=3, padx=10)

        boton_simular_1 = ttk.Button(ventana_simulacion, text=texto_1vez, image=imagen_simular1_final, compound='top', command=lambda: simular(1), style='PersonalizacionBoton2.TButton')
        boton_simular_1.grid(row=1, column=0, padx=5, pady=5)
        boton_simular_5 = ttk.Button(ventana_simulacion,text=texto_5veces, image=imagen_simular5_final, compound='top', command=lambda: simular(5), style='PersonalizacionBoton2.TButton')
        boton_simular_5.grid(row=1, column=1, padx=5, pady=5)
        boton_simular_10 = ttk.Button(ventana_simulacion,text=texto_10veces, image=imagen_simular10_final, compound='top', command=lambda: simular(10), style='PersonalizacionBoton2.TButton')
        boton_simular_10.grid(row=2, column=0, padx=5, pady=5)
        boton_simular_100 = ttk.Button(ventana_simulacion,text=texto_100veces, image=imagen_simular100_final, compound='top', command=lambda: simular(100), style='PersonalizacionBoton2.TButton')
        boton_simular_100.grid(row=2, column=1, padx=5, pady=5)
        boton_volver = ttk.Button(ventana_simulacion, image=imagen_volver, command=volver_atras, style='PersonalizacionBoton2.TButton')
        boton_volver.grid(row=0, column=0, padx=5, pady=5, sticky='nw')
        ventana_simulacion.mainloop()

    def mostrar_historial_partidos():
        nonlocal idioma
        if idioma:
            with open(ruta_partidosCSV, mode='r') as archivo_csv:
                if os.path.getsize(ruta_partidosCSV) > 0:
                    registros = csv.reader(archivo_csv)
                    data = list(registros)
                    df = pd.DataFrame(data)
                    mostrar_tabla(df)
                else:
                    messagebox.showerror("Sin Datos", "No hay datos en la base de datos")
        else: 
            with open(ruta_gamesCSV, mode='r') as archivo_csv:
                if os.path.getsize(ruta_gamesCSV) > 0:
                    registros = csv.reader(archivo_csv)
                    data = list(registros)
                    df = pd.DataFrame(data)
                    mostrar_tabla(df)
                else:
                    messagebox.showerror("No Data", "There is no data in the database")

    def mostrar_historial_torneos():
        nonlocal idioma
        if idioma:
            with open(ruta_resultadosCSV, mode='r') as archivo_csv:
                if os.path.getsize(ruta_resultadosCSV) > 0:
                    registros = csv.reader(archivo_csv)
                    data = list(registros)
                    df = pd.DataFrame(data)
                    mostrar_tabla(df)
                else:
                    messagebox.showerror("Sin Datos", "No hay datos en la base de datos")
        else:
            with open(ruta_resultsCSV, mode='r') as archivo_csv:
                if os.path.getsize(ruta_resultsCSV) > 0:
                    registros = csv.reader(archivo_csv)
                    data = list(registros)
                    df = pd.DataFrame(data)
                    mostrar_tabla(df)
                else:
                    messagebox.showerror("No Data", "There is no data in the database")
    
    def mostrar_estadisticas_equipos():
        nonlocal idioma
        if idioma:
            with open(ruta_victoriasCSV, mode='r') as archivo_csv:
                if os.path.getsize(ruta_victoriasCSV) > 0:
                    registros = csv.reader(archivo_csv)
                    data = list(registros)
                    df = pd.DataFrame(data)
                    mostrar_tabla(df)
                else:
                    messagebox.showerror("Sin Datos", "No hay datos en la base de datos")
        else:
            with open(ruta_victoriesCSV, mode='r') as archivo_csv:
                if os.path.getsize(ruta_victoriesCSV) > 0:
                    registros = csv.reader(archivo_csv)
                    data = list(registros)
                    df = pd.DataFrame(data)
                    mostrar_tabla(df)
                else:
                    messagebox.showerror("No Data", "There is no data in the database")    
    
    def mostrar_tabla(df):
        nonlocal idioma
        ancho_imagen = 51
        alto_imagen = 29
        ancho_filtro= 150
        alto_filtro=150
        imagen_volver = PhotoImage(file=ruta_volver)
        imagen_filtrar_datos = Image.open(ruta_filtrar_datos)
        imagen_filtrar_datos50x75 = imagen_filtrar_datos.resize((ancho_filtro,alto_filtro),Image.LANCZOS)
        imagen_filtrar_datosfinal=ImageTk.PhotoImage(imagen_filtrar_datos50x75)
        imagen_limpiar_filtro = Image.open(ruta_limpiar_filtros)
        imagen_limpiar_filtro50x75 = imagen_limpiar_filtro.resize((ancho_filtro,alto_filtro),Image.LANCZOS)
        imagen_limpiar_filtrofinal=ImageTk.PhotoImage(imagen_limpiar_filtro50x75)
        
        if not trofeos_conseguidos[3]:
            trofeos_conseguidos[3] = True
            trofeo()
        if idioma:
            titulo= "Tabla"
        else: titulo = "Table"
        ventana_tabla = tk.Toplevel()
        ventana_tabla.title(titulo)
        ventana_tabla.attributes("-fullscreen", True)  # Hacer que la ventana ocupe toda la pantalla
        ancho_pantalla = ventana_tabla.winfo_screenwidth()
        ancho_tabla = int(ancho_pantalla * 0.9)
        ancho_boton = int(ancho_pantalla * 0.01)
        style = ttk.Style()
        style2= ttk.Style()
        style.configure("Flat.TButton",font=('Arial', 22, 'bold') ,relief="flat", background="SystemButtonFace", foreground='deep sky blue')

        def volver_atras():
            ventana.deiconify()
            ventana_tabla.destroy()
        
        boton_salir = ttk.Button(ventana_tabla, image=imagen_volver, compound='center', command=volver_atras,  style="Flat.TButton")
        boton_salir.configure(width=ancho_boton)  # Configurar el ancho y alto del botón
        boton_salir.grid(row=0, column=0, padx=10, pady=10, sticky="n")
        
        def filtrar_datos():

            def volver_atras2():
                ventana_tabla.deiconify()
                ventana_filtro.destroy()
            global imagen_buscarfinal
            nonlocal idioma
            if idioma: 
                title = "Filtrar datos"
            else: title= "Filter data"
            ventana_filtro = tk.Toplevel()
            ventana_filtro.title(title)
            ventana_filtro.attributes("-fullscreen", True)
            ventana_filtro.resizable(width=False, height=False)
            ventana_filtro.attributes("-toolwindow", True)
            ventana_filtro.rowconfigure(2, weight=1)
            ventana_filtro.columnconfigure(1, weight=1)
            ventana_filtro.columnconfigure(2, weight=1) 
            imagen_buscar = Image.open(ruta_buscador)
            imagen_buscar25x25= imagen_buscar.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
            imagen_buscarfinal = ImageTk.PhotoImage(imagen_buscar25x25)
            style.configure("Custom.TFrame", background="#0878D7") 

            boton_volver = ttk.Button(ventana_filtro, image=imagen_volver, command=volver_atras2, style='PersonalizacionBoton2.TButton')
            boton_volver.grid(row=0, column=0, padx=5, pady=5, sticky='nw')
            
            frame_buscador = ttk.Frame(ventana_filtro, style= "Custom.TFrame")
            frame_buscador.grid(row=1, column=0)
            entry_busqueda = ttk.Entry(frame_buscador, width=18, font=("Arial", 25, "bold"))  
            entry_busqueda.grid(row=1, column=0)

            opciones_busqueda = ['Equipo', 'Local', 'Visitante', 'Set', 'Ganador', 'Cuartos', 'Semifinales', 'Final', 'Victorias', 'Porcentaje (V)', 'Derrotas','Porcentaje (D)', 'Relacion (V/D)']
            opciones_busqueda_ingles = ['Team', 'Home', 'Visitor', 'Set', 'Winner', 'Quarters', 'Semifinals', 'Final', 'Victories', 'Percentage (V)', 'Defeats', 'Percentage (D)', 'Relationship(W/L)']
            
            listbox_opciones = tk.Listbox(ventana_filtro)
            if idioma:
                for opcion in opciones_busqueda:
                    if df.applymap(lambda x: opcion in str(x)).any().any():
                        listbox_opciones.insert(tk.END, opcion)
                listbox_opciones.grid(row=2, column=0, padx=10, pady=5, sticky='s')
                listbox_opciones.configure(font=("Impact", 30), bg="#0878D7", fg="#00FF00", justify="center", width=30, height=10)
            else:
                for opcion in opciones_busqueda_ingles:
                    if df.applymap(lambda x: opcion in str(x)).any().any():
                        listbox_opciones.insert(tk.END, opcion)
                listbox_opciones.grid(row=2, column=0, padx=10, pady=5, sticky='s')
                listbox_opciones.configure(font=("Impact", 30), bg="#0878D7", fg="#00FF00", justify="center")
            
            def seleccionar_opcion(event):
                if listbox_opciones.curselection():
                    seleccion = listbox_opciones.get(listbox_opciones.curselection())
                    entry_busqueda.delete(0, tk.END)
                    entry_busqueda.insert(tk.END, seleccion)

            listbox_opciones.bind("<<ListboxSelect>>", seleccionar_opcion)
            
            def aplicar_filtro():
                termino_busqueda = entry_busqueda.get()  
                termino_busqueda2 = entry_busqueda2.get()  
                if all(filtros[i] for i in range(22)) and not trofeos_conseguidos[12]:
                    trofeos_conseguidos[12] = True
                    trofeo()
                else:
                    if (termino_busqueda == 'Local' or termino_busqueda == 'Visitante' or termino_busqueda == 'Home' or termino_busqueda== 'Visitor') and not filtros[0]:
                        filtros[0] = True
                    if termino_busqueda == 'Set' and not filtros[1]:
                        filtros[1] = True
                    if termino_busqueda == 'Set' and (termino_busqueda2 == 'Terminado en 2 sets' or termino_busqueda2 == 'Finished in 2 sets') and not filtros[2]:
                        filtros[2] = True
                    if termino_busqueda == 'Set' and (termino_busqueda2 == 'Terminado en 3 sets' or termino_busqueda2 == 'Finished in 3 sets') and not filtros[3]:
                        filtros[3] = True
                    if (termino_busqueda == 'Ganador' or termino_busqueda == 'Winner') and not filtros[4]:
                        filtros[4] = True
                    if (termino_busqueda == 'Cuartos' or termino_busqueda == 'Quarters') and not filtros[5]:
                        filtros[5] = True
                    if (termino_busqueda == 'Cuartos' or termino_busqueda == 'Quarters') and (termino_busqueda2 == 'Eliminado en Cuartos' or termino_busqueda2 == 'Eliminated in Quarters') and not filtros[6]:
                        filtros[6] = True
                    if (termino_busqueda == 'Cuartos' or termino_busqueda == 'Quarters') and (termino_busqueda2 == 'Pasa a Semifinales' or termino_busqueda2 == 'Go throught Semifinals') and not filtros[7]:
                        filtros[7] = True
                    if (termino_busqueda == 'Semifinales' or termino_busqueda == 'Semifinals') and not filtros[8]:
                        filtros[8] = True
                    if (termino_busqueda == 'Semifinales' or termino_busqueda == 'Semifinals') and (termino_busqueda2 == 'Eliminado en Semifinales' or termino_busqueda2 == 'Eliminated in Semifinals') and not filtros[9]:
                        filtros[9] = True
                    if (termino_busqueda == 'Semifinales' or termino_busqueda == 'Semifinals') and (termino_busqueda2 == 'Pasa a la Final' or termino_busqueda2 == 'Go throught the Final') and not filtros[10]:
                        filtros[10] = True
                    if termino_busqueda == 'Final' and not filtros[11]:
                        filtros[11] = True
                    if termino_busqueda == 'Final' and (termino_busqueda2 == 'Eliminado en la Final' or termino_busqueda2 == 'Eliminated in the Final') and not filtros[12]:
                        filtros[12] = True
                    if termino_busqueda == 'Final' and (termino_busqueda2 == 'Gana el torneo' or termino_busqueda2 == 'Wins the tournament') and not filtros[13]:
                        filtros[13] = True
                    if (termino_busqueda == 'Victorias' or termino_busqueda == 'Victories') and not filtros[14]:
                        filtros[14] = True
                    if (termino_busqueda == 'Victorias' or termino_busqueda == 'Victories') and termino_busqueda2 == '0' and not filtros[15]:
                        filtros[15] = True
                    if (termino_busqueda == 'Victorias' or termino_busqueda == 'Victories') and termino_busqueda2 == '1' and not filtros[16]:
                        filtros[16] = True
                    if (termino_busqueda == 'Victorias' or termino_busqueda == 'Victories') and termino_busqueda2 == '2' and not filtros[17]:
                        filtros[17] = True
                    if (termino_busqueda == 'Victorias' or termino_busqueda == 'Victories') and termino_busqueda2 == '3' and not filtros[18]:
                        filtros[18] = True
                    if (termino_busqueda == 'Victorias' or termino_busqueda == 'Derrotas' or termino_busqueda == 'Victories' or termino_busqueda == 'Defeats') and not filtros[19]:
                        filtros[19] = True
                    if (termino_busqueda == 'Porcentaje (V)' or termino_busqueda == 'Porcentaje (D)' or termino_busqueda == 'Percentage (V)' or termino_busqueda == 'Percentage (D)') and not filtros[20]:
                        filtros[20] = True
                    if (termino_busqueda == 'Relacion (V/D)' or termino_busqueda== 'Relationship(W/L)') and not filtros[21]:
                        filtros[21]= True

                if (termino_busqueda == 'Local' or termino_busqueda == 'Visitante' or termino_busqueda== 'Equipo' or termino_busqueda == 'Home' or termino_busqueda== 'Visitor' or termino_busqueda == 'Team') and not trofeos_conseguidos[4]:
                    trofeos_conseguidos[4] = True
                    trofeo()    
                if termino_busqueda == 'Set' and (termino_busqueda2 == 'Terminado en 2 sets' or termino_busqueda2 == 'Finished in 2 sets') and not trofeos_conseguidos[5]:
                    trofeos_conseguidos[5] = True
                    trofeo()
                if (termino_busqueda == 'Cuartos' or termino_busqueda == 'Semifinales' or termino_busqueda == 'Final' or termino_busqueda == 'Quarters' or termino_busqueda == 'Semifinals' or termino_busqueda == 'Final') and ('Eliminado en' in termino_busqueda2 or 'Eliminated in' in termino_busqueda2) and not trofeos_conseguidos[6]:
                    trofeos_conseguidos[6] = True
                    trofeo()
                if (termino_busqueda == 'Cuartos' or termino_busqueda == 'Semifinales' or termino_busqueda == 'Final' or termino_busqueda == 'Quarters' or termino_busqueda == 'Semifinals' or termino_busqueda == 'Final') and ('Pasa a' in termino_busqueda2 or 'Go throught' in termino_busqueda2 or 'Gana el troneo' in termino_busqueda2 or 'Wins the tournament') and not trofeos_conseguidos[7]:
                    trofeos_conseguidos[7] = True
                    trofeo()
                if (termino_busqueda == 'Victorias' or termino_busqueda == 'Derrotas' or termino_busqueda == 'Victories' or termino_busqueda == 'Defeats') and not trofeos_conseguidos[8]:
                    trofeos_conseguidos[8] = True
                    trofeo()
                if (termino_busqueda == 'Porcentaje (V)' or termino_busqueda == 'Porcentaje (D)' or termino_busqueda == 'Percentage (V)' or termino_busqueda == 'Percentage (D)') and termino_busqueda2 == '51-100' and not trofeos_conseguidos[9]:
                    trofeos_conseguidos[9] = True
                    trofeo()
                if (termino_busqueda == 'Relacion (V/D)' or termino_busqueda == 'Relationship(W/L)') and not trofeos_conseguidos[10]:
                    trofeos_conseguidos[10] = True
                    trofeo()

                df_filtrado = pd.DataFrame()  # Crear un DataFrame vacío para almacenar los datos filtrados
                for index, row in df.iterrows():
                    if idioma:
                        if termino_busqueda == 'Local'and termino_busqueda2 == row[0]:
                            df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda == 'Visitante'and termino_busqueda2 == row[1]:
                            df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda == 'Equipo' and termino_busqueda2 == row[0]:
                            df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda == 'Set': 
                            if termino_busqueda2 == 'Terminado en 2 sets' and row[4] == '' and row[5] != None:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == 'Terminado en 3 sets' and row[4] != '' and row[4] != 'Set 3' and row[5] != None:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda == 'Ganador' and row[5] != None and  termino_busqueda2 in row[5]:
                            df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda == 'Cuartos':
                            if termino_busqueda2 == 'Eliminado en Cuartos' and 'cae eliminado' in row[1]:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == 'Pasa a Semifinales' and 'pasa de ronda' in row[1]:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda == 'Semifinales':
                            if termino_busqueda2 == 'Eliminado en Semifinales' and 'cae eliminado' in row[2]:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == 'Pasa a la Final' and 'pasa de ronda' in row[2]:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda == 'Final':
                            if termino_busqueda2 == 'Eliminado en la Final' and 'pierde en la final' in row[3]:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == 'Gana el torneo' and 'gana el torneo' in row[3]:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda == 'Victorias':
                            if termino_busqueda2 == '0-30' and row[1] != 'Victorias' and (int(row[1])>=0 and int(row[1])<=30):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '31-70' and row[1] != 'Victorias' and (int(row[1])>=31 and int(row[1])<=70):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '71-150' and row[1] != 'Victorias' and (int(row[1])>=71 and int(row[1])<=150):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '151-300' and row[1] != 'Victorias' and (int(row[1])>=151 and int(row[1])<=300):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '301-1000' and row[1] != 'Victorias' and (int(row[1])>=301 and int(row[1])<=1000):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '1000+' and row[1] != 'Victorias' and int(row[1]) >1000:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '0' and row[4] != 'Victorias' and row[4] != '' and int(row[4]) == 0:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '1' and row[4] != 'Victorias' and row[4] != '' and int(row[4]) == 1:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '2' and row[4] != 'Victorias' and row[4] != '' and int(row[4]) == 2:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '3' and row[4] != 'Victorias' and row[4] != '' and int(row[4]) == 3:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda == 'Derrotas':
                            if termino_busqueda2 == '0-30' and row[3] != 'Derrotas' and (int(row[3])>=0 and int(row[3])<=30):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '31-70' and row[3] != 'Derrotas' and (int(row[3])>=31 and int(row[3])<=70):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '71-150' and row[3] != 'Derrotas' and (int(row[3])>=71 and int(row[3])<=150):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '151-300' and row[3] != 'Derrotas' and (int(row[3])>=151 and int(row[3])<=300):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '301-1000' and row[3] != 'Derrotas' and (int(row[3])>=301 and int(row[3])<=1000):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '1000+' and row[3] != 'Derrotas' and int(row[3]) >1000:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda== 'Porcentaje (V)':
                            if termino_busqueda2 == '0-10' and row[2] != ' Porcentaje (V)' and (round(float(row[2]), 2) >= 0.0 and round(float(row[2]), 2) <= 10.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '11-30' and row[2] != ' Porcentaje (V)' and (round(float(row[2]), 2) >= 11.0 and round(float(row[2]), 2) <= 30.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '31-50' and row[2] != ' Porcentaje (V)' and (round(float(row[2]), 2) >= 31.0 and round(float(row[2]), 2) <= 50.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '51-75' and row[2] != ' Porcentaje (V)' and (round(float(row[2]), 2) >= 51.0 and round(float(row[2]), 2) <= 75.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '76-100' and row[2] != ' Porcentaje (V)' and (round(float(row[2]), 2) >= 76.0 and round(float(row[2]), 2) <= 100.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '0-50' and row[2] != ' Porcentaje (V)' and (round(float(row[2]), 2) >= 0.0 and round(float(row[2]), 2) <= 50.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '51-100' and row[2] != ' Porcentaje (V)' and (round(float(row[2]), 2) >= 51.0 and round(float(row[2]), 2) <= 100.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda== 'Porcentaje (D)':
                            if termino_busqueda2 == '0-10' and row[4] != 'Porcentaje (D)' and (round(float(row[4]), 2) >= 0.0 and round(float(row[4]), 2) <= 10.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '11-30' and row[4] != 'Porcentaje (D)' and (round(float(row[4]), 2) >= 11.0 and round(float(row[4]), 2) <= 30.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '31-50' and row[4] != 'Porcentaje (D)' and (round(float(row[4]), 2) >= 31.0 and round(float(row[4]), 2) <= 50.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '51-75' and row[4] != 'Porcentaje (D)' and (round(float(row[4]), 2) >= 51.0 and round(float(row[4]), 2) <= 75.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '76-100' and row[4] != 'Porcentaje (D)' and (round(float(row[4]), 2) >= 76.0 and round(float(row[4]), 2) <= 100.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '0-50' and row[4] != 'Porcentaje (D)' and (round(float(row[4]), 2) >= 0.0 and round(float(row[4]), 2) <= 50.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '51-100' and row[4] != 'Porcentaje (D)' and (round(float(row[4]), 2) >= 51.0 and round(float(row[4]), 2) <= 100.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda == 'Relacion (V/D)':
                            if termino_busqueda2 == '0-0.25' and row[5] != 'Relacion (V/D)' and (round(float(row[5]), 2) >= 0.0 and round(float(row[5]), 2) <= 0.25):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '0.26-0.5' and row[5] != 'Relacion (V/D)' and (round(float(row[5]), 2) >= 0.26 and round(float(row[5]), 2) <= 0.50):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '0.51-0.75' and row[5] != 'Relacion (V/D)' and (round(float(row[5]), 2) >= 0.51 and round(float(row[5]), 2) <= 0.75):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '0.76-1' and row[5] != 'Relacion (V/D)' and (round(float(row[5]), 2) >= 0.76 and round(float(row[5]), 2) <= 1.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '0-0.5' and row[5] != 'Relacion (V/D)' and (round(float(row[5]), 2) >= 0.0 and round(float(row[5]), 2) <= 0.5):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '0.51-1' and row[5] != 'Relacion (V/D)' and (round(float(row[5]), 2) >= 0.51 and round(float(row[5]), 2) <= 1.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '1+' and row[5] != 'Relacion (V/D)' and round(float(row[5]), 2) >= 1.0:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                    else:
                        if termino_busqueda == 'Home'and termino_busqueda2 == row[0] :
                            df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda == 'Visitor'and termino_busqueda2 == row[1]:
                            df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda == 'Team' and termino_busqueda2 == row[0]:
                            df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda == 'Set': 
                            if termino_busqueda2 == 'Finished in 2 sets' and row[4] == '' and row[5] != None:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == 'Finished in 3 sets' and row[4] != '' and row[4] != 'Set 3' and row[5] != None:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda == 'Winner' and row[5] != None and  termino_busqueda2 in row[5]:
                            df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda == 'Quarters':
                            if termino_busqueda2 == 'Eliminated in Quarters' and 'is eliminated' in row[1]:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == 'Go throught Semifinals' and 'go throught' in row[1]:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda == 'Semifinales':
                            if termino_busqueda2 == 'Eliminated in Semifinals' and 'is eliminated' in row[2]:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == 'Go throught the Final' and 'go throught' in row[2]:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda == 'Final':
                            if termino_busqueda2 == 'Eliminated in the Final' and 'loses in the final' in row[3]:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == 'Wins the tournament' and 'is the winner' in row[3]:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda == 'Victories':
                            if termino_busqueda2 == '0-30' and row[1] != 'Victories' and (int(row[1])>=0 and int(row[1])<=30):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '31-70' and row[1] != 'Victories' and (int(row[1])>=31 and int(row[1])<=70):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '71-150' and row[1] != 'Victories' and (int(row[1])>=71 and int(row[1])<=150):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '151-300' and row[1] != 'Victories' and (int(row[1])>=151 and int(row[1])<=300):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '301-1000' and row[1] != 'Victories' and (int(row[1])>=301 and int(row[1])<=1000):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '1000+' and row[1] != 'Victories' and int(row[1]) >1000:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '0' and row[4] != 'Victories' and row[4] != '' and int(row[4]) == 0:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '1' and row[4] != 'Victories' and row[4] != '' and int(row[4]) == 1:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '2' and row[4] != 'Victories' and row[4] != '' and int(row[4]) == 2:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '3' and row[4] != 'Victories' and row[4] != '' and int(row[4]) == 3:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda == 'Defeats':
                            if termino_busqueda2 == '0-30' and row[3] != 'Defeats' and (int(row[3])>=0 and int(row[3])<=30):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '31-70' and row[3] != 'Defeats' and (int(row[3])>=31 and int(row[3])<=70):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '71-150' and row[3] != 'Defeats' and (int(row[3])>=71 and int(row[3])<=150):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '151-300' and row[3] != 'Defeats' and (int(row[3])>=151 and int(row[3])<=300):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '301-1000' and row[3] != 'Defeats' and (int(row[3])>=301 and int(row[3])<=1000):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '1000+' and row[3] != 'Defeats' and int(row[3]) >1000:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda== 'Percentage (V)':
                            if termino_busqueda2 == '0-10' and row[2] != 'Percentage (V)' and (round(float(row[2]), 2) >= 0.0 and round(float(row[2]), 2) <= 10.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '11-30' and row[2] != 'Percentage (V)' and (round(float(row[2]), 2) >= 11.0 and round(float(row[2]), 2) <= 30.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '31-50' and row[2] != 'Percentage (V)' and (round(float(row[2]), 2) >= 31.0 and round(float(row[2]), 2) <= 50.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '51-75' and row[2] != 'Percentage (V)' and (round(float(row[2]), 2) >= 51.0 and round(float(row[2]), 2) <= 75.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '76-100' and row[2] != 'Percentage (V)' and (round(float(row[2]), 2) >= 76.0 and round(float(row[2]), 2) <= 100.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '0-50' and row[2] != 'Percentage (V)' and (round(float(row[2]), 2) >= 0.0 and round(float(row[2]), 2) <= 50.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '51-100' and row[2] != 'Percentage (V)' and (round(float(row[2]), 2) >= 51.0 and round(float(row[2]), 2) <= 100.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda== 'Percentage (D)':
                            if termino_busqueda2 == '0-10' and row[4] != 'Percentage (D)' and (round(float(row[4]), 2) >= 0.0 and round(float(row[4]), 2) <= 10.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '11-30' and row[4] != 'Percentage (D)' and (round(float(row[4]), 2) >= 11.0 and round(float(row[4]), 2) <= 30.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '31-50' and row[4] != 'Percentage (D)' and (round(float(row[4]), 2) >= 31.0 and round(float(row[4]), 2) <= 50.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '51-75' and row[4] != 'Percentage (D)' and (round(float(row[4]), 2) >= 51.0 and round(float(row[4]), 2) <= 75.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '76-100' and row[4] != 'Percentage (D)' and (round(float(row[4]), 2) >= 76.0 and round(float(row[4]), 2) <= 100.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '0-50' and row[4] != 'Percentage (D)' and (round(float(row[4]), 2) >= 0.0 and round(float(row[4]), 2) <= 50.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '51-100' and row[4] != 'Percentage (D)' and (round(float(row[4]), 2) >= 51.0 and round(float(row[4]), 2) <= 100.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                        elif termino_busqueda == 'Relationship(W/L)':
                            if termino_busqueda2 == '0-0.25' and row[5] != 'Relationship(W/L)' and (round(float(row[5]), 2) >= 0.0 and round(float(row[5]), 2) <= 0.25):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '0.26-0.5' and row[5] != 'Relationship(W/L)' and (round(float(row[5]), 2) >= 0.26 and round(float(row[5]), 2) <= 0.50):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '0.51-0.75' and row[5] != 'Relationship(W/L)' and (round(float(row[5]), 2) >= 0.51 and round(float(row[5]), 2) <= 0.75):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '0.76-1' and row[5] != 'Relationship(W/L)' and (round(float(row[5]), 2) >= 0.76 and round(float(row[5]), 2) <= 1.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '0-0.5' and row[5] != 'Relationship(W/L)' and (round(float(row[5]), 2) >= 0.0 and round(float(row[5]), 2) <= 0.5):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '0.51-1' and row[5] != 'Relationship(W/L)' and (round(float(row[5]), 2) >= 0.51 and round(float(row[5]), 2) <= 1.0):
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                            elif termino_busqueda2 == '1+' and row[5] != 'Relationship(W/L)' and round(float(row[5]), 2) >= 1.0:
                                df_filtrado = pd.concat([df_filtrado, pd.DataFrame(row).transpose()], ignore_index=True)
                
                treeview.delete(*treeview.get_children()[2:])
                treeview.insert("", "end", "empty_row", values=[""], tags=("sin_contenido",))
                ultimo_indice = 2
                for row_index, fila in df_filtrado.iterrows():
                    valores = fila.tolist()
                    element_id = f"row_{ultimo_indice + row_index + 1}"
                    treeview.insert("", "end", element_id, values=valores, tags=("con_contenido",))
                    treeview.insert("", "end", f"empty_{ultimo_indice + row_index + 1}", values=[""], tags="sin_contenido")
            
            def opcion_filtro():
                global entry_busqueda2
                frame_buscador2 = ttk.Frame(ventana_filtro, style= "Custom.TFrame")
                frame_buscador2.grid(row=1, column=2)
                entry_busqueda2 = ttk.Entry(frame_buscador2, width=30, font=("Arial", 25, "bold"))  
                entry_busqueda2.grid(row=1, column=2)        
                opciones_busqueda2=[]
                listbox_opciones2 = tk.Listbox(ventana_filtro)
                if idioma:
                    if listbox_opciones.get(listbox_opciones.curselection()) == 'Equipo' or listbox_opciones.get(listbox_opciones.curselection()) == 'Local' or listbox_opciones.get(listbox_opciones.curselection()) == 'Visitante' or listbox_opciones.get(listbox_opciones.curselection()) == 'Ganador':
                        opciones_busqueda2=['La Coruna', 'Murcia', 'Toledo', 'Bilbao', 'Madrid', 'Barcelona', 'Sevilla', 'Malaga']
                    elif listbox_opciones.get(listbox_opciones.curselection()) == 'Set':
                        opciones_busqueda2=['Terminado en 2 sets', 'Terminado en 3 sets']
                    elif listbox_opciones.get(listbox_opciones.curselection()) == 'Cuartos':
                        opciones_busqueda2=['Eliminado en Cuartos', 'Pasa a Semifinales']
                    elif listbox_opciones.get(listbox_opciones.curselection()) == 'Semifinales':
                        opciones_busqueda2=['Eliminado en Semifinales', 'Pasa a la Final']
                    elif listbox_opciones.get(listbox_opciones.curselection()) == 'Final':
                        opciones_busqueda2=['Eliminado en la Final', 'Gana el torneo']
                    elif listbox_opciones.get(listbox_opciones.curselection()) == 'Victorias' and df.loc[0,4] != 'Victorias' or listbox_opciones.get(listbox_opciones.curselection()) == 'Derrotas':
                        opciones_busqueda2=['0-30','31-70', '71-150', '151-300', '301-1000', '1000+']
                    elif listbox_opciones.get(listbox_opciones.curselection()) == 'Victorias' and df.loc[0,4] == 'Victorias':
                        opciones_busqueda2=['0','1', '2', '3']
                    elif listbox_opciones.get(listbox_opciones.curselection()) == 'Porcentaje (V)' or listbox_opciones.get(listbox_opciones.curselection()) == 'Porcentaje (D)':
                        opciones_busqueda2=['0-10', '11-30', '31-50', '51-75', '76-100', '0-50', '51-100'] 
                    elif listbox_opciones.get(listbox_opciones.curselection()) == 'Relacion (V/D)':
                        opciones_busqueda2=['0-0.25', '0.26-0.5', '0.51-0.75', '0.76-1', '0-0.5', '0.51-1', '1+']
                else:
                    if listbox_opciones.get(listbox_opciones.curselection()) == 'Team' or listbox_opciones.get(listbox_opciones.curselection()) == 'Home' or listbox_opciones.get(listbox_opciones.curselection()) == 'Visitor' or listbox_opciones.get(listbox_opciones.curselection()) == 'Winner':
                        opciones_busqueda2=['La Coruna', 'Murcia', 'Toledo', 'Bilbao', 'Madrid', 'Barcelona', 'Sevilla', 'Malaga']
                    elif listbox_opciones.get(listbox_opciones.curselection()) == 'Set':
                        opciones_busqueda2=['Finished in 2 sets', 'Finished in 3 sets']
                    elif listbox_opciones.get(listbox_opciones.curselection()) == 'Quarters':
                        opciones_busqueda2=['Eliminated in Quarters', 'Go throught Semifinals']
                    elif listbox_opciones.get(listbox_opciones.curselection()) == 'Semifinals':
                        opciones_busqueda2=['Eliminated in Semifinals', 'Go throught the Final']
                    elif listbox_opciones.get(listbox_opciones.curselection()) == 'Final':
                        opciones_busqueda2=['Eliminated in the Final', 'Wins the tournament']
                    elif listbox_opciones.get(listbox_opciones.curselection()) == 'Victories' and df.loc[0,4] != 'Victories' or listbox_opciones.get(listbox_opciones.curselection()) == 'Defeats':
                        opciones_busqueda2=['0-30','31-70', '71-150', '151-300', '300-1000', '1000+']
                    elif listbox_opciones.get(listbox_opciones.curselection()) == 'Victories' and df.loc[0,4] == 'Victories':
                        opciones_busqueda2=['0','1', '2', '3']
                    elif listbox_opciones.get(listbox_opciones.curselection()) == 'Percentage (V)' or listbox_opciones.get(listbox_opciones.curselection()) == 'Percentage (D)':
                        opciones_busqueda2=['0-10', '11-30', '31-50', '51-75', '76-100', '0-50', '51-100']
                    elif listbox_opciones.get(listbox_opciones.curselection()) == 'Relationship(W/L)':
                        opciones_busqueda2=['0-0.25', '0.26-0.5', '0.51-0.75', '0.76-1', '0-0.5', '0.51-1', '1+']
                
                listbox_opciones2.delete(0, tk.END)
                for opcion in opciones_busqueda2:
                    listbox_opciones2.insert(tk.END, opcion)
                
                listbox_opciones2.grid(row=2, column=2, padx=10, pady=5, sticky='s')
                listbox_opciones2.configure(font=("Impact", 30), bg="#0878D7", fg="#00FF00", justify="center", width=30, height=10)
                
                def seleccionar_opcion2(event):
                    if listbox_opciones2.curselection():
                        seleccion2 = listbox_opciones2.get(listbox_opciones2.curselection())
                        entry_busqueda2.delete(0, tk.END)
                        entry_busqueda2.insert(tk.END, seleccion2)
                    
                listbox_opciones2.bind("<<ListboxSelect>>", seleccionar_opcion2)
                
                boton_buscar2 = ttk.Button(frame_buscador2, image=imagen_buscarfinal, compound='center', command=aplicar_filtro, style="PersonalizacionBoton.TButton")
                boton_buscar2.grid(row=1, column=2, sticky='e')

            boton_buscar = ttk.Button(frame_buscador, image=imagen_buscarfinal, compound='center', command=opcion_filtro, style="PersonalizacionBoton.TButton")
            boton_buscar.grid(row=1, column=1, sticky='e')
            
        if idioma:
            texto_filtrar= "Filtrar datos"
            texto_limpiar= "Limpiar filtros"
        else: 
            texto_filtrar= "Filter data"
            texto_limpiar= "Clean filters"

        boton_filtrar = ttk.Button(ventana_tabla, text=texto_filtrar, image= imagen_filtrar_datosfinal, compound='top', command=filtrar_datos,  style="Flat.TButton")
        boton_filtrar.configure(width=ancho_boton)  
        boton_filtrar.grid(row=0, column=0, padx=10, pady=10)

        def limpiar_filtros():
            if not trofeos_conseguidos[11]:
                trofeos_conseguidos[11]= True
                trofeo()
            treeview.delete(*treeview.get_children())
            for row_index, fila in df.iterrows():
                valores = fila.tolist()
                element_id = f"row_{row_index}"
                treeview.insert("", "end", element_id, tags=("sin_contenido",))
                if any(valores):  # Verificar si la línea no está vacía
                    valores_filtrados = [v if v is not None else "" for v in valores]
                    treeview.insert("", "end", values=valores_filtrados, tags=("con_contenido",))
                else:
                    treeview.insert("", "end", values=[""], tags=("sin_contenido",))
                    treeview.item(element_id, tags=("sin_contenido",))
        
        boton_limpiar = ttk.Button(ventana_tabla, text=texto_limpiar, image= imagen_limpiar_filtrofinal, compound='top', command=limpiar_filtros,  style="Flat.TButton")
        boton_limpiar.configure(width=ancho_boton)  
        boton_limpiar.grid(row=0, column=0, padx=10, pady=10, sticky='s')
        
        treeview = ttk.Treeview(ventana_tabla, show="tree", style="Custom.Treeview")  
        treeview.update()
        columnas = df.columns.tolist()
        treeview["columns"] = columnas
        for i, col in enumerate(columnas):
            ancho_columna = int(ancho_tabla / (len(columnas)*2))
            treeview.column(i, width=ancho_columna, anchor='w')
        style.configure("Custom.Treeview", background="#D3EAFD", foreground="black", fieldbackground="#D3EAFD", rowheight=25)
        style2.configure("Custom.Treeview_sincontenido", background="black", foreground="white", rowheight= 10)
        treeview.tag_configure("con_contenido", background="#D3EAFD", foreground="black", font=("Arial-Black", 10, "bold"))
        treeview.tag_configure("sin_contenido", background="white", foreground="white")
        treeview.tag_configure("Custom.Treeview.Row", background="#D3EAFD", foreground="black")
        style.map("Custom.Treeview", background=[("selected", "#0078D7")])
        style2.map("Custom.Treeview_sincontenido", background=[("selected", "#0078D7")])
        style.configure("Vertical.TScrollbar",
                gripcount=0,
                background="#0078D7",  
                darkcolor="#005EBF",  
                troughcolor="#D3EAFD"  
                )
        
        for row_index, fila in df.iterrows():
            valores = fila.tolist()
            element_id = f"row_{row_index}"
            treeview.insert("", "end", element_id, tags=("sin_contenido",))
            
            if any(valores):  
                valores_filtrados = [v if v is not None else "" for v in valores]
                treeview.insert("", "end", values=valores_filtrados, tags=("con_contenido",))
            else:
                treeview.insert("", "end", values=[""], tags=("sin_contenido",))
                treeview.item(element_id, tags=("sin_contenido",))
            
        treeview.columnconfigure(0, weight=ancho_tabla)
        treeview.grid(row=0, column=1, sticky="nsew")
        ventana_tabla.grid_rowconfigure(0, weight=1)
        ventana_tabla.grid_columnconfigure(1, weight=1)

        scrollbar = ttk.Scrollbar(ventana_tabla, orient="vertical", command=treeview.yview, style="Vertical.TScrollbar")
        treeview.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=2, sticky="nes")

        ventana_tabla.mainloop()
    
    def borrar_datos():
        if not trofeos_conseguidos[13]:
            trofeos_conseguidos[13]= True
            trofeo()
        with open(ruta_partidosCSV, mode='w') as archivo_csv:
            archivo_csv.truncate()
        with open(ruta_resultadosCSV, mode='w') as archivo_csv:
            archivo_csv.truncate()
        with open(ruta_victoriasCSV, mode='w') as archivo_csv:
            archivo_csv.truncate()
        with open(ruta_gamesCSV, mode='w') as archivo_csv:
            archivo_csv.truncate()
        with open(ruta_victoriesCSV, mode='w') as archivo_csv:
            archivo_csv.truncate()
        with open(ruta_resultsCSV, mode='w') as archivo_csv:
            archivo_csv.truncate()
        if idioma:
            messagebox.showinfo("Borrar Datos", "Los datos han sido borrados.")
        else: messagebox.showinfo("Delete data", "Data deleted")
    
    def salir_aplicacion():
        with open(ruta_partidosCSV, mode='w') as archivo_csv:
            archivo_csv.truncate()
        with open(ruta_resultadosCSV, mode='w') as archivo_csv:
            archivo_csv.truncate()
        with open(ruta_victoriasCSV, mode='w') as archivo_csv:
            archivo_csv.truncate()
        with open(ruta_gamesCSV, mode='w') as archivo_csv:
            archivo_csv.truncate()
        with open(ruta_victoriesCSV, mode='w') as archivo_csv:
            archivo_csv.truncate()
        with open(ruta_resultsCSV, mode='w') as archivo_csv:
            archivo_csv.truncate()
        sys.exit()
    
    if idioma:
        titulo_ventana= "Torneo de Padel"
    else: titulo_ventana = "Padel Tournament"
    ventana.title(titulo_ventana)
    ventana.attributes('-fullscreen', True) 
    ventana.configure(bg="#03254c")
    ancho_imagen= 125
    alto_imagen=120
    imagen_borrar = PhotoImage(file=ruta_borrar)
    imagen_estadisticas_equipos = PhotoImage(file=ruta_estadisticas_equipos)
    imagen_estadisticas_partidos = PhotoImage(file=ruta_estadisticas_partidos)
    imagen_estadisticas_torneos = PhotoImage(file=ruta_estadisticas_torneos)
    imagen_salir = PhotoImage(file=ruta_salir)
    imagen_simular_torneo = PhotoImage(file=ruta_simular_torneo)
    imagen_ayuda = PhotoImage(file=ruta_ayuda)
    imagen_trofeos = Image.open(ruta_trofeo)
    imagen_trofeos125x120= imagen_trofeos.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
    imagen_trofeosfinal = ImageTk.PhotoImage(imagen_trofeos125x120)
    imagen_español = Image.open(ruta_español)
    imagen_español125x120= imagen_español.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
    imagen_españolfinal = ImageTk.PhotoImage(imagen_español125x120)
    imagen_ingles = Image.open(ruta_ingles)
    imagen_ingles125x120= imagen_ingles.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
    imagen_inglesfinal = ImageTk.PhotoImage(imagen_ingles125x120)
    imagen_volumenON = Image.open(ruta_volumenON)
    imagen_volumenON125x120 = imagen_volumenON.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
    imagen_volumenONfinal=ImageTk.PhotoImage(imagen_volumenON125x120)
    imagen_volumenOFF = Image.open(ruta_volumenOFF)
    imagen_volumenOFF125x120 = imagen_volumenOFF.resize((ancho_imagen,alto_imagen),Image.LANCZOS)
    imagen_volumenOFFfinal=ImageTk.PhotoImage(imagen_volumenOFF125x120)
    ancho_pantalla = ventana.winfo_screenwidth()
    altura_pantalla = ventana.winfo_screenheight()
    ancho_boton = int(ancho_pantalla * 0.25)
    altura_boton = int(altura_pantalla * 0.2)
    ventana.grid_columnconfigure(0, weight=1, minsize=ancho_boton)
    ventana.grid_columnconfigure(1, weight=1, minsize=ancho_boton)
    ventana.grid_columnconfigure(2, weight=1, minsize=ancho_boton)
    ventana.grid_rowconfigure(0, weight=1, minsize=altura_boton)
    ventana.grid_rowconfigure(1, weight=1, minsize=altura_boton)
    ventana.style = ttk.Style()
    ventana.style.theme_use('default')
    ventana.style.configure('PersonalizacionBoton.TButton',
                        background='#03254c',
                        foreground='#D4AF37',
                        font=('impact', 15),
                        relief='flat')
    ventana.style.map('PersonalizacionBoton.TButton',
                background=[('active', 'light blue')])
    ventana.style.configure('PersonalizacionBoton.TButton:hover',
                        background='light blue',
                        foreground='black',
                        font=('impact', 15),
                        relief='gr',
                        cursor= 'hand2')
    
    encabezado = Label(ventana, text="Bienvenido a PadelDash", font=("Arial", 50, 'bold'),
                fg='yellow', bg='#007BFF', relief='raised', bd=5)
    encabezado.configure(font=font.Font(family='impact', size=50))
    encabezado.grid(row=0, column=0, columnspan=3, padx=10, pady=(20, 10))

    boton_simular = ttk.Button(ventana, text="Simular Torneo", image=imagen_simular_torneo, compound="top", command=simular_torneo, style='PersonalizacionBoton.TButton')
    boton_simular.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
    boton_historial_partidos = ttk.Button(ventana, text="Mostrar Historial de Partidos", image=imagen_estadisticas_partidos, compound="top", command=mostrar_historial_partidos, style='PersonalizacionBoton.TButton')
    boton_historial_partidos.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    boton_historial_torneos = ttk.Button(ventana, text="Mostrar Historial de Torneos", image=imagen_estadisticas_torneos, compound="top", command=mostrar_historial_torneos, style='PersonalizacionBoton.TButton')
    boton_historial_torneos.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
    boton_estadisticas_equipos = ttk.Button(ventana, text="Mostrar Estadísticas de Equipos", image=imagen_estadisticas_equipos, compound="top", command=mostrar_estadisticas_equipos, style='PersonalizacionBoton.TButton')
    boton_estadisticas_equipos.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
    boton_borrar_datos = ttk.Button(ventana, text="Borrar Datos", image=imagen_borrar, compound="top", command=borrar_datos, style='PersonalizacionBoton.TButton')
    boton_borrar_datos.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
    boton_ayuda = ttk.Button(ventana,text="Ayuda", image=imagen_ayuda, compound='top', command=abrir_ventana_ayuda, style='PersonalizacionBoton.TButton')
    boton_ayuda.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
    boton_salir = ttk.Button(ventana, image=imagen_salir, compound="top", command=salir_aplicacion, style='PersonalizacionBoton.TButton')
    boton_salir.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky="ne")
    boton_ingles = ttk.Button(ventana, image=imagen_inglesfinal, compound="center", command=cambiar_idioma_ingles, style='PersonalizacionBoton.TButton')
    boton_ingles.grid(row=0, column=0, padx=5, pady=5, sticky='s')
    boton_español = ttk.Button(ventana, image=imagen_españolfinal, compound="center", command=cambiar_idioma_español, style='PersonalizacionBoton.TButton')
    boton_español.grid(row=0, column=0, padx=5, pady=5, sticky='sw')
    boton_volumen = ttk.Button(ventana, image=imagen_volumenONfinal, command=toggle_mute)
    boton_volumen.grid(row=0, column=0,padx=5, pady=5, sticky='n')
    boton_trofeos = ttk.Button(ventana, image =imagen_trofeosfinal, command= mostrar_trofeos)
    boton_trofeos.grid(row=0, column=0, padx=5, pady=5, sticky='nw')
    ventana.mainloop()
generar_interfaz()

if __name__ == '__main__':
    main()