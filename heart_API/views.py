from django.shortcuts import render
from django.shortcuts import render
from . forms import ApprovalForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib import messages
from rest_framework.parsers import JSONParser
from . models import approvals
from . serializers import approvalsSerializers
from keras import backend as K
import pickle
import joblib
import json
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from collections import defaultdict, Counter
import warnings
warnings.filterwarnings('ignore')


def index(request):
	return render(request, 'pages/index.html')


class ApprovalsView(viewsets.ModelViewSet):
	queryset = approvals.objects.all()
	serializer_class = approvalsSerializers


def approvereject(unit):

	mdl = joblib.load("C:/Users/fatih.deveci/Desktop/ml_project/venv/Scripts/Heart_Disease API/Heart_Disease/heart_API/heart_model.pkl")
	#scalers = joblib.load("C:/Users/fatih.deveci/Desktop/ml_project/venv/Scripts/Heart_Disease API/Heart_Disease/heart_API/heart_scalers.pkl")
	scalers = MinMaxScaler()
	X=scalers.fit_transform(unit)
	y_pred=mdl.predict(X)
	y_pred=(y_pred>0.52)
	newdf=pd.DataFrame(y_pred, columns=['Status'])
	newdf=newdf.replace({True:'Riskli Hasta', False:'Risk Taşımıyor'})
	K.clear_session()

	return (newdf.values[0][0])


def cxcontact(request):
	if request.method=='POST':
		form=ApprovalForm(request.POST)
		if form.is_valid():
			İsim=form.cleaned_data['İsim']
			Soyisim=form.cleaned_data['Soyisim']
			Age=form.cleaned_data['Yaş']
			Sex=form.cleaned_data['Cinsiyet']
			Cp=form.cleaned_data['Göğüs_Ağrısı']
			Trestbps=form.cleaned_data['Tansiyon']
			Chol=form.cleaned_data['Kolesterol']
			Fbs=form.cleaned_data['Açlık_Kan_Şekeri']
			Restecg=form.cleaned_data['Elektro_Kardiografi']
			Thalach=form.cleaned_data['Maksimum_Kalp_Ritmi']
			Exang=form.cleaned_data['Egzersize_Bağlı_Anjina']
			Oldpeak=form.cleaned_data['Egzersize_Bağlı_Depresyon']
			Slope=form.cleaned_data['Egzersiz_Eğimi']
			Ca =form.cleaned_data['Renklendirilmiş_Büyük_Damar_Sayısı']
			Thal=form.cleaned_data['Thal']
			myDict = (request.POST).dict()
			del myDict["İsim"]
			del myDict["Soyisim"]
			del myDict["csrfmiddlewaretoken"]
			df=pd.DataFrame(myDict, index=[0])
			print(df)
			answer=approvereject(df)
			messages.add_message(request, messages.INFO,'Kalp Hastalığı Risk Değerlendirmesi: {}'.format(answer))
	form=ApprovalForm()

	return render(request, 'myform/heart_disease.html', {'form':form})
