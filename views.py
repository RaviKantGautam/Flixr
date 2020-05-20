from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from database import *
from database import mail,SMS
from django.core.files.storage import FileSystemStorage
from random import randrange, randint
from datetime import *
import time
import http.client
import smtplib


@csrf_exempt
def adminRegisteration(request):
    if 'admin' in request.session:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['passw']
            type = request.POST['fname']
            mobile = request.POST['mobile']
            if email and password and type and mobile and ('@' in email) and (
                    str(mobile).isnumeric() == True) and str(
                type).isnumeric() == False:
                s = 'insert into admin values ("{}","{}","{}","{}",null)'.format(email, password, type, mobile)
                print(s)

                result = Insert(s)
                print(s)
                if result == 'success':
                    return HttpResponse(result)
                else:
                    return HttpResponse('Admin Already Exist')
            else:
                return HttpResponse('Data is not valid')
        else:
            return redirect(adminLogin)
    else:
        return redirect(adminLogin)


def adminDelete(request):
    s = 'delete from admin where email="{}"'.format(request.GET['email'])
    result = Delete(s)
    return HttpResponse(result)


@csrf_exempt
def adminUpdate(request):
    if 'admin' in request.session:
        email = request.POST['email']
        type = request.POST['fname']
        mobile = request.POST['mobile']
        if type and mobile and ('@' in email) and (str(mobile).isnumeric() == True) and str(
                type).isnumeric() == False:
            s = 'update admin set type="{}",mobile="{}" where email="{}"'.format(type, mobile, email)
            # print(s)
            result = Update(s)
            return HttpResponse(result)
    else:
        return redirect(adminLogin)


def adminview(request):
    if 'admin' in request.session and request.session['admin']['type'] == 'Super-Admin':
        s = 'select * from admin'
        result = Fetchall(s)
        lt = []
        count = 1
        for i in result:
            d = {}
            d['srno'] = count
            d['email'] = i[0]
            d['password'] = i[1]
            d['type'] = i[2]
            d['mobile'] = i[3]
            count += 1
            lt.append(d)
        return render(request, 'adminview.html', {'context': lt})
    else:
        return redirect(adminLogin)


@csrf_exempt
def adminLogin(request):
    if 'admin' in request.session:
        return redirect(alladmin)
    if request.method == 'POST':
        if request.POST['email'] and request.POST['passw']:
            s = 'select * from admin where email="{}" and password="{}"'.format(
                request.POST['email'], request.POST['passw'])
            result = Fetchone(s)
            if result != None:
                request.session['admin'] = {'adminEmail': result[0], 'type': result[2], 'mobile': result[3]}
                return redirect(alladmin)
            else:
                return render(request, 'adminLogin.html',
                              {'title': 'Admin Login', 'message': 'Email and Password is not correct'})
        else:
            return render(request, 'adminLogin.html',
                          {'title': 'Admin Login', 'message': 'Email and Password is not correct'})
    return render(request, 'adminLogin.html', {'title': 'Admin Login'})


def adminChangePassword(request):
    if 'admin' in request.session:
        if request.method == 'POST':
            s = 'select password from admin where email="{}"'.format(request.session['admin']['adminEmail'])
            result = Fetchone(s)
            if request.POST['opassw'] == result[0]:
                u = 'update admin set password="{}" where email="{}"'.format(request.POST['npassw'],
                                                                             request.session['admin'][
                                                                                 'adminEmail'])
                result = Update(u)
                if result == 'success':
                    return HttpResponse(result)
                else:
                    return HttpResponse('Something went wrong. Try after sometime')
            else:
                return HttpResponse('Wrong Password; or Try after some time!!')
        return redirect(alladmin)
    else:
        return redirect(adminLogin)


def alladmin(request):
    if 'admin' in request.session:
        s = 'SELECT * FROM `booking` INNER JOIN showtimings on booking.showtimeid=showtimings.id INNER JOIN shows on showtimings.showid=shows.id INNER JOIN movies on shows.movieid=movies.movieid'
        result = Fetchall(s)
        lt = []
        for i in result:
            d = {}
            d['id'] = i[0]
            d['noofseat'] = i[4]
            d['grandtotal'] = i[3]
            d['useremail'] = i[5]
            d['bookdate'] = i[6]
            d['audi'] = i[8]
            d['showtime'] = i[10]
            d['moviename'] = i[16]
            d['coverphoto'] = i[18]
            lt.append(d)
        return render(request, 'adminDashBoard.html', {'context': lt})
    else:
        return redirect(adminLogin)


def adminlogout(request):
    if 'admin' in request.session:
        request.session['admin'] = ''
        del request.session['admin']
    return redirect(adminLogin)


@csrf_exempt
def addmovies(request):
    if 'admin' in request.session:
        if request.method == 'POST':
            moviename = request.POST['moviename']
            description = request.POST['description']
            direction = request.POST['direction']
            phouse = request.POST['phouse']
            genre = request.POST['genre']
            releaseDate = request.POST['releaseDate']
            file = request.FILES['file']
            uploadphoto = str(randint(1, 1000)) + file.name
            # print(moviename, description, direction, phouse, genre, releaseDate, uploadphoto)
            if str(moviename).isnumeric() == False and str(direction).isnumeric() == False and str(
                    phouse).isnumeric() == False:
                k = "INSERT INTO movies (movieid, moviename, description, coverphoto, direction, productionhouse, dateofrelease, genre) VALUES (null ,'{}','{}','{}','{}','{}','{}','{}')".format(
                    moviename, description, uploadphoto, direction, phouse, releaseDate, genre)
                # print(k)
                result2 = Insert(k)
                # print(result2)
                if result2 == 'success':
                    fs = FileSystemStorage()
                    fs.save(uploadphoto, file)
                    return redirect(viewMovies)
                else:
                    return render(request, 'viewMovies.html', {'message': 'Something went wrong!'})
            else:
                return render(request, 'viewMovies.html', {'message': 'Invalid Data!'})
        return render(request, 'viewMovies.html')
    else:
        return redirect(adminLogin)


def addtheatre(request):
    if 'admin' in request.session:
        if request.method == 'POST':
            description = request.POST['description']
            city = request.POST['city']
            location = request.POST['location']
            password = request.POST['password']
            file = request.FILES['file']
            uploadphoto = str(randint(1, 1000)) + file.name
            # print(moviename, description, direction, phouse, genre, releaseDate, uploadphoto)
            if str(city).isnumeric() == False and str(location).isnumeric() == False:
                k = "INSERT INTO theatres (theatreid, city, location, description,password, coverphoto) VALUES (null ,'{}','{}','{}','{}','{}')".format(
                    city, location, description, password, uploadphoto)
                # print(k)
                result2 = Insert(k)
                # print(result2)
                if result2 == 'success':
                    fs = FileSystemStorage()
                    fs.save(uploadphoto, file)
                    return redirect(theater)
                else:
                    return render(request, 'viewTheatre.html', {'message': 'Something went wrong!'})
            else:
                return render(request, 'viewTheatre.html', {'message': 'Invalid Data!'})
        return render(request, 'viewTheatre.html')
    else:
        return redirect(adminLogin)


def addMerchandise(request):
    if 'admin' in request.session:
        if request.method == 'POST':
            productname = request.POST['productname']
            price = request.POST['price']
            stock = request.POST['stock']
            movie = request.POST['movie']
            prodesc = request.POST['prodesc']
            if str(productname).isnumeric() == False and str(price).isnumeric() == True and stock:
                try:
                    photo1 = request.FILES['photo1']
                    photo2 = request.FILES['photo2']
                    photo3 = request.FILES['photo3']
                    uploadphoto1 = str(randint(1, 1000)) + photo1.name
                    uploadphoto2 = str(randint(1, 1000)) + photo2.name
                    uploadphoto3 = str(randint(1, 1000)) + photo3.name
                    k = "INSERT INTO merchandise (productid, productname, price,stock, movieid,productdescription, photo1, photo2, photo3) VALUES (null ,'{}','{}','{}','{}','{}','{}','{}','{}')".format(
                        productname, price, stock, movie, prodesc, uploadphoto1, uploadphoto2, uploadphoto3)
                    result2 = Insert(k)
                    # print(result2)
                    if result2 == 'success':
                        fs = FileSystemStorage()
                        fs.save(uploadphoto1, photo1)
                        fs.save(uploadphoto2, photo2)
                        fs.save(uploadphoto3, photo3)
                        return redirect(merchandise)
                    else:
                        return render(request, 'viewTheatre.html', {'message': 'Something went wrong!'})
                except:
                    k = "INSERT INTO merchandise (productid, productname, price,stock, movieid,prodesc) VALUES (null ,'{}','{}','{}','{}','{}','{}','{}','{}')".format(
                        productname, price, stock, movie, prodesc)
                    result2 = Insert(k)
                    if result2 == 'success':
                        return redirect(merchandise)
                    else:
                        return render(request, 'viewTheatre.html', {'message': 'Something went wrong!'})
            else:
                return render(request, 'viewTheatre.html', {'message': 'Invalid Data!'})
        return render(request, 'viewTheatre.html')
    else:
        return redirect(adminLogin)


def viewMovies(request):
    if 'admin' in request.session:
        s = "select * from movies"
        result = Fetchall(s)
        x = []
        if result != ():
            for r in result:
                d = {"movieid": r[0], 'moviename': r[1], 'description': r[2], 'coverphoto': r[3], 'direction': r[4],
                     'productionhouse': r[5], 'dateofrelease': r[6], 'genre': r[7]}
                x.append(d)
            return render(request, 'viewMovies.html', {"ar": x})
        return render(request, 'viewMovies.html')
    else:
        return redirect(adminLogin)


def theater(request):
    if 'admin' in request.session:
        s = "select * from theatres"
        result = Fetchall(s)
        x = []
        if result != ():
            for r in result:
                d = {"theatreid": r[0], 'city': r[1], 'location': r[2], 'description': r[3], 'coverphoto': r[4],
                     'password': r[5]}
                x.append(d)
            return render(request, 'viewTheatre.html', {"ar": x})
        return render(request, 'viewTheatre.html')
    else:
        return redirect(adminLogin)


def theatrelogin(request):
    if 'theatre' in request.session:
        return redirect(theatrewelcome)
    if request.method == 'POST':
        if request.POST['theatreid'] and request.POST['password']:
            s = 'select theatreid from theatres where theatreid="{}" and password="{}"'.format(
                request.POST['theatreid'], request.POST['password'])
            result = Fetchone(s)
            if result != None:
                request.session['theatre'] = {'theatreid': result[0]}
                return redirect(theatrewelcome)
            else:
                return render(request, 'theatrelogin.html', {'message': 'ID and Password is not correct'})
        else:
            return render(request, 'theatrelogin.html', {'message': 'ID and Password is not correct'})
    return render(request, 'theatrelogin.html')


def theatrewelcome(request):
    if 'theatre' in request.session:
        return render(request, 'theatrewelcome.html')
    else:
        return redirect(theatrelogin)


def theatreview(request):
    if 'theatre' in request.session:
        return render(request, 'theatreview.html')
    else:
        return redirect(theatrelogin)


def addseat(request):
    if 'theatre' in request.session:
        return render(request, 'addseat.html')
    else:
        return redirect(theatrelogin)


def theatredata(request):
    try:
        data = request.GET['data']
    except:
        data = 'main'
    # print(data)
    if data == 'main':
        s = 'select * from ticket_category where threatreid="{}"'.format(request.session['theatre']['theatreid'])
    result = Fetchall(s)
    lt = []
    for i in result:
        d = {}
        d['id'] = i[0]
        d['catname'] = i[1]
        d['price'] = i[2]
        lt.append(d)
    # print(lt)
    return JsonResponse(lt, safe=False)


def seatdata(request):
    try:
        data = request.GET['data']
    except:
        data = 'main'
    # print(data)
    if data == 'main':
        s = 'select * from seating where theatreid="{}"'.format(request.session['theatre']['theatreid'])
    result = Fetchall(s)
    lt = []
    for i in result:
        d = {}
        d['id'] = i[0]
        d['seatnumber'] = i[1]
        d['price'] = i[2]
        d['auditoriumname'] = i[3]
        d['auditoriumkey'] = i[5]
        lt.append(d)
    # print(lt)
    return JsonResponse(lt, safe=False)


@csrf_exempt
def editticketchange(request):
    id = request.GET['id']
    catname = request.GET['catname']
    price = request.GET['price']
    s = 'UPDATE `ticket_category` SET `categoryname`="{}",`price`="{}" WHERE `id`="{}" and `threatreid`="{}"'.format(
        catname, price, id, request.session['theatre']['theatreid'])
    result = Update(s)
    if result == 'success':
        return HttpResponse(result)
    else:
        return HttpResponse(result)


@csrf_exempt
def editseatchanges(request):
    id = request.GET['id']
    catname = request.GET['catname']
    price = request.GET['price']
    s = 'UPDATE `seating` SET `categoryname`="{}",`price`="{}" WHERE `id`="{}" and `threatreid`="{}"'.format(
        catname, price, id, request.session['theatre']['theatreid'])
    result = Update(s)
    if result == 'success':
        return HttpResponse(result)
    else:
        return HttpResponse(result)


def deleteticketcategory(request):
    id = request.GET['id']
    s = 'DELETE FROM `ticket_category` WHERE id="{}"'.format(id)
    result = Delete(s)
    if result == 'success':
        return redirect(theatredata)
    else:
        return HttpResponse(result)


def deleteseat(request):
    id = request.GET['id']
    s = 'DELETE FROM `seating` WHERE id="{}"'.format(id)
    result = Delete(s)
    if result == 'success':
        return redirect(seatdata)
    else:
        return HttpResponse(result)


def addticketcategory(request):
    if request.method == 'POST':
        if request.POST['categoryname'] and request.POST['price'] and str(
                request.POST['price']).isnumeric() == True and str(request.POST['categoryname']).isnumeric() == False:
            s = 'insert into ticket_category values (null ,"{}","{}","{}")'.format(request.POST['categoryname'],
                                                                                   request.POST['price'],
                                                                                   request.session['theatre'][
                                                                                       'theatreid'])
            result = Insert(s)
            # print(result)
            if result == 'success':
                return redirect(theatredata)
            else:
                return HttpResponse(result)


def addseatsubmit(request):
    if request.method == 'POST':
        if request.POST['auditoriumname'] and request.POST['auditoriumkey'] and request.POST['seatnumber'] and str(
                request.POST['seatnumber']).isnumeric() == True and request.POST['seatprice'] and str(
            request.POST['seatprice']).isnumeric() == True and str(
            request.POST['auditoriumname']).isnumeric() == False:
            s = 'insert into seating values (null ,"{}","{}",,"{}",,"{}","{}")'.format(request.POST['seatnumber'],
                                                                                       request.POST['seatprice'],
                                                                                       request.POST['auditoriumname'],
                                                                                       request.session['theatre'][
                                                                                           'theatreid'],
                                                                                       request.POST['auditoriumkey'])
            result = Insert(s)
            # print(result)
            if result == 'success':
                return redirect(theatredata)
            else:
                return HttpResponse(result)


def merchandise(request):
    if 'admin' in request.session:
        p = 'select movieid,moviename from movies'
        result2 = Fetchall(p)
        s = "select * from merchandise"
        result = Fetchall(s)
        x = []
        if result != ():
            for r in result:
                k = 'select moviename from movies where movieid="{}"'.format(r[4])
                result1 = Fetchone(k)
                d = {"productid": r[0], 'productname': r[1], 'price': r[2], 'stock': r[3], 'movieid': result1[0],
                     'photo1': r[6],
                     'photo2': r[7], 'photo3': r[8]}
                x.append(d)
            return render(request, 'viewMerchandise.html', {"ar": x, 'movie': list(result2)})
        return render(request, 'viewMerchandise.html', {'movie': list(result2)})
    else:
        return redirect(adminLogin)


def deletemovie(request):
    try:
        vid = request.GET["vid"]
        videosname = request.GET['vidname']
        # print(videosname)
        s = "delete from movies where movieid='" + vid + "'"
        result = Delete(s)
        # print(result)
        if result == 'success':
            return HttpResponse(videosname + " Deleted Successfully")
        else:
            return HttpResponse('Something went wrong. Try after sometime!')
    except:
        return redirect(http4o4page)


def deletetheater(request):
    try:
        vid = request.GET["vid"]
        videosname = request.GET['vidname']
        # print(videosname)
        s = "delete from theatres where theatreid='" + vid + "'"
        result = Delete(s)
        # print(result)
        if result == 'success':
            return HttpResponse(videosname + " Deleted Successfully")
        else:
            return HttpResponse('Something went wrong. Try after sometime!')
    except:
        return redirect(http4o4page)


def deleteMerchandise(request):
    try:
        vid = request.GET["vid"]
        videosname = request.GET['vidname']
        # print(videosname)
        s = "delete from merchandise where productid='" + vid + "'"
        result = Delete(s)
        # print(result)
        if result == 'success':
            return HttpResponse(videosname + " Deleted Successfully")
        else:
            return HttpResponse('Something went wrong. Try after sometime!')
    except:
        return redirect(http4o4page)


def http4o4page(request):
    return render(request, '4o4page.html')


@csrf_exempt
def forgetpassword(request):
    if request.method == 'POST':
        status = request.POST['status']
        # print(status)

        email = ''
        phone = ''
        try:
            email = request.POST['email']
            phone = request.POST['phone']
        except:
            try:
                phone = request.POST['phone']
                email = ''
            except:
                email = request.POST['email']
                phone = ''
        if status == 'client':
            otp = randrange(10000, 99999)
            data=''
            if email != '' and phone != '':
                s = 'select email,mobilenumber from customers where email="{}" and mobilenumber="{}"'.format(email, phone)
                d = 'UPDATE customers SET otp="{}" WHERE email="{}" and mobilenumber="{}"'.format(otp, email, phone)
                data = 'email-phone'
            elif email != '':
                s = 'select email from customers where email="{}"'.format(email)
                d = 'UPDATE customers SET otp="{}" WHERE email="{}"'.format(otp, email)
                data='email'
            else:
                s = 'select mobilenumber from customers where mobilenumber="{}"'.format(phone)
                d = 'UPDATE customers SET otp="{}" WHERE mobilenumber="{}"'.format(otp, phone)
                data='phone'
            result = Fetchone(s)
            if result != None:
                result1 = Update(d)
                if result1 == 'success':
                    request.session['otp'] = {'otp': otp, 'crendential': result[0], 'status': status}
                    msg = 'Your OTP is = ' + str(otp)
                    if data == 'email-phone':
                        mail.send_Mail(email,msg)
                        SMS.confirm_Msg(phone, msg)
                    elif data == 'email':
                        mail.send_Mail(email, msg)
                    else:
                        SMS.confirm_Msg(phone, msg)
                    return HttpResponse(result1)
            else:
                return HttpResponse(result)
        elif status == 'admin':
            otp = randrange(10000, 99999)
            data = ''
            if email != '' and phone != '':
                s = 'select email,mobile from admin where email="{}" and mobile="{}"'.format(email, phone)
                d = 'UPDATE admin SET otp="{}" WHERE email="{}" and mobile="{}"'.format(otp, email, phone)
                data = 'email-phone'
            elif email != '':
                s = 'select email from admin where email="{}"'.format(email)
                d = 'UPDATE admin SET otp="{}" WHERE email="{}"'.format(otp, email)
                data='email'
            else:
                s = 'select mobile from admin where mobile="{}"'.format(phone)
                d = 'UPDATE admin SET otp="{}" WHERE mobile="{}"'.format(otp, phone)
                data='phone'
            result = Fetchone(s)
            if result != None:
                result1 = Update(d)
                if result1 == 'success':
                    request.session['otp'] = {'otp': otp, 'crendential': result[0], 'status': status}
                    msg = 'Your OTP is = ' + str(otp)
                    if data=='email-phone':
                        mail.send_Mail(email,msg)
                        SMS.confirm_Msg(phone,msg)
                    elif data=='email':
                        mail.send_Mail(email,msg)
                    else:
                        SMS.confirm_Msg(phone,msg)
                    return HttpResponse(result1)
            else:
                print('select')
                return HttpResponse(result)
        return HttpResponse('success')
    else:
        return HttpResponse('error')

def forgetpage(request):
    if request.method == 'POST':
        otp = request.POST['otppage']
        print(otp)
        print(request.session['otp'])
        if str(request.session['otp']['otp']) == str(otp):
            return render(request, 'otpchangepassword.html')
        else:
            return render(request, 'forgetpage.html', {'message': 'otp is wrong'})
    return render(request, 'forgetpage.html')

def otpchangepassword(request):
    if request.method == "POST":
        print(request.session['otp'])
        status = request.session['otp']['status']
        if status == 'client':
            if '@' in str(request.session['otp']['crendential']):
                s = 'update customers set password="{}", otp="{}" where email="{}"'.format(
                    request.POST['cpassw'], None, request.session['otp']['crendential'])
            else:
                s = 'update customers set password="{}", otp="{}" where mobilenumber="{}"'.format(
                    request.POST['cpassw'], None, request.session['otp']['crendential'])
            result = Update(s)
            if result == 'success':
                request.session['otp'] = ''
                del request.session['otp']
                return redirect(clientLogin)
            else:
                return render(request, 'otpchangepassword.html', {'message': result})
        elif status == 'admin':
            if '@' in str(request.session['otp']['crendential']):
                s = 'update admin set password="{}", otp="{}" where email="{}"'.format(request.POST['cpassw'], None,
                                                                                       request.session['otp'][
                                                                                           'crendential'])
            else:
                s = 'update admin set password="{}", otp="{}" where mobile="{}"'.format(request.POST['cpassw'], None,
                                                                                        request.session['otp'][
                                                                                            'crendential'])
            result = Update(s)
            if result == 'success':
                request.session['otp'] = ''
                del request.session['otp']
                return redirect(adminLogin)
            else:
                return render(request, 'otpchangepassword.html', {'message': result})
        else:
            return render(request, 'otpchangepassword.html', {'message': 'unidentified status'})


def theatrechangepassword(request):
    if request.method == 'POST':
        s = 'select password from theatres where theatreid="{}"'.format(request.session['theatre']['theatreid'])
        result = Fetchone(s)
        if request.POST['opassw'] == result[0]:
            u = 'update theatres set password="{}" where theatreid="{}"'.format(request.POST['npassw'],
                                                                                request.session['theatre']['theatreid'])
            result = Update(u)
            if result == 'success':
                return HttpResponse(result)
            else:
                return HttpResponse('Something went wrong. Try after sometime')
        else:
            return HttpResponse('Wrong Password; or Try after some time!!')
    return redirect(theatreview)


def theatrelogout(request):
    if 'theatre' in request.session:
        request.session['theatre'] = ''
        del request.session['theatre']
    return redirect(theatrelogin)


def demo(request):
    result = [15, 67, 4, 32, 3, 6]
    lt = []
    for i in range(1, 201):
        d = {}
        if i in result:
            d['booked'] = i
        else:
            d['unbooked'] = i
        lt.append(d)
    # print(lt)
    return render(request, 'demo.html', {'context': lt})


def index(request):
    p = 'select movieid,moviename,coverphoto from movies limit 10'
    result2 = Fetchall(p)
    s = 'select productid,productname,photo1,stock from merchandise limit 10'
    result = Fetchall(s)
    return render(request, 'index.html', {'movie': list(result2), 'product': list(result)})


def shopproductbymovie(request):
    id = request.GET['id']
    k = 'select * from merchandise where movieid="{}"'.format(id)
    result = Fetchall(k)
    # print(result)
    x = []
    if result == ():
        s = 'select * from merchandise'
        result = Fetchall(s)
    for r in result:
        d = {"productid": r[0], 'productname': r[1], 'price': r[2], 'stock': r[3], 'photo1': r[6], 'photo2': r[7],
             'photo3': r[8]}
        x.append(d)
    t = 'select * from movies where movieid="{}"'.format(id)
    result1 = Fetchone(t)
    try:
        bookquery = 'select * from shows where movieid="{}" order by id DESC'.format(id)
        bookresult = Fetchone(bookquery)
        if bookresult[1] < date.today() and bookresult[1] > date.today() - timedelta(days=30):
            status = {"booking": 'bookticket', 'showid': bookresult[0]}
        elif bookresult[1] > date.today():
            status = {"booking": 'Release Soon'}
        else:
            status = {"booking": 'nowavailable'}
    except:
        status = {"booking": 'nowavailable'}
    return render(request, 'category.html', {'context': x, "movie": list(result1), 'status': status})


def productdetail(request):
    id = request.GET['id']
    k = 'select `productid`, `productname`, `price`, `stock`, `moviename`, `productdescription`, `photo1`, `photo2`, `photo3` from merchandise inner join movies on merchandise.movieid=movies.movieid where productid="{}"'.format(
        id)
    r = Fetchone(k)
    # print(list(r))
    value = 0
    try:
        if request.session['product']:
            lb = list(request.session['product'])
            for i in lb:
                # print(i[0])
                if str(i[0]) == str(id):
                    value = i[5]
                    break
    except:
        pass
    d = {"productid": r[0], 'productname': r[1], 'price': r[2], 'stock': r[3], 'movie': r[4], 'productdescp': r[5],
         'photo1': r[6],
         'photo2': r[7], 'photo3': r[8]}
    return render(request, 'single-product.html', {'context': d, 'value': value})


def allmovie(request):
    s = 'select * from movies'
    result = Fetchall(s)
    return render(request, 'allmovie.html', {'context': list(result)})


def allproduct(request):
    s = 'select * from merchandise'
    result = Fetchall(s)
    return render(request, 'allproduct.html', {'context': list(result)})


def clientLogin(request):
    if request.method == 'POST':
        if request.POST['email'] and request.POST['passw']:
            s = 'select email,password,mobilenumber from customers where email="{}" and password="{}"'.format(
                request.POST['email'], request.POST['passw'])
            result = Fetchone(s)
            if result == None or result=='INVALID QUERY':
                return render(request, 'login.html',
                              {'message': 'Email and Password is not correct'})
            else:
                request.session['client'] = {'clientEmail': request.POST['email'], "clientPhone": result[2]}
                return redirect(index)

        else:
            return render(request, 'login.html',
                          {'message': 'Email and Password is not correct'})
    return render(request, 'login.html')


@csrf_exempt
def clientRegistration(request):
    try:
        del request.session['client']
    except:
        pass
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        dob = request.POST['dob']
        gender = request.POST['gender']
        mobile = request.POST['mobile']
        if email and password and dob and gender and mobile and ('@' in email) and (str(mobile).isnumeric() == True):
            s = 'insert into customers values ("{}","{}","{}","{}","{}",null)'.format(email, password, dob, gender,
                                                                                      mobile)
            # print(s)
            result = Insert(s)
            if result == 'success':
                return redirect(clientLogin)
            else:
                return render(request, 'registration.html', {'message': 'Technical Error or Email is already taken'})
        else:
            return render(request, 'registration.html', {'message': 'Data is not correct'})
    return render(request, 'registration.html')


@csrf_exempt
def sessionProduct(request):
    s = 'select * from merchandise where productid="{}"'.format(request.GET['q'])
    result = Fetchone(s)
    # print(list(result))
    if 'product' in request.session:
        lt = list(request.session['product'])
        for i in lt:
            if str(i[0]) == str(request.GET['q']):
                try:
                    qty = request.GET['qty']
                    i[9] = int(qty)
                    i[10] = round(result[2] * i[5], 2)
                    request.session['product'] = lt
                    break
                except:
                    i[9] = int(1)
                    i[10] = round(result[2] * i[5], 2)
                    request.session['product'] = lt
                    break
        else:
            try:
                qty = int(request.GET['qty'])
            except:
                qty = 1
            d = list(result)
            d.append(qty)
            d.append(round(result[2] * qty, 2))
            lt.append(d)
            request.session['product'] = lt
    else:
        try:
            qty = int(request.GET['qty'])
        except:
            qty = 1
        lt = []
        d = list(result)
        d.append(qty)
        d.append(round(result[2] * qty, 2))
        lt.append(d)
        request.session['product'] = lt
    return HttpResponse(len(lt))


def categorymovies(request):
    s = 'select moviename,movieid from movies'
    result = Fetchall(s)
    return JsonResponse(list(result), safe=False)


def categoryproduct(request):
    s = 'select productname,productid from merchandise group by productname'
    result = Fetchall(s)
    return JsonResponse(list(result), safe=False)


def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        msg = "Name: "+str(name)+"\nSubject:"+str(subject)+"\n"+str(message)
        mail.send_Mail(email,msg)
    return render(request, 'contact.html')


def cart(request):
    if 'product' in request.session:
        grandtotal = 0
        for i in request.session['product']:
            grandtotal += i[10]
        return render(request, 'cart.html', {'grandtotal': grandtotal})
    else:
        return redirect(index)


def cartDetail(request):
    data = request.GET['qty']
    q = str(request.GET['q'])
    grandtotal = 0
    qty = 0
    nettotal = 0
    if 'product' in request.session:
        lt = list(request.session['product'])
        for i in lt:
            if str(i[0]) == q:
                i[9] += int(data)
                qty = i[9]
                i[10] = round(i[2] * i[9], 2)
                nettotal = i[10]
                request.session['product'] = lt
                break
        for j in lt:
            grandtotal += j[10]
    lts = [{'qty': qty, 'nettotal': nettotal, 'grandtotal': round(grandtotal, 2)}]
    # print(lts)
    return JsonResponse(lts, safe=False)


def checkout(request):
    grandtotal = 0
    for i in request.session['product']:
        grandtotal += i[10]
    return render(request, 'checkout.html', {'grandtotal': grandtotal})


@csrf_exempt
def paymentBill(request):
    result3 = ""
    msg = ""
    if request.method == "POST":
        streetAddress = request.POST['streetAddress']
        town = request.POST['town']
        zipcode = request.POST['zipcode']
        ordernote = request.POST['ordernote']
        grandtotal = request.POST['grandtotal']
        paymentmethod = request.POST['paymentmethod']
        # print(paymentmethod)
        if streetAddress and town and zipcode and str(zipcode).isnumeric() == True and str(town) != '#':
            s = 'insert into bill (billID,datatime,grandtotal,payment_method,city,zipcode,address,remarks,email,status) values (null,"{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(
                datetime.today().now(),
                grandtotal,
                paymentmethod, town,
                zipcode, streetAddress,
                ordernote, str(request.session['client']['clientEmail']), 'pending')
            # print(s)
            result = Insert(s)
            # print(result)
            if result == 'success':
                s1 = 'select billID,datatime from bill order by billID DESC'
                result1 = Fetchone(s1)
                # print(result1[0])
                msg = "Dear " + str(request.session['client'][
                    'clientEmail']) + ",\nThank you for Shopping with us.\nOrder No. " + str(result1[
                          0]) + "\nOrder Date\Time " + str(result1[1]) + "\n"
                lb = list(request.session['product'])
                # print(lb)
                for i in lb:
                    s2 = 'insert into billdetail values (null,"{}","{}","{}","{}")'.format(i[3], i[10], i[0],
                                                                                           result1[0])
                    result2 = Insert(s2)
                    # print(result2)
                    b = 'select productname from merchandise where productid="{}"'.format(i[0])
                    rest = Fetchone(b)
                    msg += str(rest[0]) + " (" + str(i[2]) +" X " + str(i[9]) + " ) = " + str(i[10]) + "\n"
                    print(msg)
                    if result2 == 'success':
                        u = 'update merchandise set stock="{}" where productid="{}"'.format(str(int(i[3]) - int(i[9])),
                                                                                            str(i[0]))
                        result3 = Update(u)
                        # print(result3)
                if result3 == 'success':
                    try:
                        mobile = request.POST["disphone"]
                    except:
                        mobile = request.session['client']['clientPhone']
                    msg += 'Total Amount = ' + str(grandtotal)
                    mail.send_Mail(str(request.session['client']['clientEmail']),msg)
                    # SMS.confirm_Msg(mobile, msg)
                    request.session['product'] = ''
                    del request.session['product']
                    return HttpResponse(result1[0])
                else:
                    return redirect(failedPayment)
            else:
                return render(request, 'checkout.html', {'message': 'Data not Valid'})
    return redirect(cart)


def thanks(request):
    if 'client' in request.session:
        return render(request, 'thanks.html', {'orderid': request.GET['orderid']})
    else:
        return redirect(index)


def failedPayment(request):
    if 'product' in request.session:
        return render(request, 'failedPayment.html')
    else:
        return redirect(index)


def grandtotal(request):
    grandtotalconfirm = 0
    for i in request.session['product']:
        grandtotalconfirm += i[10]
    # print(grandtotalconfirm)
    return HttpResponse(grandtotalconfirm)


def goback(request):
    request.session['product'] = ""
    del request.session['product']
    return redirect(index)


def myaccount(request):
    if 'client' in request.session:
        s = 'select * from bill where email="' + request.session['client']['clientEmail'] + '"'
        # print(s)
        result = Fetchall(s)
        lt = []
        count = 1
        for i in result[::-1]:
            d = {}
            d['srno'] = count
            d['billid'] = i[0]
            d['billtime'] = i[1]
            d['grandtotal'] = i[2]
            d['paymentmethod'] = i[3]
            d['city'] = i[4]
            d['zipcode'] = i[5]
            d['address'] = i[6]
            d['remarks'] = i[7]
            d['status'] = i[9]
            lt.append(d)
            count += 1
        return render(request, 'myaccount.html', {'context': lt})
    else:
        return redirect(index)


def cientproductdetail(request):
    try:
        h = 'select * from bill where billid="{}"'.format(request.GET['billid'])
        # print(h)
        result1 = Fetchone(h)
        # lt = []
        k = {}
        # k['srno'] = count1
        k['billid'] = result1[0]
        k['billtime'] = result1[1]
        k['grandtotal'] = result1[2]
        k['paymentmethod'] = result1[3]
        k['city'] = result1[4]
        k['zipcode'] = result1[5]
        k['address'] = result1[6]
        k['status'] = result1[9]
        # print(k)

        s = 'select * from billdetail where billid="{}"'.format(request.GET['billid'])
        result = Fetchall(s)
        lt = []
        count = 1
        for i in result:
            d = {}
            d['srno'] = count
            d['price'] = i[1]
            d['quantity'] = i[2]
            p = 'select productname,photo1 from merchandise where productid="{}"'.format(i[3])
            result2 = Fetchone(p)
            d['product'] = [result2[0], result2[1]]
            lt.append(d)
            count += 1
        return render(request, 'myaccountdetail.html', {'context': lt, 'i': k})
    except:
        return redirect(index)


def cancelledorder(request):
    try:
        result3 = ""
        s = 'update bill set status="cancelled",cancelledremarks="{}" where billID="{}"'.format(
            str(request.GET['remarks']),
            request.GET['billid'])
        result = Update(s)
        # print(result)
        p = 'select quantity,productid from billdetail where billid="{}"'.format(request.GET['billid'])
        result1 = Fetchall(p)
        # print(result1)
        for i in result1:
            f = 'select stock from mechandise where productid="{}"'.format(i[1])
            result2 = Fetchone(f)
            # print('result2', result2)
            u = 'update merchandise set stock="{}" where productid="{}"'.format(int(result2[0]) + int(i[0]), i[1])
            result3 = Update(u)
            # print('result3', result3)
        return HttpResponse(result3)
    except:
        return redirect(index)


def orderdetails(request):
    search = request.GET['search']
    # print(search)
    if search == 'all':
        s = 'select * from bill'
    else:
        s = 'select * from bill where status="{}"'.format(search)
    result = Fetchall(s)
    lt = []
    count = 1
    for i in result[::-1]:
        d = {}
        d['srno'] = count
        d['orderno'] = i[0]
        d['datatime'] = i[1]
        d['grandtotal'] = i[2]
        d['paymentmethod'] = i[3]
        d['useremail'] = i[8]
        f = 'select mobilenumber from customers where email="{}"'.format(i[8])
        result2 = Fetchone(f)
        d['userphone'] = [result2[0]]
        d['status'] = i[9]
        count += 1
        lt.append(d)
    # print(lt)
    return JsonResponse(lt, safe=False)


def billdetails(request):
    s = 'select * from billdetail where billid="{}"'.format(request.GET['billid'])
    result = Fetchall(s)
    lt = []
    for i in result:
        d = {}
        d['price'] = i[1]
        d['quantity'] = i[2]
        s1 = 'select productname,photo1,productid from merchandise where productid="{}"'.format(i[3])
        result1 = Fetchone(s1)
        d['product'] = [result1[0], result1[1], result1[2]]
        lt.append(d)
    return JsonResponse(lt, safe=False)


@csrf_exempt
def shipping(request):
    if request.method == 'POST':
        if request.POST['trackingid'] and request.POST['companyname'] and request.POST['trackingurl'] and request.POST[
            'email'] and str(request.POST['trackingid']).isnumeric() == True and str(
            request.POST['companyname']).isnumeric() == False:
            s = 'update bill set trackid="{}", companyname="{}", trackurl="{}", status="Shipped", remarks="{}" where billID="{}" and status!="cancelled"'.format(
                request.POST['trackingid'], request.POST['companyname'], request.POST['trackingurl'],
                request.POST['remark'], request.POST['orderno'])
            result1 = Update(s)
            if result1 == 'success':
                s = 'select email from bill where billID="{}"'.format(request.POST['orderno'])
                email = Fetchone(s)
                msg = 'Thank You For Shopping With us. Your Package Has Been Shipped Now'
                mail.send_Mail(email[0],msg)
                return HttpResponse(s)
        else:
            return HttpResponse('Data not valid')


@csrf_exempt
def dispatched(request):
    if request.method == 'POST':
        if request.POST['disorderno'] and request.POST['personrecieved'] and str(
                request.POST['personrecieved']).isnumeric() == False:
            s = 'update bill set status="Dispatched", personrecieved="{}" where billID="{}" and status!="cancelled"'.format(
                request.POST['personrecieved'], request.POST['disorderno'])
            print(s)
            result1 = Update(s)
            print(result1)
            if result1 == 'success':
                t = 'select email from bill where billID="{}"'.format(request.POST['disorderno'])
                email = Fetchone(t)
                print(email)
                msg = "Thank You For Shopping With us. Your Package has been dispatched"
                mail.send_Mail(email[0],msg)
                return HttpResponse(result1)
        else:
            return HttpResponse('Data not valid')


def searchdata(request):
    datafrom = request.GET['datafrom']
    datato = request.GET['dateto']
    status = str(request.GET['status'])
    # print(status,type(status))
    if status == 'all':
        s = 'SELECT * FROM bill WHERE datatime BETWEEN "{}" AND "{}"'.format(datafrom, datato)
    else:
        s = 'SELECT * FROM bill WHERE datatime BETWEEN "{}" AND "{}" and status="{}"'.format(datafrom, datato, status)
    # print(s)
    result = Fetchall(s)
    # print("result",list(result))
    lt = []
    count = 1
    for i in result[::-1]:
        d = {}
        d['srno'] = count
        d['orderno'] = i[0]
        d['datatime'] = i[1]
        d['grandtotal'] = i[2]
        d['paymentmethod'] = i[3]
        d['useremail'] = i[8]
        f = 'select mobilenumber from customers where email="{}"'.format(i[8])
        result2 = Fetchone(f)
        d['userphone'] = [result2[0]]
        d['status'] = i[9]
        count += 1
        lt.append(d)
    # print(lt)
    return JsonResponse(lt, safe=False)


def bookticketpage(request):
    if 'client' in request.session:
        movieid = request.GET['movieid']
        showid = request.GET['showid']
        s = 'select * from movies where movieid="{}"'.format(movieid)
        result = Fetchone(s)
        p = 'select * from showtimings where showid="{}" order by id DESC'.format(showid)
        result1 = Fetchone(p)
        return render(request, 'bookticketpage.html', {'movie': list(result), 'showtiming': list(result1)})
    else:
        return redirect(clientLogin)


def theatrecategory(request):
    try:
        s = 'select * from ticket_category where threatreid="{}"'.format(request.GET['threatedid'])
    except:
        s = 'select * from ticket_category where threatreid=1'
    result = Fetchall(s)
    lt = []
    for i in result:
        d = {}
        d['id'] = i[0]
        d['categoryname'] = i[1]
        d['price'] = i[2]
        d['threatreid'] = i[3]
        lt.append(d)
    return JsonResponse(lt, safe=False)


def theatredetails(request):
    if 'admin' not in request.session:
        return redirect(index)
    try:
        s = 'select * from theatres where theatreid="{}"'.format(request.GET['threatedid'])
    except:
        s = 'select * from theatres where theatreid=1'
    result = Fetchall(s)
    lt = []
    for i in result:
        d = {}
        d['threatreid'] = i[0]
        d['city'] = i[1]
        d['location'] = i[2]
        d['description'] = i[3]
        d['coverphoto'] = i[4]
        lt.append(d)
    return JsonResponse(lt, safe=False)


def seatchair(request):
    lt = []
    return JsonResponse(lt, safe=False)


def viewshow(request):
    if 'admin' in request.session:
        s = "select * from shows inner join movies on shows.movieid=movies.movieid"
        print(s)
        result = Fetchall(s)
        x = []
        movielist = []
        moviequery = 'select movieid,moviename from movies'
        movieresult = Fetchall(moviequery)
        for j in movieresult:
            moviedict = {'movieid': j[0], "moviename": j[1]}
            movielist.append(moviedict)
        if result != ():
            for r in result:
                d = {"showid": r[0], 'showdate': r[1], 'movieid': r[2], 'coverphoto': r[6], 'moviename': r[4]}
                x.append(d)
            return render(request, 'viewshow.html', {"ar": x, 'movie': movielist})
        return render(request, 'viewshow.html', {'movie': movielist})
    else:
        return redirect(adminLogin)


def deleteshow(request):
    try:
        showid = request.GET["showid"]
        moviename = request.GET['moviename']
        # print(videosname)
        s = "delete from shows where id='" + showid + "'"
        result = Delete(s)
        # print(result)
        if result == 'success':
            return HttpResponse(moviename + "Show Deleted Successfully")
        else:
            return HttpResponse('Something went wrong. Try after sometime!')
    except:
        return redirect(http4o4page)


def addshow(request):
    if 'admin' in request.session:
        if request.method == 'POST':
            if request.POST['showdate']:
                s = f'INSERT INTO `shows`(`id`, `showdate`, `movieid`) VALUES (null,"{request.POST["showdate"]}","{request.POST["movie"]}")'
                result = Insert(s)
                if result == 'success':
                    return redirect(viewshow)
                else:
                    return render(request, 'viewshow.html', {'message': 'Something went wrong!'})
            else:
                return render(request, 'viewshow.html', {'message': 'Invalid Data!'})
        return render(request, 'viewshow.html')
    else:
        return redirect(adminLogin)


def showtimingsview(request):
    if 'admin' in request.session:
        s = 'select * from showtimings inner join  shows on showtimings.showid=shows.id where showtimings.showid="{}"'.format(
            request.GET['showid'])
        result = Fetchall(s)
        showlist = []
        for i in result:
            showdict = {'id': i[0], 'audi': i[1], 'price': i[2], 'showtime': str(i[3]), 'showid': i[4],
                        'showdate': i[6]}
            showlist.append(showdict)
        print(showlist)
        return JsonResponse(showlist, safe=False)
    else:
        return redirect(adminLogin)


def addshowtimingsubmit(request):
    if 'admin' in request.session:
        if request.method == 'POST':
            if request.POST['price'] and str(request.POST['price']).isnumeric() == True and request.POST['time']:
                s = f'INSERT INTO `showtimings`(`id`, `audi`, `price`, `showtime`, `showid`) VALUES (null,"{request.POST["audi"]}","{request.POST["price"]}","{request.POST["time"]}","{request.POST["showid"]}")'
                result = Insert(s)
                if result == 'success':
                    return HttpResponseRedirect("showtimingsview?showid=" + request.POST['showid'])
                else:
                    return render(request, 'viewshow.html', {'message': 'Something went wrong!'})
            else:
                return render(request, 'viewshow.html', {'message': 'Invalid Data!'})
        return render(request, 'viewshow.html')
    else:
        return redirect(adminLogin)


def deleteshowtime(request):
    if 'admin' not in request.session:
        return redirect(index)
    showtimeid = request.GET['showtimeid']
    showid = request.GET['showid']
    s = 'DELETE FROM `showtimings` WHERE `id`="{}"'.format(showtimeid)
    result = Delete(s)
    if result == 'success':
        return HttpResponseRedirect("showtimingsview?showid=" + showid)
    else:
        print(s)
        print(result)


@csrf_exempt
def seatselected(request):
    if 'client' in request.session:
        if request.method == 'POST':
            seat = request.POST['seat']
            numberofseat = request.POST['numberofseat']
            grandtotal = request.POST['grandtotal']
            showtimeid = request.POST['showtimeid']
            s = f'INSERT INTO `booking`(`id`, `showtimeid`, `seats`, `grandtotal`, `noofseats`, `useremail`, `datetime`) VALUES (null,"{showtimeid}","{seat}","{grandtotal}","{numberofseat}","{request.session["client"]["clientEmail"]}","{datetime.today()}")'
            print(s)
            result = Insert(s)
            p = 'select id from booking order by id DESC'
            result1 = Fetchone(p)
            if result == 'success':
                msg = 'Thank You!'
                msg += '\n Your Ticket Id is: {}'.format(result1[0])
                mail.send_Mail(request.session["client"]["clientEmail"],msg)
                return HttpResponse(result1)
        return HttpResponse('success')
    else:
        return redirect(index)


def selectedseat(request):
    if 'client' not in request.session:
        return redirect(index)
    showtimeid = request.GET['showtimeid']
    s = 'select seats from booking where showtimeid="{}"'.format(showtimeid)
    result = Fetchall(s)
    lt = []
    print(list(result))
    for i in result:
        print(i)
        for j in list(i):
            lt.extend(j.split(','))
    print(lt)
    return JsonResponse(lt, safe=False)


def thankticketbook(request):
    if 'client' not in request.session:
        return redirect(index)
    thicketid = request.GET['thicketid']
    s = 'select * from booking where id="{}"'.format(thicketid)
    result = Fetchone(s)
    return render(request, 'thankTicketbook.html', {'ticketid': list(result)})


def failedPaymentticket(request):
    if 'client' in request.session:
        return render(request, 'failedPaymentticket.html')
    else:
        return redirect(index)


def ticketdetail(request):
    id = request.GET['id']
    s = 'SELECT * FROM `booking` INNER JOIN showtimings on booking.showtimeid=showtimings.id INNER JOIN shows on showtimings.showid=shows.id INNER JOIN movies on shows.movieid=movies.movieid where booking.id="{}"'.format(
        id)
    i = Fetchone(s)
    d = {}
    d['id'] = i[0]
    d['seat'] = i[2]
    d['noofseat'] = i[4]
    d['grandtotal'] = i[3]
    d['price'] = i[9]
    d['showdate'] = i[13]
    d['useremail'] = i[5]
    d['bookdate'] = i[6]
    d['audi'] = i[8]
    d['showtime'] = i[10]
    d['moviename'] = i[16]
    d['coverphoto'] = i[18]
    return JsonResponse(d,safe=False)

def clientlogout(request):
    try:
        if 'client' in request.session:
            request.session['client']=''
            del request.session['client']
            return redirect(index)
    except:
        return redirect(index)
