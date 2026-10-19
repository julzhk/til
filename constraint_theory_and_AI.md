TIL That knowing (and applying!) the theory of constraints with AI is obviously hard, or we'd all be doing it.
--

My current thoughts is that AI is really good at prototyping and version one - when the scope are tightly managed and simple. 

And the reason this type of development is so quick and satisfying is that the process is just simpler and smoother: ideas -> prompts -> AI code generation -> Do we like it?

If it's just me as a solo developer, then the slowest phase in the process might be coming up with the ideas, which is the source of the intoxicating 'AI mania' (the new subset of AI 
psychosis that's going 
around). And this manic point-of-view makes developing look 'solved'. 

However, in a more mature project, this isn't how developers work at all and these speed-ups aren't so obviously observed.

_"What grew ... was the wait. A pull request used to take about seven days to merge, and with agents ... it took about ten and a half.
"_ [Source: we still ship the same amount, why?](https://galratner.substack.com/p/thank-you-for-mandating-ai-we-still) 

More observations from that source:

* The researchers estimate that engineers spend between about a third of their time actually writing code and the rest of the time reviewing, planning and in meetings.
* The time from opening a pull request to merging rose 49 percent. Before AI adoption reviewers requested changes on about one pull request in eight. After, it was closer to one in four.
* Moving people into code review can clear a productivity bottleneck. A quality bottleneck will only clears when the [AI] technology gets better.

And this observation correllates to my personal experience: With AI the code review process becomes a lot more tricky: A human didn't write the code so it's not got the affordances and 'architectural 
characteristics' 
that a human-written code should have: we should care about maintainability, future extensibility, modularity / composability / reusability. And as a code reviewer I might reject code that's 
repetitive (eg not DRY.) of course, the AI doesn't really get those NFR qualities. So it requires more time to appraise and even takes a second opinion, soaking up yet more time. It's stressful to 
reject code that ostensibly 'works' yet isn't going to make our project worse in the medium or longer term. Maybe we should be adding NFRs into the prompts - but I doubt this would work (`'use DRY principles and don't make mistakes'` ) 

Lean manufacturing and '[theory of constraints](http://focusandleverage.blogspot.com/2015/03/focus-and-leverage-part-410.html)' would predict this of course: By speeding up one phase that's not the critical bottleneck , all that happens is that downstream processes become 
overloaded - and even slower!

Lean would also have comments about speed-ups making 'quality' issues harder, worse and in all ways more difficult. But that's another story.