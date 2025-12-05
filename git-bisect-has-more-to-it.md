TIL: Git bisect has more to it
--

[Git bisect](https://git-scm.com/docs/git-bisect) is great. Might be an 'if you know, you know' type thing but I've used it frequently pretty much since I started using Git.

In a nutshell: it allows you to find where something 'bad' happened in the git codebase. It does it by marking a known 'good' and a known 'bad' commit. Then it checks out half way between these 
two and asks if this is good or bad. This rapidly finds locates 'good' turned 'bad'.

Today I learned that good and bad can be replaced with 'old' and 'new', and it does a lot more than I've ever used it for:

* Tell git bisect which commit to try next with ['next'](https://git-scm.com/docs/git-bisect#_bisect_next)

* The documentation has some useful best practices. Eg: make sure all your tests pass before checking in new code, is a good one. It certainly helps when using bisect and tests together
* Another example: [check out a new bisect checkout and run the tests in one go](https://git-scm.com/docs/git-bisect-lk2009#_passing_sh_c_some_commands_to_git_bisect_run).
This means git bisect could be nicely incorporated into a CI/CD pipeline: especially if it's one that doesn't run the slower tests frequently - an automatic git bisect on failure would be quite 
convenient!  