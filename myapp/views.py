from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import random
from .models import Video
# Create your views here.


def changepwdlogin(request):
    return render(request, "changepwdlogin.html")


def changepwdlogin_post(request):
    email = request.POST['textfield']
    res = Login.objects.filter(username=email)
    if res.exists():
        import random
        new_pass = random.randint(0000, 9999)
        import smtplib
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("safedore3@gmail.com", "yqqlwlyqbfjtewam")
        # App Password
        to = email
        subject = "Test Email"
        body = "Your new password is " + str(new_pass)
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail("s@gmail.com", to, msg)
        # Disconnect from the server
        server.quit()
        ress = Login.objects.filter(username=email).update(password=new_pass)
        return HttpResponse('''<script>alert('send');window.location="/myapp/login/"</script>''')
    else:
        return HttpResponse('''<script>alert('Something went wrong');window.location="/myapp/login/"</script>''')




#ADMIN FUNCTIONS
from myapp.models import *


def adminhomepage(request):
    return render(request,"admin/adminindex.html")

def login(request):
    return render(request,"loginindex.html")

def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    res=Login.objects.filter(username=username,password=password)
    if res.exists():
        ress = Login.objects.get(username=username, password=password)
        request.session['lid']=ress.id
        if ress.type == "admin":
            return HttpResponse('''<script>alert('Login Successfully');window.location="/myapp/adminhomepage/"</script>''')
        elif ress.type=="trainer":
            return HttpResponse('''<script>alert('login succesful trainer');window.location="/myapp/trainerhomepage/"</script>''')
        elif ress.type=="user":
            return HttpResponse('''<script>alert('login succesfully user');window.location="/myapp/userhomepage/"</script>''')
        elif ress.type=="pending":
            return HttpResponse('''<script>alert('we have yet to verify your profile.');window.location="/myapp/login/"</script>''')
        else:
            return HttpResponse('''<script>alert('wrong uname or pwd');window.location="/myapp/login/"</script>''')
    else:
        return HttpResponse('''<script>alert('sign up and login');window.location="/myapp/login/"</script>''')


def sendreply(request,id):
    return render(request,"admin/sendreply.html",{'id': id })

def sendreply_post(request):
    reply=request.POST['textarea']
    id=request.POST['id']
    rep=Complaint.objects.filter(id=id).update(reply=reply,status='replied')
    return HttpResponse ('''<script>alert('replied'); window.location="/myapp/viewcomplaints/"</script>''')


def changepwd(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('login required'); window.location="/myapp/login/"</script>''')

    return render(request,"admin/changepassword.html")

def changepwd_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('login required'); window.location="/myapp/login/"</script>''')

    currentpwd=request.POST['textfield']
    newpwd=request.POST['textfield2']
    confirmpwd=request.POST['textfield3']
    log=Login.objects.filter(password=currentpwd,id=request.session['lid'])
    if log.exists():
        # log1=Login.objects.get(password=currentpwd,id=request.session['lid'])
        if newpwd == confirmpwd:
            log1=Login.objects.filter(password=currentpwd,id=request.session['lid']).update(password=newpwd)
            return HttpResponse('''<script>alert('password changed');window.location="/myapp/login/"</script>''')
        else :
            return HttpResponse('''<script>alert('password not changed');window.location="/myapp/changepassword/"</script>''')

    return HttpResponse("ok")




def viewcomplaints(request):
    cmp=Complaint.objects.all()
    return render(request,"admin/viewcomplaints.html",{'data': cmp})

def viewcomplaints_post(request):
    cmpfrom=request.POST['textfield']
    cmpto=request.POST['textfield2']
    cmp = Complaint.objects.filter(date__range=[cmpfrom,cmpto])
    return render(request, "admin/viewcomplaints.html", {'data': cmp})


def viewtrainers(request):
    view=Trainer.objects.filter(status='pending')
    return render(request,"admin/viewtrainers.html",{'data': view})

def approvetrainer(request,id):
    appr=Trainer.objects.filter(LOGIN_id=id).update(status="approve")
    f=Login.objects.filter(id=id).update(type="trainer")
    return HttpResponse('''<script>alert('approved'); window.location="/myapp/viewtrainers/" </script>''')

def blocktrainer(request,id):
    var=Trainer.objects.filter(LOGIN_id=id).update(status="blocked")
    var1=Login.objects.filter(id=id).update(type="blocked")
    return HttpResponse('''<script>alert('blocked'); window.location="/myapp/viewapprovedtrainer/" </script>''')

def unblocktrainer(request,id):
    var=Trainer.objects.filter(LOGIN_id=id).update(status="approve")
    var1=Login.objects.filter(id=id).update(type="trainer")
    return HttpResponse('''<script>alert('unblocked'); window.location="/myapp/viewapprovedtrainer/" </script>''')

def rejecttrainer(request,id):
    appr=Trainer.objects.filter(LOGIN_id=id).update(status="rejected")
    f=Login.objects.filter(id=id).update(type="pending  ")
    return HttpResponse('''<script>alert('rejected'); window.location="/myapp/viewtrainers/" </script>''')

def viewtrainers_post(request):
    name=request.POST['textfield']
    view = Trainer.objects.filter(status='pending',name__icontains=name)
    return render(request, "admin/viewtrainers.html", {'data': view})

def viewapprovedtrainer(request):
    view=Trainer.objects.filter(Q(status='approve')|Q(status='blocked'))
    return render(request,"admin/viewapprovedtrainer.html",{'data': view})

def viewapprovedtrainers_post(request):
    name=request.POST['textfield']
    view = Trainer.objects.filter(status='approve',name__icontains=name)
    return render(request, "admin/viewapprovedtrainer.html", {'data': view})

def viewrejectedtrainer(request):
    view=Trainer.objects.filter(status='rejected')
    return render(request,"admin/viewrejectedtrainer.html",{'data': view})

def viewrejectedtrainers_post(request):
    name=request.POST['textfield']
    view = Trainer.objects.filter(status='rejected',name__icontains=name)
    return render(request, "admin/viewrejectedtrainer.html", {'data': view})


def viewusers(request):
    view=User.objects.all()
    return render(request,"admin/viewusers.html",{'data': view })

def viewusers_post(request):
    name = request.POST['textfield']
    view=User.objects.filter(name__icontains=name)
    return render(request,"admin/viewusers.html",{'data' : view})



#TRAINER FUNCTIONS

def trainerhomepage(request):
    return render(request,"trainer/trainerindex.html")

def addalphabet(request):
    return render(request,"trainer/addalphabet.html")

def addalphabet_post(request):
    img=request.FILES['fileField1']
    alphabet=request.POST['textfield']
    from datetime import datetime
    date = datetime.now().strftime('%Y%m%d-%H%M%S')+ '.jpg'
    fs1 = FileSystemStorage()
    fs1.save(date, img)
    path1 = fs1.url(date)
    var = Alphabet()
    var.alphabet=alphabet
    var.image=path1
    var.TRAINER=Trainer.objects.get(LOGIN_id=request.session['lid'])
    var.save()

    return HttpResponse('''<script>alert('added'); window.location="/myapp/addalphabet/" </script>''')


def addvideo(request):
    return render(request, "trainer/addvideo.html")

def addvideo_post(request):

    title = request.POST['textarea']
    description = request.POST['textarea2']
    video = request.FILES['filefield']
    from datetime import datetime
    date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.mp4'
    date1=datetime.now().date().today()

    fs1 = FileSystemStorage()
    fs1.save(date, video)
    path1 = fs1.url(date)
    var = Video()
    var.video = path1
    var.date = date1
    var.title = title
    var.TRAINER = Trainer.objects.get(LOGIN_id=request.session['lid'])
    var.description = description
    var.save()

    return HttpResponse('''<script>alert('video added'); window.location="/myapp/addvideo/" </script>''')



def edittrainerprofile(request):
    var=Trainer.objects.get(LOGIN=request.session['lid'])
    return render(request,"trainer/edittrainerprofile.html",{'data':var})

def edittrainerprofile_post(request):
    name = request.POST['textfield']
    phno = request.POST['textfield2']
    email = request.POST['textfield3']
    dob = request.POST['textfield4']
    place = request.POST['textfield5']
    post = request.POST['textfield6']
    pin = request.POST['textfield7']
    district = request.POST['textfield8']
    qualification = request.POST['textfield9']
    experience = request.POST['textfield10']

    aadhaar = request.POST['textfield13']
    if "photo" in request.FILES:
        photo = request.FILES['photo']
        from datetime import datetime
        date = datetime.now().strftime('%y%m%d-%H%M%S') + '.jpg'
        fs = FileSystemStorage()
        fs.save(date, photo)
        path = fs.url(date)
        obj = Trainer.objects.get(LOGIN_id=request.session['lid'])
        obj.LOGIN_id=request.session['lid']
        obj.photo=path
        obj.name = name
        obj.phone = phno
        obj.email = email
        obj.dob = dob
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.district = district
        obj.aadhaar = aadhaar
        obj.qualification = qualification
        obj.experience = experience

        obj.save()
        return HttpResponse('''<script>alert(' edited'); window.location="/myapp/viewtrainerprofile/" </script>''')

    # if "aadhaarphoto" in request.FILES:
    #     aadhaarphoto = request.FILES['aadhaarphoto']
    #     from datetime import datetime
    #     date2 = datetime.now().strftime('%y%m%d-%H%M%S') + '.jpg'
    #     fs2 = FileSystemStorage()
    #     fs2.save(date2, aadhaarphoto)
    #     path2 = fs2.url(date2)
    #     obj = Trainer.objects.get(LOGIN_id=request.session['lid'])
    #     obj.LOGIN_id=request.session['lid']
    #     obj.aadhaarphoto=path2
    #
    #     obj.save()
    #     return HttpResponse('''<script>alert(' edited'); window.location="/myapp/addvideo/" </script>''')
    if "certificate" in request.FILES:
        certificate = request.FILES['certificate']
        from datetime import datetime
        date1 = datetime.now().strftime('%y%m%d-%H%M%S') + '.jpg'
        fs1 = FileSystemStorage()
        fs1.save(date1, certificate)
        path1 = fs1.url(date1)

        obj = Trainer.objects.get(LOGIN_id=request.session['lid'])
        obj.LOGIN_id=request.session['lid']
        obj.certificate=path1

        obj.save()
        return HttpResponse('''<script>alert(' edited'); window.location="/myapp/viewtrainerprofile/" </script>''')








    # if Trainer.objects.filter(email=email).exists():
    #     return HttpResponse('''<script>alert('gmail already exist');window.location="/myapp/viewtrainerprofile/"</script>''')

    obj = Trainer.objects.get(LOGIN_id=request.session['lid'])
    obj.name = name
    obj.phone = phno
    obj.email = email
    obj.dob = dob
    obj.place = place
    obj.post = post
    obj.pin = pin
    obj.district = district
    obj.aadhaar = aadhaar
    obj.qualification = qualification
    obj.experience = experience
    obj.save()
    return HttpResponse('''<script>alert('profile updated');window.location="/myapp/viewtrainerprofile/"</script>''')


def requestfromuser(request):
    view = Request.objects.filter(status='pending')
    return render(request, "trainer/requestfromuser.html", {'data': view})

def approvechatbytrainer(request,id):
    view=Request.objects.filter(id=id).update(status='approved')
    return HttpResponse ('''<script>alert('request has been approved'); window.location="/myapp/requestfromuser/" </script>''')

def rejectchatbytrainer(request,id):
    view=Request.objects.filter(id=id).update(status='rejected')
    return HttpResponse ('''<script>alert('request has been rejected'); window.location="/myapp/requestfromuser/" </script>''')



def requestfromuser_post(request):
    return HttpResponse("ok")


def signuptrainer(request):
    return render(request,"trainer/regformtrainer.html")

def signuptrainer_post(request):
    name=request.POST['textfield']
    phno=request.POST['textfield2']
    email=request.POST['textfield3']
    dob=request.POST['textfield4']
    place=request.POST['textfield5']
    post=request.POST['textfield6']
    pin=request.POST['textfield7']
    district=request.POST['textfield8']
    photo=request.FILES['filefield']
    certificate=request.FILES['filefield2']
    qualification=request.POST['textfield9']
    experience=request.POST['textfield10']
    pwd=request.POST['textfield11']
    confirmpwd=request.POST['textfield12']
    aadhaar =request.POST['textfield13']
    aadhaarphoto = request.FILES['filefield3']

    from datetime import datetime
    date = datetime.now().strftime('%Y%m%d-%H%M%S')+'.jpg'
    fs=FileSystemStorage()
    fs.save(date,photo)
    path=fs.url(date)

    from datetime import datetime
    date1 = datetime.now().strftime('%Y%m%d-%H%M%S') + '-1.jpg'
    fs1 = FileSystemStorage()
    fs1.save(date1, certificate)
    path1 = fs1.url(date1)

    from datetime import datetime
    date2 = datetime.now().strftime('%Y%m%d-%H%M%S') + '-2.jpg'
    fs2 = FileSystemStorage()
    fs2.save(date2, aadhaarphoto)
    path2 = fs2.url(date2)

    if Trainer.objects.filter(email=email).exists():
        return HttpResponse('''<script>alert('gmail already exist');window.location="/myapp/signuptrainer/"</script>''')
    lobj=Login()
    lobj.username=email
    lobj.password=pwd
    lobj.type='pending'
    lobj.save()

    if pwd == confirmpwd:
        obj=Trainer()
        obj.name=name
        obj.phone=phno
        obj.email=email
        obj.dob=dob
        obj.place=place
        obj.post=post
        obj.pin=pin
        obj.district=district
        obj.photo= path
        obj.aadhaar=aadhaar
        obj.aadhaarphoto = path2
        obj.certificate=path1
        obj.qualification=qualification
        obj.experience=experience
        obj.LOGIN=lobj
        obj.save()

    return HttpResponse('''<script>alert('signup succesfull');window.location="/myapp/login/"</script>''')


def viewalphabet(request):
    view=Alphabet.objects.filter(TRAINER__LOGIN_id=request.session['lid'])
    return render(request, "trainer/viewalphabet.html", {'data': view})

def editviewalphabet(request,id):
    view=Alphabet.objects.get(id=id)
    return render(request, "trainer/editalphabet.html", {'data': view})

def editviewalphabet_post(request):
    id=request.POST['id']
    alphabet=request.POST['alphabet']
    var = Alphabet.objects.get(id=id)

    if 'image' in request.FILES:
        image=request.FILES['image']
        from datetime import datetime
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
        fs1 = FileSystemStorage()
        fs1.save(date, image)
        path1 = fs1.url(date)
        # var = Alphabet.objects.get(id=id)
        var.alphabet = alphabet
        var.image = path1
        var.save()

        return HttpResponse('''<script>alert('edit succesful');window.location="/myapp/viewalphabet/"</script>''')

    # var = Alphabet.objects.get(id=id)
    var.alphabet = alphabet
    var.save()

    return HttpResponse('''<script>alert('edit succesful');window.location="/myapp/viewalphabet/"</script>''')

def deletealphabet(request,id):

    var = Alphabet.objects.filter(id=id).delete()
    return redirect('/myapp/viewalphabet/')
        # HttpResponse('''<script>alert('delete succesful');window.location="/myapp/viewalphabet/"</script>''')





def viewalphabet_post(request):
    name = request.POST['textfield']
    view = Alphabet.objects.filter(alphabet__icontains=name)
    return render(request, "trainer/viewalphabet.html", {'data': view})


def viewreq(request):
    var = Request.objects.filter(TRAINER__LOGIN_id=request.session['lid'])
    return render(request,"trainer/viewreq.html",{ 'data' : var} )

def searchreq(request):
    se=request.POST['se']
    res=Request.objects.filter(status=se)
    return render(request,"trainer/viewreq.html",{'data' : res})

def approvereq(request,id):
    var = Request.objects.filter(pk=id).update(status='approved')
    return HttpResponse('''<script>alert(' approve');window.location="/myapp/viewreq/" </script>''')

def rejectreq(request,id):
    var = Request.objects.filter(pk=id).update(status='rejected')
    return HttpResponse('''<script>alert(' rejected');window.location="/myapp/viewreq/" </script>''')

def blockreq(request,id):
    var = Request.objects.filter(pk=id).update(status='blocked')
    return HttpResponse('''<script>alert(' blocked');window.location="/myapp/viewreq/" </script>''')


def viewreq_post(request):
    return HttpResponse("ok")


def viewreview(request,id):
    var = Review.objects.filter(TRAINER__LOGIN_id=request.session['lid'],VIDEO_id=id)
    return render(request,"trainer/viewreview.html",{ 'data' : var })

def viewreview_post(request):
    return HttpResponse("ok")


def viewtrainerprofile(request):
    view =Trainer.objects.filter(LOGIN_id=request.session['lid'])
    return render(request, "trainer/viewtrainerprofile.html", {'data': view})

def viewtrainerprofile_post(request):
    view = Trainer.objects.get(LOGIN_id=request.session['lid'])
    return render(request, "trainer/edittrainerprofile.html", {'data': view})

def viewuserstrainer(request):
    view = User.objects.all()
    return render(request, "trainer/viewusertrainer.html", {'data': view})

def viewusertrainer_post(request):
    name = request.POST['textfield']
    view = User.objects.filter(name__icontains=name)
    return render(request, "trainer/viewusertrainer.html", {'data': view})



def viewvideo(request):
    view = Video.objects.filter(TRAINER__LOGIN_id=request.session['lid'])
    return render(request, "trainer/viewvideo.html", {'data': view})



def deletevideo(request,id):
        var = Video.objects.get(id=id).delete()
        return HttpResponse('''<script>alert('delete succesful');window.location="/myapp/viewvideo/"</script>''')



def viewvideo_post(request):
    name = request.POST['textfield']
    view = Video.objects.filter(title__icontains=name)
    return render(request, "trainer/viewvideo.html", {'data': view})

#USER FUNCTIONS

def userhomepage(request):
    return render(request,"user/userindex.html")

def edituserprofile(request):
    view = User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"user/edituserprofile.html",{'data':view})

def edituserprofile_post(request):
    name = request.POST['textfield']
    phno = request.POST['textfield2']
    place = request.POST['textfield5']
    post = request.POST['textfield6']
    pin = request.POST['textfield7']
    district = request.POST['textfield8']
    photo = request.FILES['photo']
    if "photo" in request.FILES:
        photo = request.FILES['photo']
        from datetime import datetime
        date1 = datetime.now().strftime('%y%m%d-%H%M%S') + '.jpg'
        fs1 = FileSystemStorage()
        fs1.save(date1, photo)
        path1 = fs1.url(date1)


        obj = User.objects.get(LOGIN_id=request.session['lid'])
        obj.name = name
        obj.phone = phno
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.district = district
        obj.LOGIN_id=request.session['lid']
        obj.photo=path1

        obj.save()
        return HttpResponse('''<script>alert(' profle updated'); window.location="/myapp/viewuserprofile/" </script>''')

    if "photo" in request.FILES:
        photo = request.FILES['photo']
        from datetime import datetime
        date = datetime.now().strftime('%y%m%d-%H%M%S') + '.jpg'
        fs = FileSystemStorage()
        fs.save(date, photo)
        path = fs.url(date)
        obj = Trainer.objects.get(LOGIN_id=request.session['lid'])
        obj.LOGIN_id = request.session['lid']

        # obj.aadhaar = aadhaar

        obj.save()
        return HttpResponse('''<script>alert(' edited'); window.location="/myapp/viewtrainerprofile/" </script>''')


def reqstatusofuser(request):
    view=Request.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,"user/chatrequestuser.html",{ 'data' : view })

def usersearchreq(request):
    se=request.POST['se']
    view=Request.objects.filter(USER__LOGIN_id=request.session['lid'],status=se)
    return render(request,"user/chatrequestuser.html",{ 'data' : view })



def reqstatusofuser_post(request):
    return HttpResponse("ok")


def sendcmpviewrply(request):
    var = Complaint.objects.all()
    return render(request,"user/viewreplycomp.html",{'data': var })

def sendcmpviewrply_post(request):
    return HttpResponse("ok")

def sendcomplaint(request,id):
    var = Trainer.objects.get(id=id)
    return render(request,"user/sendcomplaintdesc.html",{'data':var })

def sendcomplaint_post(request):
    from datetime import datetime
    date = datetime.now()
    tid = request.POST['tid']
    desc = request.POST['textarea']
    snd = Complaint()
    snd.USER = User.objects.get(LOGIN_id=request.session['lid'])
    snd.TRAINER_id = tid
    snd.status = 'pending'
    snd.date = date
    snd.complaint = desc
    snd.save()
    return HttpResponse(
        '''<script>alert('Complaint send to the trainer');window.location="/myapp/userhomepage/"</script>''')


def sendreviewbyuser(request,id):
    res=Video.objects.get(id=id)
    return render(request,"user/viewsinglepost.html",{'data':res})

def sendreviewbyuser_post(request):
    review=request.POST['review']
    rating=request.POST['rating']
    id=request.POST['id1']
    r=Video.objects.get(id=id).TRAINER.id
    obj=Review()
    did=request.POST['id1']
    from datetime import datetime
    obj.date=datetime.now().date().today()
    obj.review=review
    obj.rating=rating
    obj.VIDEO_id=id
    obj.TRAINER_id=r
    obj.USER=User.objects.get(LOGIN_id=request.session['lid'])
    obj.save()

    return HttpResponse('''<script>alert('Success');window.location="/myapp/viewvideouserall/"</script>''')

def email_exist(request):
    email = request.POST['textfield3']
    status = Login.objects.filter(username = email).exists()
    return JsonResponse({'status':status})

def signupuser(request):
    return render(request,"user/regformuser.html")

def signupuser_post(request):
    name=request.POST['textfield']
    phno=request.POST['textfield2']
    email=request.POST['textfield3']
    dob=request.POST['textfield4']
    place=request.POST['textfield5']
    post=request.POST['textfield6']
    pin=request.POST['textfield7']
    district=request.POST['textfield8']
    photo=request.FILES['filefield']
    aadhaar=request.POST['textfield9']
    aadhaarphoto = request.FILES['filefield2']
    udid=request.POST['textfield10']
    pwd=request.POST['textfield11']
    confirmpwd=request.POST['textfield12']


    from datetime import datetime
    date = datetime.now().strftime('%y%m%d-%H%M%S') + '.jpg'
    fs = FileSystemStorage()
    fs.save(date, photo)
    path = fs.url(date)

    from datetime import datetime
    date2 = datetime.now().strftime('%y%m%d-%H%M%S') + '.jpg'
    fs2 = FileSystemStorage()
    fs2.save(date2, aadhaarphoto)
    path2 = fs2.url(date2)

    if User.objects.filter(email=email).exists():
        return HttpResponse('''<script>alert('gmail already exist');window.location="/myapp/signupuser/"</script>''')
    lobj = Login()
    lobj.username = email
    lobj.password = pwd
    lobj.type = 'user'
    lobj.save()

    if pwd == confirmpwd:
        obj = User()
        obj.name = name
        obj.phone = phno
        obj.email = email
        obj.dob = dob
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.district = district
        obj.photo = path
        obj.aadhaar = aadhaar
        obj.aadhaarphoto = path2
        obj.udid = udid
        obj.LOGIN = lobj
        obj.save()

    return HttpResponse('''<script>alert('signup succesfull');window.location="/myapp/login/"</script>''')


def viewalphabetuser(request,id):
    view = Alphabet.objects.filter(TRAINER=id)
    request.session['taid']=id
    return render(request, "user/viewalphabetuser.html", {'data': view})

def viewalphabetuser_post(request):
    name = request.POST['textfield']
    view = Alphabet.objects.filter(TRAINER=request.session['taid'],alphabet__icontains=name)
    return render(request, "user/viewalphabetuser.html", {'data': view})


def viewreviewbysuser(request,id):
    var = Review.objects.filter(VIDEO=id)
    return render(request,"user/viewreviewbysuser.html",{'data':var })

def viewreviewbysuser_post(request):
    return HttpResponse("ok")


def viewtrainername(request):
    view = Trainer.objects.filter(status='approve')
    return render(request, "user/viewtrainersHP.html", {'data': view})

def viewtrainername_post(request):
    name = request.POST['textfield']
    view = Trainer.objects.filter(name__icontains=name)
    return render(request, "user/viewtrainersHP.html", {'data': view})


def sendreqbyuser(request,id):
    var = Trainer.objects.get(id=id)
    return render(request, "user/sendrequestchat.html",{'data':var })

def approvereqofuser(request):
    var = Request.objects.filter(status='approved',USER__LOGIN_id=request.session['lid'])
    return render(request, "user/chatrequestuser.html", {'data': var})



def sendreqbyuser_post(request):
    tid=request.POST['tid']

    res=Request.objects.filter(TRAINER_id=tid,USER__LOGIN_id=request.session['lid'])
    if res.exists():
        return HttpResponse({'''<script>alert('Request already exists');window.location="/myapp/viewtrainername/"</script>'''})

    from datetime import datetime
    date=datetime.now()
    desc=request.POST['textarea']
    snd=Request()
    snd.USER=User.objects.get(LOGIN_id=request.session['lid'])
    snd.TRAINER_id=tid
    snd.status='pending'
    snd.date=date
    snd.description=desc
    snd.save()
    return HttpResponse('''<script>alert('request send to the trainer');window.location="/myapp/viewtrainername/"</script>''')





def viewuserprofile(request):
    view=User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"user/viewuserprofile.html", { 'data' : view })

def viewuserprofile_post(request):
    view = User.objects.get(LOGIN_id=request.session['lid'])
    return render(request, "user/edituserprofile.html", {'data': view})


def viewtrainervideoall(request,id):
    view = Video.objects.filter(TRAINER=id)
    return render(request, "user/viewtrainervideoall.html", {'data': view})

def viewtrainervideoall_post(request):
    name = request.POST['textfield']
    view = Video.objects.filter(title__icontains=name)
    return render(request, "user/viewtrainervideoall.html", {'data': view})


def viewvideouser(request,id):
    view = Video.objects.get(id=id)
    view1 = Review.objects.filter(VIDEO_id=id)
    return render(request, "user/viewsinglepost.html", {'data': view , 'data1':view1 })

def viewvideouser_post(request):
    title=request.POST['textfield']
    return HttpResponse("ok")


def viewvideouserall(request):
    view = Video.objects.all()

    return render(request, "user/viewallvideo.html", {'data': view })

def viewvideouserall_post(request):
    title = request.POST['textfield']
    view = Video.objects.filter(title__icontains=title)
    return render(request, "user/viewallvideo.html", {'data': view })

def random_videos(request):
    videos = list(Video.objects.all())  # Fetch all videos and convert to list
    random.shuffle(videos)  # Shuffle the list of videos
    context = {
        'data': videos[:]  # Show 10 random videos
    }
    return render(request, "user/viewallvideo.html", context)

def changepwduser(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('login required'); window.location="/myapp/login/"</script>''')

    return render(request,"user/changepassworduser.html")

def changepwduser_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('login required'); window.location="/myapp/login/"</script>''')

    currentpwd=request.POST['textfield']
    newpwd=request.POST['textfield2']
    confirmpwd=request.POST['textfield3']
    log=Login.objects.filter(password=currentpwd,id=request.session['lid'])
    if log.exists():
        # log1=Login.objects.get(password=currentpwd,id=request.session['lid'])
        if newpwd == confirmpwd:
            log1=Login.objects.filter(password=currentpwd,id=request.session['lid']).update(password=newpwd)
            return HttpResponse('''<script>alert('password changed');window.location="/myapp/login/"</script>''')
        else :
            return HttpResponse('''<script>alert('password not changed');window.location="/myapp/changepassword/"</script>''')

    return HttpResponse("ok")

##########################trainer chat with user


def chat1(request,id):
    request.session["userid"] = id
    cid = str(request.session["userid"])
    request.session["new"] = cid
    qry = User.objects.get(LOGIN=cid)

    return render(request, "trainer/Chat.html", {'photo': qry.photo, 'name': qry.name, 'toid': cid})

def chat_view(request):
    fromid = request.session["lid"]
    toid = request.session["userid"]
    qry = User.objects.get(LOGIN=request.session["userid"])
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROM_id=fromid, TO_id=toid) | Q(FROM_id=toid, TO_id=fromid))
    l = []

    for i in res:
        l.append({"id": i.id, "message": i.message, "to": i.TO_id, "date": i.date, "from": i.FROM_id})

    return JsonResponse({'photo': qry.photo, "data": l, 'name': qry.name, 'toid': request.session["userid"]})

def chat_send(request, msg):
    lid = request.session["lid"]
    toid = request.session["userid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.message = message
    chatobt.TO_id = toid
    chatobt.FROM_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})


###############user chat with trainer



def chat2(request,id):
    request.session["userid"] = id
    cid = str(request.session["userid"])
    request.session["new"] = cid
    qry = Trainer.objects.get(LOGIN__id=id)

    return render(request, "user/Chat.html", {'photo': qry.photo, 'name': qry.name, 'toid': cid})

def chat_view2(request):
    fromid = request.session["lid"]
    toid = request.session["userid"]
    qry = Trainer.objects.get(LOGIN=request.session["userid"])
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROM_id=fromid, TO_id=toid) | Q(FROM_id=toid, TO_id=fromid))
    l = []

    for i in res:
        l.append({"id": i.id, "message": i.message, "to": i.TO_id, "date": i.date, "from": i.FROM_id})

    return JsonResponse({'photo': qry.photo, "data": l, 'name': qry.name, 'toid': request.session["userid"]})

def chat_send2(request, msg):
    lid = request.session["lid"]
    toid = request.session["userid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.message = message
    chatobt.TO_id = toid
    chatobt.FROM_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})

def chatwithtrainer(request):
    view = Request.objects.filter(USER__LOGIN_id=request.session['lid'],status='approved')
    return render(request, "user/chatmessageuser.html", {'data': view})


def chatwithuser(request):
    view = Request.objects.filter(TRAINER__LOGIN_id=request.session['lid'],status='approved')
    return render(request, "user/chatmessageuser.html", {'data': view})







#COMMON

def logout(request):
    request.session['lid']=''
    return redirect('/myapp/login/')

