import os
import unittest

from pymr import tagutils

class TestTags(unittest.TestCase):

    def test_default_tag_is_set(self):
        expected = 'default'
        actual = tagutils.set_default('')

        self.assertEqual(expected, actual)

    def test_multiple_tags_are_parsed(self):
        expected = 'foo,bar'
        actual = tagutils.parse(('foo', 'bar'))

        self.assertEqual(expected, actual)

    def test_single_tag_is_parsed(self):
        expected = 'foo'
        actual = tagutils.parse('foo')

        self.assertEqual(expected, actual)

    def test_multiple_tags_are_unpacked(self):
        expected = ['foo', 'bar']
        actual = tagutils.unpack('foo,bar')

        self.assertEqual(expected, actual)

    def test_single_tag_is_unpacked(self):
        expected = ['foo']
        actual = tagutils.unpack('foo')

        self.assertEqual(expected, actual)
