TIL - Resiliency vs reliability engineering
---

[This video is great](https://www.youtube.com/watch?v=PGLYEDpNu60) : 
Velocity NY 2013: Richard Cook, "Resilience In Complex Adaptive Systems"

& [this one too](https://www.youtube.com/watch?v=2S0k12uZR14): Velocity 2012: Richard Cook, "How Complex Systems Fail"

---

In a nutshell: 'resiliency' focuses on building systems that can withstand failures and recover quickly. 'Reliability' aims to ensure that systems operate consistently and 
without errors. Both are crucial ofc for software, but we should be aware that we're attempting to address both aspects.

That second video gives a nice insight between the forces that perturb a system and it's acceptable limits before failure:
eg: Rasmussen's systems model 
* Economic failure boundary
* unacceptable workload boundary
* accident boundary

The acceptable behaviour is between these three constraints, but human, policy, technical forces perturb it over time. Eventually it might move out of these boundraries and cause some kind of failure.