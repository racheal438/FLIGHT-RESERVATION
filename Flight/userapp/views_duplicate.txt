from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from datetime import datetime
# Create your views here.
def UserIndex(request):
         data={}
         return render(request, "index.html",data)
         
def conContact(request):
         data={}
         return render(request, "contact.html",data)        
         
def uForm(request):
         dt="Please post your comments"
         bt="submit comment"
         df=UserForm()
         data={"df":df,"formtitle":dt,"buttontext":bt}
         return render(request,"blankform.html",data)  

def msgform(request):
         dt="Send your message here"
         bt="send message !"
         df=msgForm()
         data={"df":df,"formtitle":dt,"buttontext":bt}
         return render(request,"blankform.html",data) 
         
def sendMessage(request):
          
    u= Messageform()
    data={"forms":u}
    return render(request,"usermessage.html",data)         
    
def userMessage(request):
    if request.method=="POST":
         u=user_form(request.POST)
         print(request.POST.get('name'))
         print(request.POST.get('email'))
         print(request.POST.get('phone'))
         print(request.POST.get('message'))
    u=user_form()
    data={"forms":u}
    return render(request,"usermessage.html",data)     
         
def UserFeedback(request):
      if request.method=="POST":
           form=UserFeedbackform(request.POST)
           if form.is_valid():
              form.save()
              return redirect("/userapp/userfeedback")
      form=UserFeedbackform()
      data={"forms":form}
      return render(request,"usermessage.html",data)
      
def UserFeedbackView(request):
      allfeedback=Userfeedback.objects.all()
      data={"allfeedback":allfeedback}
      return render(request,"user_feedback.html",data)
           
def GoToHomepage(request):
      return render(request,"index.html")  
         
def SignUp(request):
 #return HTtpResponse(request.method)
        myform= UserCreationForm(request.POST or None)
        if(request.method=="POST"):
             if myform.is_valid():
                 user=myform.save()
                 login(request,user)
                 return redirect('/userapp/makereservation')
        data={"form":myform,"title":"User Registration"}
        return render(request,"registration/signup.html", data)    

def Logout(request):
      txt="You have logged out"      
      data={"text":txt}
      return render(request,"registration/logout.html",data) 

def CreateTravelRoute(request):
        form= CreateTravelRouteForm(request.POST or None)
        if(request.method=="POST"):
             if form.is_valid():    
                form.save()    
                return redirect('/userapp/viewallroutes')  
        data={"forms":form}
        return render(request,"forms.html", data)
 



def CreateReservation(request):
        #return HttpResponse("Reservation")
        form= Reservationform(request.POST or None)
        if(request.method=="POST"):
             if form.is_valid():    
                form.save()    
                return redirect('/userapp/createreservation')  
        data={"forms":form}
        return render(request,"forms.html", data)

def CreateReservation_oneway(request):
       
        origin=request.session['origin']
        destination=request.session['Destination']
        #return HttpResponse(origin)
        from .models import MakeRoute
        ox = MakeRoute.objects.get(pk=origin)
        dx = MakeRoute.objects.get(pk=destination)
        tx=str(ox)+" - "+str(dx)
        print(ox)
        triptype=request.session['TripType ']        
        #goingdate =request.session['Going']
        goingdate =request.session['goingDATE']
        #return HttpResponse(origin)
        #returndate=request.session['Return']=request.POST.get('Return')
        dd= datetime.now();
        rr=dd.strftime("%Y-%M-%D-%M-%S")
        rr02=str(rr)
        rr02.replace("/","-")
        print(dd.timetuple())
        dxt = dd.timetuple()
        print(dxt[0])
        print(dxt[4])
        print(dxt[5])
        print(dxt[6])
        trnsref = str(dxt[0])+str(dxt[4])+str(dxt[5])+str(dxt[6])+str(dxt[5])+str(dxt[6])
        tripx=request.session['routeAirlineandFee']
        goingx=request.session['goingDATE']
        print("+================",trnsref)
        
        from .models import TravelRoutes
        trvlx = TravelRoutes.objects.get(pk=tripx)
        
        form= Reservationform_oneway(request.POST or None,initial={'Trip':trvlx,"options":triptype,"goingdate":goingx,"reserveId":trnsref})
        if(request.method=="POST"):
             if form.is_valid():
                print ("******************id",request.POST.get('reserveId'))
                request.session['reservid001']=request.POST.get('reserveId')
                request.session['paymymoney']=trvlx.routefee
                print ("******************Session was created ")
                print ("******************-->>",request.session['reservid001'])
                form.save()    
                return redirect('/userapp/viewreservation_oneway/'+request.session['reservid001'])  
        data={"forms":form,'origin':ox,'destination':dx,'triptype':triptype,'goingdate':goingdate,
        "trscode":trnsref}
        return render(request,"forms.html", data)
        

        
def ViewReservation_oneway(request,reserveid):
        #print(type(reserveid))
        #return HttpResponse(reserveid)
        from .models import Reservation_oneway
        oxx = Reservation_oneway.objects.all().count()
        ott = Reservation_oneway.objects.all()
        for t in ott:
            print (t.reserveId)
            if str(t.reserveId) == str(reserveid):
               print("*******Found match")
        print(oxx)
        #this works
        #ox = Reservation_oneway.objects.filter(reserveId=reserveid)  
        ox = Reservation_oneway.objects.get(reserveId=reserveid)        
        print("**************************")
        print(ox)
        data={"details":ox}
        return render(request,"viewreserve.html", data)
        
        
def ViewReservation_return(request,reserveid):
        #print(type(reserveid))
        #return HttpResponse(reserveid)
        from .models import Reservation_return
        oxx = Reservation_return.objects.all().count()
        ott = Reservation_return.objects.all()
        for t in ott:
            print (t.reserveId)
            if str(t.reserveId) == str(reserveid):
               print("*******Found match")
        print(oxx)
        #this works
        #ox = Reservation_oneway.objects.filter(reserveId=reserveid)  
        ox = Reservation_return.objects.get(reserveId=reserveid)        
        print("**************************")
        print(ox)
        data={"details":ox}
        return render(request,"viewreserve.html", data)
        
        
        
        


def CreateReservation_return(request):
        #return HttpResponse("Reservation")
        origin=request.session['origin']
        destination=request.session['Destination'] 
        from .models import MakeRoute
        ox = MakeRoute.objects.get(pk=origin)
        dx = MakeRoute.objects.get(pk=destination)
        tx=str(ox)+" - "+str(dx)
        print(ox)
        triptype=request.session['TripType ']
        goingdate=request.session['goingDATE']
        returndate=request.session['returnDATE']
        tripx=request.session['routeAirlineandFee']
       
        dd= datetime.now();
        rr=dd.strftime("%Y-%M-%D-%M-%S")
        rr02=str(rr)
        rr02.replace("/","-")
        print(dd.timetuple())
        dxt = dd.timetuple()
        print(dxt[0])
        print(dxt[4])
        print(dxt[5])
        print(dxt[6])
        print(dxt[7])
        trnsref = str(dxt[0])+str(dxt[4])+str(dxt[5])+str(dxt[6])+str(dxt[7])
        tripx=request.session['routeAirlineandFee']
        goingx=request.session['goingDATE']
        returnx=request.session['returnDATE']
        print("+================",trnsref)
        from .models import TravelRoutes
        trvlx = TravelRoutes.objects.get(pk=tripx)
        form= Reservationform_return(request.POST or None,initial={'Trip':trvlx,"options":triptype,"goingdate":goingdate,"returndate":returndate,"reserveId":trnsref})
        if(request.method=="POST"):
            if form.is_valid():
                print ("******************id",request.POST.get('reserveId'))
                request.session['reservid001']=request.POST.get('reserveId')
                request.session['paymymoney']=trvlx.routefee
                print ("******************Session was created ")
                print ("******************-->>",request.session['reservid001'])
                form.save()    
                return redirect('/userapp/viewreservation_return/'+request.session['reservid001'])
         
        data={"forms":form,'origin':ox,'destination':dx,'triptype':triptype,'goingdate':goingdate,'returndate':returndate,
        "trscode":trnsref}
        return render(request,"forms.html", data)
 



 
def MakeRoute(request):
        #return HttpResponse("Reservation")
        form= MakeRouteform(request.POST or None)
        if(request.method=="POST"):
             if form.is_valid():    
                form.save()    
                return redirect('/userapp/makereservation')  
        data={"forms":form}
        return render(request,"forms.html", data)
        

def ViewAllroutes(request):
        #return HttpResponse("Reservation")
        x = TravelRoutes.objects.all()
        data={"routes":x}
        return render(request,"viewallroutes.html", data)
        
def MakeReservation(request):
        
        print("******* submission method ",request.method)
        if request.method=="POST":
           request.session['origin']=request.POST.get('Origin')
           request.session['Destination']=request.POST.get('Destination')
           request.session['TripType ']=request.POST.get('TripType')
           request.session['Trip ']=request.POST.get('Trip')
           print("Origin is : ",request.POST.get('Origin'))
           print("destination  is : ",request.POST.get('Destination'))
           print("TripType  is : ",request.POST.get('TripType'))
           print("Trip  is : ",request.POST.get('Trip'))
           return redirect ("/userapp/makereservation-chooseairline")
        form= MakeReservation_2form()          
        data={"forms":form}
        return render(request,"reservationhome.html",data)



def MakeReservationChooseAirline(request):
        origin = request.session['origin']
        dest=request.session['Destination']
        from .models import MakeRoute
        ox2 = MakeRoute.objects.get(pk=origin)
        dx2 = MakeRoute.objects.get(pk=dest) 
        org1 = ox2.routeName       
        dst1 = dx2.routeName
        route = str(org1)+" to "+str(dst1)
        
        #return HttpResponse(route)
        from .models import TravelRoutes
        rex = TravelRoutes.objects.all()
        rex2 = TravelRoutes.objects.filter(travelroute=route)
        request.session['availableroute']=route 
        
        #return HttpResponse(rex2)
        if request.session['TripType ']=="oneway":
            return redirect ("/userapp/makereservation_oneway")            
        if request.session['TripType ']=="return":
            return redirect ("/userapp/makereservation_return") 
        return redirect ("")    
        
 



def MakeReservation02(request):
        
        
        
        print("*******Showing transient data : ")
        print("Origin is : ",request.session['origin'])
        print("destination  is : ",request.session['Destination'])
        print("TripType  is : ",request.session['TripType '])
        #if request.method=="POST":
        if request.session['TripType ']=="oneway":
            return redirect ("/userapp/makereservation_oneway")            
        if request.session['TripType ']=="return":
            return redirect ("/userapp/makereservation_return") 
             
        form= MakeReservation_2form()            
        data={"forms":form}
        return render(request,"reservationhome.html",data)
 


def MakeReservation_oneway(request):        
        route=request.session['availableroute']
        print("***********",route)
        from .models import TravelRoutes
        rex = TravelRoutes.objects.all()
        #rex2 = TravelRoutes.objects.get(travelroute=route)
        form = MakeReservation_oneway_form(request.POST or None)        
              
        if request.method=="POST":
           request.session['routeAirlineandFee']=request.POST.get('routeAirlineandFee')
           request.session['goingDATE']=request.POST.get('goingDate')
           return redirect ("/userapp/createreservation_oneway")
        
        data={"forms":form}
        return render(request,"reservationhome.html",data)            
     

def MakeReservation_return(request):
        route=request.session['availableroute']
        print("***********",route)
        from .models import TravelRoutes
        rex = TravelRoutes.objects.all()
        #rex2 = TravelRoutes.objects.get(travelroute=route)
        form = MakeReservation_return_form(request.POST or None)        
              
        if request.method=="POST":
           request.session['routeAirlineandFee']=request.POST.get('routeAirlineandFee')
           request.session['goingDATE']=request.POST.get('goingDate')
           request.session['returnDATE']=request.POST.get('returnDate')
           return redirect ("/userapp/createreservation_return")
        
        data={"forms":form}
        return render(request,"reservationhome.html",data) 
      
#def userapp(request):
 #        data={}
  #       return render(request, "index.html",data)

#def out(request):
 #        data={}
  #       return render(request, "logout.html",data)

#def test(request):
 #        fx = 12000
  #       data={"testinfo":"This data is from backend", "fx":fx}
   #      return render(request, "test.html",data)

#def UserIndex(request):
 #        data={}
  #       return render(request, "index.html",data)         