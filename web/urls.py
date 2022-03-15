from django_request_mapping import UrlPattern

from web.views import MyView
from web.views_identify import IdentifyView
from web.views_market import MarketView
from web.views_review import ReviewView

urlpatterns = UrlPattern()
urlpatterns.register(MyView)
urlpatterns.register(MarketView)
urlpatterns.register(ReviewView)
urlpatterns.register(IdentifyView)
