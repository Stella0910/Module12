import rt_with_exceptions as rt
import unittest
import logging


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner1 = rt.Runner('Runner1', speed=-5)
            logging.info('"test_walk" выполнен успешно')
            for _ in range(1, 11):
                runner1.walk()
            self.assertEqual(runner1.distance, 50)
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner1 = rt.Runner(10)
            logging.info('"test_run" выполнен успешно')
            for _ in range(1, 11):
                runner1.run()
            self.assertEqual(runner1.distance, 100)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        runner1 = rt.Runner('Runner1')
        runner2 = rt.Runner('Runner2')
        for _ in range(1, 11):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s')
