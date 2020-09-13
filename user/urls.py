from django.conf.urls import url 
from user.views import UserView , UserTypeView, ActivityHistoryView
 
urlpatterns = [ 
    url(r'^api/user$', UserView.user_list),
    url(r'^api/user/(?P<pk>[0-9]+)$', UserView.user_detail),

    url(r'^api/userType$', UserTypeView.user_type_list),
    url(r'^api/userType/(?P<pk>[0-9]+)$', UserTypeView.user_type_detail),
    
    # url(r'^api/activityhistory$', ActivityHistoryView.activity_list),
    # url(r'^api/activityhistory/(?P<pk>[0-9]+)$', ActivityHistoryView.activity_detail),
    
]