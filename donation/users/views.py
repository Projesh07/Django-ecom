from rest_framework 			import generics
from django.contrib.auth.models import User
from campaign.models 			import Donate
from users.serializers 			import UserDetailsSerializer
from users.serializers 			import UsersListSerializer
from users.serializers 			import PaymentHistoryOfUserSerializer
from api.permissions            import IsOwner
from django.shortcuts           import get_object_or_404

from rest_framework.permissions import (
    IsAuthenticated,
    )

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,IsOwner,)
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer

class UserList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = User.objects.all()

    serializer_class = UsersListSerializer

class PaymentHistoryOfUser(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated,IsOwner,)

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
        
 
    def get_queryset(self):
        
    	
        user_id = self.kwargs['user_id']
        obj = Donate.objects.filter(user_id=user_id)
        return obj.order_by('-donate_at')

    serializer_class = PaymentHistoryOfUserSerializer
