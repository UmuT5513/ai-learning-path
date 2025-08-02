import pytest
from validator import can_perform, is_valid_number

@pytest.mark.parametrize("role, operation, expected", [("user", "topla", True), 
                                        ("user", "carp", False), 
                                        ("user", "bol", False), 
                                        ("user", "cikar", True), 
                                        ("admin", "topla", True), 
                                        ("admin", "carp", True), 
                                        ("admin", "cikar", True), 
                                        ("admin", "bol", True)
                                        ])
def test_validator(role, operation, expected):
    assert can_perform(operation=operation, role=role) == expected



@pytest.mark.parametrize("x, expected ", [(5, True), 
                                          (1.5, True),
                                          ("a", False),
                                          ([], False),
                                          ({}, False),
                                          (None, False),
                                          ])
def test_is_valid_number(x, expected):
    assert is_valid_number(x) == expected
    