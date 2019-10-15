from rest_framework.decorators import api_view
from skfweb import settings
from django.core.mail import BadHeaderError, EmailMessage, send_mail
from django.http import JsonResponse
from .chatboot import get_response_data, bot_traner, self_traner
from .browsing import SpeechRecognitions




@api_view(['GET', 'POST'])
def chatboots(request):
    text = request.data['text']
    res = get_response_data(text)
    response_data = res.serialize()
    data = {
        'response': res,
    }
    return JsonResponse(response_data)

@api_view(['GET', 'POST'])
def chatbot_traner(request):
    text = request.data['train']
    response = bot_traner(text)
    data = {
        'response': response,
    }
    return JsonResponse(data)

@api_view(['GET', 'POST'])
def chatbot_self_traner(request):
    text = request.data
    response = self_traner(text)
    data = {
        'response': response,
    }
    return JsonResponse(data)

@api_view(['GET', 'POST'])
def recognition(request):
    response = SpeechRecognitions.speech_recognition(request)
    data = {
        'response': response,
    }
    return JsonResponse(data)

@api_view(['GET', 'POST'])
def sendmail(request):
    try:
        subject = request.data['subject']
        html_content = (
            '<h4>You have received a new message from the contact us form on your website</h4><br/>'
            '<strong>Name: </strong>' + request.data['name'] + '<br/>'
            '<strong>Email: </strong>' + request.data['email'] + '<br/>'
            '<strong>Message: </strong>' + request.data['message'] + ''
        )
        from_email = settings.EMAIL_HOST_USER
        to = [settings.ADMINS[0][1]]
        msg = EmailMessage(subject, html_content, from_email, to)
        msg.content_subtype = "html"
        msg.send() 
        return_value = {
            "message": "Success"
        }
    except BaseException as ex:
        return_value = {
            "message": str(ex)
        }
    return JsonResponse(return_value)

