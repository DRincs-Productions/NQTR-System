init -1 python:
    if not "routine" in locals() | globals():
        routine = {}
    if not "df_routine" in locals() | globals():
        df_routine = {}

# dictionary editable at runtime, but it is strongly discouraged to pre-enter elements (dictionary contents are based only on saves)
default routine = {}
