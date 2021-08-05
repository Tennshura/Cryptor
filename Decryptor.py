import random as rnd
import string as st

"""
Author: Dylan Wade
Date: 03-Aug-2021

Seeded Decryptor: Goal is to allow a user to input an encrypted string
with its corresponding seed from the paired encryptor and return the
decrypted information.
"""

class SeededDecryptor:
    def __init__(self, seed, enc_string):
        self.seed = seed
        self.enc_string = enc_string
        self.out_string = self.enc_string
        # initiate rng using provided seed and determines encryption values
        rnd.seed(self.seed)
        self.enc_1 = rnd.randint(1, 2)
        self.enc_2 = rnd.randint(0, 10)
        self.shuffle_seed_2 = rnd.randint(1, 99999)
        self.shuffle_seed_3 = rnd.randint(1, 999999)
        # saves rng state to reset post string shuffle
        self.shuffle_reset_state = rnd.getstate()

    def state_reset(self):
        # function to reset rng state
        rnd.setstate(self.shuffle_reset_state)

    def first_decryption(self):
        # determines whether or not the string was reversed
        if self.enc_1 == 1:
            None
        else:
            self.out_string = self.out_string[::-1]

    def second_decryption(self):
        # determines whether or not string was shuffled
        if self.enc_2 == 0:
            None
        else:
            # first we make a list out of the partially decrypted string
            # and recreate the parameters we used to break
            # the initial string into pieces in the encryptor
            out_list = list(self.out_string)
            string_length = len(self.out_string)
            if int(len(self.enc_string) / self.enc_2) != 0:
                chunk_size = int(len(self.enc_string) / self.enc_2)
            else:
                chunk_size = 1
            # creates a list with a digit corresponding to each
            # letter in the string
            shuf_index = [i for i in range(0, string_length)]
            # takes that list and seperates it using the
            # same parameters as encryptor
            index_sep = [
                shuf_index[i : i + chunk_size]
                for i in range(0, string_length, chunk_size)
            ]
            # shuffles it with the same seed that the encryptor uses
            rnd.seed(self.shuffle_seed_2)
            rnd.shuffle(index_sep)
            # rejoins as one wholly inclusive list.
            deshuffle_index = sum(index_sep, [])
            # now we have a list of numbers, with each number corresponding
            # to the original index of the character before the string was
            # shuffled during encryption
            self.state_reset()
            # zips the list of characters in the encrypted string with the list
            # of the original character indexes and then sorts the list by index
            # creating an unshuffle list
            out_list = [char for index, char in sorted(zip(deshuffle_index, out_list))]
            self.out_string = "".join(out_list)

    def third_decryption(self):
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
        # sets the seed, shuffles my decryption list into the
        # same order as the encryprion list, and then resets rng
        rnd.seed(self.shuffle_seed_3)
        rnd.shuffle(trans_list)
        self.state_reset()
        trans_set = "".join(trans_list)
        # makes the decryption table in the
        # reverse order as the encryption table
        decrypt_table = str.maketrans(trans_set, ascii_cl)
        # translates the final decrypted string
        self.out_string = self.out_string.translate(decrypt_table)

    def run_decryption(self):
        self.third_decryption()
        self.second_decryption()
        self.first_decryption()
        return self.out_string
    
    def test(self):
        return self.run_decryption()
    

if __name__ == "__main__":
    test_dec = SeededDecryptor("Seed1","qO^¦B‡dœ0#»²œ1OB")
    print(test_dec.test())
