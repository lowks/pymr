import unittest

from pymr import register


class TestRegiser(unittest.TestCase):

    def setUp(self):
        self.foo = 'bar'

    def test_default_tag_is_set(self):
        expected = 'default'
        actual = register.set_default_tag('')

        self.assertEqual(expected, actual)

    def test_multiple_tags_are_parsed(self):
        expected = 'foo,bar'
        actual = register.parse_tag(('foo', 'bar'))

        self.assertEqual(expected, actual)

    def test_single_tag_is_parsed(self):
        expected = 'foo'
        actual = register.parse_tag('foo')

        self.assertEqual(expected, actual)
