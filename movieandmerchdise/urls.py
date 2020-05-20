"""movieandmerchdise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from views import *


urlpatterns = [
    path('adminLogin', adminLogin),
    path('adminRegisteration', adminRegisteration),
    path('adminlogout', adminlogout),
    path('alladmin', alladmin),
    path('adminview', adminview),
    path('adminChangePassword', adminChangePassword),
    path('adminUpdate', adminUpdate),
    path('adminDelete', adminDelete),

    path('movie',viewMovies),
    path('addmovies',addmovies),
    path('deletemovie',deletemovie),

    path('theater',theater),
    path('addtheatre',addtheatre),
    path('deletetheater',deletetheater),
    path('theatrelogin',theatrelogin),
    path('theatreview',theatreview),
    path('theatrechangepassword',theatrechangepassword),
    path('theatrelogout',theatrelogout),
    path('theatredata',theatredata),
    path('addticketcategory',addticketcategory),
    path('deleteticketcategory',deleteticketcategory),
    path('editticketchange',editticketchange),

    path('deleteMerchandise',deleteMerchandise),
    path('merchandise',merchandise),
    path('addMerchandise',addMerchandise),


    path('demo',demo),
    path('seatselected',seatselected),
    path('',index),
    path('shopproductbymovie',shopproductbymovie),
    path('productdetail',productdetail),
    path('allmovie',allmovie),
    path('allproduct',allproduct),

    path('clientLogin',clientLogin),
    path('clientRegistration',clientRegistration),

    path('sessionProduct',sessionProduct),
    path('categorymovies',categorymovies),
    path('categoryproduct',categoryproduct),
    path('cart',cart),
    path('cartDetail',cartDetail),
    path('checkout',checkout),
    path('contact',contact),

    path('thanks',thanks),
    path('paymentBill',paymentBill),
    path('grandtotal',grandtotal),
    path('goback',goback),
    path('failedPayment',failedPayment),

    path('myaccount',myaccount),
    path('cientproductdetail',cientproductdetail),
    path('cancelledorder',cancelledorder),
    path('orderdetails',orderdetails),
    path('billdetails',billdetails),
    path('shipping',shipping),
    path('dispatched',dispatched),
    path('searchdata',searchdata),

    path('bookticketpage',bookticketpage),
    # path('theatrecategory',theatrecategory),
    # path('theatredetails',theatredetails),
    path('theatrewelcome',theatrewelcome),
    path('seatchair',seatchair),
    path('addseat',addseat),
    path('addseatsubmit',addseatsubmit),
    path('seatdata',seatdata),
    path('editseatchanges',editseatchanges),
    path('deleteseat',deleteseat),
    path('show',viewshow),
    path('deleteshow',deleteshow),
    path('addshow',addshow),
    path('showtimingsview',showtimingsview),
    path('addshowtimingsubmit',addshowtimingsubmit),
    path('deleteshowtime',deleteshowtime),
    path('selectedseat',selectedseat),
    path('thankticketbook',thankticketbook),
    path('failedPaymentticket',failedPaymentticket),
    path('ticketdetail',ticketdetail),
    path('forgetpassword',forgetpassword),
    path('forgetpage',forgetpage),
    path('otpchangepassword',otpchangepassword),
    path('clientlogout',clientlogout),
]

