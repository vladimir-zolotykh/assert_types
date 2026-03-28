#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from functools import wraps


def assert_types(*ty_args, **ty_kwargs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


@assert_types(name=str, age=int, is_student=bool)
def create_greeting(name: str, age: int = 18, is_student: bool = False) -> str:
    student_status = "a student" if is_student else "not a student"
    return f"Hello, {name}! You are {age} years old and you are {student_status}."


if __name__ == "__main__":
    print(create_greeting("Alice"))
    print(create_greeting("Bob", 25, True))
    print(create_greeting("Charlie", is_student=True))
