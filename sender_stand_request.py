import configuration
import requests
import data

def get_headers():
    return data.headers

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=get_headers())

def get_order(query_params):
        return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                        params=query_params,
                        headers=get_headers())
