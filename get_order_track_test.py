import sender_stand_request
import data
# Соколова Любовь, когорта № 9 — Финальный проект. Инженер по тестированию плюс
def test_get_new_order_by_track():
    # Переменная с функцией создания заказа
    new_order = sender_stand_request.post_new_order(data.order_body)
    # Переменная со значением словарь из ответа при создании нового набора
    current_track = new_order.json()
    # Переменная со значением ключа из ответа создания нового набора
    current_track_number = current_track['track']
    track = {'t': current_track_number}
    # Переменная с функцией получения заказа по треку
    order_responce = sender_stand_request.get_order(track)
    assert order_responce.status_code == 200

