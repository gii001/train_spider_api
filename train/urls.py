
from django.conf.urls import url
import views
urlpatterns = [
    url(r'train/(.+)/(.+)/',views.train,name='train'),
    url(r'station/(\w{3})/(\w{3})/(.+)/',views.station,name='station')
]