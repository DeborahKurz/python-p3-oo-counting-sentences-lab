#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self._value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")