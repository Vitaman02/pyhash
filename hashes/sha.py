import sys
import struct


class SHA256:
    def __init__(self, text: str):
        if not isinstance(text, str):
            raise ValueError("Can only accept type 'str'.")

        self.text = text
        self.binary_string = self.to_bin(self.text)
        # self.hash = self.get_hash(self.text)

        # Hard-coded hash values
        # These are the first primary numbers
        self.h = [
            0x6a09e667, 0xbb67ae85,
            0x3c6ef372, 0xa54ff53a,
            0x510e527f, 0x9b05688c,
            0x1f83d9ab, 0x5be0cd19
        ]

        # Hard-coded constants
        # These are the cube roots of the first 64 primes
        self.k = [
            0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
            0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
            0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
            0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
            0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
            0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
            0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
            0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
            0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
            0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
            0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
            0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
            0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
            0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
            0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
            0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
        ]

    def to_bin(self, text: str) -> str:
        """Converts the text to a binary string

        Parameters
        ----------
        text: str
            The text to convert to binary
        """
        out = []
        for char in text:
            val = f"{ord(char):8b}"
            out.append(val.strip())
        
        # Append a 1 with the padded zeros
        out.append("10000000")

        # Appends extra '0' bits to the end
        padded = self.pad(out)        
        
        return "".join(padded)
    
    def pad(self, bits: list) -> list:
        """Pads a list of bits with 0s

        The list of bits is assummed to be less than 512 bits.

        Parameters
        ----------
        bits: List[str]
            A list of bits with the message to hash.
        
        Returns
        -------
        list:
            A list with padded 0s at the end and the big-endian integer representing
            the original input in binary.
        """
        
        # Get message length
        message_length = len(bits) * 8 - 8

        # There should be 56 8bit strings in the list [ (512 - 64) / 8 ]
        # So to append the bits we need to find how many we need to append
        padding = 56 - len(bits)
        bits += ["00000000"] * padding

        # We also need to append 64 big-endian bits with the length of the message
        # First we need to get the bit value of the length
        bit_message_length = f"{message_length:64b}".replace(" ", "")

        # And then add missing 0s
        last_64 = bit_message_length.zfill(64)

        # Then convert to a list of 8bit values
        chunk = 8
        last_64_list = [last_64[i:i+chunk] for i in range(0, len(last_64), chunk)]

        return bits + last_64_list

    def __str__(self):
        return f"<{self.__class__.__name__}: text='{self.text}'>"

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    key = "hello world"
    hash = SHA256(key)
    print(hash.binary_string)