## TIL: Finding Datastar works nicely for a prototype

Of course there's objections and exceptions to this hot take: but I think dividing up a web app into a distinct Front-end and Backend techologies is often a reflex. It's often done for staffing and 
ease-of-management over project requirements.

It makes sense when the application is complex and there's a lot to do! Splitting the work into these functional domains helps the project chug along. And there's a 'this is how it's always done orthodoxy' too..

Contrast this to a humble solo developed project: Complexity is an impediment: there's only so much that a solo dev can manage conceptually - even with LLMs. 

So why not render the content in the server and use hypermedia for interactivity - rather than treat the front-end as an application and the backend as a separate concern?  

Anway this is all pre-amble for saying HTMX+Alpine.js fits this nicely - for more CRUD interactions. The mental model of what's happening is simple enough and it just works.

And [data-star.dev](data-star.dev) 
works nicely for more reactive 
applications; the mental model (and hence the debugging flow) is a bit more radical but it's still elegantly server-side and simple.

Keeping the scope in one code base - and compartmentalized - seems to suit generative AI coding too.

I say this as this Claude-assisted project : [A 'digital Audio Workstation'  (DAW)](https://github.com/julzhk/Daw#poc-daw) works great. It supports a real-time chat (exactly the kind of thing Data-star is 
good at); it has a 'source of truth' on the server, so a shared state, which allows real-time collaboration and edits.; & music playback is handled locally of course.  

![](../images/projects/datastar-daw.jpg "Digital Audio Workstation in data-star")

For an alternative comparison approach I also wanted to take a look at attempting this spike with NiceGUI: hence [NiceGUI DAW](https://github.com/julzhk/DawNiceGUI#poc-daw-nicegui) spike.

![](../images/projects/nicegui-daw.jpg "Digital Audio Workstation in NiceGUI ")

It's meant to replicate the same look and behaviour, which it does. Hard to choose which one's better functionally. Have to examine other characteristics: such as maintainability and load and 
resource efficiency...

Anyway a fun experiment.