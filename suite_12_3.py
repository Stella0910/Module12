import unittest
import tests_12_3

run_tour_ts = unittest.TestSuite()
run_tour_ts.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
run_tour_ts.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_tour_ts)
