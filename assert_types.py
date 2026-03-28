#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from functools import wraps
import inspect


def assert_types(*ty_args, **ty_kwargs):
    def decorator(func):
        sig = inspect.signature(func)
        bount_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_args = sig.bind(*args, **kwargs).arguments
            for name, value in bound_args.items():
                if name not in bount_types:
                    continue
                if not isinstance(value, bount_types[name]):
                    raise TypeError(
                        f"{name!r} must be of type {bount_types[name].__name__!r}"
                    )
            return func(*args, **kwargs)

        return wrapper

    return decorator


@assert_types(name=str, age=int, is_student=bool)
def create_greeting(name: str, age: int = 18, is_student: bool = False) -> str:
    student_status = "a student" if is_student else "not a student"
    return f"Hello, {name}! You are {age} years old and you are {student_status}."


def test_assert_types(capsys):
    print(create_greeting("Alice"))
    print(create_greeting("Bob", 25, True))
    print(create_greeting("Charlie", is_student=True))
    out = capsys.readouterr().out
    assert "Hello, Alice! You are 18 years old and you are not a student." in out
    assert "Hello, Bob! You are 25 years old and you are a student." in out
    assert "Hello, Charlie! You are 18 years old and you are a student." in out
