TIL how to make sure my brew installed postgres is not running.

It auto-restarts so we have to stop it properly!

Hence [killport](https://github.com/jkfran/killport) 5432 doesn't work. 

--- 


Use `brew services list`

...to give the list of services.

Then:

`brew services stop postgresql@14`