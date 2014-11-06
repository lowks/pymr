import os
import unittest

from click.testing import CliRunner

from pymr import run


class TestRun(unittest.TestCase):

    def test_run_command_finds_default(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('.pymr', 'w') as f:
                f.write('[tags]\ntags = default\n\n')

            expected = 'calling : in ./.pymr\n'
            result = runner.invoke(run.run, args=[':'])

            self.assertFalse(result.exception)
            self.assertEqual(result.output, expected)

    def test_run_command_finds_tags(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('.pymr', 'w') as f:
                f.write('[tags]\ntags = test\n\n')

            expected = 'calling : in ./.pymr\n'
            result = runner.invoke(run.run, args=['-ttest', ':'])

            self.assertFalse(result.exception)
            self.assertEqual(result.output, expected)

    def test_run_command_finds_tags_when_multiple_tags_exist(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('.pymr', 'w') as f:
                f.write('[tags]\ntags = test,test2\n\n')

            expected = 'calling : in ./.pymr\n'
            result = runner.invoke(run.run, args=['-ttest2', ':'])

            self.assertFalse(result.exception)
            self.assertEqual(result.output, expected)
