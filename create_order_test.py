#Самойлова Надежда, 5 когорта - дипломный проект. Инженер по тестированию плюс
import sender_stand_request
import data
import requests
import configuration


def get_new_order_track(order_body): #Получение трекера заказа
    order_response = sender_stand_request.post_new_order(data.order_body) #создание заказа с данными из data
    order_track = data.track_number.copy() #копирование примера трекера заказа из data
    order_track["t"] = order_response.json()["track"] # замена значения трекера в data
    return order_track #возвращение значения трекера


def test_get_order_by_track():  # Функция для получения заказа по треку
    new_track_number = get_new_order_track(data.order_body) #получение трекера нового заказа
    response = sender_stand_request.order_info(new_track_number) #замена значения трекера заказа на новый в функции получения заказа по номеру
    assert response.status_code == 200 #подтверждение того, что код ответа на запрос заказа по трекеру 200







#response = test_get_order_by_track()