TIL About Architecture Decision Records
---

I hold a weekly mentoring session and this week the topic of 'ADR' came up. I've had experience with them of course but this gave me the opportunity to dive into them a bit more deeply; this is 
why I like mentoring: it's a two-way street.

## What are ADRs?

When I want to learn something new my first stop is [O'Reilly](https://www.oreilly.com). I like to 
go back to the original sources or at least a measured and thoughtful introduction to the topic.

So here's my references: [Facilitating software architecture](https://learning.oreilly.com/library/view/facilitating-software-architecture/9781098151850/ch06.html#ch06_introducing_architecture_decision_records_1728364283183110) has a good chapter on ADRs.
  In this case the [source](https://personal.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf) is brief and sensible: 

>[Previous Developers]... mostly had good intentions and did what
seemed right in the moment. The decisions
made sense under the circumstances, which
cost and schedule constrained. 
> 
>However, looking back, after the dust has settled and the original system designers are long gone, we have
no context around these decisions; we have no
history. All we can do is shake our heads in disbelief. In the end, as Gustave Flaubert reportedly wrote in 1871, “Our ignorance of history
causes us to slander our own times.”

Nice to see a pithy literary quote in a technical article!

## Observations

As usual when looking back at source materials, there's insights that are not obvious. In this case: 
* ADR are immutable
* ADRs conclusions need to be shared
* They should be short - a couple of pages max

> Once the team reaches a final architectural
decision, they’ll need to “socialize” the result — that is, convince the rest of the organization that they’ve chosen appropriately. 
* todo: More to follow. 

## What deserves an ADR?

It's tempting to make everything worthy of an ADR - then (apparently) it's called an 'All Decision Record' - which is _possibly_ useful but probably onerous and for CYA rather than sharing & 
learning.

However: there is a standard answer to architectural questions : 'It depends'. Using this it gives a suggestion on when an ADR should be created: eg: whenever there's a choice. If there's no 
trade-offs 
it's 
not an 
architectural decision; thus no documentation. If it's a decision that posterity might want insight on, then make it an ADR!

