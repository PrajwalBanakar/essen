from django.contrib import admin
from django.urls import path
from school import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),

    path('adminclick', views.adminclick_view),
    path('studentclick', views.studentclick_view),


    path('adminsignup', views.admin_signup_view),
    path('studentsignup', views.student_signup_view,name='studentsignup'),
    path('adminlogin', LoginView.as_view(template_name='school/adminlogin.html')),
    path('studentlogin', LoginView.as_view(template_name='school/studentlogin.html')),


    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='school/index.html'),name='logout'),


    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),


    path('admin-student', views.admin_student_view,name='admin-student'),
    path('admin-add-student', views.admin_add_student_view,name='admin-add-student'),
    path('admin-view-student', views.admin_view_student_view,name='admin-view-student'),
    path('delete-student-from-school/<int:pk>', views.delete_student_from_school_view,name='delete-student-from-school'),
    path('delete-student/<int:pk>', views.delete_student_view,name='delete-student'),
    path('update-student/<int:pk>', views.update_student_view,name='update-student'),
    path('admin-approve-student', views.admin_approve_student_view,name='admin-approve-student'),
    path('approve-student/<int:pk>', views.approve_student_view,name='approve-student'),
    path('admin-view-student-donations', views.admin_view_student_donations_view,name='admin-view-student-fee'),



    path('admin-notice', views.admin_notice_view,name='admin-notice'),


    path('student-dashboard', views.student_dashboard_view,name='student-dashboard'),
    path('student-donation', views.student_donation_view,name='student-donation'),




    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
    
    path('register_event/', views.register_event, name='register_event'),
]
