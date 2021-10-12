import pytest
from time import sleep
from pathlib import Path


@pytest.mark.parametrize(
    'test_input',
    [
        'pic_test.jpg',
        'text_test.txt'
    ]
)
def test_post_task(test_input, test_client, post_endpoint, path_prefix):
    """asserting task creation response is ok and returns task_id"""
    files = {'uploaded_file': open(Path(f'{path_prefix}{test_input}'), 'rb')}
    response = test_client.post(post_endpoint, files=files)
    len_task_id = len(response.json()['task_id'])
    assert response.status_code == 200
    assert len_task_id > 0


@pytest.mark.parametrize(
    'test_input',
    [
        'pic_test.jpg',
        'text_test.txt'
    ]
)
def test_hash_response(test_input, test_client, post_endpoint, path_prefix, get_endpoint_prefix):
    """assert that md5 hash is counted and returned on endpoint"""
    files = {'uploaded_file': open(Path(f'{path_prefix}{test_input}'), 'rb')}
    post_response = test_client.post(post_endpoint, files = files)
    task_id = post_response.json()['task_id']
    sleep(3)
    get_response = test_client.get(f'{get_endpoint_prefix}/{task_id}')
    len_result_hash = len(get_response.json()['result_hash'])
    assert get_response.status_code == 200
    assert len_result_hash > 0


@pytest.mark.parametrize(
    'test_input, correct_sum',
    [
        ('pic_test.jpg', '1e62648f6195beeb7fb1ac6a5852bf65'),
        ('text_test.txt', 'c30569b88d875c74cbbf9ae0c7861b5c')
    ]
)
def test_sum_correctness(test_input, correct_sum, test_client, post_endpoint, path_prefix, get_endpoint_prefix):
    """assert that md5 sum is counted correctly"""
    files = {'uploaded_file': open(Path(f'{path_prefix}{test_input}'), 'rb')}
    post_response = test_client.post(post_endpoint, files = files)
    task_id = post_response.json()['task_id']
    sleep(3)
    get_response = test_client.get(f'{get_endpoint_prefix}/{task_id}')
    result_hash = get_response.json()['result_hash']
    assert result_hash == correct_sum

