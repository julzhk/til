Fly sprites are a new VM deployment model (they're fast starting/fast pausing persistant VMs)
Really good for a cheap dev or demo; or some particular workers and spinning up AI related.

DBOS is a neat async persistant execution framework; these two go together quite nicely - fast starting workers that sleep when they're not needed. That's a bingo!