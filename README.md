# OpenAD Tools

This library contains a collection of modules for [OpenAD](https://github.com/acceleratedscience/open-ad-toolkit) plugin development.

<!-- When updating version, please also update below under ### Usage -->
Latest version: 0.0.1

<br>

### Usage

To use this library in your OpenAD plugins, please refer to our [Demo Plugin](https://github.com/acceleratedscience/openad-plugin-demo).

1. Add the library to your Poetry development dependencies in `pyproject.toml`, making sure to specify the latest version.

    <!-- Make sure to update version here -->
    [tool.poetry.dependencies]
    openad_tools = { git = "ssh://git@github.com/acceleratedscience/openad-tools", branch = "main", tag = "v0.0.1" }

2. In your code, import the tools as you need them.

    from openad_tools.output import output_table

<br>

## Available Tools

#### Output Modules

Modules related to the output of text or data in the terminal and Jupyter Notebook.

1.  `output.py`
    A simple way to output styled text and data to the termninal and Jupyter Notebook.
2.  `style_parser.py`
    Converts XML styling tags like `<bold>` or `<error>` to ansi characters for terminal output, and HTML for Jupyter Notebook output. Mostly consumed by `output.py`.
3.  `spinner.py`
    A spinner (based on [Halo](https://pypi.org/project/halo)) to provide instant user feedback during longer processes like API calls.
4.  `pretty_data.py`
    Methods to display lists and key-value lists in organized columns in the terminal.
5.  `output_msg.py`
    A library of templated output messages.
6.  `ascii_type.py`
    Display massive type in the CLI, using an ascii art alphabet.

<br>

#### Utility Modules

Modules providing utility

1.  `grammar_def.py`
    Pyparsing grammar definitions, used as ready-made building blocks to build new commands.
2.  `pyparsing.py`
    Functions to process some of the clauses provided in `grammar_def.py`.
3.  `helpers.py`
    A collection of helper functions for various purposes.
4.  `jupyter.py`
    Methods for working with dataframes in Jupyter Notebook.
5.  `locale.py`
    Support for language localisation.
6.  `edit_json.py`
    A library for quickly editing JSON files directly from the CLI.


    plugins
    general -> helpers