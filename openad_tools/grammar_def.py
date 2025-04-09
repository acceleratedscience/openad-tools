"""
Pyparsing grammar definitions for the OpenAD command line interface.

Usage:
    from openad_tools.grammar_def import molecule_identifier_s


Pyparsing documentation:
    https://pyparsing-docs.readthedocs.io/en/latest/HowToUsePyparsing.html
Pyparsing types:
    https://pyparsing-docs.readthedocs.io/en/latest/pyparsing.html
"""

import pyparsing as pp

# ------------------------------------------
# region - Strings

str_catchall = pp.OneOrMore(pp.Word(pp.printables))
str_any = pp.Word(pp.printables)
str_strict = pp.Word(pp.alphanums + "-_")
str_quoted = pp.QuotedString("'", escChar="\\")
# str_quoted = pp.Suppress("'") + pp.Word(pp.printables) + pp.Suppress("'")

str_opt_quoted = str_strict | str_quoted
str_strict_or_quoted = str_strict | str_quoted  # Legacy

# endregion
# ------------------------------------------
# region - Lists

# Open and close square brackets, with optional space on inside
_sb_open = pp.Suppress(pp.Literal("[") + pp.Optional(pp.White()))
_sb_close = pp.Suppress(pp.Optional(pp.White()) + pp.Literal("]"))

# List of quoted strings separated by commas (white space optional by default) and encapsulated in square brackets
list_quoted = _sb_open + pp.delimitedList(str_quoted) + _sb_close

# endregion
# ------------------------------------------
# region - Molecules

# Molecule(s) keywords
molecule = pp.CaselessKeyword("molecule") | pp.CaselessKeyword("mol")
molecules = pp.CaselessKeyword("molecules") | pp.CaselessKeyword("mols")
molecule_s = pp.MatchFirst([molecule, molecules])

# Molecule identifier
molecule_identifier = (pp.Word(pp.alphanums + "_[]()=,-+/\\#@.*;")) | (
    pp.Suppress("'") + pp.Word(pp.alphanums + "_[]()=,-+/\\#@.*;") + pp.Suppress("'")
)

# Agnostic parser that handler both single and list of molecules input, always resulting in a list of identifiers
# Input:
#   - foo
#   - [foo,bar]
# Output:
#   - ["foo"]
#   - ["foo", "bar"]
molecule_identifier_s = pp.MatchFirst(
    [
        list_quoted("identifiers"),
        molecule_identifier("identifiers"),
    ]
)

# Molecule woroking set
molecule_working_set = pp.MatchFirst(
    [
        pp.CaselessKeyword("@mws"),
        pp.CaselessKeyword("@mols"),
        pp.CaselessKeyword("@molecules"),
    ]
)("mws")


# endregion
# ------------------------------------------
# region - Clauses

# Save as <filename>
clause_save_as = pp.Optional(
    pp.Suppress(pp.CaselessKeyword("save")) + pp.Suppress(pp.CaselessKeyword("as")) + str_quoted("results_file")
)("save_as")

# USING (param1=value, param2=value, ...)
_using = pp.CaselessKeyword("USING").suppress()
_param_value = pp.Group(str_strict_or_quoted + pp.Suppress("=") + str_strict_or_quoted)
clause_using = pp.Optional(
    _using + pp.Suppress("(") + pp.Optional(pp.OneOrMore(_param_value))("using") + pp.Suppress(")")
)

# Update molecule working set
clause_update_mws = pp.Optional(pp.CaselessKeyword("update") + molecule_working_set)

# endregion
