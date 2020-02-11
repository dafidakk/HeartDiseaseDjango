from django import forms
from . import views

#['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach','exang', 'oldpeak', 'slope', 'ca', 'thal']


class ApprovalForm(forms.Form):
	İsim=forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'İsim'}))
	Soyisim=forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Soyisim'}))
	Yaş=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Yaş'}))
	Cinsiyet=forms.ChoiceField(choices=[(1, 'Erkek'),(0,'Kadın')])
	#chest pain type
	Göğüs_Ağrısı=forms.ChoiceField(choices=[('0', 0),('1', 1),('2', 2),('3', 3),('4',4)])
	#resting blood pressure
	Tansiyon=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Tansiyon(Holter değeri)'}))
	#serum cholestoral in mg/dl
	Kolesterol=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Kolesterol'}))
	#(fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)  (Açlık Kan Şekeri)
	Açlık_Kan_Şekeri=forms.ChoiceField(choices=[('0', 0),('1', 1)])
	#resting electrocardiographic results
	Elektro_Kardiografi=forms.ChoiceField(choices=[('0', 0),('1', 1),('2', 2)])
	#maximum heart rate achieved
	Maksimum_Kalp_Ritmi=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Ölçülen En Yüksek Kalp Ritmi'}))
	#egzersize bağlı anjina (1 = yes; 0 = no)
	Egzersize_Bağlı_Anjina=forms.ChoiceField(choices=[(1 , 'Evet'),(0 , 'Hayır')])
	#egzersize bağlı depresyon
	Egzersize_Bağlı_Depresyon=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Egzersize Bağlı Depresyon'}))
	#tepe egzersizin eğimi
	Egzersiz_Eğimi=forms.ChoiceField(choices=[('0', 0),('1', 1),('2', 2)])
	#floroskopi ile renklendirilmiş büyük damar (0-3) sayısı
	Renklendirilmiş_Büyük_Damar_Sayısı =forms.ChoiceField(choices=[('0', 0),('1', 1),('2', 2),('3', 3),('4',4)])
	Thal=forms.ChoiceField(choices=[('0', 0),('1', 1),('2', 2),('3', 3)])
