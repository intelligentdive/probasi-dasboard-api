from django.shortcuts import render

# Create your views here.
import os
from django.conf import settings
from firebase_admin import credentials
from firebase_admin import initialize_app

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from user.models import User


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


# Define the path to your service account JSON file in the project root folder
service_account_json = os.path.join(settings.BASE_DIR, 'credentitial.json')

# Initialize Firebase using the service account JSON file
cred = credentials.Certificate(service_account_json)
initialize_app(cred)







# @csrf_exempt
# @login_required
# def save_fcm_token(request):
#     if request.method == 'POST':
#         user = request.user
#         token = request.POST.get('fcm_token')

#         FCMToken.objects.update_or_create(user=user, defaults={'token': token})

#         return JsonResponse({'message': 'FCM token saved successfully'})
#     else:
#         return JsonResponse({'error': 'Invalid request method'}, status=400)

# @login_required
# def send_notification(request, target_user_id):
#     sender = request.user
#     target_user = get_object_or_404(User, id=target_user_id)
#     try:
#         target_token = FCMToken.objects.get(user=target_user).token
#     except FCMToken.DoesNotExist:
#         return JsonResponse({'error': 'FCM token not found for the target user'}, status=404)

#     # Now you can send a notification to the target user using their FCM token
#     # You can implement this part using the Firebase Console or a server-side script

#     # For demonstration purposes, let's just return a JSON response
#     return JsonResponse({'message': f'Notification sent to {target_user.username}'})





from django.shortcuts import render

def my_view(request):
    # Your view logic goes here
    context = {'variable_name': 'Hello, World!'}
    return render(request, 'a.html', context)




def showFirebaseJS(request):
    data='importScripts("https://www.gstatic.com/firebasejs/8.10.1/firebase-app.js");' \
         'importScripts("https://www.gstatic.com/firebasejs/8.10.1/firebase-messaging.js"); ' \
         'var firebaseConfig = {' \
         '        apiKey: "AIzaSyCA0Sq1k68fgZHb4E4Kr8FcTcYcqxO54WE",' \
         '        authDomain: "probashi-fec05.firebaseapp.com",' \
         '        databaseURL: "probashi-fec05",' \
         '        projectId: "probashi-fec05",' \
         '        storageBucket: "probashi-fec05.appspot.com",' \
         '        messagingSenderId: "719020799409",' \
         '        appId: "1:719020799409:web:e80e6cb91b724b08b6f990",' \
         '        measurementId: "G-5J7HMHE77G"' \
         ' };' \
         'firebase.initializeApp(firebaseConfig);' \
         'const messaging=firebase.messaging();' \
         'messaging.setBackgroundMessageHandler(function (payload) {' \
         '    console.log(payload);' \
         '    const notification=JSON.parse(payload);' \
         '    const notificationOption={' \
         '        body:notification.body,' \
         '        icon:notification.icon' \
         '    };' \
         '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
         '});'

    return HttpResponse(data,content_type="text/javascript")
