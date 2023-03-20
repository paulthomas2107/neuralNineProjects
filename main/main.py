import logging

values = [10, 5, 6, 0, 9, 8, "Hello", 2]

for value in values:
    try:
        print(10 / int(value))
    except ZeroDivisionError as e:
        pass
    except ValueError as e:
        print("Me....")
        raise
    try:
        # print(int("Hello"))
        print(10 / int(value))
        raise AttributeError
    except (ValueError, ZeroDivisionError) as e:
        # print(str(e))
        # print("Value error")
        pass
    except AttributeError as e:
        print("Hello....")
        continue
    except Exception as e:
        logging.exception(e)
    else:
        print("No Exception")
    finally:
        print("I always get run...")
        pass
