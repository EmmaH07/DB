from dict_db import DictDB
import os
import pickle

FILE_PATH = 'db.pkl'


class FileDB(DictDB):
    def __init__(self, dic={}):
        super().__init__(dic)
        if os.path.exists(FILE_PATH):
            self.__file__ = open(FILE_PATH, 'wb')
        else:
            self.__file__ = open(FILE_PATH, 'x')
        try:
            pickle.dump(self.__dic__, self.__file__)
        except Exception as err:
            print('Got an exception in FileDB: ' + str(err))

    def set_val(self, key, new_val):
        """
        sets a new value for the key. creates a new key-value pair if the key doesn't exist.
        dumps the updated dictionary to a file.
        :param key: the wanted key
        :param new_val: the new value
        :return: True if it worked, False if it didn't.
        """
        try:
            file_size = os.stat(FILE_PATH).st_size
            if file_size > 0:
                self.__dic__ = pickle.load(self.__file__)
            b = super().set_val(key, new_val)
            pickle.dump(self.__dic__, self.__file__)
            return b
        except Exception as err:
            print(err)
            return False

    def delete_data(self, key):
        """
        deletes the key-value pair from the dictionary. dumps the updated dictionary to a file.
        :param key: the wanted key
        :return: the value of said key. None if the key doesn't exist.
        """
        try:
            file_size = os.stat(FILE_PATH).st_size
            if file_size > 0:
                self.__dic__ = pickle.load(self.__file__)
            val = super().delete_data(key)
            pickle.dump(self.__dic__, self.__file__)
            return val
        except Exception as err:
            print(err)
            return None

    def get_val(self, key):
        """

        :param key: the wanted key
        :return: the value of said key. None if the key doesn't exist.
        """
        try:
            file_size = os.stat(FILE_PATH).st_size
            if file_size > 0:
                self.__dic__ = pickle.load(self.__file__)
            val = super().get_val(key)
            pickle.dump(self.__dic__, self.__file__)
            return val
        except Exception as err:
            print(err)
            return None
