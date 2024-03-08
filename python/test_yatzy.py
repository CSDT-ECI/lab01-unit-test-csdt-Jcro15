from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_demo():
        expected = 15
        actual = 15
        assert expected == actual

def test_chance_sum_of_all_dices():
        dices = [1,1,3,3,6]
        expected_score = 14
        score = Yatzy.chance(dices[0],dices[1],dices[2],dices[3],dices[4])
        assert expected_score == score

def test_yatzy_player_scores_50():
        dices = [1,1,1,1,1]
        expected_score = 50
        score = Yatzy.yatzy(dices)
        assert expected_score == score

def test_yatzy_player_scores_0():
        dices = [1,1,2,1,1]
        expected_score = 0
        score = Yatzy.yatzy(dices)
        assert expected_score == score

def test_ones_all_occurrences_summed():
        dices = [1,1,1,1,2]
        expected_score = 4
        score = Yatzy.ones(dices[0],dices[1],dices[2],dices[3],dices[4])
        assert expected_score == score

def test_twos_all_occurrences_summed():
        dices = [2,2,2,2,4]
        expected_score = 8
        score = Yatzy.twos(dices[0],dices[1],dices[2],dices[3],dices[4])
        assert expected_score == score

def test_threes_all_occurrences_summed():
        dices = [3,1,3,3,3]
        expected_score = 12
        score = Yatzy.threes(dices[0],dices[1],dices[2],dices[3],dices[4])
        assert expected_score == score

def test_fours_all_occurrences_summed():
        dices = [4,4,4,4,1]
        expected_score = 16
        yatzy = Yatzy(dices[0],dices[1],dices[2],dices[3],dices[4])
        score = yatzy.fours()
        assert expected_score == score

def test_fives_all_occurrences_summed():
        dices = [5,5,1,5,5]
        expected_score = 20
        yatzy = Yatzy(dices[0],dices[1],dices[2],dices[3],dices[4])
        score = yatzy.fives()
        assert expected_score == score

def test_sixes_all_occurrences_summed():
        dices = [6,6,2,6,6]
        expected_score = 24
        yatzy = Yatzy(dices[0],dices[1],dices[2],dices[3],dices[4])
        score = yatzy.sixes()
        assert expected_score == score

def test_score_pair_player_scores_0():
        dices = [1,2,3,4,5]
        expected_score = 0
        score = Yatzy.score_pair(dices[0],dices[1],dices[2],dices[3],dices[4])
        assert expected_score == score

def test_score_pair_player_scores_sum_of_pairs():
        dices = [3,3,3,4,4]
        expected_score = 8
        score = Yatzy.score_pair(dices[0],dices[1],dices[2],dices[3],dices[4])
        assert expected_score == score

def test_crazy_chance_all_even_3_multiplier():
        dices = [2,4,6,2,2]
        expected_score = 48
        score = Yatzy.crazy_chance(dices)
        assert expected_score == score

def test_crazy_chance_all_odd_2_multiplier():
        dices = [2,4,6,2,2]
        expected_score = 48
        score = Yatzy.crazy_chance(dices)
        assert expected_score == score

def test_crazy_chance_mixed():
        dices = [2,4,3,5,6]
        expected_score = 52
        score = Yatzy.crazy_chance(dices)
        assert expected_score == score
