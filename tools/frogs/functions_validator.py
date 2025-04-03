def validate_input(trans, error_map, param_values, page_param_map):
    """
    Validates the user input, before execution.
    """
    functions = param_values["functions"]
    if "EC" not in functions and "KO" not in functions:
        error_map["functions"] = "EC or KO should be at least selected."