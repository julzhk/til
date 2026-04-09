TIL how to make sure my brew installed postgres is not running.

It auto-restarts so we have to stop it properly!

Hence [killport](https://github.com/jkfran/killport) 5432 doesn't work. 

--- 


Use `brew services list`

...to give the list of services.

Then:

`brew services stop postgresql@14`

----

[Thanks stackoverflow!](https://stackoverflow.com/questions/34173451/stop-postgresql-service-on-mac-via-terminal)

---
More homebrew learning :
`Brew install openjdk` : needs a symlink to really work : [thanks to John Siu's blog](https://johnsiu.com/blog/macos-brew-java/). And I learned to use `brew info openjdk` : which gives this vital 
follow up task. 