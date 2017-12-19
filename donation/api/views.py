from rest_framework import generics
from rest_framework import viewsets
from api.serializers import CommentSerializer
from campaign.models import Tag
from django.core.mail import send_mail

# def list(request):
#         print request.GET.get("email")
#         return

def email_client(request):
    # id = request.POST.get('id')
    # client = Client.objects.get(id=id)
    # msg_html = render_to_string('templates/email.html', {'client': client})
    msg_html = '<div> <p> hello </p> </div>'
    # template_email_text = ''
    send_mail('Lelander work samples', 'template_email_text', 'shakeelcse09@gmail.com', ['shakeelcse09@gmail.com'], html_message=msg_html, fail_silently=False)
    return HttpResponseRedirect('/email/thankyou/')

class SendContactMessage(viewsets.ViewSet):
    # queryset = Tag.objects.all()
    serializer_class = CommentSerializer

    # def list(self, request):
    #     print request
    #     return

    def get(self, request, *args, **kwargs):
        # pass
    	# print self.request.POST
        return 'hello'
    	# return email_client(request)


# class CommentViewSet(viewsets.ViewSet):

#     def list(self, request): #, format=None
#         comment = CommentSerializer(data=request.data)
#         if comment.is_valid():
#             form_email = comment.data['email']
#             form_message = comment.data['message'] + "email: " + form_email
#             form_name = comment.data['name']

#             send_mail("New contact form submission",
#                 form_message,
#                 form_email,
#                 ['myemailaddress@gmail.com'],
#                 fail_silently=False
#             )
#             return Response(comment.data)

#         # Not sure how the html connects here:
#         # return render('comment.html', {
#             # 'form': form_class,
#         # })       
#         return Response(
#             {
#                 "success": False,
#                 'error-code':'invalid-data'
#             }, 
#             )
