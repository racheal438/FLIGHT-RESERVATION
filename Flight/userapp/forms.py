from django import forms
from .models import *
from django.forms.widgets import DateInput
# Create your forms here.
class UserForm(forms.Form):
       name=forms.CharField(label="Enter your name")
       email=forms.CharField(label="Enter Email")
       comment=forms.CharField(label="Type your comment")
       
class msgForm(forms.Form):
       fromemail=forms.CharField(label="Enter from email")
       toemail=forms.CharField(label="Enter destination Email")
       message=forms.CharField(label="Type in your message")

class user_form(forms.Form):
    name=forms.CharField(label="enter your names") 
    email=forms.EmailField(label="enter user email")
    phone=forms.IntegerField(label="enter phone number")
    message=forms.CharField(label="enter your message")    
    
class Messageform(forms.ModelForm):
    class Meta:
        model = Message
        fields="__all__"
        
class UserFeedbackform(forms.ModelForm):
     class Meta:
         model=Userfeedback
         fields="__all__"         
         
class CreateTravelRouteForm(forms.ModelForm):         
      class Meta:
          model=TravelRoutes
          fields="__all__"
      
class Reservationform(forms.ModelForm):
       class Meta:
           model=Reservation
           fields="__all__"
class Reservationform_oneway(forms.ModelForm):
       reserveId=forms.CharField(label="",widget=forms.HiddenInput())
       class Meta:
           model=Reservation_oneway
           fields="__all__"
class Reservationform_return(forms.ModelForm):
       reserveId=forms.CharField(label="",widget=forms.HiddenInput())
       class Meta:
           model=Reservation_return
           fields="__all__"

class MakeRouteform(forms.ModelForm):
       class Meta:
           model=MakeRoute
           fields="__all__"
class MakeReservation_2form(forms.Form):       
       Origin=forms.ModelChoiceField(label="From:",queryset=MakeRoute.objects.all())
       Destination=forms.ModelChoiceField(label="To:",queryset=MakeRoute.objects.all())  
       triptTypeOptions=[("oneway","One Way"),("return","RETURN")]
       TripType=forms.ChoiceField(label="",choices=triptTypeOptions,widget=forms.RadioSelect())
              
class MakeReservation_3form(forms.Form):       
       Going=forms.DateField(label="Going on:",widget=forms.widgets.DateInput(attrs={'type':'date'}))

class MakeReservation_oneway_form(forms.ModelForm):       
        goingDate=forms.DateField(label="Going on:",widget=forms.widgets.DateInput(attrs={'type':'date'}))
        class Meta:
           model=ReserveForm_oneway
           fields="__all__"       
class MakeReservation_return_form(forms.ModelForm):       
        goingDate=forms.DateField(label="Going on:",widget=forms.widgets.DateInput(attrs={'type':'date'}))
        returnDate=forms.DateField(label="Return on:",widget=forms.widgets.DateInput(attrs={'type':'date'}))
        class Meta:
           model=ReserveForm_return
           fields="__all__"     
             
class MakeReservation_4form(forms.Form):       
       Going=forms.DateField(label="Going on:",widget=forms.widgets.DateInput(attrs={'type':'date'}))
       Return=forms.DateField(label="Coming Back on:",widget=forms.widgets.DateInput(attrs={'type':'date'}))       
class MakeReservation_4formBKUP(forms.Form):       
       Origin=forms.ModelChoiceField(label="From:",queryset=MakeRoute.objects.all())
       Destination=forms.ModelChoiceField(label="To:",queryset=MakeRoute.objects.all())  
       triptTypeOptions=[("oneway","One Way"),("return","RETURN")]
       TripType=forms.ChoiceField(label="",choices=triptTypeOptions,widget=forms.RadioSelect())
       Going=forms.DateField(label="Going on:",widget=forms.widgets.DateInput(attrs={'type':'date'}))
       Return=forms.DateField(label="Coming Back on:",widget=forms.widgets.DateInput(attrs={'type':'date'}))       
