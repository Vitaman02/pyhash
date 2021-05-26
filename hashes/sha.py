class SHA256:
    def __init__(self, text: str):
        if not isinstance(text, str):
            raise ValueError("Can only accept type 'str'.")

        self.text = text
        self.binary_string = self.to_bin(self.text)
        self.hash = self.get_hash(self.text)

        # Hard-coded hash values
        # These are the first primary numbers
        self.h = [
            0x6a09e667, 0xbb67ae85,
            0x3c6ef372, 0xa54ff53a,
            0x510e527f, 0x9b05688c,
            0x1f83d9ab, 0x5be0cd19
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
            out.append(val)
        
        # TODO
        # Appends extra '0' bits to the end
        padded = self.pad("".join(out))
        # out.append("10000000")
        # length += 8
        
        
        return 
            
    def __str__(self):
        return f"<{self.__class__.__name__}: text='{self.text}' bin={self.binary_string}>"

    def __repr__(self):
        return self.__str__()

