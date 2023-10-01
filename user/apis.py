from rest_framework import views, response, exceptions, permissions


from . import services, authentication
from . import serializer as user_serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializer import UserCreateSerializerphone,UserCreateSerializeremail
# class RegisterApi(views.APIView):
#     def post(self, request):
#         serializer = user_serializer.UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         data = serializer.validated_data
#         serializer.instance = services.create_user(user_dc=data)

#         return response.Response(data=serializer.data)


class LoginApi(views.APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = services.user_email_selector(email=email)

        if user is None:
            raise exceptions.AuthenticationFailed("Invalid Credentials")

        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Invalid Credentials")

        token = services.create_token(user_id=user.id)

        resp = response.Response()

        resp.set_cookie(key="jwt", value=token, httponly=True)

        return resp
    

class LoginApi1(views.APIView):
    def post(self, request):
        phone_number = request.data["phone_number"]
        password = request.data["password"]

        user = services.user_phone_selector(phone_number=phone_number)

        if user is None:
            raise exceptions.AuthenticationFailed("Invalid Credentials")

        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Invalid Credentials")

        token = services.create_token(user_id=user.id)

        resp = response.Response()

        resp.set_cookie(key="jwt", value=token, httponly=True)

        return resp   


class UserApi(views.APIView):
    """
    This endpoint can only be used
    if the user is authenticated
    """

    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user

        serializer = user_serializer.UserSerializer(user)

        return response.Response(serializer.data)


class LogoutApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        resp = response.Response()
        resp.delete_cookie("jwt")
        resp.data = {"message": "so long farewell"}

        return resp
    







class UserCreateAPIViewphone(APIView):
    def post(self, request, format=None):
        serializer = UserCreateSerializerphone(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class UserCreateAPIViewemail(APIView):
    def post(self, request, format=None):
        serializer = UserCreateSerializeremail(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    