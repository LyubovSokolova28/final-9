import configuration
import requests
import data

# Запрос на создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)
#responce = post_new_order(data.order_body)
#print(responce.status_code)
#print(responce.json())

def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params=track)

