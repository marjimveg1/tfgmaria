# -*- coding: utf-8 -*-


from django.shortcuts import  redirect
from .forms import *
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from datetime import date, timedelta
from .models import *
from django.core.paginator import Paginator
from decimal import  Decimal
from django.utils.timezone import activate
import numpy as np
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from django.shortcuts import render
import os
from Universidad.settings import base
import schedule
import time





def inicio(request):
    return render(request, 'inicio.html', {"inicioview": True} )

def graficas(request):
    if request.user.is_authenticated:
        user = request.user
        diario_owner = Diario.objects.filter(user=user)[0]

        #Peso mamá------------------------------------------------------------
        query_pesoMama = Peso.objects.filter(diario=diario_owner, tipo="Madre")
        lista_pesoMama = []

        for dato  in query_pesoMama:
            peso = dato.peso
            peso = float("{:.2f}".format(peso))
            fecha = dato.fecha
            lista_pesoMama.append([fecha.day, fecha.month, fecha.year,peso])

        # Peso bebé------------------------------------------------------------
        query_pesoBebe = Peso.objects.filter(diario=diario_owner, tipo="Bebe")
        lista_pesoBebe = []
        for dato in query_pesoBebe:
            peso = dato.peso
            peso = float("{:.3f}".format(peso))
            fecha = dato.fecha
            lista_pesoBebe.append([fecha.day, fecha.month, fecha.year, peso])

        #Tensión ------------------------------------------------------------
        query_tension = Tension.objects.filter(diario=diario_owner)
        lista_tension = []
        for dato in query_tension:
            pulsaciones = dato.pulsaciones
            tSistolica = dato.tSistolica
            tDiastolica = dato.tDiastolica
            tSistolica = float("{:.2f}".format(tSistolica))
            tDiastolica = float("{:.2f}".format(tDiastolica))
            momento = dato.momento
            lista_tension.append([momento.day, momento.month, momento.year, momento.hour, momento.minute,tSistolica,tDiastolica,pulsaciones ])


        #Medida ------------------------------------------------------------
        query_medida = Medida.objects.filter(diario=diario_owner)
        lista_medida = []
        for dato in query_medida:
            dBiparieta = dato.dBiparieta
            cAbdominal = dato.cAbdominal
            lFemur = dato.lFemur
            dBiparieta = float("{:.2f}".format(dBiparieta))
            cAbdominal = float("{:.2f}".format(cAbdominal))
            lFemur = float("{:.2f}".format(lFemur))
            fecha = dato.fecha
            lista_medida.append([fecha.day, fecha.month, fecha.year,dBiparieta,cAbdominal,lFemur ])

    #Medida ------------------------------------------------------------
        query_patadas = Patada.objects.filter(diario=diario_owner, cantidad = 10)
        lista_patadas = []
        for dato in query_patadas:
            duracion = dato.duracion
            duracion = float("{:.2f}".format(duracion))
            momento = dato.momento
            lista_patadas.append([momento.day, momento.month, momento.year,momento.hour, momento.minute, duracion ])

        return render(request, 'diarioSeguimiento/graficas.html', {"lista_pesoMama": lista_pesoMama,
                                                                   "lista_pesoBebe": lista_pesoBebe,
                                                                   "lista_tension": lista_tension,
                                                                   "lista_medida": lista_medida,
                                                                   "lista_patadas": lista_patadas})
    else:
        return render(request, 'inicio.html', {"inicioview": True})



def grafica(request):
    todos_los_datos = pd.read_excel(
        'C:/Users/maria/OneDrive/Escritorio/dataset/AHS_Woman_23_Madhya_Pradesh/datos.xlsx')



    columna_w_id = todos_los_datos['age']  #Filtra por columna
    columna_age = todos_los_datos['media'] # Filtra por columna



    Data = {'age' : columna_w_id,
            'media' : columna_age}



    df = pd.DataFrame(Data, columns=['age','media'])
    df = df.fillna(0)

    kmeans = KMeans(n_clusters=3).fit(df)
    centroids = kmeans.cluster_centers_


    nuevoDato = np.array([[4400,25]])
    prediccionNuevoDato = kmeans.predict(nuevoDato)

    plt.scatter(df['age'], df['media'], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)

    imagen = plt
    rutaImagen = os.path.join(os.getcwd(), 'Universidad', 'Apps', 'Gestion', 'static', 'img', 'predicciones', 'prediccion')
    imagen.savefig(rutaImagen)


    return render(request, 'grafica.html', {'prediccionNuevoDato': prediccionNuevoDato} )

def error(request):
    return render(request, 'error.html')

def ruedaObstetrica(request):
    return render(request, 'ruedaObstetrica.html')

def miPerfil(request):
    try:
        if request.user.is_authenticated:
            user = request.user
            return render(request, 'miPerfil.html', {"user": user})
        else:
            return render(request, 'inicio.html', {"inicioview": True})
    except:
        return render(request, 'error.html')


def borrarUsuario(request):
    try:
        if request.user.is_authenticated:
            User = get_user_model()
            user = request.user
            if request.method == "POST":
                user.delete()
                return redirect("../../inicio")
            else:

                context = {
                    "User": user
                }
                return render(request, 'borrarUsuario.html', context)
        else:
            return render(request, 'inicio.html', {"inicioview": True})

    except:
        return render(request, 'error.html')


def editarPerfil(request):
    if request.user.is_authenticated:
        User = get_user_model()
        user = request.user

        if request.method == 'GET':
            form = EditarPerfilForm(instance=user)
        else:
            form = EditarPerfilForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return render(request, 'miPerfil.html', {"user": user})
            else:
                form = form

        return render(request, 'editarPerfil.html', {'form': form})
    else:
        return render(request, 'inicio.html', {"inicioview": True})


def cambiar_contra(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('cambiarContra')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'cambiarContra.html', {'form': form})
    else:
        return render(request, 'inicio.html', {"inicioview": True})


#REGISTRO DE USUARIOS
def registro(request):
    user = request.user
    if request.method == 'POST':
        form = MamaCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('../inicioSesion')
        else:
            form = form
    else:
        form = MamaCreateForm()
    return render(request, 'registro.html', {'form': form})


# DIARIO
def diario(request):
    if request.user.is_authenticated:
        return render(request, 'diarioSeguimiento/diarioSeguimiento.html')
    else:
        return render(request, 'inicio.html', {"inicioview": True})


#TENSION
def inicioTension(request):
    lista_tension = {}
    page = ""
    if request.user.is_authenticated:
        user = request.user
        diario_owner = Diario.objects.filter(user=user)[0]
        lista_tension = Tension.objects.filter(diario=diario_owner).order_by('momento').reverse()

        paginator = Paginator(lista_tension, 10)
        page = request.GET.get('pagina')
        lista_tension = paginator.get_page(page)

        return render(request, 'diarioSeguimiento/inicioTension.html', {"lista_tension": lista_tension, 'page':page, 'MEDIA_URL': settings.MEDIA_URL})
    else:
        return render(request, 'inicio.html', {"inicioview": True})

def anadirTension(request):
    global form
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = CrearTensionForm(request.POST)
            if form.is_valid():
                diario = Diario.objects.filter(user=user)[0]
                obj = form.save(commit=False)
                obj.diario = diario
                form.save()
                return redirect('/inicioTension/')
        else:
            form = CrearTensionForm()

        return render(request, 'diarioSeguimiento/anadirTension.html', {'form': form})
    else:
        return render(request, 'inicio.html', {"inicioview": True})

def borrarTension(request, idTension):
    try:
        tension = Tension.objects.get(id=idTension)
        user = request.user
        diario = Diario.objects.filter(user=user)[0]
        lista_tension = Tension.objects.filter(diario=diario)

        if tension in lista_tension:
            tension.delete()
        return redirect('/inicioTension/')
    except:
        return render(request, 'error.html')


def inicioPesoMama(request):
    lista_peso = {}
    page = ""
    if request.user.is_authenticated:
        user = request.user
        diario_owner = Diario.objects.filter(user=user)[0]
        lista_peso = Peso.objects.filter(diario=diario_owner, tipo="Madre").order_by('fecha').reverse()

        paginator = Paginator(lista_peso, 10)
        page = request.GET.get('pagina')
        lista_peso = paginator.get_page(page)

        return render(request, 'diarioSeguimiento/inicioPeso.html', {"isMama":True, "lista_peso": lista_peso, 'page':page, 'MEDIA_URL': settings.MEDIA_URL})
    else:
        return render(request, 'inicio.html', {"inicioview": True})

def anadirPesoMama(request):
    global form
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = CrearPesoForm(request.POST)
            if form.is_valid():
                diario = Diario.objects.filter(user=user)[0]
                obj = form.save(commit=False)
                obj.diario = diario
                obj.tipo = "Madre"
                form.save()
                return redirect('/inicioPesoMama/')
        else:
            form = CrearPesoForm()

        return render(request, 'diarioSeguimiento/anadirPesoMama.html', {'form': form})
    else:
        return render(request, 'inicio.html', {"inicioview": True})

def borrarPeso(request, idPeso):
    try:
        peso = Peso.objects.get(id=idPeso)
        user = request.user
        diario = Diario.objects.filter(user=user)[0]
        lista_peso = Peso.objects.filter(diario=diario)

        if peso in lista_peso:
            peso.delete()
        return redirect('/miDiario/')
    except:
        return render(request, 'error.html')


def inicioPesoBebe(request):
    lista_peso = {}
    page = ""
    if request.user.is_authenticated:
        user = request.user
        diario_owner = Diario.objects.filter(user=user)[0]
        lista_peso = Peso.objects.filter(diario=diario_owner, tipo="Bebe").order_by('fecha').reverse()

        paginator = Paginator(lista_peso, 10)
        page = request.GET.get('pagina')
        lista_peso = paginator.get_page(page)

        return render(request, 'diarioSeguimiento/inicioPeso.html', {"isMama":False, "lista_peso": lista_peso, 'page':page, 'MEDIA_URL': settings.MEDIA_URL})
    else:
        return render(request, 'inicio.html', {"inicioview": True})

def anadirPesoBebe(request):
    global form
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = CrearPesoForm(request.POST)
            if form.is_valid():
                diario = Diario.objects.filter(user=user)[0]
                obj = form.save(commit=False)
                obj.diario = diario
                obj.tipo = "Bebe"
                form.save()
                return redirect('/inicioPesoBebe/')
        else:
            form = CrearPesoForm()

        return render(request, 'diarioSeguimiento/anadirPesoBebe.html', {'form': form})
    else:
        return render(request, 'inicio.html', {"inicioview": True})


def inicioPatada(request):
    lista_patadas = {}
    page = ""
    if request.user.is_authenticated:
        user = request.user
        diario_owner = Diario.objects.filter(user=user)[0]
        lista_patadas = Patada.objects.filter(diario=diario_owner).order_by('momento').reverse()

        paginator = Paginator(lista_patadas, 10)
        page = request.GET.get('pagina')
        lista_patadas = paginator.get_page(page)

        return render(request, 'diarioSeguimiento/inicioPatada.html',
                      {"lista_patadas": lista_patadas, 'page': page, 'MEDIA_URL': settings.MEDIA_URL})
    else:
        return render(request, 'inicio.html', {"inicioview": True})

def contadorPatada(request):
    if request.user.is_authenticated:
        user = request.user
        diario = Diario.objects.filter(user=user)[0]
        if request.method == 'POST':
            fecha = request.POST['form_fecha']
            duracion = request.POST['form_duracion']
            cantidad = request.POST['form_numero']
            if cantidad == "":
                return render(request, 'diarioSeguimiento/contadorPatadas.html')
            else:
                crearPatada(fecha,duracion,cantidad,diario)
                return redirect('/inicioPatada/')

        return render(request, 'diarioSeguimiento/contadorPatadas.html')
    else:
        return render(request, 'inicio.html', {"inicioview": True})

def crearPatada(fecha,duracion,cantidad,diario):
    patada = Patada(diario=diario, duracion = duracion, cantidad=cantidad, momento=fecha)
    patada.save()

def borrarPatada(request, idPatada):
    try:
        patada = Patada.objects.get(id=idPatada)
        user = request.user
        diario = Diario.objects.filter(user=user)[0]
        lista_patada = Patada.objects.filter(diario=diario)

        if patada in lista_patada:
            patada.delete()
        return redirect('/inicioPatada/')
    except:
        return render(request, 'error.html')

def inicioMedicacion(request):
    lista_medicacion = {}
    page = ""
    if request.user.is_authenticated:
        user = request.user
        diario_owner = Diario.objects.filter(user=user)[0]
        lista_medicacion = Medicacion.objects.filter(diario=diario_owner).order_by('fechaInicio').reverse()

        paginator = Paginator(lista_medicacion, 10)
        page = request.GET.get('pagina')
        lista_medicacion = paginator.get_page(page)
        fechaActual = date.today()

        return render(request, 'diarioSeguimiento/inicioMedicacion.html', {"lista_medicacion": lista_medicacion,'fechaActual': fechaActual ,'page':page, 'MEDIA_URL': settings.MEDIA_URL})
    else:
        return render(request, 'inicio.html', {"inicioview": True})


def anadirMedicacion(request):
    global form
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = CrearMedicacionForm(request.POST)
            if form.is_valid():
                diario = Diario.objects.filter(user=user)[0]
                obj = form.save(commit=False)
                obj.diario = diario
                form.save()
                return redirect('/inicioMedicacion/')
        else:
            form = CrearMedicacionForm()

        return render(request, 'diarioSeguimiento/anadirMedicacion.html', {'form': form})
    else:
        return render(request, 'inicio.html', {"inicioview": True})

def borrarMedicacion(request, idMedicacion):
    medicacion = Medicacion.objects.get(id=idMedicacion)
    user = request.user
    diario = Diario.objects.filter(user=user)[0]
    lista_medicacion = Medicacion.objects.filter(diario=diario)

    if medicacion in lista_medicacion:
        medicacion.delete()
    return redirect('/inicioMedicacion/')


def inicioContracciones(request):
    lista_contracciones = {}
    page = ""
    if request.user.is_authenticated:
        user = request.user
        diario_owner = Diario.objects.filter(user=user)[0]
        lista_contracciones = Contraccion.objects.filter(diario=diario_owner).order_by('momento').reverse()

        paginator = Paginator(lista_contracciones, 10)
        page = request.GET.get('pagina')
        lista_contracciones = paginator.get_page(page)

        return render(request, 'diarioSeguimiento/inicioContracciones.html',
                      {"lista_contracciones": lista_contracciones, 'page': page, 'MEDIA_URL': settings.MEDIA_URL})
    else:
        return render(request, 'inicio.html', {"inicioview": True})


def contadorContracciones(request):
    if request.user.is_authenticated:
        user = request.user
        diario = Diario.objects.filter(user=user)[0]
        if request.method == 'POST':
            fecha = request.POST['form_fecha']
            duracion = request.POST['form_duracion']
            intervalo = request.POST['form_intervalo']
            crearContracciones(fecha,duracion,intervalo,diario)
            return redirect('/inicioContracciones/')

        return render(request, 'diarioSeguimiento/contadorContracciones.html')
    else:
        return render(request, 'inicio.html', {"inicioview": True})

def crearContracciones(fecha,duracion,intervalo,diario):
    intervalo = intervalo + "00.00;"
    lista_fecha = fecha.split(";")
    lista_duracion = duracion.split(";")
    lista_intervalo = intervalo.split(";")



    for i in range(0,len(lista_fecha)-1):
        fecha = lista_fecha[i]
        duracion = lista_duracion[i]
        intervalo = lista_intervalo[i]
        contraccion = Contraccion(diario=diario, duracion=Decimal(duracion.strip(' "')), intervalo=Decimal(intervalo.strip(' "')), momento=fecha)
        contraccion.save()

    return lista_fecha,lista_intervalo,lista_duracion

def borrarContraccion(request, idContraccion):
    try:
        contraccion = Contraccion.objects.get(id=idContraccion)
        user = request.user
        diario = Diario.objects.filter(user=user)[0]
        lista_contraccion = Contraccion.objects.filter(diario=diario)

        if contraccion in lista_contraccion:
            contraccion.delete()
        return redirect('/inicioContracciones/')
    except:
        return render(request, 'error.html')



def inicioMedida(request):
    lista_medida = {}
    page = ""
    if request.user.is_authenticated:
        user = request.user
        diario_owner = Diario.objects.filter(user=user)[0]
        lista_medida = Medida.objects.filter(diario=diario_owner).order_by('fecha').reverse()

        paginator = Paginator(lista_medida, 10)
        page = request.GET.get('pagina')
        lista_medida = paginator.get_page(page)

        return render(request, 'diarioSeguimiento/inicioMedida.html', {"lista_medida": lista_medida, 'page':page, 'MEDIA_URL': settings.MEDIA_URL})
    else:
        return render(request, 'inicio.html', {"inicioview": True})

def anadirMedida(request):
    global form
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = CrearMedidaForm(request.POST)
            if form.is_valid():
                diario = Diario.objects.filter(user=user)[0]
                obj = form.save(commit=False)
                obj.diario = diario
                form.save()
                return redirect('/inicioMedida/')
        else:
            form = CrearMedidaForm()

        return render(request, 'diarioSeguimiento/anadirMedida.html', {'form': form})
    else:
        return render(request, 'inicio.html', {"inicioview": True})

def borrarMedida(request, idMedida):
    try:
        medida = Medida.objects.get(id=idMedida)
        user = request.user
        diario = Diario.objects.filter(user=user)[0]
        lista_medida = Medida.objects.filter(diario=diario)

        if medida in lista_medida:
            medida.delete()
        return redirect('/inicioMedida/')
    except:
        return render(request, 'error.html')


# CALENDARIO
def buscarFecha(request):
    if request.user.is_authenticated:
        return render(request, 'agenda/buscarFecha.html')
    else:
        return render(request, 'inicio.html', {"inicioview": True})


def crearFechaCalendario(request):
    global form
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = FechaCalendarioForm(request.POST)
            if form.is_valid():
                calendario = Calendario.objects.filter(user=user)[0]
                obj = form.save(commit=False)
                obj.calendario = calendario
                form.save()
                return redirect('/miAgenda/')
        else:
            form = FechaCalendarioForm()

        return render(request, 'agenda/anadirFechaCalendario.html', {'form': form})
    else:
        return render(request, 'inicio.html', {"inicioview": True})



def borrarEvento (request, idEvento):
    try:

        evento = Evento.objects.get(id=idEvento)
        user = request.user
        calendario = Calendario.objects.filter(user=user)[0]
        lista_eventos = Evento.objects.filter(calendario=calendario)

        if evento in lista_eventos:
            evento.delete()
        return redirect('/miAgenda/')
    except:
        return render(request, 'error.html')

def agenda(request):
    try:
        activate(settings.TIME_ZONE)
        global nueva_fecha
        dic_solicitud = request.GET.dict()

        detalle, fecha = getValores(dic_solicitud)

        user = request.user
        calendario_owner = Calendario.objects.filter(user_id=user.id)[0]
        eventos_owner_lista = Evento.objects.filter(calendario_id=calendario_owner.id )
        hoy = date.today()
        getDetalle = False
        getMes= False
        proximosEventosQuery = Evento.objects.filter(calendario_id=calendario_owner.id, fecha__gte= datetime.now()).order_by('fecha')

        if len(proximosEventosQuery) <5:
            proximoEventos = proximosEventosQuery
        else:
            proximosEventos = proximosEventosQuery[0:4]



        if (detalle=="" and fecha==""): #Quiero ver el mes actual, sin detalles
            year = hoy.year
            month = hoy.month
            fecha_pedida = hoy

        elif(detalle=="" and fecha!=""): #Quiero ver el mes siguiente o el anterior
            fecha_pedida = date(int(fecha[0:4]), int(fecha[5:7]), 1)
            month = fecha_pedida.month
            year = fecha_pedida.year
            getMes = True

        elif(detalle !="" and fecha==""): #Detalle de la fecha detalle en el mes actual
            year = hoy.year
            month = hoy.month
            fecha_pedida = hoy

            if (len(detalle) == 8):
                ano_parametro = detalle[0:4]
                mes_parametro = detalle[4:6]
                dia_parametro = detalle[6:8]

                try:
                    nueva_fecha = date(int(ano_parametro), int(mes_parametro), int(dia_parametro))
                    getDetalle = True

                except:
                    detalles = ""


        else: #Detalle de la fecha detalle en el mes siguiente o anteerior
            fecha_pedida = date(int(fecha[0:4]), int(fecha[5:7]), 1)
            month = fecha_pedida.month
            year = fecha_pedida.year
            getMes = True

            if (len(detalle) == 8):
                ano_parametro = detalle[0:4]
                mes_parametro = detalle[4:6]
                dia_parametro = detalle[6:8]

                try:
                    nueva_fecha = date(int(ano_parametro), int(mes_parametro), int(dia_parametro))
                    getDetalle = True

                except:
                    getDetalle = False


        primer_dia_mes = date(year, month, 1)
        mes_actual = month
        if (month == 12):
            year += 1
            month = 1
        else:
            month += 1
        ultimo_dia_mes = date(year, month, 1) - timedelta(1)
        primer_dia_calendario = primer_dia_mes - timedelta(primer_dia_mes.weekday())
        ultimo_dia_calendario = ultimo_dia_mes + timedelta(7 - ultimo_dia_mes.weekday())


        detalles = []
        cal_mes = []
        week = []
        week_headers = []


        i = 0
        dia = primer_dia_calendario
        while dia <= ultimo_dia_calendario:
            if i < 7:
                week_headers.append(dia)
            cal_day = {}
            cal_day['day'] = dia
            cal_day['event'] = False
            for evento in eventos_owner_lista:
                if dia == evento.fecha.date():
                    cal_day['event'] = True
                    if getDetalle and nueva_fecha == dia:
                        detalles.append(evento)

            if dia.month == mes_actual:
                cal_day['in_month'] = True
            else:
                cal_day['in_month'] = False
            week.append(cal_day)
            if dia.weekday() == 6:
                cal_mes.append(week)
                week = []
            i += 1
            dia += timedelta(1)
        mesCal = getMesEspañol(fecha_pedida)
        añoCal = fecha_pedida.strftime("%Y")

        return render(request, 'agenda/cal_mes.html',
                      {'mesCal': mesCal, 'anoCal': añoCal, 'calendar': cal_mes, 'headers': week_headers,
                      'getDetalle': getDetalle, 'detalles': detalles, "getMes": getMes, 'masMes': fecha, 'proximosEventos': proximosEventos})

    except:
        return render(request, 'error.html')

def getMesEspañol(fecha):
    numeroMes = fecha.month

    if numeroMes ==1:
        res = 'Enero'
    elif numeroMes ==2:
        res = 'Febrero'
    elif numeroMes ==3:
        res = 'Marzo'
    elif numeroMes ==4:
        res = 'Abril'
    elif numeroMes ==5:
        res = 'Mayo'
    elif numeroMes ==6:
        res = 'Junio'
    elif numeroMes ==7:
        res = 'Julio'
    elif numeroMes ==8:
        res = 'Agosto'
    elif numeroMes ==9:
        res = 'Septiembre'
    elif numeroMes ==10:
        res = 'Octubre'
    elif numeroMes ==11:
        res = 'Noviembre'
    else:
        res = 'Diciembre'


    return res



def getValores(dic_solicitud):
    try:
        fechaDetalle =  dic_solicitud["detalle"]

    except:
        fechaDetalle = ""

    try:
        fecha = dic_solicitud["fecha"]
    except:
        fecha = ""

    return fechaDetalle, fecha










