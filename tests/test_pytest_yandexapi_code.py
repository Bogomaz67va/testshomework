import yandex_folder
import pytest


class TestYandex:
    expected = [("test", 201), ("test1", 201), ("test", 409), ("_123", 201)]

    @pytest.mark.parametrize("argument, expected_result", expected)
    def test_folder_status_code_argument(self, argument, expected_result):
        assert yandex_folder.folder(argument) == expected_result, 'Error'
