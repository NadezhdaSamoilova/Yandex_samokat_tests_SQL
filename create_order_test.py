#Самойлова Надежда, 5 когорта - дипломный проект. Инженер по тестированию плюс
import sender_stand_request
import data
import requests
import configuration


def get_new_order_track():  # Функция для сохранения трека созданного заказа
    # задается значение order_track из ответа на запрос создания заказа
    order_track = sender_stand_request.post_new_order(data.order_body).json()["track"]
    #возвращение полученного значения
    return order_track
#вывод ответа запроса
response = get_new_order_track()
#вывдение на экран ответа запроса
print(response)


def test_get_order_by_track():  # Функция для получения заказа по треку
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_BY_TRACK_PATH + '?t=' + str(get_new_order_track()))  # url получения заказа по треку /
    # /с результатом запроса на получение номера
#выведение ответа запроса
response = test_get_order_by_track()
#вывдение на экран ответа запроса
print(response.status_code)

#подтверждение того, что код ответа на запрос заказа по трекеру 200
assert test_get_order_by_track().status_code == 200

