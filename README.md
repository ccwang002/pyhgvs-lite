## PyHGVS-lite
A Python parser for HGVS names using [Lark] and EBNF grammar.
Its goal is to achieve efficient parsing LALR(1) and works on pypy 3+ as well.


The package is heavily inspired by the following works:

- [biocommons/hgvs] HGVS grammar ([`hgvs.pymeta`]) under Apache License 2.0


Other existing works:

- <https://github.com/counsyl/hgvs/>
- <https://github.com/mutalyzer/hgvs-parser>


[Lark]: https://github.com/lark-parser/lark
[biocommons/hgvs]: https://github.com/biocommons/hgvs/
[`hgvs.pymeta`]: https://github.com/biocommons/hgvs/blob/1d5a47fd0ac2c657510077d672a369469e05256d/hgvs/_data/hgvs.pymeta
