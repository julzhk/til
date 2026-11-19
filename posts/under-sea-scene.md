TIL About two demos and a digression about LLMs and diagrams
--

This started out as a 'gosh these two demos are nice' and I got distracted into something about communicating concepts with diagrams. 

---

This demo is quite amazing. Dreamy even: [abyssal-garden](https://noniv.github.io/abyssal-garden/)
& the source (via hacker news) : https://github.com/Noniv/abyssal-garden

Is this edifying or instructional? Not really - I guess shaders are a complex and interesting niche I'd like to look at one day.

--- 
And update (so I don't forget it) this too is a charming and simple flying game : https://baron.by.dai.studio/ . And this fun demo was a nice hook to find out what `dai.studio` actually do!

Turns out [dai.studio](https://about.dai.studio/blog/how-dai-started) is a communication tool between humans and LLMs. The clarity and layout of the tool is appealing : what's happening at a glance. 
eg : https://dai.studio/blog/generating-an-auth-app-with-dai-studio

Interesting it provides the LLM XML - which is of course a nicely structured text file, but isn't very human-friendly. Maybe this tool tips towards being more convenient to our machines than us. 
XML is notoriously verbose too, which might make it a slightly more expensive format for LLMs.

I might comment that this shows nicely the current map of the territory, but I often want to know history, areas of architectural concern (where performance bottlenecks might be; or which components 
requiring 
updates - and how these changes have consequences... ). In other words: there's other axes of interest.

My go-to tool for an architectural notation is a [C4 diagram](https://learning.oreilly.com/library/view/the-c4-model/9798341660113/) (and UML - especially sequence diagrams)  (both with mermaid.js of course!) As a more text based document it allows raising these 
topics ad 
hoc. And I've found 
LLMs capable 
of both creating and digesting them.

All formats have the problem of becoming unmaintained: Hence, at least make the process as frictionless as possible, even at the cost of being less precise. 

With the step change in the developer experience brought by LLMs, there's a lot of skills that were always valuable, but are going to be more important than ever: diagramming, UML, team 
co-ordination, systems thinking, Stakeholder expectation management, managing sprawling legacy code....  

And some that we're all likely to change our understanding and implementation: TDD, Agile, UX, Product development...