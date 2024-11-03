from adv_db import AdvDB
from threading import Thread


def handle_single_thread(dict_file_obj):
    """

    :param dict_file_obj: an object from the class AdvDb
    :type dict_file_obj: AdvDB
    :return:
    """
    key = input('Enter key: ')
    val = input('Enter value: ')
    print(dict_file_obj.set_val(key, val))
    print(dict_file_obj.get_val(key))
    print(dict_file_obj.delete_data(key))


def handle_writing_thread(dict_file_obj, key):
    """

    :param dict_file_obj: an object from the class AdvDb
    :type dict_file_obj: AdvDB
    :param key: the wanted key
    :return:
    """
    print(dict_file_obj.set_val(str(key), str(key)))


def handle_reading_thread(dict_file_obj, key):
    """

    :param dict_file_obj: an object from the class AdvDb
    :type dict_file_obj: AdvDB
    :param key: the wanted key
    :return:
    """
    print(dict_file_obj.get_val(str(key)))


def handle_deleting_thread(dict_file_obj, key):
    """

    :param dict_file_obj: an object from the class AdvDb
    :type dict_file_obj: AdvDB
    :param key: the wanted key
    :return:
    """
    print(dict_file_obj.delete_data(str(key)))


def main():
    dict_file_obj = AdvDB(True)
    thread = Thread(target=handle_single_thread, args=(dict_file_obj,))
    thread.start()
    thread.join()
    for i in range(20):
        t = Thread(target=handle_writing_thread, args=(dict_file_obj, i))
        t.start()

    for i in range(20):
        t = Thread(target=handle_reading_thread, args=(dict_file_obj, i))
        t.start()

    for i in range(20):
        t = Thread(target=handle_deleting_thread, args=(dict_file_obj, i))
        t.start()


if __name__ == '__main__':
    main()
