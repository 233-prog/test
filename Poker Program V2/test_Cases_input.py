test_cases = {
    "test_case_1": {
        "user_cards": [("A", "H"), ("K", "D")],
        "community_cards": [("Q", "H"), ("J", "H"), ("T", "H")],
        "expected_output": "Valid input"
    },
    "test_case_2": {
        "user_cards": [("1", "H"), ("K", "D")],
        "community_cards": [("Q", "H"), ("J", "H"), ("T", "H")],
        "expected_output": "Invalid format pls recheck."
    },
    "test_case_3": {
        "user_cards": [("Q", "C"), ("10", "D")],
        "community_cards": [("Q", "H"), ("J", "H"), ("T", "H")],  
        "expected_output": "Invalid card format in user cards"
    },
    "test_case_4": {
        "user_cards": [("A", "H"), ("K", "X")],
        "community_cards": [("Q", "H"), ("J", "H"), ("T", "H")],
        "expected_output": "Invalid suit in user cards"
    },
    "test_case_5": {
        "user_cards": [("A", "H"), ("A", "H")],
        "community_cards": [("Q", "H"), ("J", "H"), ("T", "H")],
        "expected_output": "Duplicate cards in user input"
    },
    "test_case_6": {
        "user_cards": [("A", "H"), ("K", "D")],
        "community_cards": [("Q", "H"), ("K", "D"), ("T", "H")],
        "expected_output": "Duplicate cards across inputs"
    },
    "test_case_7": {
        "user_cards": [("A", "H"), ("K", "D"), ("Q", "H")],
        "community_cards": [("J", "H"), ("T", "H"), ("9", "H")],
        "expected_output": "Invalid number of user cards"
    },
    "test_case_8": {
        "user_cards": [("A", "H")],
        "community_cards": [("K", "D"), ("Q", "H"), ("J", "H")],
        "expected_output": "Invalid number of user cards"
    },
    "test_case_9": {
        "user_cards": [("A", "H"), ("K", "D")],
        "community_cards": [("Q", "H"), ("J", "H")],
        "expected_output": "Invalid number of community cards"
    },
    "test_case_10": {
        "user_cards": [("A", "H"), ("K", "D")],
        "community_cards": [("Q", "H"), ("J", "H"), ("T", "H"), ("9", "H"), ("8", "H"), ("7", "H")],
        "expected_output": "Invalid number of community cards"
    },
    "test_case_11": {
        "user_cards": [("A", "H"), ("K", "D")],
        "community_cards": [],
        "expected_output": "Valid input"
    },
    "test_case_12": {
        "user_cards": [("2", "C"), ("3", "D")],
        "community_cards": [("4", "H"), ("5", "H"), ("6", "H"), ("7", "H")],
        "expected_output": "Valid input"
    },
    "test_case_13": {
        "user_cards": [("2", "C"), ("3", "D")],
        "community_cards": [("4", "H"), ("5", "H"), ("6", "H"), ("7", "H"), ("8", "H")],
        "expected_output": "Valid input"
    },
    "test_case_14": {
        "user_cards": [("A", "H"), ("K", "D")],
        "community_cards": [("Q", "H"), ("J", "H"), ("10", "H")],
        "expected_output": "Invalid card format in community cards"
    },
    "test_case_15": {
        "user_cards": [("A", "H"), ("K", "D")],
        "community_cards": [("Q", "H"), ("1", "H"), ("J", "H")],
        "expected_output": "Invalid rank in community cards"
    },
    "test_case_16": {
        "user_cards": [("A", "H"), ("K", "D")],
        "community_cards": [("Q", "X"), ("J", "H"), ("T", "H")],
        "expected_output": "Invalid suit in community cards"
    },
    "test_case_17": {
        "user_cards": [("a", "h"), ("K", "D")],
        "community_cards": [("Q", "H"), ("J", "H"), ("T", "H")],
        "expected_output": "Invalid card format in user cards"
    },
    "test_case_18": {
        "user_cards": [("A", "H"), ("K", "D")],
        "community_cards": [("q", "h"), ("J", "H"), ("T", "H")],
        "expected_output": "Invalid card format in community cards"
    },
    "test_case_19": {
        "user_cards": [("Q", "S"), ("J", "D")],
        "community_cards": [("T", "C"), ("9", "H"), ("8", "S")],
        "expected_output": "Valid input"
    },
    "test_case_20": {
        "user_cards": [("2", "H"), ("3", "D")],
        "community_cards": [("4", "S"), ("5", "C"), ("6", "H")],
        "expected_output": "Valid input"
    },
    "test_case_21": {
        "user_cards": [("2H", "H"), ("3", "D")],
        "community_cards": [("4", "S"), ("5", "C"), ("6", "H")],
        "expected_output": "Invalid card format in user cards"
    },
    "test_case_22": {
        "user_cards": [("2", "H"), ("3", "D")],
        "community_cards": [("4",), ("5", "C"), ("6", "H")],
        "expected_output": "Invalid card format in community cards"
    },
    "test_case_23": {
        "user_cards": [("A", "H"), ("K", "D")],
        "community_cards": [("Q", "H"), ("Q", "H"), ("J", "H")],
        "expected_output": "Duplicate cards detected. Please enter unique cards."
    },
    "test_case_24": {
        "user_cards": [("A", "H"), ("K", "D")],
        "community_cards": [("Q", "H"), ("A", "H"), ("J", "H")],
        "expected_output": "Duplicate cards across inputs"
    },
    "test_case_25": {
        "user_cards": [("T", "C"), ("9", "C")],
        "community_cards": [("8", "C"), ("7", "C"), ("6", "C")],
        "expected_output": "Valid input"
    },
    "test_case_26": {
        "user_cards": [("1", "S"), ("9", "C")],
        "community_cards": [("8", "C"), ("7", "C"), ("6", "C")],
        "expected_output": "Invalid rank in user cards"
    },
    "test_case_27": {
        "user_cards": [("T", "X"), ("9", "C")],
        "community_cards": [("8", "C"), ("7", "C"), ("6", "C")],
        "expected_output": "Invalid suit in user cards"
    },
    "test_case_28": {
        "user_cards": [("A", "H"), ("K", "D")],
        "community_cards": [("1", "D"), ("Q", "D"), ("J", "D")],
        "expected_output": "Invalid rank in community cards"
    },
    "test_case_29": {
        "user_cards": [("A", "H"), ("K", "D")],
        "community_cards": [("Q", "Z"), ("J", "D"), ("T", "H")],
        "expected_output": "Invalid suit in community cards"
    },
    "test_case_30": {
        "user_cards": [("A", "H"), ("K", "D")],
        "community_cards": [("Q", "H"), ("J", "H"), ("T", "H"), ("9", "H"), ("8", "H"), ("7", "H"), ("6", "H")],
        "expected_output": "Invalid number of community cards"
    },
    "test_case_31": {
        "user_cards": [("A", "H"), ("K", "D")],
        "community_cards": [("Q", "H")],
        "expected_output": "Invalid number of community cards"
    },
    "test_case_32": {
        "user_cards": [("J", "H"), ("T", "C")],
        "community_cards": [("9", "S"), ("8", "D"), ("7", "C")],
        "expected_output": "Valid input"
    },
    "test_case_33": {
        "user_cards": [("J", "H"), ("T", "C")],
        "community_cards": [("9", "S"), ("8", "D"), ("7", "C"), ("6", "H"), ("5", "D")],
        "expected_output": "Valid input"
    },
    "test_case_34": {
        "user_cards": [("4", "H"), ("5", "H")],
        "community_cards": [],
        "expected_output": "Valid input"
    },
    "test_case_35": {
        "user_cards": [("4", "H"), ("5", "H")],
        "community_cards": [("6", "H"), ("7", "H"), ("8", "H"), ("9", "H")],
        "expected_output": "Valid input"
    },
    "test_case_36": {
        "user_cards": [("4", "H"), ("5", "H")],
        "community_cards": [("6", "H"), ("7", "H"), ("8", "H"), ("8", "H")],
        "expected_output": "Duplicate cards detected. Please enter unique cards."
    },
    "test_case_37": {
        "user_cards": [(), ("K", "D")],
        "community_cards": [("Q", "H"), ("J", "H"), ("T", "H")],
        "expected_output": "Invalid card format in user cards"
    },
    "test_case_38": {
        "user_cards": [("A", "H"), ("K", "D")],
        "community_cards": [("Q", "H"), (), ("J", "H")],
        "expected_output": "Invalid card format in community cards"
    },
    "test_case_39": {
        "user_cards": [("A ", "H"), ("K", "D")],
        "community_cards": [("Q", "H"), ("J", "H"), ("T", "H")],
        "expected_output": "Invalid card format in user cards"
    },
    "test_case_40": {
        "user_cards": [("A", "H"), ("K", "D")],
        "community_cards": [("Q ", "H"), ("J", "H"), ("T", "H")],
        "expected_output": "Invalid card format in community cards"
    },
    "test_case_41": {
        "user_cards": [("10", "H"), ("K", "D")],
        "community_cards": [("Q", "H"), ("J", "H"), ("T", "H")],
        "expected_output": "Invalid card format in user cards"
    },
    "test_case_42": {
        "user_cards": [("A", "H"), ("K", "D")],
        "community_cards": [("10", "H"), ("J", "H"), ("T", "H")],
        "expected_output": "Invalid card format in community cards"
    },
    "test_case_43": {
        "user_cards": [("2", "H"), ("3", "D")],
        "community_cards": [("4", "S"), ("5", "C"), ("6", "H")],
        "expected_output": "Valid input"
    },
    "test_case_44": {
        "user_cards": [("A", "S"), ("A", "H")],
        "community_cards": [("A", "D"), ("A", "C"), ("K", "D")],
        "expected_output": "Valid input"
    },
    "test_case_45": {
        "user_cards": [("A", "H"), ("K", "D")],
        "community_cards": [("Q", "H"), ("J", "1"), ("T", "H")],
        "expected_output": "Invalid suit in community cards"
    },
    "test_case_46": {
        "user_cards": [("9", "H"), ("8", "H")],
        "community_cards": [("7", "H"), ("6", "H"), ("5", "X")],
        "expected_output": "Invalid suit in community cards"
    },
    "test_case_47": {
        "user_cards": [("2", "S"), ("3", "H")],
        "community_cards": [("4", "D"), ("5", "C"), ("6", "S")],
        "expected_output": "Valid input"
    },
    "test_case_48": {
        "user_cards": [("A", "H"), ("K", "D")],
        "community_cards": [(" Q", "H"), ("J", "H"), ("T", "H")],
        "expected_output": "Invalid card format in community cards"
    },
    "test_case_49": {
        "user_cards": [("A", "H"), ("K", "D")],
        "community_cards": [("Q", "H"), ("J", "H"), ("TH", "\n")],
        "expected_output": "Invalid card format in community cards"
    },
    "test_case_50": {
        "user_cards": [("J", "S"), ("Q", "C")],
        "community_cards": [("K", "D"), ("T", "H"), ("9", "S")],
        "expected_output": "Valid input"
    }
}

print(test_cases)
