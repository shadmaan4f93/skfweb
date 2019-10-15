from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, SubjectForm, UploadedWorkForm
from django.core.mail import BadHeaderError, EmailMessage, send_mail
from skfweb import settings
from .models import HomePage, Member, Projects, Services
from django.contrib.auth.decorators import login_required
from .utils import SpeechRecognitions
from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        print(request)
        return redirect('accounts/login')
    else:
        return redirect('home')

def home(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        html_content = (
            '<h4>You have received a new message from the contact us form on your website</h4><br/>'
            '<strong>Name: </strong>' + request.POST['name'] + '<br/>'
            '<strong>Email: </strong>' + request.POST['email'] + '<br/>'
            '<strong>Message: </strong>' + request.POST['message'] + ''
        )
        from_email = settings.EMAIL_HOST_USER
        to = [settings.ADMINS[0][1]]
        try:
            msg = EmailMessage(subject, html_content, from_email, to)
            msg.content_subtype = "html"
            msg.send()
            return redirect('/')  
            
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
    else:
        SpeechRecognitions.play_welcome_message("shadmaan")
        #messages.add_message(request, messages.INFO, 'Thank you for your email confirmation.')
        context = {
            'form': ContactForm(), 
            'page': HomePage.objects.get(),  
            'members': Member.objects.all(),
            'projects': Projects.objects.all(),
            'services': Services.objects.all()
        }
    return render(request, 'home.html', context)

@login_required()
def subject_upload(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SubjectForm()
    return render(request, 'subject.html', {'form': form})

@login_required()
def work_upload(request):
    if request.method == 'POST':
        form = UploadedWorkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UploadedWorkForm()
    return render(request, 'workupload.html', {
        'form': form
    })

@login_required()
def dev_deatil(request, pk):
    context = {
            'devdetails': Member.objects.get(pk=pk),
        }
    return render(request, 'devdetail.html', context)


   

