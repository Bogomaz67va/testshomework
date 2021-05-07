import builtins
from unittest import mock
import pytest
import bookkeeping


class TestBookkeeping:

    @pytest.mark.parametrize("document_number", [
        "2207 876234",
        "11-2",
        "10006",
    ])
    def test_check_document_existance(self, document_number):
        assert bookkeeping.check_document_existance(document_number), "error no documents number"

    @pytest.mark.parametrize("number_document, expected_result", [
        ("11-2", "Геннадий Покемонов"),
        ("2207 876234", "Василий Гупкин"),
        ("10006", "Аристарх Павлов"),
    ])
    def test_get_document_owner_name(self, number_document, expected_result):
        with mock.patch.object(builtins, 'input', lambda _: number_document):
            assert bookkeeping.get_doc_owner_name() == expected_result, "error no name"

    def test_get_all_document_owners_names(self):
        assert bookkeeping.get_all_doc_owners_names()

    @pytest.mark.skip
    def test_error_all_document_owners_names_list(self):
        with pytest.raises(NameError):
            bookkeeping.get_all_doc_owners_names()

    @pytest.mark.parametrize("number_shelf", ["4", "5", "6"])
    def test_add_new_shelf(self, number_shelf):
        assert bookkeeping.add_new_shelf(number_shelf) == (number_shelf, True)

    @pytest.mark.parametrize("number_document, expected_result", [
        ("11-2", "1"),
        ("2207 876234", "1"),
        ("10006", "2"),
    ])
    def test_get_doc_shelf(self, number_document, expected_result):
        with mock.patch.object(builtins, 'input', lambda _: number_document):
            assert bookkeeping.get_doc_shelf() == expected_result

    @pytest.mark.parametrize(
        "new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number, expected_result",
        [("1", "1", "1", "1", "1")])
    def test_add_new_doc(
            self, new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number, expected_result):
        assert bookkeeping.add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name,
                                       new_doc_shelf_number) == expected_result, "error"

    @pytest.mark.parametrize("number_document", ["10006", "11-2", "2207 876234"])
    def test_delete_document(self, number_document):
        with mock.patch.object(builtins, 'input', lambda _: number_document):
            assert bookkeeping.delete_doc(), "error no such document exists"
