def oxford_comma(arr):
    result = ""

    # Check for empty array
    if len(arr) == 0:
        return result

    # Handle single-element case
    if len(arr) == 1:
        return arr[0]

    # Iterate through elements, adding commas and "and"
    for i in range(len(arr) - 1):
        result += arr[i] + ", "

    # Add the last element with "and"
    result += "and " + arr[-1]

    return result



    
