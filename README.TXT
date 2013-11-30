P21 Data Dump Parser 

created by: Vaughan Schmidt
date: 		2013.11.30

Description:

Simple parser to be used with on dump file generated
by Epicor P21 software support tool.  (P21 > HELP >
SEND DATA TO SOFTWARE SUPPORT).

Support tool generates a .txt file of all the various 
records in multiple database tables associated with a
particular transaction, example: all the records in any
table associated with a particular order number.

This script scans the .txt file and processes out the
various unique table sets.

Ultimately, should be able to nicely display the
particulars in a more readable format to improve
admin troubleshooting.
