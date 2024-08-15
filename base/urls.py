from django.urls import path
from . import views
from .views import generateInvoicePDF
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordResetForm, CustomSetPasswordForm

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    # url for forgot password
    # 1 - Submit email form                     //PasswordResetView.as view()
    # 2 - Email sent success message            //PasswordResetDoneView.as view()
    # 3 - Link to password Rest form in email   //PasswordResetConfirmView.as view()
    # 4 - Password successfully changed message //PasswordResetCompleteView.as_view()
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(
             template_name="base/main/reset_pass/password_reset.html",
             form_class=CustomPasswordResetForm), 
         name="reset_password"),

    path('reset_password_sent', 
         auth_views.PasswordResetDoneView.as_view(template_name="base/main/reset_pass/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name="base/main/reset_pass/password_reset_form.html",
             form_class=CustomSetPasswordForm),
         name="password_reset_confirm"),

    path('reset_password_complete', 
         auth_views.PasswordResetCompleteView.as_view(template_name="base/main/reset_pass/password_reset_done.html"),
         name="password_reset_complete"),

    #end for got button

    #url for botchat
    path('getResponse', views.getResponse, name='getResponse'),
    #end botchat

    path('', views.home, name="home"),
    path('product/<str:pk>/', views.productPage, name='product'),

    path ('cart', views.cart, name="cart"),
    path ('cart-add/', views.cartAdd, name="cart_add"),
    path ('cart-delete/', views.cartDelete, name="cart_delete"),
    path ('cart-update/', views.cartUpdate, name="cart_update"),

    path('checkout/', views.checkout, name="checkout"),
    path('create-order', views.createOrder, name="createOrder"),

    path('delete-review/<str:pk>', views.deleteReview, name="delete-review"),

    path('profile/<str:pk>', views.userProfile, name="user-profile"),
    path('update-password', views.updatePassword, name="updatePassword"),
    path('order-detail/<str:pk>', views.orderDetailMain, name="orderDetailMain"),


    # path for admin
    path('super',views.adminHome,name="adminHome"), 
    path('super/login/',views.adminLogin,name="admin_login"),
    path('super/logout/',views.adminLogout,name="admin_logout"),

    path('super/product/', views.productAdmin, name="productAdmin"),
    path('super/add-product/', views.addProduct, name="addProduct"),
    path('super/update-product/<str:pk>', views.updateProduct, name="updateProduct"),
    path('super/delete-product/<str:pk>', views.deleteProduct, name="deleteProduct"),

    path('super/suppiler/', views.suppilerAdmin, name="suppilerAdmin"),
    path('super/add-suppiler/', views.addSuppiler, name="addSuppiler"),
    path('super/update-suppiler/<str:pk>', views.updateSuppiler, name="updateSuppiler"),
    path('super/delete-suppiler/<str:pk>', views.deleteSuppiler, name="deleteSuppiler"),

    path('super/category/', views.categoryAdmin, name="categoryAdmin"),
    path('super/add-category/', views.addCategory, name="addCategory"),
    path('super/update-category/<str:pk>', views.updateCategory, name="updateCategory"),
    path('super/delete-category/<str:pk>', views.deleteCategory, name="deleteCategory"),

    path('super/customer/', views.customerAdmin, name="customerAdmin"),
    path('super/update-customer/<str:pk>', views.updateCustomer, name="updateCustomer"),
    path('super/delete-customer/<str:pk>', views.deleteCustomer, name="deleteCustomer"),

    path('super/invoice/', views.invoiceAdmin, name="invoiceAdmin"),
    path('super/invoice/<int:pk>/', views.invoiceDetail, name='invoiceDetail'),
    path('super/add-invoice/', views.addInvoice, name='addInvoice'),
    path('super/add-invoice-item/<str:suppiler>/<str:invoice_id>/', views.addInvoiceItem, name='addInvoiceItem'),
    path('super/invoice/change-status/<str:pk>', views.updateInvoiceStatus, name="updateInvoiceStatus"),
    path('super/delete-invoice/<str:pk>', views.deleteInvoice, name="deleteInvoice"),
    path('super/invoice/generate-pdf/<str:pk>', views.generateInvoicePDF.as_view(), name="generateInvoicePDF"),

    path('super/order/', views.orderAdmin, name="orderAdmin"),
    path('super/order/<int:pk>/', views.orderDetail, name='orderDetail'),
    path('super/order/change-status/<str:pk>', views.updateOrderStatus, name="updateOrderStatus"),
    path('super/order/generate-pdf/<str:pk>', views.generateOrderPDF.as_view(), name="generateOrderPDF"),

    path('super/staff/', views.staffAdmin, name="staffAdmin"),
    path('super/add-staff/', views.addStaff, name="addStaff"),
    path('super/update-staff/<str:pk>', views.updateStaff, name="updateStaff"),
    path('super/update-staff-password/<str:pk>', views.updateStaffPassword, name="updateStaffPassword"),
    path('super/delete-staff/<str:pk>', views.deleteStaff, name="deleteStaff"),



    path('test', views.test, name="test")

]
