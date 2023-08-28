from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views
from .forms import LoginForm , MyPasswordChangeForm


admin.site.site_header = "Welcome to Eren Yeager's Admin panel"
admin.site.site_title = "Admin panel of shopify"
admin.site.index_title = "Welcome to this portal"
urlpatterns = [
#    path('', views.home),
    path('',views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/',views.show_cart,name="showcart"),
    path('pluscart/',views.plus_cart),
    path('removecart/',views.remove_cart),
    path('minuscart/',views.minus_cart),
    path('buy/', views.buy_now, name='buy-now'),
#    path('profile/', views.profile, name='profile'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
#    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm),name='passwordchange'),
#    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('registration/', views.CustomerRegistrationView.as_view() , name='customerregistration'),

    # Extra urls
    path('searchpage',views.searchpage,name='searchpage'),
    path('searchpage/<slug:data>', views.searchpage, name='searchpage'),
    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),

   # path('pricebarg/', views.Pricebarg, name='pricebarg'),
    path('pricebarg/<int:prod>', views.Pricebarg, name='pricebarg'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:post_slug>', views.blogdetails , name='blogdetails'),
    path('subscription', views.subscription , name='subscription'),
    path('contact', views.contact , name='contact'),
  #  path('blog/<int:pk>', views.blogdetails , name='blogdetails')

   # path('pricebarg/', views.Pricebarg.as_view(), name='pricebarg'),
   # path('pricebarg/<int:data>', views.Pricebarg.as_view(), name='pricebarg'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# path('pricebarg/<int:prod>', views.Pricebarg, name='pricebarg'), --- working




