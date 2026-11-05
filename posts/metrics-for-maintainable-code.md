TIL Metrics for Maintainable Code
---
Was looking for some tools to look into the code quality of a project by looking at it's git history. Something like charting cyclometric complexity over time.

Well! There are a lot of projects out there that do this. eg: [Git-commit-analysis](https://github.com/CoderAllan/GitCommitsAnalysis)
 which let me to the video : 
[Seven Secrets of Maintainable Codebases
](https://www.youtube.com/watch?v=a74UkJxKWVM&t=881s).


This video has a bunch of interesting ways to analyze code quality for maintainability. Maintainability is ofc a hugely important factor for most software development projects: Making a clever 
solution is 
table 
stakes for long-term software development. Making it able to extend over time is the real valuable aspect.

[Seven Secrets of Maintainable Codebases
](https://www.youtube.com/watch?v=a74UkJxKWVM&t=881s)
 says look at: 

1 Hotspots: Code that changes often

2 We're not very accurate at estimating where hte problems are

3 The cost of surprise: It's the most expensive part of a software project: So make the code unsurprising.

4 The metric of temporal coupling. If two areas of code change at the same time, they are temporally coupled: This can be good - they might be related - but it's often not a good sign.

5 Organizations aspects of code: If we count how many contributors to each file in our project, this gives an indication of the degree of quality issues there are likely to be.

6 When  a developer leaves, this gives an indication of 'knowledge loss': abandoned code is related to the creator.

7 Make the work fun; it's a lot easier to do something well if you're motivated.

https://learning.oreilly.com/library/view/your-code-as/9798888650837/ - which I'll be reading!