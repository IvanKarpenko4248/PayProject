from django.shortcuts import render

from requests import Response

from .models import *
import stripe
from django.views.generic import View
from django.http.response import HttpResponse, JsonResponse

stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"


class GetStripeSessionIdView(View):

    def get(self, *args, **kwargs):
        item = Item.objects.filter(id=kwargs.get('item_id')).first()
        if not item:
            return HttpResponse('Item not found')

        session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': Item.name,
                            'description': Item.description
                        },
                        'unit_amount': 2000,
                    },
                    'quantity': 1,
                }],
            mode='payment',
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',
        )
        return JsonResponse(session.id, safe=False)
        # return {"sessionId": session.id}
        # return JsonResponse({'foo': 'bar'})


# def get_id_session(**kwargs):
#     item = Item.objects.filter(id=kwargs.get('item_id')).first()
#     if not item:
#         return HttpResponse('Item not found')
#
#     session = stripe.checkout.Session.create(
#         line_items=[
#             {
#                 'price_data': {
#                     'currency': 'usd',
#                     'product_data': {
#                         'name': Item.name,
#                         'description': Item.description
#                     },
#                     'unit_amount': 2000,
#                 },
#                 'quantity': 1,
#             }],
#         mode='payment',
#         success_url='https://example.com/success',
#         cancel_url='https://example.com/cancel',
#     )
#     return session.id


class GetItemView(View):

    def get(self, *args, **kwargs):
        item = Item.objects.filter(id=kwargs.get('item_id')).first()
        if not item:
            return HttpResponse('Item not found')
        context = {"item": item}
        return render(self.request, 'PaymentApp1/item.html', context=context)
