# CSC 315 DB with App

This is a simple database of integer sequences (like OEIS). 

## DB creation
Run intseq.sql to 
- create intseq db
- add a few sequences
- add an app user with insert and select permissions

## DB connection
Run main.py to
- connect to intseq db
- insert a new sequence
- select a sequence

# Socket communication (via Flask)
Run server.py to
- connect to intseq db and start listening on port 5000
- root url will display all existing sequences by name

## View sequence
- make a request to /viewseq?name=sequence_name

## Add sequence
- make a request to /addseq?id=seq_id&name=seq_name&seq=integer_seq

Take care to handle spaces when using curl (replace with %20 char code). There is no error handling.