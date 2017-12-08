# # from unittest import mock 
# import pytest
# from mock import Mock

# from iterable_wrapper import IterableAPI
# # Set API_KEY for my instance

# # import iterable_wrapper


# from https://auth0.com/blog/mocking-api-calls-in-python/
# import unittest
# from iterable_wrapper import IterableAPI
# from unittest.mock import patch

# class TestIterableClient(unittest.TestCase):
#     """Tests for `iterable_wrapper.py`."""    
#     def setUp(self):
#     	self.ic = IterableAPI(api_key='foo')

#     def test_init(self):
#     	self.assertEqual(self.ic.api_key, 'foo')
#     	self.assertIsNotNone(self.ic.base_uri)

# if __name__ == '__main__':
#     unittest.main()




# Youtube video: https://www.youtube.com/watch?v=GYkGguhdqw0
# import unittest
# import requests
# from unittest.mock import Mock, patch
# from iterable_wrapper import IterableAPI

# class TestCalls(unittest.TestCase):

# 	def setUp(self):
# 		self.ic = IterableAPI(api_key="94c3333a8e224b32b93a40788d1927cc")

# 	def test_list_channels(self):
# 		with patch.object(requests, 'get') as get_mock:
# 			mock_response = Mock()

# 			get_mock.return_value = mock_response

# 			mock_response.status_code = 200
# 			assert self.ic.list_channels() == 200

# 	def test_list_campaign_info(self):
# 		with patch.object(requests, 'get') as get_mock:
# 			mock_response = Mock()

# 			get_mock.return_value = mock_response

# 			mock_response.status_code = 200
# 			assert self.ic.list_campaign_info() == 200


# 	def test_get_events(self):
# 		with patch.object(requests, 'get') as get_mock:
# 			mock_response = Mock()

# 			get_mock.return_value = mock_response

# 			mock_response.status_code = 200
# 			user = "carter@iterable.com"

# 			assert self.ic.get_events(email=user) == 200

# 	def test_create_list(self):
# 		with patch.object(requests, 'post') as get_mock:
# 			mock_response = Mock()

# 			get_mock.return_value = mock_response

# 			mock_response.status_code = 200
# 			the_list = "unittest"

# 			assert self.ic.create_list(list_name=the_list) == 200






# Based on Jeps tests
# import pytest

# from iterable_wrapper import IterableAPI


# @pytest.fixture
# def ic():
# 	return IterableAPI(api_key='foo')


# def test_init_values(ic):

# 	assert isinstance(ic, object)
# 	assert ic.base_uri == 'https://api.iterable.com'
# 	assert ic.api_key == 'foo'

# 	ic = IterableAPI(api_key='bar')
# 	assert ic.api_key == 'bar'

# @patch('IterableAPI.requests')
# def test_api_call(m_request, ic):
# 	rv= {
# 		  "channels": [
# 		    {
# 		      "id": 9721,
# 		      "name": "Push Marketing Channel",
# 		      "channelType": "Marketing",
# 		      "messageMedium": "Push"
# 		    },
# 		    {
# 		      "id": 9720,
# 		      "name": "Transactional Channel",
# 		      "channelType": "Transactional",
# 		      "messageMedium": "Email"
# 		    },
# 		    {
# 		      "id": 9719,
# 		      "name": "Marketing Channel",
# 		      "channelType": "Marketing",
# 		      "messageMedium": "Email"
# 		    }
# 		  ]
# 		}
# 	get_request_Mock = Mock(return_value=rv)

# 	request_mock = Mock(get=get_request_Mock)

# 	m_request.return_value = request_mock


# https://medium.com/python-pandemonium/python-mocking-you-are-a-tricksy-beast-6c4a1f8d19b2

from unittest import mock

import iterable_wrapper

@mock.patch("iterable_wrapper.IterableApi")
def mock_simple_class(mock_class):
	print(mock_class)


mock_simple_class()

	