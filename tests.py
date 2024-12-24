from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_with_no_symbols(self):
        collector = BooksCollector()

        collector.add_new_book('')

        assert len(collector.books_genre) == 0

    def test_add_new_book_with_41_symbols(self):
        collector = BooksCollector()

        collector.add_new_book('01234567890123456789012345678901234567890')

        assert len(collector.books_genre) == 0

    ##################### TEST set_book_genre ####################

    def test_set_book_genre_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Dracula')
        collector.set_book_genre('Dracula', 'Ужасы')

        assert collector.books_genre['Dracula'] == 'Ужасы'

    def test_set_book_genre_with_no_exist_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Dracula')
        collector.set_book_genre('Dracula', 'Arthouse')

        assert collector.books_genre['Dracula'] == ''

    def test_set_book_genre_without_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Dracula')

        assert collector.books_genre['Dracula'] == ''

    ##################### TEST get_book_genre ####################

    def test_get_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Dracula')
        collector.add_new_book('Witcher')
        collector.set_book_genre('Dracula', 'Ужасы')
        collector.set_book_genre('Witcher', 'Фантастика')

        assert collector.get_book_genre('Dracula') == 'Ужасы'

    def test_get_book_genre_book_without_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Dracula')

        assert collector.get_book_genre('Dracula') == ''

    def test_get_book_genre_book_with_no_exist_book(self):
        collector = BooksCollector()

        assert collector.get_book_genre('Dracula') == None

    ##################### TEST get_books_with_specific_genre ####################

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Dracula')
        collector.set_book_genre('Dracula', 'Ужасы')

        assert collector.get_books_with_specific_genre('Ужасы') == ['Dracula']

    def test_get_books_with_specific_genre_with_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Dracula')
        collector.add_new_book('Call of Ctulhu')
        collector.set_book_genre('Call of Ctulhu', 'Ужасы')
        collector.set_book_genre('Dracula', 'Ужасы')

        assert collector.get_books_with_specific_genre('Ужасы') == ['Dracula', 'Call of Ctulhu']

    def test_get_books_with_specific_genre_with_two_books_with_different_genres(self):
        collector = BooksCollector()

        collector.add_new_book('Dracula')
        collector.add_new_book('Witcher')
        collector.set_book_genre('Dracula', 'Ужасы')
        collector.set_book_genre('Witcher', 'Фантастика')

        assert collector.get_books_with_specific_genre('Ужасы') == ['Dracula']

    def test_get_books_with_specific_genre_with_no_exist_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Dracula')
        collector.add_new_book('Witcher')
        collector.set_book_genre('Dracula', 'Ужасы')
        collector.set_book_genre('Witcher', 'Фантастика')

        assert collector.get_books_with_specific_genre('Arthouse') == []

    def test_get_books_with_specific_genre_without_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Dracula')
        collector.add_new_book('Witcher')
        collector.set_book_genre('Dracula', '')
        collector.set_book_genre('Witcher', 'Фантастика')

        assert collector.get_books_with_specific_genre('') == []

    def test_get_books_with_specific_genre_without_books(self):
        collector = BooksCollector()

        assert collector.get_books_with_specific_genre('Фантастика') == []

    ##################### TEST get_books_for_children ####################

    def test_get_books_for_children_with_book_in_not_genre_age_rating(self):
        collector = BooksCollector()

        collector.add_new_book('Witcher')
        collector.set_book_genre('Witcher', 'Фантастика')

        assert collector.get_books_for_children() == ['Witcher']

    def test_get_books_for_children_with_book_in_genre_age_rating_scary(self):
        collector = BooksCollector()

        collector.add_new_book('Dracula')
        collector.set_book_genre('Dracula', 'Ужасы')

        assert collector.get_books_for_children() == []

    def test_get_books_for_children_with_book_in_genre_age_rating_detectives(self):
        collector = BooksCollector()

        collector.add_new_book('Sherlock Holmes')
        collector.set_book_genre('Sherlock Holmes', 'Детективы')

        assert collector.get_books_for_children() == []

    def test_get_books_for_children_with_book_without_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Sherlock Holmes')

        assert collector.get_books_for_children() == []

    ##################### TEST favorites ####################

    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Sherlock Holmes')
        collector.add_book_in_favorites('Sherlock Holmes')

        assert collector.favorites == ['Sherlock Holmes']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Sherlock Holmes')
        collector.add_book_in_favorites('Sherlock Holmes')
        collector.delete_book_from_favorites('Sherlock Holmes')

        assert collector.favorites == []
