init -1 python:
    if not "df_actions" in locals() | globals():
        df_actions = {}

# dictionary editable at runtime, but it is strongly discouraged to pre-enter elements (dictionary contents are based only on saves)
default actions = {}
