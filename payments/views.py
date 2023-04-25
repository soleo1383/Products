import uuid

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticated

from .models import Gateway, Payment
from .serializers import GatewaySerializer, PaymentSerializer

class GatewayView(APIView):
    def get(self, request):
        gateway = Gateway.objects.filter(is_enable=True)
        serializer = GatewaySerializer(payments, many=True)
        return Response(serializer.data)

class PaymentView(APIView):
    permission_class = [IsAuthenticated]

    def get(self, request):
        gateway_id = request.query_params.get('gateway')
        package_id = request.query_params.get('package')

        try:
            package = Package.objects.get(pk=package_id, is_enable=True)
            gateway = Gateway.objects.get(pk=gateway_id, is_enable=True)
        except (Package.DoesNotExist, Gateway.DoesNotExist):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        payment = Payment.objects.create(
            user=request.user,
            package=package,
            gateway=gateway,
            price=package.price,
            phone_number=request.user.phone_number,
            token=str(uuid.uuid4())
        )

        # return redirect()
        return Response({'token': payment.token, 'callback_url': 'https://my-site.com/payments/pay/'})

    def post(self, request):
        token = request.data.get('token')
        st = request.data.get('status')

        try:
            payment = Payment.objects.get(token=token)
        except Payment.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if st != 10:
            payment.status = Payment.STATUS_CANCELED
            payment.save()
            # render(request, 'payment-result.html', context={'status': Payment})
            return Response({'detail': 'Payment canceled by user.'},
                            status=status.HTTP_400_BAD_REQUEST)
        r = request.port('bank_verify_url', data={})
        if r.status_code // 100 != 2:
            payment.status = Payment.STATUS_ERROR
            payment.save()
            # render(request, 'payment-result.html', context={'status': Payment})
            return Response({'detail': 'Payment ver'})
