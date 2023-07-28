from django.shortcuts import render

# Create your views here.

from SalasCuna_api.models import ChildState

from django.http import HttpResponse

import os
import pandas as pd
import numpy

# {'SALA CUNA': 'I.0041',
# 'APELLIDO': 'ABBA',
# 'NOMBRE': 'MIA OLIVIA',
# 'N DNI': '59074326',
# 'FECHA DE NACIMIENTO': datetime.datetime(2021, 12, 3, 0, 0),
# 'EDAD': 1,
# 'SEXO': 'F',
# 'CALLE': 'ITUZAINGO',
# 'NUMERO': 'S/N',
# 'DEPARTAMENTO': 'CALAMUCHITA',
# 'LOCALIDAD': 'SAN AGUSTIN',
# 'CARACTERISTICA TELEFONICA': 3547,
# 'TELEFONO': 564346,
# 'APELLIDO Y NOMBRE': 'VELARDEZ SOLEDAD',
# 'DNI': '29437676',
# 'TURNO': 'MAÑANA',
# 'ESTADO': 'SIN MODIFICAR'}

def storage_method(request):
    rta = "todo bien"

    try:
        folder_path = '..//02. FEBREROS A DATOS'
        folders = [f for f in os.listdir(folder_path)]
        
        for folder in folders:
            files = [f for f in os.listdir(f'{folder_path}//{folder}')]
            
            # analize each file
            for file in files:
                print(file)
                
                # file is .xslm ?
                if file[-4:len(file)] == 'xlsm':

                    # read excel file
                    file_path = os.path.abspath(f"{folder_path}//{folder}//{file}")
                    df = pd.read_excel(file_path, )
                    
                    # analize each col index until see data
                    for num in range(len(df['Unnamed: 1'])):

                        # create object
                        obj = [df[col][num] for col in df.columns]
                        print(obj)
                        file_table = {
                            'SALA CUNA': obj[1],
                            'APELLIDO': obj[2],
                            'NOMBRE': obj[3],
                            'N DNI': obj[4],
                            'FECHA DE NACIMIENTO': obj[5],
                            'EDAD': obj[6],
                            'SEXO': obj[7],
                            'CALLE': obj[8],
                            'NUMERO': obj[9],
                            'DEPARTAMENTO': obj[10],
                            'LOCALIDAD': obj[11],
                            'CARACTERISTICA TELEFONICA': obj[12],
                            'TELEFONO': obj[13],
                            'APELLIDO Y NOMBRE': obj[14],
                            'DNI': obj[15],
                            'TURNO': obj[16],
                            'ESTADO': obj[17],
                        }
                        if file_table['SALA CUNA'] != 'SALA CUNA' and not pd.isna(file_table['NOMBRE']) and not pd.isna(file_table['APELLIDO']) and not pd.isna(file_table['APELLIDO Y NOMBRE']):
                            print(f'file_table: {file_table}')
                            rta = str(file_table)
                            break
                    break
                break
            break
        

    except Exception as e:
        rta = f"error: {e}"

    return HttpResponse(rta)

# import os
# import pandas as pd
# import numpy

# def migration(request):
#     rta = 'todo bien'
#     try:
#         # obtain files
#         folder_path = '..//02. FEBREROS A DATOS' #//COMUNAS Y MUNICIPIOS'
#         folders = [f for f in os.listdir(folder_path)]
        

#         for folder in folders:
#             files = [f for f in os.listdir(f'{folder_path}//{folder}')]
            
#             print(folder)
#             print(f'{folder_path}//{folder}')
            
#             # analize each file
#             for file in files:
#                 print(file)
                
#                 # file is .xslm ?
#                 if file[-4:len(file)] == 'xlsm':

#                     # read excel file
#                     file_path = os.path.abspath(f"{folder_path}//{folder}//{file}")
#                     df = pd.read_excel(file_path, )
                    
#                     # check if SALA CUNA have been found
#                     save_data = False
                    
#                     # obtain file col to init for loop
#                     sc_col = df[df.columns[1]]
                    
#                     # analize each col index until see data
#                     for num in range(len(df['Unnamed: 1'])):

#                         # create object
#                         obj = [df[col][num] for col in df.columns]
#                         file_table = {
#                             'SALA CUNA': obj[1],
#                             'APELLIDO': obj[2],
#                             'NOMBRE': obj[3],
#                             'N DNI': obj[4],
#                             'FECHA DE NACIMIENTO': obj[5],
#                             'EDAD': obj[6],
#                             'SEXO': obj[7],
#                             'CALLE': obj[8],
#                             'NUMERO': obj[9],
#                             'DEPARTAMENTO': obj[10],
#                             'LOCALIDAD': obj[11],
#                             'CARACTERISTICA TELEFONICA,': obj[12],
#                             'TELEFONO': obj[13],
#                             'APELLIDO Y NOMBRE': obj[14],
#                             'DNI': obj[15],
#                             'TURNO': obj[16],
#                             'ESTADO': obj[17],
#                         }


#                         # if SALA CUNA and there is not nan values, save data into db
#                         if save_data and not pd.isna(file_table['NOMBRE']) and not pd.isna(file_table['APELLIDO']) and not pd.isna(file_table['APELLIDO Y NOMBRE']):

#                             try:                            
#                                 barrio = obj[10]
#                                 tipBar = TipoBarrio.objects.filter(barrio = barrio)
#                                 if not tipBar:
#                                     tipBar = TipoBarrio.objects.create(
#                                         barrio = barrio,
#                                     )
                                
#                                 caracteristica = obj[12] if type(obj[12]) == int else 0
#                                 tipCarTel = TipoCaracteristicaTel.objects.filter(caracteristica = caracteristica)
#                                 if not tipCarTel:
#                                     tipCarTel = TipoCaracteristicaTel.objects.create(
#                                         caracteristica = caracteristica,
#                                     )  

#                                 localidad = obj[11]
#                                 tipLoc = TipoLocalidad.objects.filter(localidad = localidad)
#                                 if not tipLoc:
#                                     tipLoc = TipoLocalidad.objects.create(
#                                         localidad = localidad,
#                                     )

#                                 estado = obj[-3] #
#                                 tipEst = TipoEstado.objects.filter(estado = estado)
#                                 if not tipEst:
#                                     tipEst = TipoEstado.objects.create(
#                                         estado = estado,
#                                     )

#                                 turno = obj[-4] #
#                                 tipTur = TipoTurno.objects.filter(turno = turno)
#                                 if not tipTur:
#                                     tipTur = TipoTurno.objects.create(
#                                         turno = turno,
#                                     )
                                
#                                 sexo = obj[7] #
#                                 tipSex = TipoSexo.objects.filter(sexo = sexo)
#                                 if not tipSex:
#                                     tipSex = TipoSexo.objects.create(
#                                         sexo = sexo,
#                                     )
                    
#                                 dniMad = obj[-5] if type(obj[-5]) == int else 0
#                                 madre = Madre.objects.filter(dni = dniMad, apellido_y_nombre = obj[-6])
#                                 if not madre:
#                                     madre = Madre.objects.create(
#                                         dni = dniMad,
#                                         apellido_y_nombre = obj[-6],
#                                     )
                                
#                                 dniChi = obj[4] if type(obj[4]) == int else 0
#                                 chico = Chico.objects.filter(dni = dniChi, fecha_nacimiento = obj[5], sexo = tipSex[0] if type(tipSex) == models.QuerySet else tipSex, apellido = file_table['APELLIDO'] )
#                                 if not chico:
#                                     chico = Chico.objects.create(
#                                         apellido = file_table['APELLIDO'],
#                                         nombre = file_table['NOMBRE'],
#                                         calle = file_table['CALLE'],
#                                         numero_calle = obj[9] if type(obj[9]) == int else 0,
#                                         caracteristica = tipCarTel[0] if type(tipCarTel) == models.QuerySet else tipCarTel,
#                                         numero_telefono = obj[9] if type(obj[9]) == int else 0,
#                                         dni = dniChi,
#                                         fecha_nacimiento = file_table['FECHA DE NACIMIENTO'],
#                                         barrio = tipBar[0] if type(tipBar) == models.QuerySet else tipBar,
#                                         localidad = tipLoc[0] if type(tipLoc) == models.QuerySet else tipLoc,
#                                         estado = tipEst[0] if type(tipEst) == models.QuerySet else tipEst,
#                                         turno = tipTur[0] if type(tipTur) == models.QuerySet else tipTur,
#                                         sexo = tipSex[0] if type(tipSex) == models.QuerySet else tipSex,
#                                         madre = madre[0] if type(madre) == models.QuerySet else madre,
#                                         sala_cuna = salacuna[0] if type(salacuna) == models.QuerySet else salacuna,
#                                     )

#                             except Exception as e:
#                                 print(f'model object error: {e}')

#                         # find SALA CUNA's codigo and name
#                         # then change save_data to True to analize excel data
#                         if sc_col[num] == 'SALA CUNA':
#                             codigo = sc_col[num+1]
#                             salacuna = SalaCuna.objects.filter(codigo = codigo)
#                             if not salacuna:
#                                 salacuna = SalaCuna.objects.create(
#                                     codigo = codigo,
#                                     nombre = df[df.columns[0]][0]  #df['Sala Cuna:'][0],
#                                 )

#                             print(codigo)
#                             print(' ')

#                             save_data = True

#     except Exception as e:
#         rta = f"{e} {obj}"

#     return HttpResponse(rta)

