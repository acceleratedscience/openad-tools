"""
Pyparsing grammar definitions for the OpenAD command line interface.
"""

# https://pyparsing-docs.readthedocs.io/en/latest/pyparsing.html

# -fmt: off

import pyparsing as py

#############################################
# region - Strings

str_any = py.Word(py.printables)
str_strict = py.Word(py.alphanums + "-_")
str_quoted = py.QuotedString("'", escChar="\\")
str_strict_or_quoted = str_strict | str_quoted
str_opt_quoted = str_quoted | (py.Suppress("'") + py.Word(py.printables) + py.Suppress("'"))

# endregion


#############################################
# region - Lists

# Open and close square brackets, with optional space on inside
_sb_open = py.Suppress(py.Literal("[") + py.Optional(py.White()))
_sb_close = py.Suppress(py.Optional(py.White()) + py.Literal("]"))

# Comma with optional spaces before/after
_comma = py.Suppress(py.Optional(py.White()) + py.Literal(",") + py.Optional(py.White()))

# List of quoted strings separated by commas and encapsulated in square brackets
list_quoted = _sb_open + py.delimitedList(str_quoted, delim=",") + _sb_close

# endregion


#############################################
# region - Molecules

# Molecule(s) keywords
molecule = py.CaselessKeyword("molecule") | py.CaselessKeyword("mol")
molecules = py.CaselessKeyword("molecules") | py.CaselessKeyword("mols")

# Recursive molecule identifier that allows to parse a square brackets list
# with molecule identifiers that contain square brackets themselves.
# This requires that the list is the end of the command.

# molecule_identifier = py.Forward()
# _mol_chars = py.alphanums + "_()=-+/\\#@.*;"
# _mol_str = py.Word(_mol_chars)
# _mol_str_brackets = py.Combine(py.Literal("[") + molecule_identifier + py.Literal("]"))
# molecule_identifier <<= py.Combine(py.OneOrMore(_mol_str | _mol_str_brackets))

molecule_identifier = (py.Word(py.alphanums + "_[]()=,-+/\\#@.*;")) | (
    py.Suppress("'") + py.Word(py.alphanums + "_[]()=,-+/\\#@.*;") + py.Suppress("'")
)

# List of identifier strings separated by comas
_delimited_molecule_identifiers = py.delimitedList(molecule_identifier, delim=_comma)

# List of strings separated by comas and encapsulated in square brackets
molecule_identifier_list = _sb_open + _delimited_molecule_identifiers + _sb_close

# Molecule woroking set
molecule_working_set = py.MatchFirst(
    [
        py.CaselessKeyword("@mws"),
        py.CaselessKeyword("@mols"),
        py.CaselessKeyword("@molecules"),
    ]
)


# endregion


#############################################
# region - Clauses

# Save as <filename>
clause_save_as = py.Optional(
    py.Suppress(py.CaselessKeyword("save")) + py.Suppress(py.CaselessKeyword("as")) + str_quoted("results_file")
)("save_as")

# USING (param1=value, param2=value, ...)
_using = py.CaselessKeyword("USING").suppress()
_param_value = py.Group(str_strict_or_quoted + py.Suppress("=") + str_strict_or_quoted)
clause_using = py.Optional(
    _using + py.Suppress("(") + py.Optional(py.OneOrMore(_param_value))("using") + py.Suppress(")")
)

# Update molecule working set
clause_update_mws = py.Optional(py.CaselessKeyword("update") + molecule_working_set)

# endregion
