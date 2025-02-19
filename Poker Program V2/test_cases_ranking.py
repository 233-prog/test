

test_cases = {
    # Category 1: High Card (15 test cases)
    "test_case_1": {
        'user_cards': [('A','H'), ('K','D')],
        'community_cards': [('Q','S'), ('J','H'), ('9','D'), ('5','C'), ('3','S')],
        'expected_output_rank': 'High Card',
        'best_five_cards': 'AH KD QS JH 9D'
    },
    "test_case_2": {
        'user_cards': [('Q','H'), ('8','D')],
        'community_cards': [('A','S'), ('K','H'), ('7','C'), ('5','S'), ('3','D')],
        'expected_output_rank': 'High Card',
        'best_five_cards': 'AS KH QH 8D 7C'
    },
    "test_case_3": {
        'user_cards': [('J','C'), ('9','D')],
        'community_cards': [('A','H'), ('K','S'), ('8','C'), ('6','D'), ('4','H')],
        'expected_output_rank': 'High Card',
        'best_five_cards': 'AH KS JC 9D 8C'
    },
    "test_case_4": {
        'user_cards': [('T','S'), ('7','H')],
        'community_cards': [('K','C'), ('9','S'), ('5','D'), ('3','C'), ('2','H')],
        'expected_output_rank': 'High Card',
        'best_five_cards': 'KC TS 9S 7H 5D'
    },
    "test_case_5": {
        'user_cards': [('9','H'), ('6','C')],
        'community_cards': [('A','D'), ('K','H'), ('4','S'), ('3','D'), ('2','C')],
        'expected_output_rank': 'High Card',
        'best_five_cards': 'AD KH 9H 6C 4S'
    },
    "test_case_6": {
        'user_cards': [('8','S'), ('5','H')],
        'community_cards': [('Q','D'), ('J','C'), ('7','S'), ('4','D'), ('2','H')],
        'expected_output_rank': 'High Card',
        'best_five_cards': 'QD JC 8S 7S 5H'
    },
    "test_case_7": {
        'user_cards': [('7','D'), ('4','C')],
        'community_cards': [('A','S'), ('9','D'), ('6','H'), ('3','C'), ('2','S')],
        'expected_output_rank': 'High Card',
        'best_five_cards': 'AS 9D 7D 6H 4C'
    },
    "test_case_8": {
        'user_cards': [('6','H'), ('3','S')],
        'community_cards': [('K','D'), ('Q','H'), ('8','C'), ('5','S'), ('2','D')],
        'expected_output_rank': 'High Card',
        'best_five_cards': 'KD QH 8C 6H 5S'
    },
    "test_case_9": {
        'user_cards': [('5','C'), ('3','D')],
        'community_cards': [('J','S'), ('9','C'), ('7','D'), ('4','H'), ('2','S')],
        'expected_output_rank': 'High Card',
        'best_five_cards': 'JS 9C 7D 5C 4H'
    },
    "test_case_10": {
        'user_cards': [('4','H'), ('2','C')],
        'community_cards': [('Q','S'), ('J','D'), ('8','H'), ('7','C'), ('5','S')],
        'expected_output_rank': 'High Card',
        'best_five_cards': 'QS JD 8H 7C 5S'
    },
    "test_case_11": {
        'user_cards': [('3','S'), ('2','H')],
        'community_cards': [('K','C'), ('T','D'), ('9','H'), ('8','S'), ('4','C')],
        'expected_output_rank': 'High Card',
        'best_five_cards': 'KC TD 9H 8S 4C'
    },
    "test_case_12": {
        'user_cards': [('A','C'), ('8','D')],
        'community_cards': [('K','H'), ('Q','S'), ('7','D'), ('5','C'), ('3','H')],
        'expected_output_rank': 'High Card',
        'best_five_cards': 'AC KH QS 8D 7D'
    },
    "test_case_13": {
        'user_cards': [('K','S'), ('7','C')],
        'community_cards': [('Q','D'), ('J','H'), ('8','S'), ('4','D'), ('3','C')],
        'expected_output_rank': 'High Card',
        'best_five_cards': 'KS QD JH 8S 7C'
    },
    "test_case_14": {
        'user_cards': [('Q','C'), ('6','H')],
        'community_cards': [('J','S'), ('9','D'), ('5','C'), ('4','H'), ('2','D')],
        'expected_output_rank': 'High Card',
        'best_five_cards': 'QC JS 9D 6H 5C'
    },
    "test_case_15": {
        'user_cards': [('J','D'), ('8','S')],
        'community_cards': [('T','H'), ('7','D'), ('4','S'), ('3','H'), ('2','C')],
        'expected_output_rank': 'High Card',
        'best_five_cards': 'JD TH 8S 7D 4S'
    },
    
    # Category 2: One Pair (15 test cases)
    "test_case_16": {
        'user_cards': [('A','H'), ('A','D')],
        'community_cards': [('K','S'), ('Q','H'), ('J','D'), ('5','C'), ('3','S')],
        'expected_output_rank': 'One Pair',
        'best_five_cards': 'AH AD KS QH JD'
    },
    "test_case_17": {
        'user_cards': [('K','H'), ('K','D')],
        'community_cards': [('A','S'), ('Q','H'), ('J','D'), ('4','C'), ('2','S')],
        'expected_output_rank': 'One Pair',
        'best_five_cards': 'KH KD AS QH JD'
    },
    "test_case_18": {
        'user_cards': [('Q','S'), ('Q','C')],
        'community_cards': [('A','H'), ('K','D'), ('J','S'), ('5','C'), ('3','H')],
        'expected_output_rank': 'One Pair',
        'best_five_cards': 'QS QC AH KD JS'
    },
    "test_case_19": {
        'user_cards': [('J','H'), ('J','D')],
        'community_cards': [('A','S'), ('K','H'), ('Q','D'), ('8','C'), ('2','S')],
        'expected_output_rank': 'One Pair',
        'best_five_cards': 'JH JD AS KH QD'
    },
    "test_case_20": {
        'user_cards': [('T','H'), ('T','D')],
        'community_cards': [('A','S'), ('K','C'), ('Q','H'), ('7','D'), ('3','S')],
        'expected_output_rank': 'One Pair',
        'best_five_cards': 'TH TD AS KC QH'
    },
    "test_case_21": {
        'user_cards': [('9','H'), ('9','D')],
        'community_cards': [('A','S'), ('K','H'), ('8','C'), ('5','D'), ('3','S')],
        'expected_output_rank': 'One Pair',
        'best_five_cards': '9H 9D AS KH 8C'
    },
    "test_case_22": {
        'user_cards': [('8','H'), ('8','D')],
        'community_cards': [('A','S'), ('K','C'), ('Q','H'), ('5','S'), ('2','D')],
        'expected_output_rank': 'One Pair',
        'best_five_cards': '8H 8D AS KC QH'
    },
    "test_case_23": {
        'user_cards': [('7','H'), ('7','D')],
        'community_cards': [('A','S'), ('K','H'), ('Q','D'), ('9','C'), ('4','S')],
        'expected_output_rank': 'One Pair',
        'best_five_cards': '7H 7D AS KH QD'
    },
    "test_case_24": {
        'user_cards': [('6','H'), ('6','D')],
        'community_cards': [('A','S'), ('K','H'), ('Q','C'), ('8','D'), ('3','S')],
        'expected_output_rank': 'One Pair',
        'best_five_cards': '6H 6D AS KH QC'
    },
    "test_case_25": {
        'user_cards': [('5','H'), ('5','D')],
        'community_cards': [('A','S'), ('K','H'), ('Q','D'), ('9','C'), ('4','S')],
        'expected_output_rank': 'One Pair',
        'best_five_cards': '5H 5D AS KH QD'
    },
    "test_case_26": {
        'user_cards': [('4','H'), ('4','D')],
        'community_cards': [('A','S'), ('K','H'), ('Q','C'), ('8','S'), ('3','D')],
        'expected_output_rank': 'One Pair',
        'best_five_cards': '4H 4D AS KH QC'
    },
    "test_case_27": {
        'user_cards': [('3','H'), ('3','D')],
        'community_cards': [('A','S'), ('K','H'), ('Q','D'), ('8','C'), ('5','S')],
        'expected_output_rank': 'One Pair',
        'best_five_cards': '3H 3D AS KH QD'
    },
    "test_case_28": {
        'user_cards': [('2','H'), ('2','D')],
        'community_cards': [('A','S'), ('K','H'), ('Q','C'), ('J','D'), ('8','S')],
        'expected_output_rank': 'One Pair',
        'best_five_cards': '2H 2D AS KH QC'
    },
    "test_case_29": {
        'user_cards': [('A','C'), ('A','D')],
        'community_cards': [('K','S'), ('J','H'), ('9','C'), ('5','D'), ('3','S')],
        'expected_output_rank': 'One Pair',
        'best_five_cards': 'AC AD KS JH 9C'
    },
    "test_case_30": {
        'user_cards': [('K','C'), ('K','D')],
        'community_cards': [('A','S'), ('Q','H'), ('8','C'), ('7','D'), ('4','S')],
        'expected_output_rank': 'One Pair',
        'best_five_cards': 'KC KD AS QH 8C'
    },
    
    # Category 3: Two Pair (15 test cases)
    "test_case_31": {
        'user_cards': [('A','H'), ('K','H')],
        'community_cards': [('A','D'), ('K','D'), ('Q','S'), ('3','C'), ('5','D')],
        'expected_output_rank': 'Two Pair',
        'best_five_cards': 'AH AD KH KD QS'
    },
    "test_case_32": {
        'user_cards': [('Q','C'), ('J','C')],
        'community_cards': [('Q','H'), ('J','H'), ('T','S'), ('8','D'), ('2','C')],
        'expected_output_rank': 'Two Pair',
        'best_five_cards': 'QC QH JC JH TS'
    },
    "test_case_33": {
        'user_cards': [('T','H'), ('9','H')],
        'community_cards': [('T','D'), ('9','D'), ('K','S'), ('4','C'), ('3','D')],
        'expected_output_rank': 'Two Pair',
        'best_five_cards': 'TH TD 9H 9D KS'
    },
    "test_case_34": {
        'user_cards': [('8','S'), ('7','S')],
        'community_cards': [('8','D'), ('7','D'), ('J','H'), ('4','C'), ('2','S')],
        'expected_output_rank': 'Two Pair',
        'best_five_cards': '8S 8D 7S 7D JH'
    },
    "test_case_35": {
        'user_cards': [('6','H'), ('5','H')],
        'community_cards': [('6','D'), ('5','D'), ('A','S'), ('3','C'), ('2','D')],
        'expected_output_rank': 'Two Pair',
        'best_five_cards': '6H 6D 5H 5D AS'
    },
    "test_case_36": {
        'user_cards': [('4','C'), ('3','C')],
        'community_cards': [('4','H'), ('3','H'), ('K','D'), ('8','S'), ('T','D')],
        'expected_output_rank': 'Two Pair',
        'best_five_cards': '4C 4H 3C 3H KD'
    },
    "test_case_37": {
        'user_cards': [('2','H'), ('A','H')],
        'community_cards': [('2','D'), ('A','D'), ('Q','S'), ('7','C'), ('9','D')],
        'expected_output_rank': 'Two Pair',
        'best_five_cards': 'AH AD 2H 2D QS'
    },
    "test_case_38": {
        'user_cards': [('K','S'), ('Q','S')],
        'community_cards': [('K','C'), ('Q','C'), ('J','D'), ('5','H'), ('3','S')],
        'expected_output_rank': 'Two Pair',
        'best_five_cards': 'KS KC QS QC JD'
    },
    "test_case_39": {
        'user_cards': [('J','H'), ('T','H')],
        'community_cards': [('J','D'), ('T','D'), ('9','S'), ('4','C'), ('2','H')],
        'expected_output_rank': 'Two Pair',
        'best_five_cards': 'JH JD TH TD 9S'
    },
    "test_case_40": {
        'user_cards': [('9','C'), ('8','C')],
        'community_cards': [('9','H'), ('8','H'), ('K','D'), ('7','S'), ('3','C')],
        'expected_output_rank': 'Two Pair',
        'best_five_cards': '9C 9H 8C 8H KD'
    },
    "test_case_41": {
        'user_cards': [('7','D'), ('6','D')],
        'community_cards': [('7','S'), ('6','S'), ('A','C'), ('4','H'), ('2','D')],
        'expected_output_rank': 'Two Pair',
        'best_five_cards': '7D 7S 6D 6S AC'
    },
    "test_case_42": {
        'user_cards': [('5','C'), ('4','C')],
        'community_cards': [('5','H'), ('4','H'), ('Q','D'), ('8','S'), ('3','D')],
        'expected_output_rank': 'Two Pair',
        'best_five_cards': '5C 5H 4C 4H QD'
    },
    "test_case_43": {
        'user_cards': [('3','S'), ('2','S')],
        'community_cards': [('3','D'), ('2','D'), ('K','H'), ('9','C'), ('7','D')],
        'expected_output_rank': 'Two Pair',
        'best_five_cards': '3S 3D 2S 2D KH'
    },
    "test_case_44": {
        'user_cards': [('A','C'), ('K','C')],
        'community_cards': [('A','D'), ('K','D'), ('J','S'), ('5','H'), ('4','S')],
        'expected_output_rank': 'Two Pair',
        'best_five_cards': 'AC AD KC KD JS'
    },
    "test_case_45": {
        'user_cards': [('Q','H'), ('J','H')],
        'community_cards': [('Q','D'), ('J','D'), ('9','S'), ('7','C'), ('3','H')],
        'expected_output_rank': 'Two Pair',
        'best_five_cards': 'QH QD JH JD 9S'
    },
    
    # Category 4: Three of a Kind (15 test cases)
    "test_case_46": {
        'user_cards': [('A','H'), ('A','D')],
        'community_cards': [('A','S'), ('K','H'), ('Q','D'), ('3','C'), ('5','S')],
        'expected_output_rank': 'Three of a Kind',
        'best_five_cards': 'AH AD AS KH QD'
    },
    "test_case_47": {
        'user_cards': [('K','H'), ('K','D')],
        'community_cards': [('K','S'), ('A','C'), ('9','H'), ('4','D'), ('2','S')],
        'expected_output_rank': 'Three of a Kind',
        'best_five_cards': 'KH KD KS AC 9H'
    },
    "test_case_48": {
        'user_cards': [('Q','S'), ('Q','C')],
        'community_cards': [('Q','H'), ('J','D'), ('8','S'), ('5','H'), ('3','C')],
        'expected_output_rank': 'Three of a Kind',
        'best_five_cards': 'QS QC QH JD 8S'
    },
    "test_case_49": {
        'user_cards': [('J','H'), ('J','D')],
        'community_cards': [('J','S'), ('T','C'), ('9','D'), ('7','S'), ('2','H')],
        'expected_output_rank': 'Three of a Kind',
        'best_five_cards': 'JH JD JS TC 9D'
    },
    "test_case_50": {
        'user_cards': [('T','H'), ('T','D')],
        'community_cards': [('T','S'), ('K','C'), ('8','H'), ('4','S'), ('3','D')],
        'expected_output_rank': 'Three of a Kind',
        'best_five_cards': 'TH TD TS KC 8H'
    },
    "test_case_51": {
        'user_cards': [('9','H'), ('9','D')],
        'community_cards': [('9','S'), ('A','H'), ('7','C'), ('5','D'), ('3','S')],
        'expected_output_rank': 'Three of a Kind',
        'best_five_cards': '9H 9D 9S AH 7C'
    },
    "test_case_52": {
        'user_cards': [('8','H'), ('8','D')],
        'community_cards': [('8','S'), ('K','H'), ('Q','C'), ('6','S'), ('3','D')],
        'expected_output_rank': 'Three of a Kind',
        'best_five_cards': '8H 8D 8S KH QC'
    },
    "test_case_53": {
        'user_cards': [('7','H'), ('7','D')],
        'community_cards': [('7','S'), ('J','C'), ('9','H'), ('4','D'), ('2','S')],
        'expected_output_rank': 'Three of a Kind',
        'best_five_cards': '7H 7D 7S JC 9H'
    },
    "test_case_54": {
        'user_cards': [('6','H'), ('6','D')],
        'community_cards': [('6','S'), ('T','C'), ('8','D'), ('5','H'), ('3','S')],
        'expected_output_rank': 'Three of a Kind',
        'best_five_cards': '6H 6D 6S TC 8D'
    },
    "test_case_55": {
        'user_cards': [('5','H'), ('5','D')],
        'community_cards': [('5','S'), ('K','D'), ('9','C'), ('7','H'), ('4','S')],
        'expected_output_rank': 'Three of a Kind',
        'best_five_cards': '5H 5D 5S KD 9C'
    },
    "test_case_56": {
        'user_cards': [('4','H'), ('4','D')],
        'community_cards': [('4','S'), ('A','C'), ('8','H'), ('7','D'), ('3','S')],
        'expected_output_rank': 'Three of a Kind',
        'best_five_cards': '4H 4D 4S AC 8H'
    },
    "test_case_57": {
        'user_cards': [('3','H'), ('3','D')],
        'community_cards': [('3','S'), ('Q','C'), ('T','H'), ('9','D'), ('2','S')],
        'expected_output_rank': 'Three of a Kind',
        'best_five_cards': '3H 3D 3S QC TH'
    },
    "test_case_58": {
        'user_cards': [('2','H'), ('2','D')],
        'community_cards': [('2','S'), ('K','C'), ('J','H'), ('8','D'), ('5','S')],
        'expected_output_rank': 'Three of a Kind',
        'best_five_cards': '2H 2D 2S KC JH'
    },
    "test_case_59": {
        'user_cards': [('A','C'), ('A','D')],
        'community_cards': [('A','S'), ('Q','H'), ('8','C'), ('4','S'), ('3','D')],
        'expected_output_rank': 'Three of a Kind',
        'best_five_cards': 'AC AD AS QH 8C'
    },
    "test_case_60": {
        'user_cards': [('K','C'), ('K','D')],
        'community_cards': [('K','S'), ('J','H'), ('7','C'), ('5','D'), ('2','S')],
        'expected_output_rank': 'Three of a Kind',
        'best_five_cards': 'KC KD KS JH 7C'
    },
    
    # Category 5: Straight (15 test cases)
    "test_case_61": {
        'user_cards': [('2','H'), ('3','D')],
        'community_cards': [('4','S'), ('5','C'), ('6','D'), ('9','H'), ('K','S')],
        'expected_output_rank': 'Straight',
        'best_five_cards': '2H 3D 4S 5C 6D'
    },
    "test_case_62": {
        'user_cards': [('3','C'), ('7','D')],
        'community_cards': [('4','H'), ('5','S'), ('6','C'), ('Q','D'), ('2','H')],
        'expected_output_rank': 'Straight',
        'best_five_cards': '3C 4H 5S 6C 7D'
    },
    "test_case_63": {
        'user_cards': [('5','D'), ('7','S')],
        'community_cards': [('4','C'), ('6','H'), ('8','D'), ('A','S'), ('3','C')],
        'expected_output_rank': 'Straight',
        'best_five_cards': '4C 5D 6H 7S 8D'
    },
    "test_case_64": {
        'user_cards': [('6','C'), ('8','S')],
        'community_cards': [('5','H'), ('7','D'), ('9','C'), ('J','S'), ('2','D')],
        'expected_output_rank': 'Straight',
        'best_five_cards': '5H 6C 7D 8S 9C'
    },
    "test_case_65": {
        'user_cards': [('7','H'), ('9','D')],
        'community_cards': [('6','S'), ('8','C'), ('T','H'), ('Q','S'), ('3','D')],
        'expected_output_rank': 'Straight',
        'best_five_cards': '6S 7H 8C 9D TH'
    },
    "test_case_66": {
        'user_cards': [('8','D'), ('T','D')],
        'community_cards': [('7','C'), ('9','H'), ('J','S'), ('4','C'), ('2','H')],
        'expected_output_rank': 'Straight',
        'best_five_cards': '7C 8D 9H TD JS'
    },
    "test_case_67": {
        'user_cards': [('9','S'), ('J','D')],
        'community_cards': [('8','H'), ('T','S'), ('Q','C'), ('3','D'), ('5','H')],
        'expected_output_rank': 'Straight',
        'best_five_cards': '8H 9S TD JD QC'
    },
    "test_case_68": {
        'user_cards': [('T','C'), ('Q','H')],
        'community_cards': [('9','D'), ('J','S'), ('K','C'), ('2','S'), ('3','H')],
        'expected_output_rank': 'Straight',
        'best_five_cards': '9D TC JS QH KC'
    },
    "test_case_69": {
        'user_cards': [('J','C'), ('Q','D')],
        'community_cards': [('T','H'), ('K','S'), ('A','C'), ('5','D'), ('2','H')],
        'expected_output_rank': 'Straight',
        'best_five_cards': 'TH JC QD KS AC'
    },
    "test_case_70": {
        'user_cards': [('2','S'), ('3','H')],
        'community_cards': [('4','D'), ('5','C'), ('A','D'), ('K','H'), ('8','S')],
        'expected_output_rank': 'Straight',
        'best_five_cards': 'AD 2S 3H 4D 5C'
    },
    "test_case_71": {
        'user_cards': [('4','S'), ('5','C')],
        'community_cards': [('3','D'), ('6','H'), ('7','S'), ('Q','C'), ('2','D')],
        'expected_output_rank': 'Straight',
        'best_five_cards': '3D 4S 5C 6H 7S'
    },
    "test_case_72": {
        'user_cards': [('6','S'), ('7','D')],
        'community_cards': [('4','H'), ('5','D'), ('8','C'), ('J','H'), ('2','S')],
        'expected_output_rank': 'Straight',
        'best_five_cards': '4H 5D 6S 7D 8C'
    },
    "test_case_73": {
        'user_cards': [('6','D'), ('8','H')],
        'community_cards': [('5','C'), ('7','S'), ('9','D'), ('K','C'), ('3','H')],
        'expected_output_rank': 'Straight',
        'best_five_cards': '5C 6D 7S 8H 9D'
    },
    "test_case_74": {
        'user_cards': [('7','C'), ('9','S')],
        'community_cards': [('6','H'), ('8','D'), ('T','C'), ('Q','H'), ('4','D')],
        'expected_output_rank': 'Straight',
        'best_five_cards': '6H 7C 8D 9S TC'
    },
    "test_case_75": {
        'user_cards': [('8','H'), ('T','D')],
        'community_cards': [('7','S'), ('9','C'), ('J','H'), ('5','D'), ('2','C')],
        'expected_output_rank': 'Straight',
        'best_five_cards': '7S 8H 9C TD JH'
    },
    
    # Category 6: Flush (15 test cases)
    "test_case_76": {
        'user_cards': [('2','D'), ('3','D')],
        'community_cards': [('6','D'), ('8','D'), ('T','D'), ('5','C'), ('4','S')],
        'expected_output_rank': 'Flush',
        'best_five_cards': '2D 3D 6D 8D TD'
    },
    "test_case_77": {
        'user_cards': [('A','H'), ('7','H')],
        'community_cards': [('3','H'), ('K','H'), ('5','H'), ('2','D'), ('9','S')],
        'expected_output_rank': 'Flush',
        'best_five_cards': 'AH 7H 3H KH 5H'
    },
    "test_case_78": {
        'user_cards': [('4','C'), ('9','C')],
        'community_cards': [('J','C'), ('6','C'), ('8','C'), ('2','H'), ('3','S')],
        'expected_output_rank': 'Flush',
        'best_five_cards': '4C 9C JC 6C 8C'
    },
    "test_case_79": {
        'user_cards': [('5','S'), ('Q','S')],
        'community_cards': [('3','S'), ('9','S'), ('K','S'), ('4','D'), ('2','H')],
        'expected_output_rank': 'Flush',
        'best_five_cards': '5S QS 3S 9S KS'
    },
    "test_case_80": {
        'user_cards': [('8','H'), ('J','H')],
        'community_cards': [('4','H'), ('T','H'), ('Q','H'), ('6','D'), ('2','C')],
        'expected_output_rank': 'Flush',
        'best_five_cards': '8H JH 4H TH QH'
    },
    "test_case_81": {
        'user_cards': [('7','D'), ('T','D')],
        'community_cards': [('2','D'), ('J','D'), ('Q','D'), ('3','S'), ('5','H')],
        'expected_output_rank': 'Flush',
        'best_five_cards': '7D TD 2D JD QD'
    },
    "test_case_82": {
        'user_cards': [('K','C'), ('3','C')],
        'community_cards': [('5','C'), ('6','C'), ('8','C'), ('2','S'), ('4','H')],
        'expected_output_rank': 'Flush',
        'best_five_cards': 'KC 3C 5C 6C 8C'
    },
    "test_case_83": {
        'user_cards': [('2','S'), ('6','S')],
        'community_cards': [('4','S'), ('9','S'), ('T','S'), ('7','D'), ('8','H')],
        'expected_output_rank': 'Flush',
        'best_five_cards': '2S 6S 4S 9S TS'
    },
    "test_case_84": {
        'user_cards': [('3','H'), ('5','H')],
        'community_cards': [('7','H'), ('9','H'), ('K','H'), ('2','C'), ('4','D')],
        'expected_output_rank': 'Flush',
        'best_five_cards': '3H 5H 7H 9H KH'
    },
    "test_case_85": {
        'user_cards': [('T','H'), ('K','H')],
        'community_cards': [('A','H'), ('5','H'), ('8','H'), ('3','C'), ('2','D')],
        'expected_output_rank': 'Flush',
        'best_five_cards': 'TH KH AH 5H 8H'
    },
    
    # Category 7: Full House (15 test cases)
    "test_case_91": {
        'user_cards': [('A','H'), ('A','D')],
        'community_cards': [('A','S'), ('K','H'), ('K','D'), ('3','C'), ('2','S')],
        'expected_output_rank': 'Full House',
        'best_five_cards': 'AH AD AS KH KD'
    },
    "test_case_92": {
        'user_cards': [('Q','S'), ('Q','D')],
        'community_cards': [('Q','H'), ('J','S'), ('J','D'), ('5','C'), ('3','H')],
        'expected_output_rank': 'Full House',
        'best_five_cards': 'QS QD QH JS JD'
    },
    "test_case_93": {
        'user_cards': [('T','C'), ('T','D')],
        'community_cards': [('T','S'), ('9','H'), ('9','D'), ('4','C'), ('2','H')],
        'expected_output_rank': 'Full House',
        'best_five_cards': 'TC TD TS 9H 9D'
    },
    "test_case_94": {
        'user_cards': [('8','H'), ('8','D')],
        'community_cards': [('8','S'), ('K','C'), ('K','D'), ('J','H'), ('3','S')],
        'expected_output_rank': 'Full House',
        'best_five_cards': '8H 8D 8S KC KD'
    },
    "test_case_95": {
        'user_cards': [('7','S'), ('7','D')],
        'community_cards': [('7','H'), ('A','C'), ('A','D'), ('5','S'), ('4','H')],
        'expected_output_rank': 'Full House',
        'best_five_cards': '7S 7D 7H AC AD'
    },
    "test_case_96": {
        'user_cards': [('6','C'), ('6','D')],
        'community_cards': [('6','S'), ('Q','H'), ('Q','D'), ('9','C'), ('3','H')],
        'expected_output_rank': 'Full House',
        'best_five_cards': '6C 6D 6S QH QD'
    },
    "test_case_97": {
        'user_cards': [('5','H'), ('5','D')],
        'community_cards': [('5','S'), ('K','H'), ('K','S'), ('8','C'), ('2','D')],
        'expected_output_rank': 'Full House',
        'best_five_cards': '5H 5D 5S KH KS'
    },
    "test_case_98": {
        'user_cards': [('4','C'), ('4','D')],
        'community_cards': [('4','S'), ('J','H'), ('J','S'), ('A','D'), ('7','C')],
        'expected_output_rank': 'Full House',
        'best_five_cards': '4C 4D 4S JH JS'
    },
    "test_case_99": {
        'user_cards': [('3','H'), ('3','D')],
        'community_cards': [('3','S'), ('T','C'), ('T','D'), ('K','H'), ('9','S')],
        'expected_output_rank': 'Full House',
        'best_five_cards': '3H 3D 3S TC TD'
    },
    "test_case_100": {
        'user_cards': [('2','S'), ('2','D')],
        'community_cards': [('2','H'), ('Q','C'), ('Q','S'), ('8','D'), ('7','H')],
        'expected_output_rank': 'Full House',
        'best_five_cards': '2S 2D 2H QC QS'
    },
    "test_case_101": {
        'user_cards': [('A','C'), ('A','D')],
        'community_cards': [('K','S'), ('K','C'), ('K','D'), ('9','H'), ('4','S')],
        'expected_output_rank': 'Full House',
        'best_five_cards': 'KS KC KD AC AD'
    },
    "test_case_102": {
        'user_cards': [('J','H'), ('J','D')],
        'community_cards': [('J','S'), ('8','C'), ('8','D'), ('5','S'), ('2','H')],
        'expected_output_rank': 'Full House',
        'best_five_cards': 'JH JD JS 8C 8D'
    },
    "test_case_103": {
        'user_cards': [('T','S'), ('T','D')],
        'community_cards': [('T','H'), ('9','C'), ('9','S'), ('4','D'), ('3','C')],
        'expected_output_rank': 'Full House',
        'best_five_cards': 'TS TD TH 9C 9S'
    },
    "test_case_104": {
        'user_cards': [('Q','C'), ('Q','D')],
        'community_cards': [('Q','S'), ('7','H'), ('7','D'), ('5','C'), ('2','S')],
        'expected_output_rank': 'Full House',
        'best_five_cards': 'QC QD QS 7H 7D'
    },
    "test_case_105": {
        'user_cards': [('K','H'), ('K','S')],
        'community_cards': [('K','D'), ('4','C'), ('4','D'), ('9','H'), ('3','S')],
        'expected_output_rank': 'Full House',
        'best_five_cards': 'KH KS KD 4C 4D'
    },
    
    # Category 8: Four of a Kind (15 test cases)
    "test_case_106": {
        'user_cards': [('A','H'), ('A','D')],
        'community_cards': [('A','S'), ('A','C'), ('K','H'), ('3','D'), ('5','C')],
        'expected_output_rank': 'Four of a Kind',
        'best_five_cards': 'AH AD AS AC KH'
    },
    "test_case_107": {
        'user_cards': [('K','H'), ('K','D')],
        'community_cards': [('K','S'), ('K','C'), ('Q','H'), ('7','D'), ('2','C')],
        'expected_output_rank': 'Four of a Kind',
        'best_five_cards': 'KH KD KS KC QH'
    },
    "test_case_108": {
        'user_cards': [('Q','S'), ('Q','C')],
        'community_cards': [('Q','H'), ('Q','D'), ('A','S'), ('4','H'), ('9','D')],
        'expected_output_rank': 'Four of a Kind',
        'best_five_cards': 'QS QC QH QD AS'
    },
    "test_case_109": {
        'user_cards': [('J','H'), ('J','D')],
        'community_cards': [('J','S'), ('J','C'), ('T','S'), ('8','D'), ('3','C')],
        'expected_output_rank': 'Four of a Kind',
        'best_five_cards': 'JH JD JS JC TS'
    },
    "test_case_110": {
        'user_cards': [('T','H'), ('T','D')],
        'community_cards': [('T','S'), ('T','C'), ('K','D'), ('5','H'), ('2','S')],
        'expected_output_rank': 'Four of a Kind',
        'best_five_cards': 'TH TD TS TC KD'
    },
    "test_case_111": {
        'user_cards': [('9','H'), ('9','D')],
        'community_cards': [('9','S'), ('9','C'), ('A','H'), ('7','S'), ('3','D')],
        'expected_output_rank': 'Four of a Kind',
        'best_five_cards': '9H 9D 9S 9C AH'
    },
    "test_case_112": {
        'user_cards': [('8','H'), ('8','D')],
        'community_cards': [('8','S'), ('8','C'), ('K','S'), ('Q','D'), ('5','C')],
        'expected_output_rank': 'Four of a Kind',
        'best_five_cards': '8H 8D 8S 8C KS'
    },
    "test_case_113": {
        'user_cards': [('7','S'), ('7','C')],
        'community_cards': [('7','H'), ('7','D'), ('Q','S'), ('J','H'), ('4','C')],
        'expected_output_rank': 'Four of a Kind',
        'best_five_cards': '7S 7C 7H 7D QS'
    },
    "test_case_114": {
        'user_cards': [('6','H'), ('6','D')],
        'community_cards': [('6','S'), ('6','C'), ('T','D'), ('9','S'), ('2','H')],
        'expected_output_rank': 'Four of a Kind',
        'best_five_cards': '6H 6D 6S 6C TD'
    },
    "test_case_115": {
        'user_cards': [('5','S'), ('5','C')],
        'community_cards': [('5','H'), ('5','D'), ('K','H'), ('8','S'), ('3','C')],
        'expected_output_rank': 'Four of a Kind',
        'best_five_cards': '5S 5C 5H 5D KH'
    },
    "test_case_116": {
        'user_cards': [('4','H'), ('4','D')],
        'community_cards': [('4','S'), ('4','C'), ('A','D'), ('7','H'), ('9','C')],
        'expected_output_rank': 'Four of a Kind',
        'best_five_cards': '4H 4D 4S 4C AD'
    },
    "test_case_117": {
        'user_cards': [('3','H'), ('3','D')],
        'community_cards': [('3','S'), ('3','C'), ('Q','H'), ('8','D'), ('T','S')],
        'expected_output_rank': 'Four of a Kind',
        'best_five_cards': '3H 3D 3S 3C QH'
    },
    "test_case_118": {
        'user_cards': [('2','H'), ('2','D')],
        'community_cards': [('2','S'), ('2','C'), ('K','C'), ('J','D'), ('9','H')],
        'expected_output_rank': 'Four of a Kind',
        'best_five_cards': '2H 2D 2S 2C KC'
    },
    "test_case_119": {
        'user_cards': [('A','H'), ('A','S')],
        'community_cards': [('A','D'), ('A','C'), ('3','H'), ('K','D'), ('7','C')],
        'expected_output_rank': 'Four of a Kind',
        'best_five_cards': 'AH AS AD AC KD'
    },
    "test_case_120": {
        'user_cards': [('9','C'), ('9','D')],
        'community_cards': [('9','H'), ('9','S'), ('4','C'), ('6','H'), ('3','D')],
        'expected_output_rank': 'Four of a Kind',
        'best_five_cards': '9C 9D 9H 9S 6H'
    },
    
        # Category 9: Straight Flush (15 test cases)
        "test_case_121": {
            'user_cards': [('6','H'), ('7','H')],
            'community_cards': [('4','H'), ('5','H'), ('8','H'), ('2','D'), ('9','C')],
            'expected_output_rank': 'Straight Flush',
            'best_five_cards': '4H 5H 6H 7H 8H'
        },
        "test_case_122": {
            'user_cards': [('7','S'), ('8','S')],
            'community_cards': [('5','S'), ('6','S'), ('9','S'), ('3','H'), ('2','D')],
            'expected_output_rank': 'Straight Flush',
            'best_five_cards': '5S 6S 7S 8S 9S'
        },
        "test_case_123": {
            'user_cards': [('3','C'), ('4','C')],
            'community_cards': [('2','C'), ('5','C'), ('6','C'), ('9','H'), ('7','D')],
            'expected_output_rank': 'Straight Flush',
            'best_five_cards': '2C 3C 4C 5C 6C'
        },
        "test_case_124": {
            'user_cards': [('T','D'), ('J','D')],
            'community_cards': [('7','D'), ('8','D'), ('9','D'), ('4','S'), ('2','C')],
            'expected_output_rank': 'Straight Flush',
            'best_five_cards': '7D 8D 9D TD JD'
        },
        "test_case_125": {
            'user_cards': [('T','H'), ('J','H')],
            'community_cards': [('9','H'), ('Q','H'), ('K','H'), ('3','D'), ('2','C')],
            'expected_output_rank': 'Straight Flush',
            'best_five_cards': '9H TH JH QH KH'
        },
        "test_case_126": {
            'user_cards': [('4','S'), ('5','S')],
            'community_cards': [('3','S'), ('6','S'), ('7','S'), ('8','H'), ('2','D')],
            'expected_output_rank': 'Straight Flush',
            'best_five_cards': '3S 4S 5S 6S 7S'
        },
        "test_case_127": {
            'user_cards': [('8','C'), ('9','C')],
            'community_cards': [('6','C'), ('7','C'), ('T','C'), ('Q','D'), ('3','H')],
            'expected_output_rank': 'Straight Flush',
            'best_five_cards': '6C 7C 8C 9C TC'
        },
        "test_case_128": {
            'user_cards': [('5','D'), ('6','D')],
            'community_cards': [('4','D'), ('7','D'), ('8','D'), ('K','S'), ('3','C')],
            'expected_output_rank': 'Straight Flush',
            'best_five_cards': '4D 5D 6D 7D 8D'
        },
        "test_case_129": {
            'user_cards': [('9','H'), ('T','H')],
            'community_cards': [('8','H'), ('J','H'), ('Q','H'), ('2','S'), ('3','D')],
            'expected_output_rank': 'Straight Flush',
            'best_five_cards': '8H 9H TH JH QH'
        },
        "test_case_130": {
            'user_cards': [('2','S'), ('3','S')],
            'community_cards': [('4','S'), ('5','S'), ('6','S'), ('7','D'), ('8','C')],
            'expected_output_rank': 'Straight Flush',
            'best_five_cards': '2S 3S 4S 5S 6S'
        },
        "test_case_131": {
            'user_cards': [('6','C'), ('7','C')],
            'community_cards': [('5','C'), ('8','C'), ('9','C'), ('T','H'), ('2','D')],
            'expected_output_rank': 'Straight Flush',
            'best_five_cards': '5C 6C 7C 8C 9C'
        },
        "test_case_132": {
            'user_cards': [('4','D'), ('5','D')],
            'community_cards': [('3','D'), ('6','D'), ('7','D'), ('K','H'), ('8','S')],
            'expected_output_rank': 'Straight Flush',
            'best_five_cards': '3D 4D 5D 6D 7D'
        },
        "test_case_133": {
            'user_cards': [('7','H'), ('8','H')],
            'community_cards': [('6','H'), ('9','H'), ('T','H'), ('2','C'), ('3','D')],
            'expected_output_rank': 'Straight Flush',
            'best_five_cards': '6H 7H 8H 9H TH'
        },
        "test_case_134": {
            'user_cards': [('9','S'), ('T','S')],
            'community_cards': [('7','S'), ('8','S'), ('J','S'), ('3','H'), ('4','D')],
            'expected_output_rank': 'Straight Flush',
            'best_five_cards': '7S 8S 9S TS JS'
        },
        "test_case_135": {
            'user_cards': [('A','C'), ('2','C')],
            'community_cards': [('3','C'), ('4','C'), ('5','C'), ('8','D'), ('9','H')],
            'expected_output_rank': 'Straight Flush',
            'best_five_cards': 'AC 2C 3C 4C 5C'
        }
}
print(test_cases)
