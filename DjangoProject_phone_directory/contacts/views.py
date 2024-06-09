from rest_framework import generics, permissions
from rest_framework.response import Response  # Add this import
from rest_framework.views import APIView  # Add this import
from .models import Contact
from .serializers import ContactSerializer
from users.models import User

class ContactListCreateView(generics.ListCreateAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class MarkSpamView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, phone_number):
        contacts = Contact.objects.filter(phone_number=phone_number)
        for contact in contacts:
            contact.is_spam = True
            contact.save()
        return Response({'status': 'marked as spam'})

class SearchByNameView(generics.ListAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if not name:
            return Contact.objects.none()
        return Contact.objects.filter(name__icontains=name).order_by('name')

class SearchByPhoneNumberView(generics.ListAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        phone_number = self.request.query_params.get('phone_number')
        if not phone_number:
            return Contact.objects.none()
        return Contact.objects.filter(phone_number=phone_number)
