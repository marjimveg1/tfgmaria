# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from Universidad.Apps.Gestion.models import *

from datetime import datetime, timedelta, date
User = get_user_model()


# REGISTRO DE UN USUARIO (MAMÁ)
class MamaCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ( "nombre", "apellidos",  "email", "direccion","fechaNacimiento","fechaUltMens","nickName","password1", "password2", "quiereNot")

        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'email': 'Correo electrónico',
            'direccion': 'Dirección',
            'fechaNacimiento': 'Fecha de nacimiento',
            'fechaUltMens': 'Fecha última menstruación',
            'nickName': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirme contraseña',
            'quiereNot': '¿Desea que se le recuerde si lleva dos horas sin introducir registro de patadas?',

        }

    widgets = {
        'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.TextInput(attrs={'class': 'form-control'}),
        'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        'fechaNacimiento': forms.DateInput(attrs={'placeholder': 'dd/mm/aaaa'}),
        'fechaUltMens': forms.DateInput(attrs={'placeholder': 'dd/mm/aaaa'}),
        'nickName': forms.TextInput(attrs={'class': 'form-control'}),
        'password1': forms.TextInput(attrs={'class': 'form-control'}),
        'password2': forms.TextInput(attrs={'class': 'form-control'}),
    }

    def anadirEventos( user, calendario):
        # Añadir  Ultima menst
        evento_fechaUltMenst = Evento()
        evento_fechaUltMenst.titulo = "Última menstruación"
        evento_fechaUltMenst.fecha = user.fechaUltMens
        evento_fechaUltMenst.calendario = calendario


        # Añadir Fecha posible de parto
        fechaParto = evento_fechaUltMenst.fecha + timedelta(days=280) #40 semanas
        evento_fechaParto = Evento()
        evento_fechaParto.titulo = "Fecha posible de parto"
        evento_fechaParto.fecha = fechaParto
        evento_fechaParto.calendario = calendario

        # Añadir Fin amenaza aborto
        finFechaAborto = evento_fechaUltMenst.fecha + timedelta(days=98) # 13 semanas
        evento_fechaFinAborto = Evento()
        evento_fechaFinAborto.titulo = "Fin amenaza de aborto"
        evento_fechaFinAborto.fecha = finFechaAborto
        evento_fechaFinAborto.calendario = calendario

        # Añadir Visitas matrón
        cita1 = evento_fechaUltMenst.fecha + timedelta(days=84) #12 semanas
        eventoCita1 = Evento()
        eventoCita1.titulo = "Recordatorio"
        eventoCita1.categoria = "Fecha importante"
        eventoCita1.descripcion = "Recuerda, ya deberias haber ido al médico de At. Primaria, para una primera revisión"
        eventoCita1.fecha = cita1
        eventoCita1.calendario = calendario

        cita2 = evento_fechaUltMenst.fecha + timedelta(days=56) #8semanas
        eventoCita2 = Evento()
        eventoCita2.titulo = "Recordatorio"
        eventoCita2.categoria = "Fecha importante"
        eventoCita2.descripcion = "Recuerda pedir la cita para la primera ECO, debes hacertela antes de un mes"
        eventoCita2.fecha = cita2
        eventoCita2.calendario = calendario

        cita3 = evento_fechaUltMenst.fecha + timedelta(days=112) #16 semanas
        eventoCita3 = Evento()
        eventoCita3.titulo = "Recordatorio"
        eventoCita3.categoria = "Fecha importante"
        eventoCita3.descripcion = "Recuerda, esta semana deberias ir al médico de At. Primaria"
        eventoCita3.fecha = cita3
        eventoCita3.calendario = calendario

        cita4 = evento_fechaUltMenst.fecha + timedelta(days=140) # 20 semanas
        eventoCita4 = Evento()
        eventoCita4.titulo = "Recordatorio"
        eventoCita4.categoria = "Fecha importante"
        eventoCita4.descripcion = "Recuerda, esta semana deberias ir al hospital para hacerte una Ecografía"
        eventoCita4.fecha = cita4
        eventoCita4.calendario = calendario

        cita5 = evento_fechaUltMenst.fecha + timedelta(days=168) # 24 semanas
        eventoCita5 = Evento()
        eventoCita5.titulo = "Recordatorio"
        eventoCita5.categoria = "Fecha importante"
        eventoCita5.descripcion = "Recuerda, esta semana deberias ir al médico de At. Primaria"
        eventoCita5.fecha = cita5
        eventoCita5.calendario = calendario

        cita6 = evento_fechaUltMenst.fecha + timedelta(days=196) # 28 semanas
        eventoCita6 = Evento()
        eventoCita6.titulo = "Recordatorio"
        eventoCita6.categoria = "Fecha importante"
        eventoCita6.descripcion = "Recuerda, esta semana deberias ir al médico de At. Primaria"
        eventoCita6.fecha = cita6
        eventoCita6.calendario = calendario

        cita7 = evento_fechaUltMenst.fecha + timedelta(days=224) # 32 semanas
        eventoCita7 = Evento()
        eventoCita7.titulo = "Recordatorio"
        eventoCita7.categoria = "Fecha importante"
        eventoCita7.descripcion = "Recuerda, esta semana deberias ir al hospital para hacerte una Ecografía"
        eventoCita7.fecha = cita7
        eventoCita7.calendario = calendario

        cita8 = evento_fechaUltMenst.fecha + timedelta(days=252) # 36 semanas
        eventoCita8 = Evento()
        eventoCita8.titulo = "Recordatorio"
        eventoCita8.categoria = "Fecha importante"
        eventoCita8.descripcion = "Recuerda, esta semana deberias ir al médico de At. Primaria"
        eventoCita8.fecha = cita8
        eventoCita8.calendario = calendario

        cita9 = evento_fechaUltMenst.fecha + timedelta(days=266) # 38 semanas
        eventoCita9 = Evento()
        eventoCita9.titulo = "Recordatorio"
        eventoCita9.categoria = "Fecha importante"
        eventoCita9.descripcion = "Recuerda, esta semana deberias ir al médico de At. Primaria"
        eventoCita9.fecha = cita9
        eventoCita9.calendario = calendario

        cita10 = evento_fechaUltMenst.fecha + timedelta(days=273) # 39 semanas
        eventoCita10 = Evento()
        eventoCita10.titulo = "Recordatorio"
        eventoCita10.categoria = "Fecha importante"
        eventoCita10.descripcion = "Recuerda, esta semana deberias ir al hospital para hacerte una Ecografía"
        eventoCita10.fecha = cita10
        eventoCita10.calendario = calendario


        # Añadir Inicio trimestres
        inicioSecTrim = evento_fechaUltMenst.fecha + timedelta(days=98) # 14 semanas
        inicioTerTrim = evento_fechaUltMenst.fecha + timedelta(days=196)# 28 semanas
        eventoSecTrim = Evento()
        eventoSecTrim.titulo = "Inicio segundo trimestre de embarazo"
        eventoSecTrim.fecha = inicioSecTrim
        eventoSecTrim.calendario = calendario

        eventoTerTrim = Evento()
        eventoTerTrim.titulo = "Inicio tercer trimestre de embarazo"
        eventoTerTrim.fecha = inicioTerTrim
        eventoTerTrim.calendario = calendario


        evento_fechaUltMenst.save()
        evento_fechaFinAborto.save()
        evento_fechaParto.save()
        eventoCita1.save()
        eventoCita2.save()
        eventoCita3.save()
        eventoCita4.save()
        eventoCita5.save()
        eventoCita6.save()
        eventoCita7.save()
        eventoCita8.save()
        eventoCita9.save()
        eventoCita10.save()
        eventoSecTrim.save()
        eventoTerTrim.save()


    def save(self):
        user = super(MamaCreateForm, self).save(commit=False)
        user.nombre = self.cleaned_data["nombre"]
        user.apellidos = self.cleaned_data["apellidos"]
        user.nickName = self.cleaned_data["nickName"]
        user.fechaNacimiento = self.cleaned_data["fechaNacimiento"]
        user.fechaUltMens = self.cleaned_data["fechaUltMens"]
        user.direccion = self.cleaned_data["direccion"]
        user.email = self.cleaned_data["email"]
        user.quiereNot = False
        user.save()

        calendario = Calendario()
        calendario.nombre = "calendario"
        calendario.user = user

        diario = Diario()
        diario.nombre = "diario"
        diario.user = user
        diario.save()

        calendario.save()
        user.save()

        MamaCreateForm.anadirEventos(user, calendario)

        return user



    def clean(self, *args, **kwargs):
        cleaned_data = super(MamaCreateForm, self).clean(*args, **kwargs)
        nickName = cleaned_data.get('nickName', None)
        # Recorremos todos los usuarios para ver si ya existe
        if nickName is not None:
            users = User.objects.all()
            for u in users:
                if nickName == u.nickName:
                    self.add_error('nickName', ('Nick Name ya existe'))
                    break

        year_birth = cleaned_data.get('fechaNacimiento', None)
        now = date.today()
        # Comprobamos que la fecha de nacimiento sea en pasado
        if year_birth is not None:
            if year_birth > now:
                self.add_error('fechaNacimiento', ('No puede ser futuro'))

        fecha_mens = cleaned_data.get('fechaUltMens', None)
        if fecha_mens is not None:
            if fecha_mens > now:
                self.add_error('fechaUltMens', ('No puede ser futuro'))


class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('nombre','apellidos','direccion','fechaNacimiento', 'fechaUltMens', "quiereNot")

        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'direccion': 'Dirección',
            'fechaNacimiento': 'Fecha de nacimiento',
            'fechaUltMens': 'Fecha última menstruación',
            'quiereNot': '¿Desea que se le recuerde si lleva dos horas sin introducir registro de patadas?',

        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaNacimiento': forms.DateInput(attrs={'placeholder': 'dd/mm/aaaa'}),
            'fechaUltMens': forms.DateInput(attrs={'placeholder': 'dd/mm/aaaa'}),
        }

    def clean(self, *args, **kwargs):
        cleaned_data = super(EditarPerfilForm, self).clean(*args, **kwargs)

        year_birth = cleaned_data.get('fechaNacimiento', None)
        now = date.today()
        # Comprobamos que la fecha de nacimiento sea en pasado
        if year_birth is not None:
            if year_birth > now:
                self.add_error('fechaNacimiento', ('No puede ser futuro'))

        fecha_mens = cleaned_data.get('fechaUltMens', None)
        if fecha_mens is not None:
            if fecha_mens > now:
                self.add_error('fechaUltMens', ('No puede ser futuro'))




class CrearTensionForm(forms.ModelForm):

    class Meta:
        model = Tension
        exclude = {'diario',}
        fields = ['momento','tSistolica','tDiastolica','pulsaciones',]

        labels = {
            'momento': 'Fecha',
            'tSistolica': 'Tensión sistólica',
            'tDiastolica': 'Tensión diastólica',
            'pulsaciones': 'Pulsaciones',

        }
        widgets = {
            'momento': forms.DateTimeInput(attrs={'placeholder': 'dd/mm/aaaa hh:mm'}),
            'tSistolica': forms.NumberInput(),
            'tDiastolica' : forms.NumberInput(),
            'pulsaciones' : forms.NumberInput(),
        }

    def clean(self, *args, **kwargs):
        cleaned_data = super(CrearTensionForm, self).clean(*args, **kwargs)

        tSistolica = cleaned_data.get('tSistolica', None)
        tDiastolica = cleaned_data.get('tDiastolica', None)
        pulsaciones = cleaned_data.get('pulsaciones', None)
        # Comprobamos que la tensión diastolica sea menos que la sistólica
        if tSistolica <= tDiastolica:
            self.add_error('tSistolica', ('La tensión sistólica debe er mayor que la diastólica'))

        # Comprobamos que la tensión diastolica o sistólica no sea negativo
        if tSistolica <= 0.:
            self.add_error('tSistolica', ('Error. Introduzca una medida válida'))

        if tDiastolica <= 0.:
            self.add_error('tDiastolica', ('Error. Introduzca una medida válida'))

        # Comprobamos que el momento introducido no sea futuro
        momento = cleaned_data.get('momento', None)
        if momento is not None:

            utc_dt = datetime.now(timezone.utc)
            now = utc_dt + timedelta(hours=2)
            if momento > now:
                self.add_error('momento', ('No puede ser futuro'))

                # Comprobamos que la tensión diastolica o sistólica no sea negativo
        if pulsaciones <= 0.:
            self.add_error('pulsaciones', ('Error. Introduzca una medida válida'))


class CrearPesoForm(forms.ModelForm):

    class Meta:
        model = Peso
        exclude = {'diario','tipo'}
        fields = ['fecha','peso',]

        labels = {
            'fecha': 'Fecha',
            'peso': 'Peso',

        }
        widgets = {
            'fecha': forms.DateInput(attrs={'placeholder': 'dd/mm/aaaa'}),
            'peso': forms.NumberInput(),
        }

    def clean(self, *args, **kwargs):
        cleaned_data = super(CrearPesoForm, self).clean(*args, **kwargs)

        peso = cleaned_data.get('peso', None)
        fecha = cleaned_data.get('fecha', None)
        now = date.today()
        # Comprobamos que el peso es mayor que cero
        if peso <= 0:
            self.add_error('peso', ('Error. Introduzca un peso válido'))

        # Comprobamos que la fecha introducido no sea futuro
        if fecha is not None:

            if fecha > now:
                self.add_error('fecha', ('No puede ser futuro'))




class CrearMedicacionForm(forms.ModelForm):

    class Meta:
        model = Medicacion
        exclude = {'diario',}
        fields = ['medicamento','fechaInicio','fechaFin', 'frecuencia']

        labels = {
            'medicamento': 'Medicamento',
            'fechaInicio': 'Fecha de inicio del tratamiento',
            'fechaFin': 'Fecha de fin del tratamiento',
            'frecuencia': 'Frecuencia de tomas (en horas)',

        }

        widgets = {
            'medicamento': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaInicio': forms.DateInput(attrs={'placeholder': 'dd/mm/aaaa'}),
            'fechaFin': forms.DateInput(attrs={'placeholder': 'dd/mm/aaaa'}),
            'frecuencia': forms.NumberInput(),
        }

    def clean(self, *args, **kwargs):
        cleaned_data = super(CrearMedicacionForm, self).clean(*args, **kwargs)

        # Comprobamos que la frecuencia no sea negativa
        frecuencia = cleaned_data.get('frecuencia', None)
        fechaInicio = cleaned_data.get('fechaInicio', None)
        fechaFin = cleaned_data.get('fechaFin', None)
        if frecuencia <= 0:
            self.add_error('frecuencia', ('Error. Introduzca una frecuencia válida'))

        # Comprobamos que la fecha inicio sea antes que la fecha fin del tratamiento
        if str(fechaInicio) > str(fechaFin):
            self.add_error('fechaInicio', ('El inicio del tratamiento no puede ser después que el fin'))


class CrearMedidaForm(forms.ModelForm):

    class Meta:
        model = Medida
        exclude = {'diario'}
        fields = ['fecha', 'dBiparieta', 'cAbdominal','lFemur',]

        labels = {
            'fecha': 'Fecha',
            'dBiparieta': 'Diámetro biparietal (mm)',
            'cAbdominal': 'Circunferencia abdominal (mm)',
            'lFemur': 'Longitud del fémur (mm)',

        }
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'placeholder': 'dd/mm/aaaa'}),
            'dBiparieta' : forms.NumberInput(),
            'cAbdominal': forms.NumberInput(),
            'lFemur': forms.NumberInput(),
        }

    def clean(self, *args, **kwargs):
        cleaned_data = super(CrearMedidaForm, self).clean(*args, **kwargs)

            # Comprobamos que los valores no sean negativo
        dBiparieta = cleaned_data.get('dBiparieta', None)
        cAbdominal = cleaned_data.get('cAbdominal', None)
        lFemur = cleaned_data.get('lFemur', None)
        fecha = cleaned_data.get('fecha', None)
        if dBiparieta <= 0:
            self.add_error('dBiparieta', ('Error. Introduzca una medida válida'))

        if cAbdominal <= 0:
            self.add_error('cAbdominal', ('Error. Introduzca una medida válida'))

        if lFemur <= 0:
            self.add_error('lFemur', ('Error. Introduzca una medida válida'))

        now = date.today()
        if fecha > now:
            self.add_error('fecha', ('No puede ser futuro'))


class FechaCalendarioForm(forms.ModelForm):

    class Meta:
        model = Evento
        exclude = {'calendario',}
        fields = ['titulo','fecha','categoria','descripcion',]

        labels = {
            'titulo': 'Título',
            'fecha': 'Fecha',
            'categoria': 'Categoria',
            'descripcion': 'Descripción',

        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateTimeInput(attrs={'placeholder': 'dd/mm/aaaa hh:mm'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'})
        }


class BuscarFechaForm(forms.ModelForm):
    class Meta:
        fields = ['mes','año',]

        labels = {
            'mes': 'Mes',
            'año': 'Año',

        }

        widgets = {
            'mes': forms.TextInput(attrs={'class':'form-control'}),
            'año': forms.TextInput(attrs={'class':'form-control'}),
        }
