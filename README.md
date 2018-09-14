# linux
## Tools which run and work on Linux.


* ps-to-csv.py : 
  + Take the output of multiple  "ps -eT" invocations > to file called "ps.out.txt" and create a CSV file that can be imported into Excel for charting etc.
  + e.g $  for i in [1..10] ; do ps -eT >> ps.out.txt ;sleep 1 ; done ; python ps-to-csv.py > out.csv

