from rest_framework import viewsets, status
from rest_framework.authentication import authenticate
from rest_framework.decorators import action, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from api.serializers import RegisterSerializer, ProductSerializer

from shop.models import Product


class ProductDetailAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk) 
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'type': product.types,
            'created_at': product.created_at,
            }, status=status.HTTP_200_OK)


class ProductListAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class RegisterAPIView(APIView): 
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            refresh = RefreshToken.for_user(user)
            refresh.payload.update({
                'user_id': user.id,
                'username': user.username
            })

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        refresh_token = request.data.get('refresh_token', '')

        if not refresh_token:
            return Response({"error": "Нужен refresh_token"})

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({'success': "Выход успешен"}, status=status.HTTP_200_OK)

        except Exception as e:

            return Response({'error': 'Неверный Refresh token'}, status=status.HTTP_400_BAD_REQUEST)


