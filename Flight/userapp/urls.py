from django.contrib import admin
from django.urls import path,include
from .views import *

# Create your urls here.
app_name="userapp"

urlpatterns = [
path("index",UserIndex,name="index"),
path("contact",conContact,name="Contact"),
path('userapp/' ,include('django.contrib.auth.urls')),
path("userform",uForm,name="userform"),
path("messageform",msgform,name="messageform"),
path("useform",userMessage,name="useform"),
path("sendmessage",sendMessage,name="sendmessage"),
path("userfeedbackform",UserFeedback,name="userfeedbackform"),
path("userfeedback",UserFeedbackView,name="userfeedback"),
path("gotohomepage",GoToHomepage,name="homepage"),
path("register",SignUp,name="register"),
path("userlogout",Logout,name="userlogout"),
path("createtravelroute",CreateTravelRoute,name="create"),
path("createreservation",CreateReservation,name="createreservation"),
path("createreservation_oneway",CreateReservation_oneway,name="createreservation_oneway"),
path("createreservation_return",CreateReservation_return,name="createreservation_return"),
path("viewallroutes",ViewAllroutes,name="viewallroutes"),
path("makereservation",MakeReservation,name="makereservation"),
path("makereservation-2",MakeReservation02,name="makereservation-2"),
path("makereservation-chooseairline",MakeReservationChooseAirline,name="makereservation-chooseairline"),
path("makereservation_oneway",MakeReservation_oneway,name="makereservation_oneway"),
path("makereservation_return",MakeReservation_return,name="makereservation_return"),
path("viewreservation_oneway/<str:reserveid>",ViewReservation_oneway,name="viewreservation"),
path("viewreservation_oneway",ViewReservation_oneway,name="viewreservation_oneway"),
path("viewreservation_return/<str:reserveid>",ViewReservation_return,name="viewreservation_return"),
path("makeroute",MakeRoute,name="makeroute"),


]