'''
Script elaborado por: Jeferson Yesid Gonzalez Ortiz
Github: @T4ya
hacer código en Python que me calculé cuánto necesito sacar en dos parciales de 3 que 
hacen, para aprobar una curso, conociendo la nota del primer parcial Los procengajes son 25 30 35 respectivamente
Esto lo tengo que hacer en python y crear un .exe que me ejecute el script
'''

import subprocess
#Funcion para instalar los paquetes necesarios para ejecutar el programa
def instalar_paquetes():
    """
    Instalar los paquetes necesarios para ejecutar el programa
    """
    packages = ['sympy', 'rich']
    for package in packages:
        try:
            subprocess.check_call(['pip', 'install', package])
        except subprocess.CalledProcessError as e:
            print(f"\nError, no se han podido instalar los paquetes{package}: {e}\n")
        else:
            print(f"\nPaquete {package} instalado satisfactoriamente!\n")

#Llamar a la funcion install_packages
instalar_paquetes()
    
#Importar las librerias necesarias para ejecutar el programa
from time import sleep
import sys
import sympy as sp
from sympy import Symbol, Eq, solve
import os
import rich
import sys
from rich.console import Console
from rich.table import Table
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
#from rich.style import Style

class Estudiante:
    def __init__(self, nota1, nota2, nota3):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        #Suma de notas minimas para aprobar
        self.Suma_Aprobatoria = 3

    #limpiar la terminal por sistema operativo
    def Limpiar(self):
        if sys.platform.startswith('win'):
            os.system('cls') #Windows
        else:
            os.system('clear') #Linux o Mac
        
    #Funcion para darle negrita a un texto
    def Negrita(self, texto):
        return f"[bold]{texto}[/bold]"

    #Funcion para imprimir el menu en un panel
    def Menu(self):
        #Crear un panel
        panel = Panel(Text("Bienvenido, yo te ayudaré en tu desesperación\nElaborado por: Jeferson Yesid Gonzalez Ortiz :D\nGithub: @T4ya", justify="center"), title="CALCULADORA DE NOTA REQUERIDA", style="bold white")
        #Imprimir el panel
        print(panel)
    
    #Funcion para preguntar si el estudiante hizo el 1er, 2do o 3er parcial
    def Preguntas(self):
        #Pedir la nota que sacó el estudiante en el primer parcial
        while True:
            try:
                #Usar la libreria rich para hacer el programa mas interactivo
                self.nota1 =   float(Prompt.ask("[bold]\nIngrese la nota del primer parcial[/bold] -->"))
                if self.nota1 > 5:
                    print("[bold red]\n¡ERROR![/bold red] La nota no puede ser mayor a 5")
                elif self.nota1 < 0:
                    print("[bold red]\n¡ERROR![/bold red] La nota no puede ser menor a 0")
                else:
                    break
            except ValueError:
                print("[bold red]\n¡ERROR![/bold red] El valor ingresado no es válido. Intente nuevamente...")
        
        #Preguntar si el estudiante hizo el segundo parcial
        while True:
            try:
                parcial2 = int(Prompt.ask("[bold]\n¿Ya hizo el segundo parcial?[/bold] [1] Si [2] No -->"))
                if parcial2 == 1:
                    self.nota2 = float(Prompt.ask("[bold]\nIngrese la nota del segundo parcial[/bold] -->"))
                    break
                elif parcial2 == 2:
                    break
                else:
                    print("[bold red]\n¡ERROR![/bold red] La opción ingresada no es válida. Intente nuevamente...")
            except ValueError:
                print("[bold red]\n¡ERROR![/bold red] El valor ingresado no es válido. Intente nuevamente...")

        #Ejecutar la funcion Calculo
        self.Calculo()
        
    #Funcion para calcular la nota que el estudiante necesita para aprobar según las notas que ya tiene
    def Calculo(self):
        #Caso1: El estudiante ya hizo el parcial 1 y 2
        if self.nota1 != None and self.nota2 != None:
            #Utilizar la libreria sympy para resolver la ecuacion
            x = Symbol('x')
            #Ecuacion para calcular la nota que necesita el estudiante en el tercer parcial
            #(3 = (nota1 * 0.35) + (nota2 * 0.30) + (x * 0.35))
            ecuacion = Eq(self.Suma_Aprobatoria, (self.nota1 * 0.35) + (self.nota2 * 0.30) + (x * 0.35))
            #Resolver la ecuacion
            solucion = solve(ecuacion)
            if solucion[0] > 5:
                print(f"[bold red]Sacando ({self.nota1}) en el parcial #1 y ({self.nota2}) en el parcial #2 no es posible aprobar el curso :'C[/bold red]\n")
            elif solucion[0] < 0:
                print(f"[bold green]Sacando {self.nota1} en el parcial #1 y {self.nota2} en el parcial #2 ya aprobaste el curso necesitas sacar solo {solucion[0]:.2f} en el tercer parcial, ¡Felicidades! :D[/bold green]\n")
            else:
                #Imprimir la solucion
                print(f"[bold blue]Para aprobar el curso debes sacar en el tercer parcial: {solucion[0]:.2f}, ¡Ánimo![/bold blue]\n")
                
        #Caso2: El estudiante ya hizo el parcial 1, se le pregunta cual nota planea sacar en el parcial 2
        elif self.nota1 != None:
            #Preguntar cual nota planea sacar en el parcial 2
            while True:
                try:
                    nota2 = float(Prompt.ask("[bold]\n¿Qué nota planeas sacar en el segundo parcial?[/bold] -->"))
                    break
                except ValueError:
                    print("[bold red]\n¡ERROR![/bold red] El valor ingresado no es válido. Intente nuevamente...")
            #Utilizar la libreria sympy para resolver la ecuacion
            x = Symbol('x')
            #Ecuacion para calcular la nota que necesita el estudiante en el tercer parcial
            #(3 = (nota1 * 0.35) + (nota2 * 0.30) + (x * 0.35))
            ecuacion = Eq(self.Suma_Aprobatoria, (self.nota1 * 0.35) + (nota2 * 0.30) + (x * 0.35))
            #Resolver la ecuacion
            solucion = solve(ecuacion)
            if solucion[0] > 5:
                print(f"[bold red]Sacando ({self.nota1}) en el parcial #1 y ({nota2}) en el parcial #2 no es posible aprobar el curso :'C[/bold red]\n")
            elif solucion[0] < 0:
                print(f"[bold green]Sacando ({self.nota1}) en el parcial #1 y ({nota2}) en el parcial #2 ya aprobaste el curso necesitas sacar solo {solucion[0]:.2f} en el tercer parcial, ¡Felicidades! :D[/bold green]\n")
            else:
                #Imprimir la solucion
                print(f"[bold blue]Para aprobar el curso debes sacar en el tercer parcial: {solucion[0]:.2f}, ¡Ánimo![/bold blue]\n")

    #Funcion para limpiar la consola y preguntar si desea volver a ejecutar el programa
    def Reiniciar(self):
        #Preguntar si desea volver a ejecutar el programa
        while True:
            try:
                reiniciar = int(Prompt.ask("[bold]\n¿Desea volver a ejecutar el programa?[/bold] [1] Si [2] No -->"))
                if reiniciar == 1:
                    #Limpiar la terminal
                    self.Limpiar()
                    #Llamar a la funcion Menu
                    self.Menu()
                    #Llamar a la funcion Preguntas
                    self.Preguntas()
                    #Llamar a la funcion Reiniciar
                    self.Reiniciar()
                    break
                elif reiniciar == 2:
                    print("[bold]\n¡Gracias por usar el programa! :D[/bold]")
                    sleep(2)
                    sys.exit()
                else:
                    print("[bold red]\n¡ERROR![/bold red] La opción ingresada no es válida. Intente nuevamente...")
            except ValueError:
                print("[bold red]\n¡ERROR![/bold red] El valor ingresado no es válido. Intente nuevamente...")


if __name__ == '__main__':
    #Instanciar la clase
    estudiante = Estudiante(None, None, None)
    #Limpiar la terminal
    estudiante.Limpiar()
    #Llamar a la funcion Menu
    estudiante.Menu()
    #Llamar a la funcion Preguntas
    estudiante.Preguntas()
    #Llamar a la funcion Reiniciar
    estudiante.Reiniciar()
