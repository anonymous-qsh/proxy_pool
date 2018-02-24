from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.settings import PROXY_LIST
from proxy_pool.models import Proxy
from proxy_pool.serializers import ProxyListSerializer
from proxy_pool.tasks import get_proxy


class ProxyListView(generics.ListAPIView):
    queryset = Proxy.objects.all()
    serializer_class = ProxyListSerializer


@api_view(['GET'])
def manual_get_proxy(request):
    for proxy_method in PROXY_LIST:
        get_proxy(proxy_method).delay()
    # fixme: 暂时不考虑限制接口调用频率
    return Response("手动获取代理成功, 请不要频繁调用此接口")
