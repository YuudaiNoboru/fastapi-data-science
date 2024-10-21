from typing import Any, cast

def f(x: Any) -> Any:
    return x

a = f("a")
a = cast(str, f("a"))