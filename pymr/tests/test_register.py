import os
import unittest

from click.testing import CliRunner

from pymr import register


class TestRegiser(unittest.TestCase):

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

    def test_register_command_creates_file(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(register.register)
            assert not result.exception
            assert os.path.exists('.pymr')

    def test_register_command_creates_default_tag(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(register.register)
            assert not result.exception

            expected = '[tags]\ntags = default\n\n'
            with open('.pymr', 'r') as f:
                actual = f.read()

            self.assertEqual(expected, actual)

    def test_register_command_creates_single_tag(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(register.register, args=['-ttest'])
            assert not result.exception

            expected = '[tags]\ntags = test\n\n'
            with open('.pymr', 'r') as f:
                actual = f.read()

            self.assertEqual(expected, actual)

    def test_register_command_creates_multiple_tags(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(register.register, args=['-ttest', '-ttest2'])
            assert not result.exception

            expected = '[tags]\ntags = test,test2\n\n'
            with open('.pymr', 'r') as f:
                actual = f.read()

            self.assertEqual(expected, actual)
