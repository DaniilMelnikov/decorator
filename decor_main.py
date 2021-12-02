from datetime import datetime

def path_to_logs(path):
    def decorator_logger(old_function):
        def new_function(*args):
            return_func = old_function(*args)
            today = datetime.today()
            date_func = today.strftime('%Y-%m-%d')
            time_func = today.strftime('%H:%M:%S')
            name_func = old_function.__name__
            string = f'date: {date_func}, time: {time_func}, name function: {name_func}, arguments: {args}, return: {return_func}'
            with open(path, 'a', encoding='utf-8') as file:
                file.write(f'{string}\n')
            return return_func
        return  new_function
    return decorator_logger

@path_to_logs('data.txt')
def summator(a, b):
    return a + b

summator(7, 7)