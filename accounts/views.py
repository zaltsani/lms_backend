from rest_framework import generics

from .models import CustomUser
from .serializers import UserSerializer

# Create your views here.
class Me(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class UserDetail(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer    
