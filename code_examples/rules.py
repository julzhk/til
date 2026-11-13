import polars as pl
from typing import Collection
from dataclasses import dataclass



@dataclass
class User:
    is_admin: bool
    is_active: bool
    account_age: int
    is_banned: bool
    country: str
    credit_score: int
    has_manual_override: bool

is_admin = pl.col("is_admin")
is_active = pl.col("is_active")
is_banned = pl.col("is_banned")
has_override = pl.col("has_manual_override")

def account_older_than(days: int) -> pl.Expr:
    return pl.col("account_age") > days

def from_country(countries: Collection[str]) -> pl.Expr:
    return pl.col("country").is_in(countries)

def credit_score_above(threshold: int) -> pl.Expr:
    return pl.col("credit_score") > threshold



is_admin = pl.col("is_admin")
is_active = pl.col("is_active")
is_banned = pl.col("is_banned")
has_override = pl.col("has_manual_override")
def account_older_than(days: int) -> pl.Expr: 
    return pl.col("account_age") > days

api_check1 = is_admin | (
    is_active
    & account_older_than(30)
)

api_check2 = is_admin | (
    is_active
    & account_older_than(30)
    & ~is_banned
    & from_country(["NL", "BE"])
    & (credit_score_above(650) | has_override)
)


def main() -> None:
    users = [
        User(True, False, 1, False, "US", 100, False),
        User(False, True, 40, False, "NL", 700, False),
        User(False, True, 40, False, "BE", 500, True),
        User(False, True, 5, False, "NL", 900, False),
        User(False, False, 100, True, "NL", 900, False),
    ]

    print("=== Access via Python DSL ===")
    df = pl.DataFrame(users)
    print(df.with_columns(
        api_check1.alias("api_check"),
        api_check2.alias("api_check2")
        )
    )
    
if __name__ == "__main__":
    main()
    
"""
The Specification Pattern is essentially an embedded DSL for Boolean logic, 
but the underlying structure naturally generalizes further.
The pattern composes predicates (a -> Bool) using and/or/not, which is fine for simple cases.
 But the same compositional structure could support first-order predicate logic with implicit 
 quantification, unification, and backtracking - essentially Horn clauses.

Horn clauses give you decidable proof search (SLD resolution), a computational fixed point 
(the guaranteed minimal Herbrand model), and nice algebraic properties: monotonicity 
(new facts don't invalidate old ones), clean composition (programs combine by union in a well-behaved manner),
 and stratification (layered definitions).
This isn't theoretical wankery - it means your specifications become relations that yield bindings,
 not just true/false. In addition to questions like is_premium(customer) and 
 not is_delinquent(customer), you can also run queries like find(X) where premium(X) 
 
 and owes(X, Amount) and Amount < threshold.
The OO pattern works for Boolean queries, but if you need richer expressiveness,
 the logic programming approach is already there - same compositional foundation, 
 more powerful evaluation semantics. And you can embed Horn clauses in Python. 
 It's a bit more elaborate than simple Boolean (propositional) logic, but it's doable
 . I know it's doable because I've done it. And the extra complexity pays for itself 
 when you're modeling search, constraints, or any problem that's naturally relational
  rather than just filtering.

Happy to discuss the embedding approach if anyone's curious about the implementation."""