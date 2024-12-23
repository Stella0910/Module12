import runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner1 = runner.Runner('Runner1')
        for _ in range(1, 11):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    def test_run(self):
        runner1 = runner.Runner('Runner1')
        for _ in range(1, 11):
            runner1.run()
        self.assertEqual(runner1.distance, 100)

    def test_challenge(self):
        runner1 = runner.Runner('Runner1')
        runner2 = runner.Runner('Runner2')
        for _ in range(1, 11):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)
