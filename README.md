# OpenAD Tools

A common library of modules for [OpenAD](https://github.com/acceleratedscience/open-ad-toolkit) plugin development.

<!-- When updating version, please also update below under ### Usage -->
Latest version: 0.0.1

<br>

## Usage

To use this library in your OpenAD plugins, please refer to our [Demo Plugin](https://github.com/acceleratedscience/openad-plugin-demo).

1.  Add the library to your Poetry development dependencies in `pyproject.toml`, making sure to specify the latest version.
    <!-- Make sure to update version here -->

        [tool.poetry.dependencies]
        openad_tools = { git = "ssh://git@github.com/acceleratedscience/openad-tools", branch = "main", tag = "v0.0.1" }

1.  In your code, import the tools as you need them.

        from openad_tools.output import output_table

<br>

## Available Modules

#### Output Modules

*Modules related to the output of text or data in the terminal and Jupyter Notebook.*

1.  `output.py`<br>
    A simple way to output styled text and data to the termninal and Jupyter Notebook.

2.  `style_parser.py`<br>
    Converts XML styling tags like `<bold>` or `<error>` to ansi characters for terminal output, and HTML for Jupyter Notebook output. Mostly consumed by `output.py`.

3.  `spinner.py`<br>
    A spinner (based on [Halo](https://pypi.org/project/halo)) to provide instant user feedback during longer processes like API calls.

4.  `pretty_data.py`<br>
    Methods to display lists and key-value lists in organized columns in the terminal.

5.  `output_msg.py`<br>
    A library of templated output messages.

6.  `ascii_type.py`<br>
    Display massive type in the CLI, using an ascii art alphabet.

<br>

#### Utility Modules

*A variety of practical tools.*

1.  `grammar_def.py`<br>
    Pyparsing grammar definitions, used as ready-made building blocks to build new commands.

2.  `pyparsing.py`<br>
    Functions to process some of the clauses provided in `grammar_def.py`.

3.  `helpers.py`<br>
    A collection of helper functions for various purposes.

4.  `jupyter.py`<br>
    Methods for working with dataframes in Jupyter Notebook.

5.  `locale.py`<br>
    Support for language localisation.

6.  `edit_json.py`<br>
    A library for quickly editing JSON files directly from the CLI.


<!--

For maintainers
---------------

Whenever doing changes, please add a new tag with the next version number,
then update this README with the latest version number.

# Adding a tag
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0

# Removing a tag locally & remotely
git tag -d v1.0.0
git push origin --delete tag v1.0.0

-->