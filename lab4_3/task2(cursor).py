def centimeters_to_inches(cm):
    """
    Converts centimeters to inches.
    Args:
        cm (float): The length in centimeters.
    Returns:
        float: The length in inches, rounded to 3 decimal places.
    """
    inches = cm / 2.54
    return round(inches, 3)

# Example usage:
result = centimeters_to_inches(10)
print(result)  # Output: 3.937
