# Updated dropout layer logic to handle edge cases

def dropout_layer(input, rate):
    if rate < 0 or rate > 1:
        raise ValueError('Dropout rate must be between 0 and 1')
    # Apply dropout logic
    return output
