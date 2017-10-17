# -*- coding: utf-8 -*-
import pytest


def is_numeric(value):
    '''Check if value is numeric.'''
    return value.isnumeric()


@pytest.mark.gen_string()
def test_gen_alpha_string_with_no_arguments(value):
    '''Passing no arguments should return a random string type.'''
    assert len(value) > 0


@pytest.mark.gen_string(1)
def test_gen_alpha_string_with_limit_arguments(value):
    '''Passing limit argument should return a random string type.'''
    assert len(value) > 0


@pytest.mark.gen_string(4, 'alpha', length=12)
def test_gen_alpha_string_with_length(value):
    '''Generate an `alpha` string of length 12.'''
    assert len(value) == 12


@pytest.mark.gen_string(1, 'punctuation', length=12, validator=is_numeric, default='1')
def test_gen_alpha_string_with_validator(value):
    '''Call `gen_string` with validator that returns default of `1`.'''
    assert value == '1'
