import unittest

from pymr import run


class TestRun(unittest.TestCase):

    def setUp(self):
        self.foo = 'bar'

    def test_default_tag_is_set(self):
        expected = 'default'
        actual = run.set_default_tag('')

        self.assertEqual(expected, actual)

    def test_multiple_tags_are_parsed(self):
        expected = ('foo', 'bar')
        actual = run.parse_tag(('foo', 'bar'))

        self.assertEqual(expected, actual)

    def test_single_tag_is_parsed(self):
        expected = ('foo',)
        actual = run.parse_tag('foo')

        self.assertEqual(expected, actual)

    def test_tags_are_unpacked(self):
        expected = ['foo', 'bar']
        actual = run.unpack_tags('foo,bar')

        self.assertEqual(expected, actual)
