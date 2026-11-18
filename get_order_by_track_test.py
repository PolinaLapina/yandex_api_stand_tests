import sender_stand_request
import data

def assert_order_created(response):
    assert response.status_code == 201
    assert "track" in response.json()

def get_new_order_track():
    response = sender_stand_request.post_new_order(data.order_body)
    assert_order_created(response)
    return response.json()['track']

def assert_order_get(response):
    assert response.status_code == 200
    assert "order" in response.json()

def test_api_samokat():
    query_params = {
        "t" : get_new_order_track()
    }

    response = sender_stand_request.get_order(query_params)
    assert_order_get(response)


