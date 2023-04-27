from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import *

import pandas as pd
import numpy

def migration(request):

    df = pd.read_excel("..\dataMigrate\data\\02-C.0012.xlsm")

    save_dato = False
    sc_col = df['Unnamed: 1']
    for num in range(len(df['Unnamed: 1'])):
        
        if save_dato and not pd.isna(sc_col[num]): #== False:
            obj = [df[col][num] for col in df.columns]
            # print(obj)
            
            barrio = obj[10] #df['BARRIO'][num]
            tipBar = TipoBarrio.objects.filter(barrio = barrio)
            if not tipBar:
                tipBar = TipoBarrio.objects.create(
                    barrio = barrio,
                )
            
            caracteristica = obj[12]
            tipCarTel = TipoCaracteristicaTel.objects.filter(caracteristica = caracteristica)
            if not tipCarTel:
                tipCarTel = TipoCaracteristicaTel.objects.create(
                    caracteristica = caracteristica,
                )  

            localidad = obj[11]
            tipLoc = TipoLocalidad.objects.filter(localidad = localidad)
            if not tipLoc:
                tipLoc = TipoLocalidad.objects.create(
                    localidad = localidad,
                )

            estado = obj[-3] #
            tipEst = TipoEstado.objects.filter(estado = estado)
            if not tipEst:
                tipEst = TipoEstado.objects.create(
                    estado = estado,
                )

            turno = obj[-4] #
            tipTur = TipoTurno.objects.filter(turno = turno)
            if not tipTur:
                tipTur = TipoTurno.objects.create(
                    turno = turno,
                )
            
            sexo = obj[7] #
            tipSex = TipoSexo.objects.filter(sexo = sexo)
            if not tipSex:
                tipSex = TipoSexo.objects.create(
                    sexo = sexo,
                )
            
            dniMad = obj[-5] #
            madre = Madre.objects.filter(dni = dniMad)
            if not madre:
                madre = Madre.objects.create(
                    dni = dniMad,
                    apellido_y_nombre = obj[-6],
                )
            
            dniChi = obj[4] 
            chico = Chico.objects.filter(dni = dniChi)
            if not chico:
                chico = Chico.objects.create(
                    apellido = obj[2],
                    nombre = obj[3],
                    calle = obj[8],
                    numero_calle = obj[9] if type(obj[9]) == int else 0,
                    caracteristica = tipCarTel[0] if type(tipCarTel) == models.QuerySet else tipCarTel,
                    numero_telefono = obj[9] if type(obj[9]) == int else 0,
                    dni = dniChi,
                    fecha_nacimiento = obj[5],
                    barrio = tipBar[0] if type(tipBar) == models.QuerySet else tipBar,
                    localidad = tipLoc[0] if type(tipLoc) == models.QuerySet else tipLoc,
                    estado = tipEst[0] if type(tipEst) == models.QuerySet else tipEst,
                    turno = tipTur[0] if type(tipTur) == models.QuerySet else tipTur,
                    sexo = tipSex[0] if type(tipSex) == models.QuerySet else tipSex,
                    madre = madre[0] if type(madre) == models.QuerySet else madre,
                    sala_cuna = salacuna[0] if type(salacuna) == models.QuerySet else salacuna,
                )

        if sc_col[num] == 'SALA CUNA':
            codigo = sc_col[num+1]
            salacuna = SalaCuna.objects.filter(codigo = codigo)
            if not salacuna:
                salacuna = SalaCuna.objects.create(
                    codigo = codigo,
                    nombre = df['Sala Cuna:'][0],
                )

            save_dato = True


    return HttpResponse('todo bien')


