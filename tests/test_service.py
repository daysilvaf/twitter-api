from unittest import mock

from src.services import _get_trends

def test_get_trends_with_success():
    #Arrange
    mock_api = mock.Mock()
    mock_api.trends_place.return_value = [
        {
            "trends": [
                "name": "#gunsnroses", "url": "https://twitter.com/search?q=%23gunsnroses"},
                {"name": "thenbhd", "url": "https://twitter.com/search?q=%23thenbhd"},
    ]
    }
    ]

        #Act
        trends = _get_trends(woe_id=1000, api=mock_api)

        #Assert
        assert trends == [
            {"name": "#gunsnroses", "url": "https://twitter.com/search?q=%23gunsnroses"},
            {"name": "thenbhd", "url": "https://twitter.com/search?q=%23thenbhd"},
        ]

        def test_get_trends_without_return_with_success():
            #Arrange
            mock_api = mock.Mock()
            mock_api.trends_place.return_value = [{"trends": []}]


            #Act
            trends = _get_trends(woe_id=1000, api=mock_api)

            #Assert
            assert trends == []
