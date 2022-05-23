from django.urls import path
from .views import GetStripeSessionIdView, GetItemView

urlpatterns = [
    path('buy/<int:item_id>', GetStripeSessionIdView.as_view()),
    path('item/<int:item_id>', GetItemView.as_view())
]
