class Codec:
    delimiter = chr(128)

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return f'{self.delimiter}'.join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split(self.delimiter)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))