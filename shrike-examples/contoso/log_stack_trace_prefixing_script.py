# To-Do: import relevant libraries
from shrike.compliant_logging.exceptions import prefix_stack_trace 



def try_a_error():
    print(1 / 0)

# To-Do: decorator with custom prefix
@prefix_stack_trace(prefix="MyCustomPrefix")
def custom_prefix():
    print(1 / 0)


# To-Do: decorator with custom message
@prefix_stack_trace(scrub_message="Private data was divided by zero")
def custom_message():
    print(1 / 0)


# To-Do: decorator with exception message displayed
@prefix_stack_trace(keep_message=True)
def keep_exception_message():
    print(1 / 0)


# To-Do: decorator with allow-list for exceptions
@prefix_stack_trace(keep_message=False, allow_list=["ZeroDivision"])
def keep_allowed_exceptions():
    print(1 / 0)


# To-Do: decorator with timestamp displayed in logs
@prefix_stack_trace(add_timestamp=True)
def add_timestamp():
    print(1 / 0)


def main():
    try:
        print("try -- no decorator")
        try_a_error()
    except:
        print("expect -- no decorator")
        pass
    try:
        custom_prefix()
    except:
        pass
    try:
        custom_message()
    except:
        pass
    try:
        keep_exception_message()
    except:
        pass
    try:
        keep_allowed_exceptions()
    except:
        pass
    try:
        add_timestamp()
    except:
        pass


if __name__ == "__main__":
    main()
