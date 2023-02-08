import math,random
from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.views.generic import View,FormView,CreateView, ListView, DetailView

from django.shortcuts import render,redirect
from django.http import HttpResponse
from pyexpat.errors import messages

from .models import *
from django.template import loader
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView

from MNCSApp.forms import ValidateFrm


from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings


def index(request):
    return render(request,"MNCSApp/login.html")

def User_Register(request):
    if request.method=="POST":
        authenticatedEmail = authentication.objects.filter(email=request.POST["Email"])
        if authenticatedEmail:
            #ID = request.POST["Reporter_ID"]
            Name = request.POST["Nick_Name"]
            Password = request.POST["Pass_Word"]
            SecurityQuestion = request.POST["Security_Question"]
            District = request.POST["District"]
            State = request.POST["State"]
            E_mail = request.POST["Email"]
            print("aaaaaaaaaaa", E_mail, Password)
            Contact_Number = request.POST["Report"]
            get_email=Registration.objects.filter(Email=E_mail)
            print("get_email",get_email)
            #encrypt user data
            encrypted_name = ""
            for c in Name:
                x = ord(c)
                x = x + 1
                c2 = chr(x)
                encrypted_name = encrypted_name + c2
                print(encrypted_name)

            encrypted_SecurityQuestion = ""
            for c in SecurityQuestion:
                x = ord(c)
                x = x + 1
                c2 = chr(x)
                encrypted_SecurityQuestion = encrypted_SecurityQuestion + c2
                print(encrypted_SecurityQuestion)

            encrypted_District = ""
            for c in District:
                x = ord(c)
                x = x + 1
                c2 = chr(x)
                encrypted_District = encrypted_District + c2
                print(encrypted_District)

            encrypted_State = ""
            for c in State:
                x = ord(c)
                x = x + 1
                c2 = chr(x)
                encrypted_State = encrypted_State + c2
                print(encrypted_State)

            encrypted_E_mail = ""
            for c in E_mail:
                x = ord(c)
                x = x + 1
                c2 = chr(x)
                encrypted_E_mail = encrypted_E_mail + c2
                print(encrypted_E_mail)


            encrypted_Contact_Number = ""
            for c in Contact_Number:
                x = ord(c)
                x = x + 1
                c2 = chr(x)
                encrypted_Contact_Number = encrypted_Contact_Number + c2
                print(encrypted_Contact_Number)



            if get_email:
                message = "Email Already Exist"
                return render(request, "MNCSApp/register.html", {"message": message})
            else:
                Regstrn = Registration(Nick_Name=encrypted_name, Pass_Word=Password, Security_Question=encrypted_SecurityQuestion,
                                       District=encrypted_District, State=encrypted_State, Email=encrypted_E_mail, Contact_Num=encrypted_Contact_Number, Blocked="False")
                Regstrn.save()
            Regstrn=Registration.objects.all()
            # Decryption
            encrypted_name = ""
            password = ""
            encrypted_SecurityQuestion  = ""
            encrypted_District = ""
            encrypted_State = ""
            encrypted_E_mail = ""
            encrypted_Contact_Number = ""
            for item in Regstrn:
                encrypted_name = item.Nick_Name
                password = item.Pass_Word
                encrypted_SecurityQuestion = item.Security_Question
                encrypted_District = item.District
                encrypted_State =  item.State
                encrypted_E_mail = item.Email
                encrypted_Contact_Number = item.Contact_Num
            plain_name = ""
            for c in encrypted_name:
                x = ord(c)
                x = x - 1
                c2 = chr(x)
                plain_name = plain_name + c2
                print(plain_name)
            plain_SecurityQuestion = ""
            for c in encrypted_SecurityQuestion:
                x = ord(c)
                x = x - 1
                c2 = chr(x)
                plain_SecurityQuestion = plain_SecurityQuestion + c2
                print(plain_SecurityQuestion)
            plain_District = ""
            for c in encrypted_District:
                x = ord(c)
                x = x - 1
                c2 = chr(x)
                plain_District = plain_District + c2
                print(plain_District)
            plain_State = ""
            for c in encrypted_State:
                x = ord(c)
                x = x - 1
                c2 = chr(x)
                plain_State = plain_State + c2
                print(plain_State)
            plain_encrypted_E_mail = ""
            for c in encrypted_E_mail:
                x = ord(c)
                x = x - 1
                c2 = chr(x)
                plain_encrypted_E_mail = plain_encrypted_E_mail + c2
            plain_Contact_Number = ""
            for c in encrypted_Contact_Number:
                x = ord(c)
                x = x - 1
                c2 = chr(x)
                plain_Contact_Number = plain_Contact_Number + c2
                print(plain_Contact_Number)
        #return render(request, "MNCSApp/login.html", {'Registration': Regstrn})
        context = {
            "Nick_Name" : plain_name,
            "Pass_Word" : password,
            "Security_Question" : plain_SecurityQuestion,
            "District" : plain_District,
            "State" : plain_State,
            "Email" : plain_encrypted_E_mail,
            "Contact_Num" :plain_Contact_Number
        }
    return render(request,"MNCSApp/login.html",context)
def Dashboard(request):
    Regstrn=Registration.objects.filter(id=request.session['ID'])
    encrypted_name = ""
    password = ""
    encrypted_SecurityQuestion = ""
    encrypted_District = ""
    encrypted_State = ""
    encrypted_E_mail = ""
    encrypted_Contact_Number = ""
    for item in Regstrn:
        encrypted_name = item.Nick_Name
        password = item.Pass_Word
        encrypted_SecurityQuestion = item.Security_Question
        encrypted_District = item.District
        encrypted_State = item.State
        encrypted_E_mail = item.Email
        encrypted_Contact_Number = item.Contact_Num
    plain_name = ""
    for c in encrypted_name:
        x = ord(c)
        x = x - 1
        c2 = chr(x)
        plain_name = plain_name + c2
        print(plain_name)
    plain_SecurityQuestion = ""
    for c in encrypted_SecurityQuestion:
        x = ord(c)
        x = x - 1
        c2 = chr(x)
        plain_SecurityQuestion = plain_SecurityQuestion + c2
        print(plain_SecurityQuestion)
    plain_District = ""
    for c in encrypted_District:
        x = ord(c)
        x = x - 1
        c2 = chr(x)
        plain_District = plain_District + c2
        print(plain_District)
    plain_State = ""
    for c in encrypted_State:
        x = ord(c)
        x = x - 1
        c2 = chr(x)
        plain_State = plain_State + c2
        print(plain_State)
    plain_encrypted_E_mail = ""
    for c in encrypted_E_mail:
        x = ord(c)
        x = x - 1
        c2 = chr(x)
        plain_encrypted_E_mail = plain_encrypted_E_mail + c2
    plain_Contact_Number = ""
    for c in encrypted_Contact_Number:
        x = ord(c)
        x = x - 1
        c2 = chr(x)
        plain_Contact_Number = plain_Contact_Number + c2
        print(plain_Contact_Number)
    # return render(request, "MNCSApp/login.html", {'Registration': Regstrn})


    context = {
    "id" : request.session['ID'],
    "Nick_Name": plain_name,
    "Pass_Word": password,
    "Security_Question": plain_SecurityQuestion,
    "District": plain_District,
    "State": plain_State,
    "Email": plain_encrypted_E_mail,
    "Contact_Num": plain_Contact_Number
}
    print(request.session['USERNAME'])
    return render(request,"MNCSApp/dashboard.html",context )
def Investigator_Dashboard(request):
    Investigator_Registrn = Investigator_Registration.objects.filter(Email= request.session['INVESTIGATOR'])
    print(request.session['INVESTIGATOR'])
    return render(request,"MNCSApp/investigator_dashboard.html",{'Inve_Registration': Investigator_Registrn,} )
def edit_profile(request, id):
    Reg = Registration.objects.filter(id=id)
    encrypted_name = ""
    password = ""
    encrypted_SecurityQuestion = ""
    encrypted_District = ""
    encrypted_State = ""
    encrypted_E_mail = ""
    encrypted_Contact_Number = ""
    for item in Reg:
        encrypted_name = item.Nick_Name
        password = item.Pass_Word
        encrypted_SecurityQuestion = item.Security_Question
        encrypted_District = item.District
        encrypted_State = item.State
        encrypted_E_mail = item.Email
        encrypted_Contact_Number = item.Contact_Num
    plain_name = ""
    for c in encrypted_name:
        x = ord(c)
        x = x - 1
        c2 = chr(x)
        plain_name = plain_name + c2
        print(plain_name)
    plain_SecurityQuestion = ""
    for c in encrypted_SecurityQuestion:
        x = ord(c)
        x = x - 1
        c2 = chr(x)
        plain_SecurityQuestion = plain_SecurityQuestion + c2
        print(plain_SecurityQuestion)
    plain_District = ""
    for c in encrypted_District:
        x = ord(c)
        x = x - 1
        c2 = chr(x)
        plain_District = plain_District + c2
        print(plain_District)
    plain_State = ""
    for c in encrypted_State:
        x = ord(c)
        x = x - 1
        c2 = chr(x)
        plain_State = plain_State + c2
        print(plain_State)
    plain_encrypted_E_mail = ""
    for c in encrypted_E_mail:
        x = ord(c)
        x = x - 1
        c2 = chr(x)
        plain_encrypted_E_mail = plain_encrypted_E_mail + c2
    plain_Contact_Number = ""
    for c in encrypted_Contact_Number:
        x = ord(c)
        x = x - 1
        c2 = chr(x)
        plain_Contact_Number = plain_Contact_Number + c2
        print(plain_Contact_Number)
    # return render(request, "MNCSApp/login.html", {'Registration': Regstrn})

    context = {
        "id": request.session['ID'],
        "Nick_Name": plain_name,
        "Pass_Word": password,
        "Security_Question": plain_SecurityQuestion,
        "District": plain_District,
        "State": plain_State,
        "Email": plain_encrypted_E_mail,
        "Contact_Num": plain_Contact_Number
    }

    return render(request, "MNCSApp/edit_user_profile.html", context)
def edit_Investigator_profile(request, id):
    Inves = Investigator_Registration.objects.get(id=id)

    context = {"Inve_Registration":Inves}
    return render(request, "MNCSApp/edit_investigator_profile.html", context)
def update_profile(request, id):
    Name = request.POST["Nick_Name"]
    District = request.POST["District"]
    State = request.POST["State"]
    Contact_Number = request.POST["Report"]
    encrypted_name = ""
    for c in Name:
        x = ord(c)
        x = x + 1
        c2 = chr(x)
        encrypted_name = encrypted_name + c2
        print(encrypted_name)
    encrypted_District = ""
    for c in District:
        x = ord(c)
        x = x + 1
        c2 = chr(x)
        encrypted_District = encrypted_District + c2
        print(encrypted_District)

    encrypted_State = ""
    for c in State:
        x = ord(c)
        x = x + 1
        c2 = chr(x)
        encrypted_State = encrypted_State + c2
        print(encrypted_State)

    encrypted_Contact_Number = ""
    for c in Contact_Number:
        x = ord(c)
        x = x + 1
        c2 = chr(x)
        encrypted_Contact_Number = encrypted_Contact_Number + c2
        print(encrypted_Contact_Number)

    Registration.objects.filter(id=id).update(Nick_Name=encrypted_name, District=encrypted_District,
                                              State=encrypted_State, Contact_Num=encrypted_Contact_Number, )
    Regstrn = Registration.objects.filter(Email=request.session['USERNAME'])
    response = redirect('/Dashboard/')
    return response

def update_Investigator_profile(request, id):
    print("id=====",id)
    Name = request.POST["Nick_Name"]
    District = request.POST["District"]
    OfficeCode = request.POST["Office_Code"]
    State = request.POST["State"]
    Contactnum = request.POST["Contactnum"]
    investigator_image = request.FILES["image"]
    fs = FileSystemStorage()

    Image_name = investigator_image
    fs.save(Image_name, investigator_image)
    Investigator_Registration.objects.filter(id=id).update(Nick_Name=Name,Office_Code=OfficeCode,  District=District, State=State, Contact_Num=Contactnum, Image=Image_name)
    Investigator_Registrn = Investigator_Registration.objects.filter(Email=request.session['INVESTIGATOR'])
    return render(request, "MNCSApp/investigator_dashboard.html", {'Inve_Registration': Investigator_Registrn, })

class Register(View):

    def get(self,request,*args,**kwargs):
        Kerala_State = ["Kasaragod", "Kannur", "Wayanad", "Kozhikkode", "Malappuram", "Palakkad", "Thrissur",
                           "Eranakulam", "Thiruvananthapuram", "Kollam", "Alappuzha", "Pathanamthitta", "Kottayam",
                           "Idukki"]
        return render (request,"MNCSApp/register.html",{'data':Kerala_State})
    def post(self,request,*args,**kwargs):
        form=ValidateFrm(request.POST)

        if form.is_valid():
            return redirect('register')
        else:
            return render(request,"MNCSApp/register.html",{'form':form})




def DBLogin(request):
    template = loader.get_template('MNCSApp/Login.html')
    team = Investigator_Registration.objects.all()
    context={"Team":team}
    if request.method == "POST":
            try:
                username = request.POST.get('txtEmail')
                password = request.POST.get('txtPassword')

                print(username,password)
                encrypted_email = ""
                for c in username:
                    x = ord(c)
                    x = x + 1
                    c2 = chr(x)
                    encrypted_email = encrypted_email + c2
                    print("bbb",encrypted_email)
                login_obj = Registration.objects.filter(Email=encrypted_email).exists()
                ivestigator_login = Investigator_Registration.objects.filter(Email=username).exists()
                if login_obj:
                    user_obj = Registration.objects.get(Email=encrypted_email, Pass_Word=password, Blocked="False")
                    plain_email = ""
                    for c in encrypted_email:
                        x = ord(c)
                        x = x - 1
                        c2 = chr(x)
                        plain_email = plain_email + c2
                        print(plain_email)
                    request.session['ID'] = user_obj.id
                    request.session['USERNAME'] = plain_email
                    template = loader.get_template('MNCSApp/Home.html')
                    return render(request, "MNCSApp/Home.html", context)
                elif ivestigator_login:
                    user_obj = Investigator_Registration.objects.get(Email=username, Pass_Word=password)
                    request.session['ID'] = user_obj.id
                    request.session['INVESTIGATOR'] = user_obj.Email
                    template = loader.get_template('MNCSApp/Home.html')
                    return render(request, "MNCSApp/Home.html", context)
                else:
                    print("")
                    context = {"error": login_obj}
                    HttpResponse(template.render(context, request))
            except Exception as e:
                context = {"error": e}
                HttpResponse(template.render(context, request))
    return HttpResponse(template.render(context, request))

def logout(request):
    del request.session['USERNAME']
    return render(request, "MNCSApp/Login.html")
def Invetigator_logout(request):
    del request.session['INVESTIGATOR']
    return render(request, "MNCSApp/Login.html")

def Reporter(request):
    if request.method == "POST":
        date_time = datetime.timestamp(datetime.now())
        Report = request.POST["report_text"]
        Image = request.FILES["proof_image"]
        Clip = request.FILES["proof_clip"]
        fs = FileSystemStorage()
        Image_name = str(datetime.timestamp(datetime.now())) + Image.name
        fs.save(Image_name, Image)
        fv = FileSystemStorage()
        Clip_name = str(datetime.timestamp(datetime.now())) + Clip.name
        fv.save(Clip_name, Clip)

        get_id = Registration.objects.get(id=request.session['ID']) # geting forein key id
        #request.session['Report'] = Report

        #print(get_id.id)

        Report = Crime_Reporting( Reporter_ID_id= get_id.id,Date_and_time=datetime.now(), Report_text=Report, Proof_Image=Image_name,
                               Proof_clip=Clip_name)
        Report.save()
    Report = Crime_Reporting.objects.all()
    return render(request, "MNCSApp/reporter_form.html", {'Reporting': Report})


def user_complaints(request, user_id):

    Kerala_District= ["Kasaragod", "Kannur", "Wayanad", "Kozhikkode" , "Malappuram" , "Palakkad", "Thrissur" , "Eranakulam", "Thiruvananthapuram", "Kollam", "Alappuzha", "Pathanamthitta", "Kottayam" , "Idukki"]
    get_id = Registration.objects.get(id=request.session['ID'])

    reports=Crime_Reporting.objects.filter(Reporter_ID_id=user_id)




    print("njdnjvjjj", user_id)
    return render(request,"MNCSApp/user_complaints.html",{'Reports':reports, 'data':Kerala_District, 'id':get_id,} )
def edit_user_complaints(request, id):
    rports = Crime_Reporting.objects.get(id=id)
    context = {'complaints': rports}
    return render(request, "MNCSApp/edit_user_complaints.html", context)
def update_edit_user_complaints(request, id):
    if request.method == "POST":
        rports = Crime_Reporting.objects.get(id=id)
        print("id===", id)
        if request.FILES["proof_image"] != '' and request.FILES["proof_clip"] != '':
            rports.Report_text = request.POST["report_text"]
            rports.Proof_Image = request.FILES["proof_image"]
            rports.Proof_clip = request.FILES["proof_clip"]
            fs = FileSystemStorage()

            Image_name =  rports.Proof_Image
            fs.save(Image_name, rports.Proof_Image)
            fv = FileSystemStorage()
            Clip_name = rports.Proof_clip
            fv.save(Clip_name, rports.Proof_clip)

            rports.save()
            print("hiiii")
        else:
            rports.Report_text = request.POST["report_text"]
            rports.save()
            print("hello")

        get_id = Registration.objects.get(id=request.session['ID'])

        reports = Crime_Reporting.objects.filter(Reporter_ID_id=id)

        return render(request, "MNCSApp/user_complaints.html",
                      {'Reports': reports,'id': get_id, })
def Investigator_view_cmplaints(request):
    reports = Crime_Reporting.objects.filter(Investigator_ID=request.session['ID'])
    return render(request,"MNCSApp/Investigator_Crime_Events.html",{'Reports':reports, } )


def Investigator_Register(request):
    if request.method=="POST":
        #ID = request.POST["Reporter_ID"]
        Name = request.POST["Nick_Name"]
        Password = request.POST["Pass_Word"]
        Officecode = request.POST["OfficeCode"]
        District = request.POST["District"]
        State = request.POST["State"]
        Email = request.POST["Email"]
        Report = request.POST["Report"]
        Image = request.FILES["proof_image"]
        fs = FileSystemStorage()
        Image_name = str(datetime.timestamp(datetime.now())) + Image.name
        fs.save(Image_name, Image)
        get_email = Registration.objects.filter(Email=Email)
        print("get_email", get_email)
        if get_email:
            message = "Email Already Exist"
            return render(request, "MNCSApp/Investigator_Registration_Form.html", {"message": message})
        else:
            Regstrn = Investigator_Registration(Nick_Name=Name, Pass_Word=Password, Office_Code=Officecode,
                                                District=District, State=State, Email=Email, Contact_Num=Report,
                                                Image=Image_name)
            Regstrn.save()

    Regstrn=Investigator_Registration.objects.all()
    return render(request,"MNCSApp/login.html",{'Registration':Regstrn})

def Investigator_Registration_Form(request):

    Kerala_District= ["Kasaragod", "Kannur", "Wayanad", "Kozhikkode" , "Malappuram" , "Palakkad", "Thrissur" , "Eranakulam", "Thiruvananthapuram", "Kollam", "Alappuzha", "Pathanamthitta", "Kottayam" , "Idukki"]


    Regstrn=Investigator_Registration.objects.all()
    return render(request,"MNCSApp/Investigator_Registration_Form.html",{'Registration':Regstrn, 'data':Kerala_District} )


def take_action(request, id):

    Regsterd_id = Crime_Reporting.objects.filter(id=id)
    return render(request, "MNCSApp/take_action.html",{'details':Regsterd_id})



def Update_Status(request, id):
    if request.method == "POST":
        stts = request.POST["status"]
        report = request.POST["report"]
        Regstrn = Crime_Reporting.objects.filter(id=id).update(Status=stts)
        InvestigatorId= request.session['ID']
        InvestigatorRegistration = Investigator_Registration.objects.get(id=InvestigatorId)
        InveName = InvestigatorRegistration.Nick_Name
        InveOfficeCode = InvestigatorRegistration.Office_Code
        print(id,stts, InvestigatorId, report)
        #InvestigatorsCases=Investigators_Cases(CASE_ID = id,Status = stts,Investigator_ID = InvestigatorId ,Investigator_Name= InveName, Investigator_Office_Code= InveOfficeCode,Investigator_Report = report)
        InvestigationProcess=Investigation_Process(CASE_ID = id,Status = stts,Investigator_ID = InvestigatorId ,Investigator_Name= InveName, Investigator_Office_Code= InveOfficeCode,Investigator_Report = report,  Date_and_time=datetime.now())
        InvestigationProcess.save()
        print(id, stts, InvestigatorId, report)
        Regsterd_id = Crime_Reporting.objects.filter(id=id)
    return render(request, "MNCSApp/take_action.html",{"registration":Regstrn,'details': Regsterd_id})

def Admin_Login(request):
    template = loader.get_template('MNCSAdministration/Administration_login.html')
    context = {}
    if request.method == "POST":
        try:
            securityCode = request.POST.get('txtCode')
            password = request.POST.get('txtPassword')
            sCode = "724017104017"
            pwd = "123456"

            print(securityCode, password)
            if sCode==securityCode and pwd==password :
                request.session['SECURITYCODE'] = sCode
                request.session['PASSWORD'] = pwd
                return render(request, "MNCSAdministration/home.html")
            else:
                print("")
                context = {"error": sCode}
                #HttpResponse(template.render(context, request))
        except Exception as e:
            context = {"error": e}
            #HttpResponse(template.render(context, request))
    return HttpResponse(template.render(context, request))
def home(request):
    return render(request, "MNCSAdministration/home.html")


#Manage Investigators
def ManageInvestigators(request):
    Investigators=Investigator_Registration.objects.all()
    return render(request,"MNCSAdministration/manageInvestigators.html",{'Reports':Investigators,  } )
def ManageRepotrters(request):
    reports = Crime_Reporting.objects.all()
    details = Registration.objects.all()
    return render(request, "MNCSAdministration/user_complaints.html", {'Reports': reports, 'details': details})
def Allocate_Investigators(request):
    reports = Crime_Reporting.objects.all()
    details = Registration.objects.all()
    Investigators = Investigator_Registration.objects.all()
    return render(request, "MNCSAdministration/allocate_investigators.html", {'Reports': reports, 'details': details, 'Investigators':Investigators})

def ManageReportersComplaints(request,user_id):

    Kerala_District= ["Kasaragod", "Kannur", "Wayanad", "Kozhikkode" , "Malappuram" , "Palakkad", "Thrissur" , "Eranakulam", "Thiruvananthapuram", "Kollam", "Alappuzha", "Pathanamthitta", "Kottayam" , "Idukki"]
    get_id = Registration.objects.get(id=request.session['ID'])

    reports=Crime_Reporting.objects.filter(Reporter_ID_id=user_id)
    print("njdnjvjjj", user_id)
    return render(request,"MNCSAdministration/user_complaints.html",{'Reports':reports, 'data':Kerala_District, 'id':get_id,} )

def DeleteFakeReport(request, id):
        reports = Crime_Reporting.objects.get(id=id)
        reports.delete()
        return render(request,"MNCSAdministration/manage_reporters.html")

def Investigator_take_action(request, id):

    Regsterd_id = Crime_Reporting.objects.filter(id=id)
    Investigator= Investigation_Process.objects.filter(CASE_ID=id)
    for i in Investigator:
        print(i.CASE_ID, i.Investigator_ID, i.Investigator_Name, i.Investigator_Office_Code, i.Investigator_Report)
    return render(request, "MNCSAdministration/take_action.html",{'details':Regsterd_id, "Investigator":Investigator})

def block_user(request, id):
    print("ugfh")
    Registration.objects.filter(id=id).update(Blocked="True")
    reports = Crime_Reporting.objects.all()
    details = Registration.objects.all()
    return render(request, "MNCSAdministration/user_complaints.html", {'Reports': reports, 'details': details})


def unblock_user(request, id):
    print("ugfh")
    Registration.objects.filter(id=id).update(Blocked="False")
    reports = Crime_Reporting.objects.all()
    details = Registration.objects.all()
    return render(request, "MNCSAdministration/user_complaints.html", {'Reports': reports, 'details': details})

def Allot_Investigators(request, id):
    if request.method == "POST":
        investigator = request.POST["iid"]
        Crime_Reporting.objects.filter(id=id).update(Investigator_ID=investigator)
        reports = Crime_Reporting.objects.all()
        details = Registration.objects.all()
        Investigators = Investigator_Registration.objects.all()
        return render(request, "MNCSAdministration/allocate_investigators.html",
                      {'Reports': reports, 'details': details, 'Investigators': Investigators})

def Send_Feedback(request):
    team = Investigator_Registration.objects.all()
    context = {"Team": team}
    if request.method == "POST":
        Name = request.POST["name"]
        Email = request.POST["email"]
        Subject = request.POST["subject"]
        message = request.POST["message"]
        Regstrn = Feedback_form(name=Name,email=Email,sub=Subject,message=message)
        Regstrn.save()
        return render(request, "MNCSApp/home.html",context)

def View_Feedback(request):
    feedback = Feedback_form.objects.all()
    context = {"Feedbacks": feedback}
    return render(request, "MNCSAdministration/feedbacks.html", context)

def generateOTP():
    # Declare a digits variable
    # which stores all digits
    digits = "0123456789"
    OTP = ""

    # length of password can be changed
    # by changing value in range
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


class Email_Verification(View):

    def get(self,request,*args,**kwargs):
        return render (request,"MNCSApp/emailverification.html",)
otp =""
def send_OTP(request):
    subject = "mncrs otp"
    message = generateOTP()
    recepient = request.POST.get('to')
    if subject and message:
        try:
             send_mail(subject, message, settings.EMAIL_HOST_USER, [recepient],fail_silently=False)
             verified_email = authentication(email=recepient)
             verified_email.save()
             otp = message
             print(subject, message, settings.EMAIL_HOST_USER, [recepient],otp)
        except Exception:
                return HttpResponse('Invalid header found.')
        return render(request,'MNCSApp/OTP_Success.html',{"recepient":recepient})
    else:
            return HttpResponse('Make sure all fields are entered and valid.')

def Verifyotp(request):
    recepient = request.POST.get('otp')
    if otp == recepient:
        return render(request, 'MNCSApp/register.html')
    return render(request, 'MNCSApp/emailverification.html')


"""def Update_Status(request, id):
    Regsterd_id = Reporter_Forms.objects.filter(id=id)
    if request.method == "POST":
        stts = request.POST["status"]
        report = request.POST["report"]
        print("status=====", stts)
        Regstrn = Status(Status=stts,Inestigator_Report=report, CASE_ID_id=id)
        Regstrn.save()
        Regstrn = Status.objects.filter(id=id)
    return render(request, "MNCSApp/take_action.html",{"registration":Regstrn, 'details':Regsterd_id, })
def edit_stat(request, id):

    status = Status.objects.get(id=id)
    print("bhkbhhbhb",id)
    context = {'status': status}
    return render(request,"MNCSApp/edit_status.html", context)

def edited_status_update(request, id):
    status = Status.objects.get(id=id)
    status.Status = request.POST["status"]
    print("edited_status=====", id)
    status.save()
    return render(request, "MNCSApp/edit_user_complaints.html")

"""