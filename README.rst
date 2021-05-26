# cryptography

A repo that implements cryptographic functions

Current supported algorithms
----------------------------

- None


This is an example of how the algorithm works
(Not implemented yet)

.. code:: py

  from hashes import SHA256
  
  text = "abc"
  h = SHA256(text)
  
  >>> print(h)
  'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'
  

**Disclaimer: This shouldn't be considered a production ready package, so unly use it in experimental ways**
