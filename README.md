# Classification-and-Summarization-of-Fani-Cyclone

Fani Cyclone Tweets were initially extracted, and further have been cleaned according to the input for getting the summarization output, for the tweets being informative for the government.

File Name:- Fani_Cyclon_Input_Tweets, contains the raw extracted cyclone tweets.
There are around 40 files, divided on hourly basis, further the informative tweets have been extracted.

File Name:- Clean_Tweets.py - gives the output, for being the input file for the Summarization Algorithm.
File Name:- Full_Stop_at_End.py - gives a full stop at the end, in order to help the summarization algorithm understand as where the sentece is ending for it to read all the tweets.

Further, the Summarization has been performed on the extracted tweets.
The summarization algorithm which has been used are:- Luhn and LSA.
Also, tried few more summarization algorithms alongside and considered them keeping in mind the future perspective. Algorithms like Lex-Rank and Sum-Basic.

Also tried, mixing out these summarization algorithms of which the best results has been found with the intersection of 1.(Luhn, LSA and Text-Rank), 2.(Luhn, LSA), 3.(Luhn, Text-Rank) and 4.(LSA, Text-Rank).

The Output of the Summarization algorithm has been uploaded in the the folder named as "Summarization_Output_File", where we have showed the result in the csv file, for the above mentioned summarization algorithm's. We have posted the summarization output in the combination of different files, as it would help us to get the updated summarized information with the time.

Future Work:-
Further, trying to improve the summarization algorithm for the encoded data and the multilingual tweets.

The above work is available at:-
https://ieeexplore.ieee.org/abstract/document/9087159
