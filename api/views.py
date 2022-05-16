from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializer
from products.models import Product

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    Post view with DRF Serializer Validation.
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.data
        print(data)
        return Response(data)
    return Response(serializer.errors , status=status.HTTP_418_IM_A_TEAPOT)