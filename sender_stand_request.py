import requests
import configuration
import data


def post_new_order(order_body):  # запрос создания нового заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # url создания заказа
                         json=order_body,  # тело
                         headers=data.order_headers)  # заголовки

response = post_new_order(data.order_body);
