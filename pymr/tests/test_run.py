import os
import unittest

from click.testing import CliRunner

from pymr import run


class TestRun(unittest.TestCase):

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

    def test_run_command_finds_default(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('.pymr', 'w') as f:
                f.write('[tags]\ntags = default\n\n')

            expected = 'calling echo in ./.pymr\n'
            result = runner.invoke(run.run, args=['echo'])

            assert not result.exception
            assert result.output == expected

    def test_run_command_finds_tags(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('.pymr', 'w') as f:
                f.write('[tags]\ntags = test\n\n')

            expected = 'calling echo in ./.pymr\n'
            result = runner.invoke(run.run, args=['-ttest', 'echo'])

            assert not result.exception
            assert result.output == expected

    def test_run_command_finds_tags_when_multiple_tags_exist(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('.pymr', 'w') as f:
                f.write('[tags]\ntags = test,test2\n\n')

            expected = 'calling echo in ./.pymr\n'
            result = runner.invoke(run.run, args=['-ttest2', 'echo'])

            assert not result.exception
            assert result.output == expected
