# Classification-and-Summarization-of-Fani-Cyclone

Fani Cyclone Tweets were initially extracted, and further have been cleaned according to the input for getting the summarization output, for the tweets being informative for the government.

File Name:- Fani_Cyclon_Input_Tweets, contains the raw extracted cyclone tweets.
There are around 40 files, divided on hourly basis, further the informative tweets have been extracted.

File Name:- Clean_Tweets.py - gives the output, for being the input file for the Summarization Algorithm.
File Name:- Full_Stop_at_End.py - gives a full stop at the end, in order to help the summarization algorithm understand as where the sentece is ending for it to read all the tweets.

Further, the Summarization has been performed on the extracted tweets.
The summarization algorith which has been used are:- Lex-Rank, Luhn, LSA, Text-Rank and Sum-Basic.
Out of which the best results has been found with the intersection of 1.(Luhn, LSA and Text-Rank), 2.(Luhn, LSA), 3.(Luhn, Text-Rank) and 4.(LSA, Text-Rank).

Codes and Final Output will be uploaded Soon..
