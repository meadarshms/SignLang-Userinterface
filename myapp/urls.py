"""signlanguage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('changepwdlogin/', views.changepwdlogin),
    path('changepwdlogin_post/', views.changepwdlogin_post),

    #admin
    path('adminhomepage/',views.adminhomepage),
    path('login/',views.login),
    path('login_post/',views.login_post),
    path('sendreply/<id>',views.sendreply),
    path('sendreply_post/',views.sendreply_post),
    path('changepwd/',views.changepwd),
    path('changepwd_post/',views.changepwd_post),
    path('viewcomplaints/',views.viewcomplaints),
    path('viewcomplaints_post/',views.viewcomplaints_post),
    path('viewtrainers/',views.viewtrainers),
    path('viewtrainers_post/',views.viewtrainers_post),
    path('approvetrainer/<id>', views.approvetrainer),
    path('rejecttrainer/<id>', views.rejecttrainer),
    path('viewrejectedtrainer/', views.viewrejectedtrainer),
    path('viewrejectedtrainers_post/',views.viewrejectedtrainers_post),
    path('viewapprovedtrainer/', views.viewapprovedtrainer),
    path('blocktrainer/<id>',views.blocktrainer),
    path('unblocktrainer/<id>',views.unblocktrainer),
    path('viewapprovedtrainers_post/',views.viewapprovedtrainers_post),
    path('viewusers/',views.viewusers),
    path('viewusers_post/',views.viewusers_post),

    #trainer
    path('trainerhomepage/',views.trainerhomepage),
    path('addalphabet/',views.addalphabet),
    path('editviewalphabet/<id>',views.editviewalphabet),
    path('editviewalphabet_post/',views.editviewalphabet_post),
    path('deletealphabet/<id>',views.deletealphabet),
    path('addalphabet_post/',views.addalphabet_post),
    path('addvideo/',views.addvideo),
    path('deletevideo/<id>', views.deletevideo),
    path('addvideo_post/',views.addvideo_post),
    path('edittrainerprofile/',views.edittrainerprofile),
    path('edittrainerprofile_post/',views.edittrainerprofile_post),
    path('viewuserstrainer/',views.viewuserstrainer),
    path('viewusertrainer_post/',views.viewusertrainer_post),

    #path('requestfromuser/',views.requestfromuser),
   # path('approvechatbytrainer/<id>',views.approvechatbytrainer),
   # path('rejectchatbytrainer/<id>',views.rejectchatbytrainer),
   # path('requestfromuser_post/',views.requestfromuser_post),
    path('signuptrainer/',views.signuptrainer),
    path('signuptrainer_post/',views.signuptrainer_post),
    path('viewalphabet/',views.viewalphabet),
    path('viewalphabet_post/',views.viewalphabet_post),
    path('viewreq/',views.viewreq),
    path('searchreq/',views.searchreq),
    path('approvereq/<id>',views.approvereq),
    path('rejectreq/<id>',views.rejectreq),
    path('blockreq/<id>',views.blockreq),
    path('viewreq_post/',views.viewreq_post),
    path('viewreview/<id>',views.viewreview),
    path('viewreview_post/',views.viewreview_post),
    path('viewtrainername/',views.viewtrainername),

    path('sendreqbyuser/<id>',views.sendreqbyuser),
    path('viewtrainername_post/',views.viewtrainername_post),
    path('viewtrainerprofile/',views.viewtrainerprofile),
    path('viewtrainerprofile_post/',views.viewtrainerprofile_post),
    path('viewvideo/',views.viewvideo),
    path('random_videos/', views.random_videos, name='random_videos'),

    path('viewvideo_post/',views.viewvideo_post),
    path('chatwithuser/',views.chatwithuser),


    #user

    path('userhomepage/',views.userhomepage),
    path('edituserprofile/',views.edituserprofile),
    path('edituserprofile_post/',views.edituserprofile_post),

    path('reqstatusofuser/',views.reqstatusofuser),
    path('sendreqbyuser/<id>',views.sendreqbyuser),
    path('sendreqbyuser_post/',views.sendreqbyuser_post),
    path('usersearchreq/',views.usersearchreq),

    path('reqstatusofuser_post/',views.reqstatusofuser_post),

    path('sendcmpviewrply/',views.sendcmpviewrply),
    path('sendcmpviewrply_post/',views.sendcmpviewrply_post),
    path('sendcomplaint/<id>',views.sendcomplaint),
    path('sendcomplaint_post/',views.sendcomplaint_post),
    path('sendreviewbyuser/<id>',views.sendreviewbyuser),
    path('sendreviewbyuser_post/',views.sendreviewbyuser_post),
    path('signupuser/',views.signupuser),
    path('email_exist/',views.email_exist),
    path('signupuser_post/',views.signupuser_post),
    path('viewalphabetuser/<id>',views.viewalphabetuser),
    path('viewalphabetuser_post/',views.viewalphabetuser_post),
    path('viewreviewbysuser/<id>',views.viewreviewbysuser),
    path('viewreviewbysuser_post/',views.viewreviewbysuser_post),
    path('viewtrainername/',views.viewtrainername),
    path('viewtrainername_post/',views.viewtrainername_post),
    path('viewuserprofile/',views.viewuserprofile),
    path('viewuserprofile_post/',views.viewuserprofile_post),
    path('viewvideouser/<id>',views.viewvideouser),
    path('viewvideouser_post/',views.viewvideouser_post),
    path('viewtrainervideoall/<id>',views.viewtrainervideoall),
    path('viewtrainervideoall_post/',views.viewtrainervideoall_post),

    path('viewvideouserall/',views.viewvideouserall),
    path('viewvideouserall_post/',views.viewvideouserall_post),

    path('logout/',views.logout),
    path('chatwithtrainer/',views.chatwithtrainer),
    path('changepwduser/',views.changepwduser),
    path('changepwduser_post/',views.changepwduser_post),



    #####t chat with u

    path('chat/<id>',views.chat1),
    path('chat_view/',views.chat_view),
    path('chat_send/<msg>',views.chat_send),

    #####u chat with t

    path('chat2/<id>', views.chat2),
    path('chat_view2/', views.chat_view2),
    path('chat_send2/<msg>', views.chat_send2),

]
