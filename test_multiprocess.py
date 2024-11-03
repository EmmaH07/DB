from adv_db import AdvDB
import multiprocessing


def handle_single_process(dict_file_obj):
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


def handle_writing_process(dict_file_obj, key):
    """

    :param dict_file_obj: an object from the class AdvDb
    :type dict_file_obj: AdvDB
    :param key: the wanted key
    :return:
    """
    print(dict_file_obj.set_val(str(key), str(key)))


def handle_reading_process(dict_file_obj, key):
    """

    :param dict_file_obj: an object from the class AdvDb
    :type dict_file_obj: AdvDB
    :param key: the wanted key
    :return:
    """
    print(dict_file_obj.get_val(str(key)))


def handle_deleting_process(dict_file_obj, key):
    """

    :param dict_file_obj: an object from the class AdvDb
    :type dict_file_obj: AdvDB
    :param key: the wanted key
    :return:
    """
    print(dict_file_obj.delete_data(str(key)))


def main():
    dict_file_obj = AdvDB(False)
    proc = multiprocessing.Process(target=handle_single_process(dict_file_obj))
    proc.start()
    proc.join()
    for i in range(40):
        p1 = multiprocessing.Process(target=handle_writing_process(dict_file_obj, i))
        p2 = multiprocessing.Process(target=handle_reading_process(dict_file_obj, i))
        p3 = multiprocessing.Process(target=handle_deleting_process(dict_file_obj, i))
        p1.start()
        p2.start()
        p3.start()


if __name__ == '__main__':
    main()
