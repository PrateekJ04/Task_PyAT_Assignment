
from configparser import ConfigParser


def config_reader(category,key):
    reader=ConfigParser()
    #Replace your config.ini file path with below one
    reader.read(r"C:\Users\HP\PycharmProjects\Task_PyAT_Assignment\Config\config.ini")

    return reader.get(category,key)