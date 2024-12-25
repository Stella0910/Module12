import runner_and_tournament as rt
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = rt.Runner('Усэйн', 10)
        self.andrey = rt.Runner('Андрей', 9)
        self.nick = rt.Runner('Ник', 3)

    def test_start_1(self):
        self.tournament1 = rt.Tournament(90, self.usain, self.nick)
        result = self.tournament1.start()
        self.all_results['Соревнование №1'] = [f'{k}: {v.name}' for k, v in result.items()]
        self.assertTrue(result[max(k for k, v in result.items())], self.nick)

    def test_start_2(self):
        self.tournament2 = rt.Tournament(90, self.andrey, self.nick)
        result = self.tournament2.start()
        self.all_results['Соревнование №2'] = [f'{k}: {v.name}' for k, v in result.items()]
        self.assertTrue(result[max(k for k, v in result.items())], self.nick)

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
