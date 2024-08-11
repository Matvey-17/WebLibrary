from rest_framework.views import APIView
from Library.api.serializers import ListBookSerializer, ListMyBookSerializer, ListDebtorsSerializer
from rest_framework.response import Response
from rest_framework import status
from Library.models import Book
from Users.models import Enrollment
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils import timezone


class ListBookView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        books = Book.objects.all().order_by('name')
        serializer = ListBookSerializer(books, many=True)
        return Response({'detail': serializer.data}, status=status.HTTP_200_OK)


class ListMyBookView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = Enrollment.objects.filter(reader=request.user).select_related('book')
        serializer = ListMyBookSerializer(books, many=True)
        return Response({'detail': serializer.data}, status=status.HTTP_200_OK)


class ListDebtorsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        debtors = Enrollment.objects.all().select_related('book', 'reader')
        serializer = ListDebtorsSerializer(debtors, many=True)
        return Response({'detail': serializer.data}, status=status.HTTP_200_OK)


class AddBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({'detail': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

        enrollment = Enrollment.objects.filter(reader=request.user, book=book).first()

        if enrollment:
            return Response({'detail': 'You have already borrowed this book'}, status=status.HTTP_400_BAD_REQUEST)

        Enrollment.objects.create(
            reader=request.user,
            book=book,
            data=timezone.now().date()
        )

        return Response({'detail': 'Book borrowed successfully'}, status=status.HTTP_201_CREATED)


class RemoveBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({'detail': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

        enrollment = Enrollment.objects.filter(reader=request.user, book=book).first()

        if enrollment:
            enrollment.delete()
            return Response({'detail': 'Book removed successfully'}, status=status.HTTP_200_OK)

        return Response({'detail': 'You have already removed this book'}, status=status.HTTP_400_BAD_REQUEST)
