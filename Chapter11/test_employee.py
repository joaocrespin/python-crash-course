import pytest
from employee import Employee

@pytest.fixture
def new_employee():
    new_employee = Employee('Jonas', 'Brother', 45_000)
    return new_employee

def test_give_default_raise(new_employee):
    new_employee.give_raise()
    assert new_employee.salary == 50_000

def test_give_custom_raise(new_employee):
    new_employee.give_raise(10_000)
    assert new_employee.salary == 55_000
