#!/usr/bin/env python3

input = open("10_input").read()
#input = open("10_test").read()








"""Solve the following problem correctly in python, and print the answer.
The input must be read from a file called 10_input
Do not write comments.



--- Day 10: Syntax Scoring ---You ask the submarine to determine the best route out of the deep-sea cave, but it only replies:
Syntax error in navigation subsystem on line: all of them
All of them?! The damage is worse than you thought. You bring up a copy of the navigation subsystem (your puzzle input).
The navigation subsystem syntax is made of several lines containing chunks. There are one or more chunks on each line, and chunks contain zero or more other chunks. Adjacent chunks are not separated by any delimiter; if one chunk stops, the next chunk (if any) can immediately start. Every chunk must open and close with one of four legal pairs of matching characters:

If a chunk opens with (, it must close with ).
If a chunk opens with [, it must close with ].
If a chunk opens with {, it must close with }.
If a chunk opens with &lt;, it must close with &gt;.

So, () is a legal chunk that contains no other chunks, as is []. More complex but valid chunks include ([]), {()()()}, &lt;([{}])&gt;, [&lt;&gt;({}){}[([])&lt;&gt;]], and even (((((((((()))))))))).
Some lines are incomplete, but others are corrupted. Find and discard the corrupted lines first.
A corrupted line is one where a chunk closes with the wrong character - that is, where the characters it opens and closes with do not form one of the four legal pairs listed above.
Examples of corrupted chunks include (], {()()()&gt;, (((()))}, and &lt;([]){()}[{}]). Such a chunk can appear anywhere within a line, and its presence causes the whole line to be considered corrupted.
For example, consider the following navigation subsystem:
[({(&lt;(())[]&gt;[[{[]{&lt;()&lt;&gt;&gt;
[(()[&lt;&gt;])]({[&lt;{&lt;&lt;[]&gt;&gt;(
{([(&lt;{}[&lt;&gt;[]}&gt;{[]{[(&lt;()&gt;
(((({&lt;&gt;}&lt;{&lt;{&lt;&gt;}{[]{[]{}
[[&lt;[([]))&lt;([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{&lt;[[]]&gt;}&lt;{[{[{[]{()[[[]
[&lt;(&lt;(&lt;(&lt;{}))&gt;&lt;([]([]()
&lt;{([([[(&lt;&gt;()){}]&gt;(&lt;&lt;{{
&lt;{([{{}}[&lt;[[[&lt;&gt;{}]]]&gt;[]]

Some of the lines aren't corrupted, just incomplete; you can ignore these lines for now. The remaining five lines are corrupted:

{([(&lt;{}[&lt;&gt;[]}&gt;{[]{[(&lt;()&gt; - Expected ], but found } instead.
[[&lt;[([]))&lt;([[{}[[()]]] - Expected ], but found ) instead.
[{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead.
[&lt;(&lt;(&lt;(&lt;{}))&gt;&lt;([]([]() - Expected &gt;, but found ) instead.
&lt;{([([[(&lt;&gt;()){}]&gt;(&lt;&lt;{{ - Expected ], but found &gt; instead.

Stop at the first incorrect closing character on each corrupted line.
Did you know that syntax checkers actually have contests to see who can get the high score for syntax errors in a file? It's true! To calculate the syntax error score for a line, take the first illegal character on the line and look it up in the following table:

): 3 points.
]: 57 points.
}: 1197 points.
&gt;: 25137 points.

In the above example, an illegal ) was found twice (2*3 = 6 points), an illegal ] was found once (57 points), an illegal } was found once (1197 points), and an illegal &gt; was found once (25137 points). So, the total syntax error score for this file is 6+57+1197+25137 = 26397 points!
Find the first illegal character in each corrupted line of the navigation subsystem. What is the total syntax error score for those errors?

Your puzzle answer was 299793.--- Part Two ---Now, discard the corrupted lines.  The remaining lines are incomplete.
Incomplete lines don't have any incorrect characters - instead, they're missing some closing characters at the end of the line. To repair the navigation subsystem, you just need to figure out the sequence of closing characters that complete all open chunks in the line.
You can only use closing characters (), ], }, or &gt;), and you must add them in the correct order so that only legal pairs are formed and all chunks end up closed.
In the example above, there are five incomplete lines:

[({(&lt;(())[]&gt;[[{[]{&lt;()&lt;&gt;&gt; - Complete by adding }}]])})].
[(()[&lt;&gt;])]({[&lt;{&lt;&lt;[]&gt;&gt;( - Complete by adding )}&gt;]}).
(((({&lt;&gt;}&lt;{&lt;{&lt;&gt;}{[]{[]{} - Complete by adding }}&gt;}&gt;)))).
{&lt;[[]]&gt;}&lt;{[{[{[]{()[[[] - Complete by adding ]]}}]}]}&gt;.
&lt;{([{{}}[&lt;[[[&lt;&gt;{}]]]&gt;[]] - Complete by adding ])}&gt;.

Did you know that autocomplete tools also have contests? It's true! The score is determined by considering the completion string character-by-character. Start with a total score of 0. Then, for each character, multiply the total score by 5 and then increase the total score by the point value given for the character in the following table:

): 1 point.
]: 2 points.
}: 3 points.
&gt;: 4 points.

So, the last completion string above - ])}&gt; - would be scored as follows:

Start with a total score of 0.
Multiply the total score by 5 to get 0, then add the value of ] (2) to get a new total score of 2.
Multiply the total score by 5 to get 10, then add the value of ) (1) to get a new total score of 11.
Multiply the total score by 5 to get 55, then add the value of } (3) to get a new total score of 58.
Multiply the total score by 5 to get 290, then add the value of &gt; (4) to get a new total score of 294.

The five lines' completion strings have total scores as follows:

}}]])})] - 288957 total points.
)}&gt;]}) - 5566 total points.
}}&gt;}&gt;)))) - 1480781 total points.
]]}}]}]}&gt; - 995444 total points.
])}&gt; - 294 total points.

Autocomplete tools are an odd bunch: the winner is found by sorting all of the scores and then taking the middle score. (There will always be an odd number of scores to consider.) In this example, the middle score is 288957 because there are the same number of scores smaller and larger than it.
Find the completion string for each incomplete line, score the completion strings, and sort the scores. What is the middle score?

Your puzzle answer was 3654963618.Both parts of this puzzle are complete! They provide two gold stars: **
At this point, you should return to your Advent calendar and try another puzzle.
If you still want to see it, you can get your puzzle input.
You can also [Shareon
  Twitter
  Mastodon</a
>] this puzzle.




(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-69522494-1', 'auto');
ga('set', 'anonymizeIp', true);
ga('send', 'pageview');



"""






"""Solve the following problem correctly in python, and print the answer.
The input must be read from a file called 10_input
Do not write comments.



--- Day 10: Syntax Scoring ---You ask the submarine to determine the best route out of the deep-sea cave, but it only replies:
Syntax error in navigation subsystem on line: all of them
All of them?! The damage is worse than you thought. You bring up a copy of the navigation subsystem (your puzzle input).
The navigation subsystem syntax is made of several lines containing chunks. There are one or more chunks on each line, and chunks contain zero or more other chunks. Adjacent chunks are not separated by any delimiter; if one chunk stops, the next chunk (if any) can immediately start. Every chunk must open and close with one of four legal pairs of matching characters:

If a chunk opens with (, it must close with ).
If a chunk opens with [, it must close with ].
If a chunk opens with {, it must close with }.
If a chunk opens with &lt;, it must close with &gt;.

So, () is a legal chunk that contains no other chunks, as is []. More complex but valid chunks include ([]), {()()()}, &lt;([{}])&gt;, [&lt;&gt;({}){}[([])&lt;&gt;]], and even (((((((((()))))))))).
Some lines are incomplete, but others are corrupted. Find and discard the corrupted lines first.
A corrupted line is one where a chunk closes with the wrong character - that is, where the characters it opens and closes with do not form one of the four legal pairs listed above.
Examples of corrupted chunks include (], {()()()&gt;, (((()))}, and &lt;([]){()}[{}]). Such a chunk can appear anywhere within a line, and its presence causes the whole line to be considered corrupted.
For example, consider the following navigation subsystem:
[({(&lt;(())[]&gt;[[{[]{&lt;()&lt;&gt;&gt;
[(()[&lt;&gt;])]({[&lt;{&lt;&lt;[]&gt;&gt;(
{([(&lt;{}[&lt;&gt;[]}&gt;{[]{[(&lt;()&gt;
(((({&lt;&gt;}&lt;{&lt;{&lt;&gt;}{[]{[]{}
[[&lt;[([]))&lt;([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{&lt;[[]]&gt;}&lt;{[{[{[]{()[[[]
[&lt;(&lt;(&lt;(&lt;{}))&gt;&lt;([]([]()
&lt;{([([[(&lt;&gt;()){}]&gt;(&lt;&lt;{{
&lt;{([{{}}[&lt;[[[&lt;&gt;{}]]]&gt;[]]

Some of the lines aren't corrupted, just incomplete; you can ignore these lines for now. The remaining five lines are corrupted:

{([(&lt;{}[&lt;&gt;[]}&gt;{[]{[(&lt;()&gt; - Expected ], but found } instead.
[[&lt;[([]))&lt;([[{}[[()]]] - Expected ], but found ) instead.
[{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead.
[&lt;(&lt;(&lt;(&lt;{}))&gt;&lt;([]([]() - Expected &gt;, but found ) instead.
&lt;{([([[(&lt;&gt;()){}]&gt;(&lt;&lt;{{ - Expected ], but found &gt; instead.

Stop at the first incorrect closing character on each corrupted line.
Did you know that syntax checkers actually have contests to see who can get the high score for syntax errors in a file? It's true! To calculate the syntax error score for a line, take the first illegal character on the line and look it up in the following table:

): 3 points.
]: 57 points.
}: 1197 points.
&gt;: 25137 points.

In the above example, an illegal ) was found twice (2*3 = 6 points), an illegal ] was found once (57 points), an illegal } was found once (1197 points), and an illegal &gt; was found once (25137 points). So, the total syntax error score for this file is 6+57+1197+25137 = 26397 points!
Find the first illegal character in each corrupted line of the navigation subsystem. What is the total syntax error score for those errors?



"""
