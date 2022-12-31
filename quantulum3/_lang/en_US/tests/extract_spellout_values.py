import unittest

from ..parser import extract_spellout_values

TEST_CASES = [
    ("one hundred and five", ["105.0"]),
    ("a million", ["1000000.0"]),
    ("a million and one", ["1000001.0"]),
    ("million", ["1000000.0"]),
    ("million and one", ["1000001.0"]),
    ("one hundred million", ["100000000.0"]),
    ("one hundred and five million", ["105000000.0"]),
    ("half", ["0.5"]),
    ("two and a half", ["2.5"]),
    ("two and a half million", ["2500000.0"]),
    ("twenty six million and seventy two hundred", ["26007200.0"]),
    ("twenty", ["20.0"]),
    ("zero", ["0.0"]),
    ("several hundred years", []),
    ("Zero is a small number.", ["0.0", "1.0"]),
    ## some "and a half" corner cases
    ("a million and a half", ["1500000.0"]),  # corner case
    ("twenty million and a half", ["20500000.0"]),  # corner case
    ("twenty billion and a half", ["20500000000.0"]),  # corner case
    ("twenty trillion and a half", ["20500000000000.0"]),  # corner caes
    ("two hundred and a half", ["200.5"]),  # default case
    ## number splitting
    ("twenty thirty fifty hundred", ["20.0", "30.0", "5000.0"]),
    ("one, two, three", ["1.0", "2.0", "3.0"]),
    ("twenty five thirty six one hundred", ["25.0", "36.0", "100.0"]),
    ("hundred and five hundred and six", ["105.0", "106.0"]),  # this is ambiguous..
    ("hundred and five twenty two", ["105.0", "22.0"]),
    ("hundred and five twenty two million", ["105.0", "22000000.0"]),
]


class ExtractSpellout(unittest.TestCase):
    def test_training(self, lang="en_US"):
        """Test extraction and conversion of spellout numbers from text"""
        self.assertEqual(lang, "en_US")
        for input, expected in TEST_CASES:
            output = [v["new_surface"] for v in extract_spellout_values(input)]
            self.assertEqual(output, expected)


###############################################################################
if __name__ == "__main__":  # pragma: no cover

    unittest.main()
