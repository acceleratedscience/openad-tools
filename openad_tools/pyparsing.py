def parse_using_clause(params: list, allowed: list):
    """
    Parse the content of the USING clause from a list of tuples into a dictionary.

    - Input: [["foo", 123], ["bar", "baz"]]
    - Output: {"foo": 123, "bar": "baz"}

    Parameters
    ----------
    params : list
        List of tuples
    allowed : list
        List of allowed keys
    """

    from openad_tools.output import output_warning

    params_dict = {}
    invalid_keys = []

    if not params:
        return params_dict

    for [key, val] in params:
        if key in allowed:
            params_dict[key] = val
        else:
            invalid_keys.append(key)

    if invalid_keys:
        output_warning(
            "Warning: Ignored invalid USING parameters:\n- <error>"
            + ("</error>\n- <error>".join(invalid_keys))
            + "</error>",
            return_val=False,
            pad=1,
        )

    return params_dict
