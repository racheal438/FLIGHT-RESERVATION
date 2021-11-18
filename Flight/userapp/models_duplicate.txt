from django.db import models

# Create your models here.

class Message(models.Model):
    names=models.CharField("Enter your name",max_length=100)
    email=models.EmailField("Enter your email")
    phone=models.IntegerField("Enter your phone number",max_length=100)
    message=models.TextField("Enter your message")
    
    
class Userfeedback(models.Model):
      names=models.CharField("Enter your names",max_length=100)
      email=models.EmailField("Enter your email",max_length=100)
      phone=models.IntegerField("Enter your phone number",max_length=100)
      message=models.TextField("Enter your feedback message")
      def __str__(self):
        return self.names
 
class TravelRoutes(models.Model):
      AirLines=(("Airpeace", "Airpeace"),
                                ("Arik Air", "Arik Air"),
                                ("Dana Air", "Dana Air"),
                                ("Ibom Air", "Ibom Air"),
                                ("Aero Contractor", "Aero Contractor"))
                                
      Routes=(("Lagos to Abuja", "Lagos to Abuja"),
                                ("Abuja to Lagos", "Abuja to Lagos"),
                                ("Asaba to Benin", "Asaba to Benin"),
                                ("Benin to Asaba", "Benin to Asaba"),
                                ("Kaduna to Jos", "Kaduna to Jos"),
                                ("Jos to Kaduna", "Jos to Kaduna"),
                                ("Port harcourt to Enugu", "Port harcourt to Enugu"),
                                ("Enugu to Port harcourt", "Enugu to Port harcourt"),
                                ("Warri to Sokoto", "Warri to Sokoto"),
                                ("Sokoto to warri", "Sokoto to warri"))
      airline=models.CharField("Select Airline",choices=AirLines,max_length=100) 
      travelroute=models.CharField("Select Routes",choices=Routes,max_length=100) 
      routefee=models.IntegerField("Route Fee ")
      def __str__(self):
        return self.airline+" "+self.travelroute+" "+str(self.routefee)
        
        
        
        
        
        
class Reservation(models.Model):
      names=models.CharField("Enter your names",max_length=100)
      email=models.EmailField("Enter your email")
      phone=models.IntegerField("Enter your phone number") 
      Trip=models.ForeignKey(TravelRoutes,on_delete=models.CASCADE)
      options=(('return','RETURN'),('OneWay','ONEWAY'))
      options=models.CharField("Select return or one way",choices=options,max_length=100)      
      goingdate=models.DateTimeField()
      returndate=models.DateTimeField()
      def __str__(self):
        return self.names

class Reservation_oneway(models.Model):

      reserveId=models.CharField("",max_length=100,default="12345")
      names=models.CharField("Enter your names",max_length=100)
      email=models.EmailField("Enter your email")
      phone=models.IntegerField("Enter your phone number") 
      Trip=models.CharField("You trip",max_length=100)
      options=models.CharField("You trip type",max_length=100)      
      goingdate=models.DateTimeField()
      
      def __str__(self):
        return self.names
        
        
        
class Reservation_return(models.Model):
      reserveId=models.CharField("",max_length=100,default="12345")
      names=models.CharField("Enter your names",max_length=100)
      email=models.EmailField("Enter your email")
      phone=models.IntegerField("Enter your phone number") 
      Trip=models.CharField("You trip",max_length=100)
      options=models.CharField("You trip type",max_length=100)      
      goingdate=models.DateTimeField()
      returndate=models.DateTimeField()
      def __str__(self):
        return self.names
        
        









        
class MakeReservation_2(models.Model):

      AirLines=(("Airpeace", "Airpeace"),
                                ("Arik Air", "Arik Air"),
                                ("Dana Air", "Dana Air"),
                                ("Ibom Air", "Ibom Air"),
                                ("Aero Contractor", "Aero Contractor"))
      SelectDestination= (("Lagos to Abuja", "Lagos to Abuja"),
                                ("Abuja to Lagos", "Abuja to Lagos"),
                                ("Asaba to Benin", "Asaba to Benin"),
                                ("Benin to Asaba", "Benin to Asaba"),
                                ("Kaduna to Jos", "Kaduna to Jos"),
                                ("Jos to Kaduna", "Jos to Kaduna"),
                                ("Portharcourt to Enugu", "Portharcourt to Enugu"),
                                ("Enugu to Portharcourt", "Enugu to Portharcourt"),
                                ("Warri to Sokoto", "Warri to Sokoto"),
                                ("Sokoto to warri", "Sokoto to warri"))
      options=(('return','RETURN'),('OneWay','ONEWAY'))
      options=models.CharField("Select return or one way",choices=options,max_length=100)

class MakeRoute(models.Model):

       Route= (("Lagos", "Lagos"),
                                ("Abuja", "Abuja"),
                                ("Asaba", "Asaba"),
                                ("Benin", "Benin"),
                                ("Kaduna", "Kaduna"),
                                ("Jos", "Jos"),
                                ("Portharcourt", "Portharcourt"),
                                ("Enugu", "Enugu"),
                                ("Warri", "Warri"),
                                ("Sokoto", "Sokoto"))
       RouteType= (("LOCAL", "Local"),
                                ("INTERNATINONAL", "International"),

                                )
       routeName=models.CharField("Select Route",choices=Route,max_length=100)
       routeType=models.CharField("Select Route",choices=RouteType,max_length=100)
       def __str__(self):
        return self.routeName+" "+self.routeType
class ReserveForm_oneway(models.Model):

       #routeName=models.CharField("Your Route",max_length=100)
       routeAirlineandFee=models.ForeignKey(TravelRoutes,on_delete=models.CASCADE)
       goingDate=models.DateField()
       def __str__(self):
        return self.routeName+" "+self.routeAirlineandFee
        
        
class ReserveForm_return(models.Model):

       #routeName=models.CharField("Your Route",max_length=100)
       routeAirlineandFee=models.ForeignKey(TravelRoutes,on_delete=models.CASCADE)
       goingDate=models.DateField()
       returnDate=models.DateField()
       def __str__(self):
        return self.routeName+" "+self.routeAirlineandFee        