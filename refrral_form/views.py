from django.shortcuts import render

from refrral_form.models import FORM

def Home(request):
    if request.method =='POST':
        name= request.POST['name']
        #DOB= request.POST('DOB')
        EMAIL= request.POST['EMAIL']
        COURSE= request.POST['COURSE']
        #YEAR= request.POST('YEAR')
        CONTACT_NUM= request.POST['CONTACT_NUM']
        #WHATSAPP= request.POST('WHATSAPP')
        COLLEGE= request.POST['COLLEGE']
        #AREA_OF_HOSTEL= request.POST('AREA_OF_HOSTEL')
        #COLLEGE_ID= request.POST('COLLEGE_ID')
        #P_HOSTEL_NAME= request.POST('P_HOSTEL_NAME')
        refral = FORM.objects.create( name=name,EMAIL=EMAIL, COURSE=COURSE,  CONTACT_NUM=CONTACT_NUM, 
                                    COLLEGE=COLLEGE)
    return render(request, 'page2.html')