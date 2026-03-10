TIL how to learn about a new codebase quickly.
---

Obviously we're using LLMs these days, but what's the best way?

As usual Simon Willison had a good suggestion: https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/

Here's the prompt:

```markdown
Read the source and then plan a linear walkthrough of the code that explains how it all works in detail

Then run “uvx showboat –help” to learn showboat - use showboat to create a 'walkthrough.md' file in the repo and build the walkthrough in there, using showboat note for commentary and showboat exec 
plus sed or grep or cat or whatever you need to include snippets of code you are talking about.

Use copious mermaid diagrams especially for entity relationships and database schemas. Include this exact prompt in the introduction of the 'walkthrough.md' file, along with a table of contents 
and the date of generation.

```

Note some additions to the prompt. The basic prompt however, I've found works really well.


Next concept: Given this unfamiliar codebase: I want an idea of where the bugs might be! So can we use the same concept to run a cyclometic complexity analysis along with some other interesting 
metrics? 
Say: What files are changed frequently? Code hotspots are a problem: Hidden bugs are likely to cluster near resolved ones! (https://medium.com/@ryan.craven.qa/defect-clustering-explained-63f0b5ec0a1e)

ruff apparently has https://docs.astral.sh/ruff/rules/#mccabe-c90 , so I'll try that.