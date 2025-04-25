import unittest
from unittest.mock import patch, MagicMock
from lista_youtube.list import listar_subscript, get_youtube_client

class TestYoutubeAPI(unittest.TestCase):
    @patch('lista_youtube.list.get_youtube_client')
    def test_listar_subscript(self,mock_get_client):
        mock_response = {
            'items': [
                {
                    'snippet':{
                        'title': 'Canal exemplo',
                        'resourceId': {'channelId': '123456'}
                    }
                }
            ]
        }

        mock_youtube = MagicMock()
        mock_list = MagicMock()
        mock_list.execute.return_value = mock_response
        mock_youtube.subscriptions.return_value.list.return_value = mock_list
        mock_get_client.return_value = mock_youtube       


        listar_subscript()

        mock_youtube.subscriptions.return_value.list.assert_called_once_with(
                    part='snippet',
                    channelId='UC__dSYOfZ8QnGLiYes82D_A',
                    maxResults=20,
                    order='relevance'
                )


if __name__ == '__main__':
    unittest.main()