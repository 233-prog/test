
test_cases = {
    "test_case_1": {
        'user_cards' : [('2','D'), ('3','D')],
        'community_cards' : [('6','D'), ('8','D'), ('T','D'), ('5','C'), ('4','S')],
        'expected_output_rank' : 'Flush',
        'best_five_cards' : '2D 3D 6D 8D TD'
    }
}


import test_cases_ranking

# print(test_cases_ranking.test_cases)


# user_cards_tuples, board_cards_tuples = user_input()
# full_hand = user_cards_tuples + board_cards_tuples
# hand_ranking = evaluate_hand(full_hand)

for test_case, data in test_cases_ranking.test_cases.items():
    print(f"Test Case: {test_case}")
    print(data)
    user_cards_tuples = data['user_cards']
    board_cards_tuples = data['community_cards']
    full_hand = user_cards_tuples + board_cards_tuples
    hand_ranking = evaluate_hand(full_hand)
    ranking_type = hand_ranking[0]
    best_cards = hand_ranking[1]

    if ranking_type == data['expected_output_rank']:
        print("Test Passed")
    else:
        print("Test Failed")
        print(f"Expected: {data['expected_output_rank']}; Actual: {ranking_type}")
    exit()
