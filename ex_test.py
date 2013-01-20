#coding: utf-8

from nose.tools import ok_, eq_
import ex

def add_test():
    eq_(ex.add(1, 2), 3);
    eq_(ex.add(1, 5), 6);

def sub_test():
    eq_(ex.sub(1, 1), 0);
    eq_(ex.sub(2, 1), 1);
    eq_(ex.sub(1, 2), -1);

def sub_test2():
    eq_(ex.sub(2, 100), 100);

