import runner
import runner_and_tournament as rt
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner1 = runner.Runner('Runner1')
        for _ in range(1, 11):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner1 = runner.Runner('Runner1')
        for _ in range(1, 11):
            runner1.run()
        self.assertEqual(runner1.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = runner.Runner('Runner1')
        runner2 = runner.Runner('Runner2')
        for _ in range(1, 11):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.usain = rt.Runner('Усэйн', 10)
        self.andrey = rt.Runner('Андрей', 9)
        self.nick = rt.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_1(self):
        self.tournament1 = rt.Tournament(90, self.usain, self.nick)
        result = self.tournament1.start()
        self.all_results['Соревнование №1'] = [f'{k}: {v.name}' for k, v in result.items()]
        self.assertTrue(result[max(k for k, v in result.items())], self.nick)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_2(self):
        self.tournament2 = rt.Tournament(90, self.andrey, self.nick)
        result = self.tournament2.start()
        self.all_results['Соревнование №2'] = [f'{k}: {v.name}' for k, v in result.items()]
        self.assertTrue(result[max(k for k, v in result.items())], self.nick)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_3(self):
        self.tournament3 = rt.Tournament(90, self.usain, self.andrey, self.nick)
        result = self.tournament3.start()
        self.all_results['Соревнование №3'] = [f'{k}: {v.name}' for k, v in result.items()]
        self.assertTrue(result[max(k for k, v in result.items())], self.nick)

    @classmethod
    def tearDownClass(cls):
        for k, v in cls.all_results.items():
            to_remove = ["'", "[", "]"]
            for i in to_remove:
                v = str(v).replace(i, '')
            print(f'{k}:\n{v}\n')
