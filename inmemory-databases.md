TIL: some new in-memory databases to choose from
- 

There's been a huge increase in database projects in the last number of years, so it shouldn't be a surprise that there's been a similar growth in in-memory data stores.

### Why are in-memory databases are interesting?

If speed and transactional consistency over a distributed system are important then keeping the data representation in RAM has some significant advantages. The downside of course is the lack of 
persistance. 

Here's an interesting [short video](https://developertoarchitect.com/lessons/lesson166.html) about this 'space-based architectural style'. [Comparison of architectural styles here.](https://www.developertoarchitect.com/downloads/architecture-styles-worksheet.pdf)

These new in-memory databases say they dump to permanent storage periodically. 

Obviously Redis and sqlite - but [Dragonfly](https://www.dragonflydb.io) db also.

[And a nice blog post here](https://memgraph.com/blog/in-memory-databases-that-work-great-with-python). 