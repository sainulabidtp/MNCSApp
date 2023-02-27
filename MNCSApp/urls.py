
from django.urls import re_path, include
from . import views
urlpatterns = [re_path(r'^$', views.index, name='index'),
               re_path(r'^DBLogin/$', views.DBLogin,name='DBLogin'),
               re_path(r'^logout/$', views.logout,name='logout'),
               re_path(r'^Invetigator_logout/$', views.Invetigator_logout,name='logout'),
               re_path(r'^register/$', views.Register.as_view(), name='register'),
               re_path(r'^Dashboard/$', views.Dashboard,name='Dashboard'),
    re_path(r'^Investigator_Dashboard/$', views.Investigator_Dashboard, name='Investigator_Dashboard'),
    re_path(r'edit_profile/(\d+)$', views.edit_profile, name='edit_profile'),
    re_path(r'update_profile/(\d+)$', views.update_profile, name='update_profile'),
    re_path(r'edit_Investigator_profile/(\d+)$', views.edit_Investigator_profile, name='edit_Investigator_profile'),
    re_path(r'update_Investigator_profile/(\d+)$', views.update_Investigator_profile, name='update_Investigator_profile'),

    re_path(r'^User_Register/$', views.User_Register, name='User_Register'),
               re_path(r'^Reporter/$', views.Reporter, name='Reporter'),
               re_path(r'^user_complaints/(\d+)$', views.user_complaints,name='user_complaints'),
               re_path(r'^Investigator_Register/$', views.Investigator_Register, name='Investigator_Register'),
               re_path(r'^Investigator_Registration_Form/$', views.Investigator_Registration_Form, name='Investigator_Registration_Form'),
               re_path(r'^Investigator_Crime_Events/$', views.Investigator_view_cmplaints,name='Investigator_view_cmplaints'),
re_path(r'^take_action/(\d+)$', views.take_action,name='take_action'),
re_path(r'^Update_Status/(\d+)$', views.Update_Status, name='Update_Status'),
#re_path(r'^edit_stat/(\d+)$', views.edit_stat, name='edit_stat'),
#re_path(r'^edited_status_update/(\d+)$', views.edited_status_update, name='edited_status_update'),
re_path(r'edit_user_complaints/(\d+)$', views.edit_user_complaints, name='edit_user_complaints'),
re_path(r'^update_edit_user_complaints/(\d+)$', views.update_edit_user_complaints, name='update_edit_user_complaints'),#re_path(r'^$', views.index, name='index'),
re_path(r'^Admin_Login/$', views.Admin_Login, name='Admin_Login'),
re_path(r'^home/$', views.home, name='home'),
re_path(r'^ManageInvestigators/$', views.ManageInvestigators, name='ManageInvestigators'),
re_path(r'^ManageReports/$', views.ManageReports, name='ManageReports'),
re_path(r'^ManageReporters/$', views.ManageReporters, name='ManageReporters'),
re_path(r'^ManageReportersComplaints/(\d+)$', views.ManageReportersComplaints, name='ManageReportersComplaints'),
re_path(r'^DeleteFakeReport/(\d+)$', views.DeleteFakeReport, name='DeleteFakeReport'),
re_path(r'^Investigator_take_action/(\d+)$', views.Investigator_take_action, name='Investigator_take_action'),
re_path(r'^block_user/(\d+)$', views.block_user, name='block_user'),
re_path(r'^unblock_user/(\d+)$', views.unblock_user, name='unblock_user'),
re_path(r'^Allocate_Investigators/$', views.Allocate_Investigators, name='Allocate_Investigators'),
re_path(r'^Allot_Investigators/(\d+)$', views.Allot_Investigators, name='Allot_Investigators'),
re_path(r'^Send_Feedback/$', views.Send_Feedback, name='Send_Feedback'),
re_path(r'^View_Feedback/$', views.View_Feedback, name='View_Feedback'),
re_path(r'^send_OTP/$', views.send_OTP, name='send_OTP'),
re_path(r'^Email_Verification/$', views.Email_Verification.as_view(), name='Email_Verification'),
re_path(r'^Verifyotp/$', views.Verifyotp, name='Verifyotp'),
re_path(r'^investigator_send_OTP/$', views.investigator_send_OTP, name='investigator_send_OTP'),
re_path(r'^Investigator_Email_Verification/$', views.Investigator_Email_Verification.as_view(), name='Investigator_Email_Verification'),
re_path(r'^Verify_investigator_otp/$', views.Verify_investigator_otp, name='Verify_investigator_otp'),


]
