# parameter
#In this function carname and company is parameters
def cars(carname , company):
    print(f" {carname} is a car of  {company}")
#arguments
# In the cars funcction are postional arguments   
cars('Civic', 'Honda Company')
cars('Swift', 'maruti Company')
cars('BMW520' , 'Bayerische Motoren Werke AG Company')     
# keywords arguments
cars(carname = 'Alto', company = 'Maruti Company')
# default parameter
def cars(carname = 'Porsche Macan', company = 'Porsche Company'):#IN this function  default parameter is porsche and porsche Macan 
    print(f" {carname} is a car of  {company}")
cars()    