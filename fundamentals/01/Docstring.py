# reStructuredText (reST)
# 在许多老牌和大型项目中，尤其是那些与Python官方工具链高度集成的项目中，reST仍然占据主导地位。
# 例如，Django、Flask、requests等广泛使用reST格式。
def example_function(param1, param2):
    """
    Example function.

    :param param1: The first parameter.
    :type param1: int
    :param param2: The second parameter.
    :type param2: str
    :returns: The result of the function.
    :rtype: bool
    """
    return True


# Google Docstring Format
# 越来越多的现代项目和新兴项目开始采用Google风格的Docstring格式。
# 例如，TensorFlow、Apache Airflow等项目使用Google格式。
def example_function2(param1, param2):
    """
    Example function.
    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The result of the function.
    """
    return True
