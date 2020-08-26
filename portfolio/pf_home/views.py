from django.shortcuts import render,redirect
from pf_home.forms import ContactForm
import smtplib

# Create your views here.


sender='jrk.webdev@gmail.com'
receiver='jrk.webdev@gmail.com'
password='Jrk898989#'
smtpserver=smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(sender,password)


def index(request):
    return render(request,"pf_home/index.html")


def home_page(request):
    return render(request,"pf_home/home_page.html")


def portfolio(request):
    return render(request,"pf_home/portfolio.html")

def about(request):
    return render(request,"pf_home/about.html")    

def contact(request,parameter="failed"):

    if(parameter=="success"):
        status = "success"
    else:
        status = "failed"    
    
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            name = form.cleaned_data['name']
            code = form.cleaned_data['code']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            mail_content = "Subject:ClientMessage-" + str(email)+"\n"
            mail_content += "name- " + str(name)+"\n"
            mail_content += "phone- +" + str(code)+" " +str(phone) +"\n"
            mail_content += "email- " + str(email)+"\n"
            mail_content += "message- " + str(message)+"\n"
           
            status = "success"
            smtpserver.sendmail(sender,receiver,mail_content)
            form_new = ContactForm()
            return redirect('pf_home:contact_second',parameter=status) 

    form = ContactForm()        

    return render(request,"pf_home/contact.html",{'form':form,'status':status})    

def process(request):
    return render(request,"pf_home/process.html")    