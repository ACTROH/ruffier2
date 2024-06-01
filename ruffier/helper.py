def check_int(str_num):
    try:
        return int(str_num)
    except:
        raise Exception('Значення не є числом')