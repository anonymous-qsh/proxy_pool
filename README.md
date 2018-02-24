# proxy_pool

## ENV Python 3.6

## Installation And Start

 1. git clone https://github.com/anonymous-qsh/proxy_pool.git
 2.  pip install -r requirements.txt
 3.  ./manage.py runserver
 4.  ./redis-server
 5.  celery -A backend worker -l info -c 10
 6.  celery -A backend beat -l info

## Using

 - Get : localhost:8000/proxy/offset=0&limit=10 (to get 10 ips)
 - Get : localhost:8000/manual_start/ (to get proxy)
 -  This app get free proxy by xicidaili_proxy, 66ip_proxy, data5u_proxy, guobanjia_proxy and so on, you also could add your own proxy ip.
 -  Costom your own proxy address.

``` Python
# You could write a get_proxy function to get your own proxy list
def get_any_proxy():
    proxy_list = [] # your own proxy list, you could get free proxy or get by some api.
    for proxy in proxy_list:
        yield proxy
# Then add this function to settings.py PROXY_LIST.
# This app could auto get proxy.
```