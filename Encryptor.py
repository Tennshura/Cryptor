import random as rnd
import string as st

"""
Author: Dylan Wade
Date: 03-Aug-2021

Seeded Encryptor: Goal is to allow a user to input a string and seed in
order to securely encrypt information. By feeding the encrypted seed
and exact string to the paired Decryptor one could retrieve the
information.
"""

class SeededEncryptor:
    def __init__(self, seed, raw_string):
        self.seed = seed
        self.raw_string = raw_string
        self.enc_string = raw_string
        # initiate rng using provided seed and determines encryption values
        rnd.seed(self.seed)
        self.enc_1 = rnd.randint(1, 2)
        self.enc_2 = rnd.randint(0, 10)
        self.shuffle_seed_2 = rnd.randint(1, 99999)
        self.shuffle_seed_3 = rnd.randint(1, 999999)
        # saves rng state to reset if string is shuffled
        self.shuffle_reset_state = rnd.getstate()

    def state_reset(self):
        # function to reset rng state
        rnd.setstate(self.shuffle_reset_state)

    def first_encryption(self):
        # determines whether or not string gets reversed
        if self.enc_1 == 1:
            None
        else:
            self.enc_string = self.enc_string[::-1]

    def second_encryption(self):
        # determines if string will be broken into pieces and shuffled
        if self.enc_2 == 0:
            None
        else:
            string_length = len(self.enc_string)
            # prevents chunk_size from being zero, which would break the
            # string seperator's range function
            if int(len(self.enc_string) / self.enc_2) != 0:
                chunk_size = int(len(self.enc_string) / self.enc_2)
            else:
                chunk_size = 1
            # one line function to break string into pieces based on 'chunk_size'
            string_sep = [
                self.enc_string[i : i + chunk_size]
                for i in range(0, string_length, chunk_size)
            ]
            # sets rng seed and then shuffles the piecemeal string
            rnd.seed(self.shuffle_seed_2)
            rnd.shuffle(string_sep)
            # joins together the new string and resets the
            # rng to its previous state
            self.enc_string = "".join(string_sep)
            self.state_reset()

    def third_encryption(self):
        # conducts character substitution on string
        # create a list of all printable ascii characters using string module
        ascii_cl = st.printable
        # self created list of random ascii characters (including extended
        # ascii)
        trans_set = ""
        trans_list = [
            "!",
            "¿",
            "Q",
            "a",
            "¢",
            "µ",
            "z",
            "Œ",
            "@",
            "s",
            "®",
            "x",
            "¾",
            "#",
            "E",
            "×",
            "d",
            "ƒ",
            "±",
            "$",
            "R",
            "f",
            "v",
            "1",
            "œ",
            "q",
            "»",
            "Ý",
            "Z",
            "2",
            "²",
            "Ð",
            "€",
            "ÿ",
            "S",
            "X",
            "¼",
            "3",
            "D",
            "C",
            "¶",
            "4",
            "r",
            "V",
            "5",
            "æ",
            "6",
            "§",
            "t",
            "h",
            "‡",
            "n",
            "B",
            "ø",
            "N",
            "H",
            "¤",
            "G",
            "^",
            "%",
            "7",
            "¬",
            "i",
            "j",
            "k",
            ",",
            "m",
            "½",
            "<",
            "K",
            "J",
            "U",
            "*",
            "&",
            "0",
            "©",
            "p",
            "£",
            "o",
            "l",
            ";",
            "ð",
            "/",
            ".",
            "Ç",
            "¦",
            "?",
            ":",
            "O",
            "Ø",
            "P",
            ")",
            "(",
            "=",
            "]",
            "[",
            "'",
            "}",
            "+",
            "_",
        ]
        # sets the seed, shuffles my encryption list, and then resets rng
        rnd.seed(self.shuffle_seed_3)
        rnd.shuffle(trans_list)
        self.state_reset()
        trans_set = "".join(trans_list)
        # makes a table to be used for the translation function that
        # maps all ascii characters to a pseudorandom character from the trans_list
        enc_table = str.maketrans(ascii_cl, trans_set)
        # translates the final encrypted
        self.enc_string = self.enc_string.translate(enc_table)

    def run_encryption(self):
        self.first_encryption()
        self.second_encryption()
        self.third_encryption()
        return self.enc_string
    
    def test(self):
        # short code to test the encryptor with step by step output
        return self.run_encryption()
    

if __name__ == "__main__":
    test_enc = SeededEncryptor("Seed1","Encryption Data!")
    print(test_enc.test())
