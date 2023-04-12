# Define decorator function

def decorator_fn(func):
    
    # Wrapper function
    def print_fn():
        print("Before function execution")

        # Calling actual function now inside wrapper fn
        func()

        print("After function execution")
    return print_fn


# Define the function to be called inside wrapper
@decorator_fn
def execution_fn():
    print("The function is executed")

# Call the wrapped function
execution_fn()