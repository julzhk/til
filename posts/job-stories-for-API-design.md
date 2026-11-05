TIL API design with job stories

Reading [Principles of web api design book](https://learning.oreilly.com/library/view/principles-of-web/9780137355754/ch03.xhtml#ch03): Applying 'job stories' to API design is a useful technique.

### What's a job story?

It's an alternative to the familiar user story _'As a ... I want to ... in order to achieve....'_ formulation. 

It's also similar ofc to the BDD/Gherkin : _Given .... when ... then ..._ style. 

So similar to other requirement 'story' formats but with a different emphasis.

### Definition of a job story?

Here's a [definition](https://learning.oreilly.com/library/view/principles-of-web/9780137355754/ch03.xhtml#:-:text=The%20Components%20of,the%20API%20design.):

> Job stories are composed of three components using the “When, I want to, so I can” format:
>
> **When**: The triggering event to establish causality is the situation or reason why the customer desires the outcome. Triggering events are key indicators for when an API will be used.
>
> **I want to**: The capability is what the customer has identified as the action that needs to be taken. The capability identifies the important role that the API will play to deliver the desired outcome. It is also used to deconstruct the operations that the API will deliver.
>
> **So I can**: The outcome is the desired end state. It is the result of applying the capability when the triggering event occurs. The outcome drives the acceptance criteria for the API design.

### Why a job story?

This 'Job to be done' variation is perhaps a bit more concrete than the others mentioned. 

I do appreciate the 'narrative' element to a user story - we should be aware of the 'voice of the customer' but this VOC concept can become quite rote and pro forma. 

Perhaps a user story formulation suit high-level epics better? Maybe 'user epics' would be better? : When there's fewer of them we might consider each component of each story more closely?

Anyway, just a thought.

---

### How does this relate to API design?

[This all maps quite neatly to an API design process:
](https://learning.oreilly.com/library/view/principles-of-web/9780137355754/ch03.xhtml#:-:text=Table%203.2%20Job%20Stories,ID)
eg: 

| When (trigger)                                       | I want to (capability)     | So I can (outcome) |
|------------------------------------------------------|----------------------------|---|
| I want to see the new books that have been released  | List recently added books  |Keep up with the latest watercooler talk
| I want to find a book that will be entertaining or teach me something new | Search for a book by topic or keyword | Browse related books |

It should be clear how this can relate to an API.

There's [more to the Jobs to be done formulation](https://jtbd.info/replacing-the-user-story-with-the-job-story-af7cdee10c27?gi=14ca43e848e9), the API book & API design, but this is a simple TIL. 