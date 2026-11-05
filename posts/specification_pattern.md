TIL: "Specification Pattern"
---

It's good to get a name for a thing. This is a great example of this principle.

In a nutshell, let's create a DSL to capture the business logic.

How it works is clever and functional too.

* https://pypi.org/project/specipy/
* https://github.com/u8slvn/specipy
* https://www.martinfowler.com/apsupp/spec.pdf
* https://github.com/u8slvn/sutoppu
* https://www.youtube.com/watch?v=KqfMiuL3cx4

=== Access via Python DSL ===
shape: (5, 9)
┌──────────┬───────────┬───────────┬───────────┬───┬───────────┬───────────┬───────────┬───────────┐
│ is_admin ┆ is_active ┆ account_a ┆ is_banned ┆ … ┆ credit_sc ┆ has_manua ┆ api_check ┆ api_check │
│ ---      ┆ ---       ┆ ge        ┆ ---       ┆   ┆ ore       ┆ l_overrid ┆ ---       ┆ 2         │
│ bool     ┆ bool      ┆ ---       ┆ bool      ┆   ┆ ---       ┆ e         ┆ bool      ┆ ---       │
│          ┆           ┆ i64       ┆           ┆   ┆ i64       ┆ ---       ┆           ┆ bool      │
│          ┆           ┆           ┆           ┆   ┆           ┆ bool      ┆           ┆           │
╞══════════╪═══════════╪═══════════╪═══════════╪═══╪═══════════╪═══════════╪═══════════╪═══════════╡
│ true     ┆ false     ┆ 1         ┆ false     ┆ … ┆ 100       ┆ false     ┆ true      ┆ true      │
│ false    ┆ true      ┆ 40        ┆ false     ┆ … ┆ 700       ┆ false     ┆ true      ┆ true      │
│ false    ┆ true      ┆ 40        ┆ false     ┆ … ┆ 500       ┆ true      ┆ true      ┆ true      │
│ false    ┆ true      ┆ 5         ┆ false     ┆ … ┆ 900       ┆ false     ┆ false     ┆ false     │
│ false    ┆ false     ┆ 100       ┆ true      ┆ … ┆ 900       ┆ false     ┆ false     ┆ false     │
└──────────┴───────────┴───────────┴───────────┴───┴───────────┴───────────┴───────────┴───────────┘
