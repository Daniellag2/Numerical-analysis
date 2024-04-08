def lagrange_interpolation(x_data, y_data, x):
    """
    Lagrange Interpolation

    Parameters:
    x_data (list): List of x-values for data points.
    y_data (list): List of y-values for data points.
    x (float): The x-value where you want to evaluate the interpolated polynomial.

    Returns:
    float: The interpolated y-value at the given x.
    """
    n = len(x_data)
    result = 0.0

    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term

    return result


if __name__ == '__main__':
    x_data = [1.2, 1.3, 1.4, 1.5, 1.6]
    y_data = [-1.2, -2.3, -0.5, 0.89, 1.37]
    x_interpolate = 1.55  # The x-value where you want to interpolate
    y_interpolate = lagrange_interpolation(x_data, y_data, x_interpolate)
    print("\nInterpolated value at x =", x_interpolate, "is y =", y_interpolate)
    x_interpolate = 1.35  # The x-value where you want to interpolate
    y_interpolate = lagrange_interpolation(x_data, y_data, x_interpolate)
    print("\nInterpolated value at x =", x_interpolate, "is y =", y_interpolate)



