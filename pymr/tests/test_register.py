import os
import unittest

from click.testing import CliRunner

from pymr import register

class TestRegiser(unittest.TestCase):

    def test_register_command_creates_file(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(register.register)
            self.assertFalse(result.exception)
            self.assertTrue(os.path.exists('.pymr'))

    def test_register_command_creates_default_tag(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(register.register)
            self.assertFalse(result.exception)

            expected = '[tags]\ntags = default\n\n'
            with open('.pymr', 'r') as f:
                actual = f.read()

            self.assertEqual(expected, actual)

    def test_register_command_creates_single_tag(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(register.register, args=['-ttest'])
            self.assertFalse(result.exception)

            expected = '[tags]\ntags = test\n\n'
            with open('.pymr', 'r') as f:
                actual = f.read()

            self.assertEqual(expected, actual)

    def test_register_command_creates_multiple_tags(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(register.register, args=['-ttest', '-ttest2'])
            self.assertFalse(result.exception)

            expected = '[tags]\ntags = test,test2\n\n'
            with open('.pymr', 'r') as f:
                actual = f.read()

            self.assertEqual(expected, actual)

    def test_register_command_appends_single_tag(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('.pymr', 'w') as f:
                f.write('[tags]\ntags = test\n\n')

            result = runner.invoke(register.register, args=['-ttest2', '--append'])
            self.assertFalse(result.exception)

            expected = '[tags]\ntags = test,test2\n\n'
            with open('.pymr', 'r') as f:
                actual = f.read()

            self.assertEqual(expected, actual)

    def test_register_command_appends_multiple_tags(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('.pymr', 'w') as f:
                f.write('[tags]\ntags = test\n\n')

            result = runner.invoke(register.register, args=['-ttest2', '-ttest3', '--append'])
            self.assertFalse(result.exception)

            expected = '[tags]\ntags = test,test2,test3\n\n'
            with open('.pymr', 'r') as f:
                actual = f.read()

            self.assertEqual(expected, actual)

    def test_register_command_appends_new_tags_only(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('.pymr', 'w') as f:
                f.write('[tags]\ntags = test\n\n')

            result = runner.invoke(register.register, args=['-ttest', '--append'])
            self.assertFalse(result.exception)

            expected = '[tags]\ntags = test\n\n'
            with open('.pymr', 'r') as f:
                actual = f.read()

            self.assertEqual(expected, actual)
