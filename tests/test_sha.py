from hashes import sha


def test_sha256():
    text = "abc"
    _hash = sha.SHA256(text)

    assert _hash.text == "abc"
    assert _hash.h == [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]
    assert _hash == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    assert _hash.hash == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"

