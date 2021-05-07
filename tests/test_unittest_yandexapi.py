import unittest
import yandex_folder


class TestYandexApi(unittest.TestCase):

    def test_folder_status_code_201(self):
        self.assertEqual(yandex_folder.folder('test'), 201)

    def test_folder_status_code_409(self):
        self.assertEqual(yandex_folder.folder('test'), 409)