from django.urls import path

from . import apis

urlpatterns = [
    path('phone_signup/',apis.UserCreateAPIViewphone.as_view(), name='create-user'),
    path('email_signup/',apis.UserCreateAPIViewemail.as_view(), name='create-user'),
   # path("register/", apis.RegisterApi.as_view(), name="register"),
    path("loginemail/", apis.LoginApi.as_view(), name="login"),
    path("loginphone/", apis.LoginApi1.as_view(), name="login"),
    path("me/", apis.UserApi.as_view(), name="me"),
    path("logout/", apis.LogoutApi.as_view(), name="logout"),


    path("create-profile1/",apis.CreateProfileAPIView.as_view(), name= "create_profile"),
    path("viewcreate-profile1/",apis.ViewCreateProfileAPIView.as_view(), name= "create_profile"),
   
    path('profilelocationbd/',apis.ProfilelocationbdCreateAPIView.as_view(), name='locationbd'),
    path('viewprofilelocationbd/',apis.viewProfilelocationbdCreateAPIView.as_view(), name='locationbd'),



    path('profilelocationabroad/',apis.ProfilelocationabroadCreateAPIView.as_view(), name='locationabroad'),
    path('viewprofilelocationabroad/',apis.viewProfilelocationabroadCreateAPIView.as_view(), name='locationabroad'),



    path('profileexperience/',apis.ProfileinfoexperienceCreateAPIView.as_view(), name='locationabroad'),
    path('viewprofileexperience/',apis.viewProfileinfoexperienceCreateAPIView.as_view(), name='locationabroad'),
    
    
]
