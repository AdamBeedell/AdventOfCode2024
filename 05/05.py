## 05.py

#### print queue

orderingrules = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""

updates = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


orderingrules = """91|95
64|54
64|53
62|96
62|91
62|35
18|28
18|78
18|73
18|95
58|89
58|32
58|99
58|66
58|14
78|69
78|88
78|58
78|74
78|79
78|84
75|11
75|32
75|28
75|54
75|62
75|17
75|35
63|17
63|75
63|78
63|79
63|94
63|62
63|91
63|88
34|73
34|26
34|44
34|93
34|74
34|55
34|82
34|47
34|18
84|16
84|65
84|99
84|44
84|88
84|96
84|34
84|89
84|76
84|57
69|53
69|93
69|18
69|41
69|99
69|36
69|76
69|47
69|95
69|73
69|57
55|62
55|33
55|65
55|16
55|18
55|53
55|28
55|95
55|43
55|75
55|54
55|73
14|99
14|36
14|56
14|65
14|55
14|76
14|84
14|96
14|79
14|88
14|89
14|26
14|44
56|75
56|55
56|76
56|18
56|66
56|26
56|16
56|36
56|96
56|65
56|47
56|44
56|53
56|41
93|57
93|75
93|96
93|82
93|47
93|64
93|16
93|26
93|44
93|74
93|41
93|66
93|36
93|76
93|97
74|57
74|16
74|26
74|44
74|89
74|82
74|75
74|65
74|64
74|47
74|28
74|97
74|55
74|41
74|63
74|95
66|41
66|28
66|75
66|35
66|71
66|62
66|54
66|53
66|94
66|43
66|82
66|18
66|16
66|95
66|33
66|97
66|92
44|94
44|73
44|65
44|66
44|55
44|33
44|97
44|54
44|18
44|36
44|75
44|41
44|71
44|78
44|35
44|28
44|95
44|16
76|57
76|97
76|73
76|36
76|28
76|16
76|75
76|96
76|89
76|47
76|18
76|74
76|64
76|63
76|53
76|43
76|26
76|95
76|44
28|92
28|78
28|79
28|62
28|21
28|56
28|35
28|54
28|99
28|17
28|29
28|69
28|94
28|14
28|33
28|88
28|71
28|93
28|58
28|91
92|78
92|26
92|56
92|32
92|14
92|69
92|93
92|21
92|58
92|88
92|35
92|99
92|94
92|11
92|79
92|62
92|29
92|84
92|17
92|34
92|76
11|93
11|57
11|89
11|74
11|91
11|88
11|47
11|29
11|99
11|69
11|76
11|58
11|26
11|32
11|64
11|44
11|21
11|96
11|14
11|34
11|79
11|56
26|54
26|44
26|64
26|53
26|66
26|71
26|36
26|89
26|43
26|96
26|82
26|47
26|95
26|65
26|75
26|28
26|16
26|73
26|18
26|97
26|63
26|41
26|55
97|79
97|29
97|32
97|92
97|91
97|99
97|14
97|69
97|54
97|34
97|21
97|17
97|33
97|11
97|28
97|88
97|78
97|35
97|58
97|56
97|94
97|71
97|84
97|62
99|95
99|55
99|56
99|34
99|64
99|66
99|26
99|57
99|89
99|93
99|16
99|65
99|74
99|43
99|41
99|82
99|73
99|36
99|53
99|96
99|76
99|47
99|18
99|44
32|96
32|93
32|36
32|73
32|89
32|95
32|64
32|16
32|18
32|69
32|34
32|47
32|26
32|88
32|55
32|44
32|74
32|57
32|99
32|76
32|66
32|65
32|53
32|56
54|34
54|79
54|32
54|91
54|88
54|99
54|33
54|84
54|29
54|58
54|21
54|56
54|11
54|14
54|76
54|71
54|69
54|92
54|35
54|93
54|78
54|94
54|17
54|62
47|28
47|75
47|65
47|66
47|55
47|53
47|71
47|43
47|89
47|16
47|97
47|73
47|57
47|36
47|96
47|18
47|44
47|63
47|54
47|92
47|41
47|64
47|82
47|95
82|32
82|33
82|91
82|62
82|58
82|11
82|97
82|78
82|41
82|79
82|92
82|94
82|29
82|17
82|28
82|71
82|54
82|21
82|35
82|14
82|75
82|43
82|84
82|63
89|92
89|65
89|64
89|28
89|62
89|36
89|63
89|57
89|73
89|66
89|18
89|97
89|43
89|82
89|75
89|94
89|55
89|41
89|44
89|95
89|54
89|53
89|16
89|71
17|57
17|47
17|64
17|76
17|96
17|26
17|88
17|74
17|32
17|91
17|79
17|55
17|56
17|65
17|66
17|34
17|36
17|93
17|89
17|99
17|69
17|84
17|53
17|44
57|62
57|43
57|63
57|71
57|65
57|55
57|16
57|95
57|82
57|35
57|36
57|92
57|41
57|44
57|18
57|66
57|73
57|97
57|28
57|54
57|53
57|94
57|64
57|75
65|75
65|63
65|16
65|11
65|62
65|18
65|94
65|82
65|54
65|21
65|33
65|97
65|53
65|78
65|71
65|95
65|28
65|29
65|92
65|58
65|41
65|43
65|35
65|73
53|73
53|35
53|33
53|62
53|11
53|71
53|58
53|75
53|54
53|43
53|92
53|14
53|94
53|95
53|78
53|41
53|63
53|16
53|29
53|28
53|82
53|21
53|97
53|18
41|17
41|92
41|29
41|71
41|91
41|78
41|21
41|54
41|43
41|58
41|63
41|33
41|94
41|97
41|75
41|11
41|32
41|88
41|14
41|62
41|35
41|79
41|84
41|28
33|93
33|56
33|26
33|21
33|58
33|84
33|76
33|69
33|14
33|96
33|11
33|99
33|88
33|17
33|78
33|79
33|47
33|74
33|29
33|89
33|32
33|91
33|57
33|34
35|34
35|47
35|11
35|84
35|99
35|21
35|29
35|74
35|89
35|76
35|69
35|33
35|88
35|96
35|56
35|78
35|91
35|79
35|14
35|93
35|58
35|32
35|26
35|17
95|33
95|11
95|75
95|73
95|97
95|58
95|71
95|21
95|78
95|92
95|63
95|43
95|94
95|84
95|29
95|17
95|14
95|79
95|62
95|35
95|41
95|82
95|54
95|28
94|88
94|29
94|14
94|17
94|58
94|99
94|56
94|91
94|79
94|84
94|93
94|78
94|32
94|76
94|74
94|21
94|47
94|34
94|26
94|35
94|69
94|11
94|33
94|62
36|71
36|75
36|43
36|92
36|62
36|16
36|33
36|82
36|65
36|95
36|41
36|18
36|29
36|97
36|53
36|28
36|63
36|73
36|66
36|11
36|54
36|94
36|35
36|78
96|97
96|64
96|28
96|55
96|66
96|44
96|82
96|53
96|65
96|94
96|36
96|57
96|75
96|71
96|41
96|95
96|16
96|89
96|54
96|43
96|73
96|63
96|18
96|92
21|17
21|26
21|89
21|64
21|36
21|69
21|84
21|57
21|58
21|14
21|99
21|56
21|96
21|34
21|74
21|47
21|79
21|55
21|76
21|93
21|44
21|88
21|91
21|32
43|35
43|71
43|28
43|29
43|91
43|58
43|97
43|92
43|69
43|21
43|62
43|63
43|75
43|79
43|78
43|54
43|17
43|94
43|33
43|88
43|84
43|11
43|32
43|14
73|71
73|79
73|58
73|43
73|97
73|84
73|11
73|78
73|82
73|17
73|29
73|54
73|35
73|33
73|14
73|28
73|91
73|63
73|21
73|92
73|94
73|41
73|75
73|62
88|36
88|95
88|18
88|64
88|96
88|73
88|65
88|47
88|34
88|76
88|26
88|93
88|55
88|56
88|69
88|53
88|82
88|99
88|89
88|44
88|74
88|57
88|66
88|16
16|97
16|18
16|94
16|29
16|17
16|92
16|75
16|14
16|33
16|63
16|43
16|62
16|54
16|21
16|11
16|28
16|73
16|71
16|58
16|78
16|35
16|41
16|95
16|82
71|35
71|91
71|94
71|74
71|92
71|88
71|33
71|21
71|17
71|99
71|62
71|78
71|84
71|34
71|79
71|56
71|93
71|32
71|58
71|14
71|76
71|69
71|11
71|29
79|93
79|57
79|66
79|91
79|99
79|64
79|16
79|34
79|56
79|69
79|88
79|84
79|44
79|36
79|65
79|96
79|74
79|76
79|53
79|47
79|55
79|32
79|26
79|89
29|74
29|84
29|79
29|56
29|44
29|14
29|99
29|57
29|91
29|88
29|34
29|93
29|89
29|26
29|96
29|64
29|17
29|32
29|55
29|76
29|21
29|69
29|47
29|58
91|65
91|34
91|96
91|56
91|53
91|16
91|47
91|64
91|93
91|57
91|89
91|99
91|76
91|69
91|44
91|18
91|66
91|32
91|88
91|55
91|74
91|26
91|36
64|62
64|75
64|43
64|35
64|71
64|55
64|73
64|94
64|36
64|44
64|18
64|97
64|41
64|65
64|82
64|33
64|95
64|92
64|66
64|16
64|28
64|63
62|34
62|79
62|78
62|32
62|14
62|74
62|93
62|17
62|47
62|58
62|56
62|88
62|29
62|69
62|33
62|11
62|21
62|76
62|26
62|99
62|84
18|58
18|35
18|79
18|82
18|71
18|54
18|94
18|21
18|97
18|92
18|62
18|14
18|11
18|43
18|41
18|63
18|75
18|17
18|33
18|29
58|84
58|57
58|96
58|47
58|74
58|56
58|69
58|88
58|79
58|55
58|17
58|93
58|36
58|76
58|91
58|34
58|26
58|64
58|44
78|14
78|17
78|47
78|29
78|26
78|11
78|99
78|96
78|21
78|76
78|89
78|57
78|93
78|32
78|34
78|91
78|56
78|64
75|14
75|79
75|88
75|91
75|34
75|33
75|78
75|84
75|97
75|99
75|21
75|71
75|69
75|58
75|29
75|94
75|92
63|99
63|32
63|21
63|71
63|92
63|14
63|97
63|54
63|69
63|29
63|11
63|28
63|58
63|84
63|35
63|33
34|66
34|63
34|41
34|56
34|89
34|16
34|53
34|57
34|43
34|95
34|96
34|36
34|64
34|65
34|76
84|36
84|91
84|53
84|93
84|18
84|66
84|69
84|26
84|74
84|47
84|55
84|64
84|32
84|56
69|34
69|55
69|74
69|44
69|96
69|65
69|89
69|66
69|26
69|16
69|64
69|56
69|82
55|94
55|66
55|78
55|41
55|63
55|35
55|92
55|71
55|11
55|97
55|82
55|36
14|91
14|64
14|66
14|57
14|93
14|32
14|34
14|74
14|47
14|69
14|17
56|73
56|64
56|93
56|95
56|74
56|82
56|63
56|43
56|57
56|89
93|53
93|43
93|55
93|18
93|89
93|73
93|95
93|65
93|63
74|18
74|96
74|53
74|66
74|43
74|73
74|36
74|54
66|29
66|63
66|65
66|78
66|21
66|11
66|73
44|53
44|63
44|62
44|82
44|92
44|43
76|65
76|55
76|82
76|41
76|66
28|84
28|32
28|34
28|11
92|74
92|33
92|91
11|84
11|17
26|57"""
### means that the left of the tuple must be processed/found in the print queue before the right of the tuple
updates = """34,74,26,89,64,44,55,65,53,16,18,95,73,82,43
36,44,89,93,56,18,76,99,26,74,96,41,65
47,96,89,57,64,44,55,36,66,65,53,16,18,95,73,82,41,63,97,54,71
66,16,64,89,84,44,91
54,94,21,71,69,32,14
26,54,96,18,75,36,97,41,95,16,55
55,79,56,47,57,69,44,34,84,88,76,17,74,96,36,99,26,32,64,66,89,65,93
96,29,93,17,56,88,58,76,69,79,99,44,32,14,34,21,84,26,47
71,92,94,62,35,33,78,11,29,17,79,32,88,69,99,34,56,93,76
75,97,28,54,71,92,94,62,35,33,78,11,29,58,17,84,91,32,88,69,99
82,43,71,62,11,21,58
97,84,92,41,43,54,75,79,32,29,63
94,35,78,11,14,79,84,88,99,34,76
79,32,74,66,65,96,64,57,55,17,44,99,93,91,56,47,84,26,34,89,76,88,36
66,65,18,63,92
28,54,71,94,62,11,21,14,17,79,84,91,88,69,99,34,56
93,18,44,96,55,53,43,95,75,36,26,63,16
97,54,62,35,33,78,11,29,21,14,84,99,34
65,16,41,43,97,71,62
75,35,62,32,29,79,84,14,97,58,28,11,41
92,28,73,71,18,58,43,75,95,17,11
32,17,93,44,91,55,21
43,66,53,54,62,71,29
99,32,62,93,74,35,26,17,88,79,69,94,34
28,54,71,92,94,62,35,33,29,21,58,14,17,79,84,91,32,88,69,34,56
57,64,44,55,36,66,65,53,16,18,95,73,82,41,43,63,75,97,28,54,71,94,62
29,18,82,43,97,33,78,35,71,75,11,28,53,54,92,63,58,95,62,41,94,73,21
71,35,33,11,29,21,58,14,17,84,91,32,88,69,34,93,76
29,58,14,17,79,84,91,32,88,99,34,56,93,76,74,26,47,96,89,64,44
99,89,69,93,32,57,36,79,55,34,74,47,44,53,76,64,26
95,96,47,44,57,43,93,18,55,53,76,65,64,66,16,75,63,41,26,89,82
69,99,56,74,26,96,64,44,55,53,18,95,82
17,79,84,91,99,34,56,76,26,47,57,36,65
95,82,41,43,63,75,28,54,71,92,94,62,35,33,78,29,21,58,14,17,79
79,56,14,99,96,91,58,78,11,26,34,47,29
73,95,33,18,65,63,75,43,94,66,92,53,82,78,16,41,54
69,33,58,84,94,35,32,14,29,88,71,54,78,56,99,92,11,93,34,62,21
63,75,28,71,92,62,35,78,11,21,14,79,84,91,69
92,62,57,16,18,41,95,65,28
73,74,63,44,26,95,56,57,89,41,65,55,18
95,82,96,76,63,16,44,26,97,89,64,74,43,57,53
64,18,96,57,43,41,34
57,64,44,55,36,65,16,82,41,43,63,75,97,28,54,71,92,94,62
94,62,35,33,29,58,17,32,88
84,32,88,69,99,34,56,76,74,26,47,96,89,57,64,55,36,66,65,53,16
54,71,92,94,62,35,33,78,11,29,21,58,14,17,91,32,88,69,93
84,26,32,17,47,93,79,88,91,33,99,76,56,21,69,78,89,29,96
63,75,94,43,21,97,62,58,11,88,35,54,78,17,29,92,79
11,73,97,62,75,63,36
21,88,33,29,56,35,11,34,99,32,26,74,93,58,96,84,79,69,76,91,47
41,74,26,64,75,96,47,97,44,66,28
47,73,76,64,26,99,66,18,93,55,41,82,53,89,36,34,57,74,95
99,17,64,93,56,55,74,89,21,91,26,14,34,57,32
62,35,17,84,32,99,56,76,47
92,84,21,62,28,79,91
79,88,56,76,47,96,57
63,64,76,89,66,53,43,36,57,18,65,95,82,93,73,96,44
34,93,74,26,89,57,53,16,73
74,26,96,89,57,64,55,36,65,53,18,95,73,82,63,75,28
53,16,18,95,73,82,41,43,63,75,97,28,54,71,92,94,62,35,33,78,11,21,58
88,96,89,57,64,55,66,16,18
47,96,57,64,44,55,36,66,65,53,16,18,95,73,82,41,43,63,75,97,28,54,71
29,58,14,79,91,32,88,99,34,93,76,74,26,47,96,89,57,64,44
33,94,82,35,63,73,18
88,35,69,58,11,91,54,14,28,21,99,71,62,32,97,29,78,33,84,75,17
99,64,44,74,55,66,57,26,32,84,53,96,34,16,65
73,18,43,97,36,96,53,41,54,47,28,26,16,89,63
92,97,28,16,63,62,71,55,75,36,33,41,65
58,26,76,33,62,69,99,78,14,56,74,94,29,17,91,32,11
75,64,95,57,73,71,44,82,18,53,54,28,16,36,55,89,92,97,43,94,66
17,79,84,32,88,69,99,34,93,76,74,26,47,57,64,55,36,66,65
18,44,55,64,57,93,96,65,47,43,41,53,76,75,82
65,34,16,88,95,69,47,66,32,64,96,53,56,36,55,93,44
92,94,62,35,33,78,11,29,21,58,14,17,79,84,91,32,88,69,99,34,56,93,74
94,33,29,58,14,88,34,93,26
17,75,79,78,92,28,33,82,14,43,95,63,41
82,41,43,63,75,97,28,54,71,62,35,33,29,21,58,14,79,84,91
84,94,88,33,32,62,78,93,35,79,54,91,21,99,92,29,14
32,76,91,96,64,11,79
47,96,57,66,65,53,16,73,82,63,97,28,54
43,17,63,54,79
65,53,16,18,95,73,82,41,43,63,75,97,28,54,71,92,94,62,35,33,78,11,21
34,56,93,76,26,47,96,89,57,64,44,55,36,66,65,53,16,18,95,73,82,41,43
63,43,95,97,26,82,57,16,36,18,73,54,89,53,47,65,64
17,79,84,32,69,99,34,56,93,76,74,26,47,96,57,64,44,66,65
36,66,53,16,18,73,82,41,43,63,75,28,54,71,92,94,62,35,33,78,11
11,21,17,14,32,71,56,76,94
63,41,57,74,89,96,97
73,41,63,97,54,94,62,33,78,11,29,17,79
56,79,26,93,69,65,32,44,91,74,99,89,64,36,96,47,76,57,34
44,17,14,66,36,32,84,89,99,34,57,76,55,47,69,91,26
36,66,65,16,18,95,82,41,43,63,75,97,28,71,92,35,78
58,54,28,21,75,11,92
78,62,99,11,97,17,34,58,28,84,14
78,53,41,73,28,58,94,82,97
26,47,96,57,65,53,18,97,54
82,41,63,75,97,54,71,92,94,62,35,78,11,21,14,17,79,84,91
41,63,75,28,92,94,14,84,32
35,14,16,29,43,92,95,21,63
16,95,73,41,43,63,97,54,62,35,33,11,29,21,14
66,65,53,16,18,95,73,82,41,43,75,97,28,54,71,92,94,62,35,33,78,11,29
41,66,57,16,97,28,89,73,43,47,55,44,74,26,63,75,95
41,97,95,53,78,66,94,18,75,55,62,28,73
73,16,11,53,36,54,71,95,43,63,33,28,75,62,18,41,92
91,32,88,99,76,26,89,55,53
66,96,16,53,36,47,55,97,64,89,18,65,75,41,63
14,17,84,91,32,88,69,99,34,93,74,26,47,96,89,57,64,44,55,36,66
96,64,55,16,82,63,92
14,62,73,78,17,71,95,58,75,35,63,28,82,43,11,41,92,54,21,97,18,33,29
73,82,41,43,63,75,97,28,54,92,94,62,78,11,29,21,58,14,17,79,84
97,14,28,43,75,58,33,82,17,62,29,91,63,78,35
71,54,14,97,92,79,58,69,99,94,75
16,18,55,93,57,91,96,53,32,64,36,88,66
21,33,63,54,17,62,92,11,35,14,32,79,84
93,63,74,96,55,56,66,41,26,65,43
95,75,73,63,35,62,65,97,82,18,66,55,71,94,44,92,53,36,43,64,41
18,95,41,43,63,75,28,54,71,92,94,62,35,33,78,11,29,21,58,14,17
69,57,76,96,44,32,21,91,79,29,93
55,36,95,65,89,44,64,73,53,71,82,63,75,43,18,28,66
54,58,97,21,35
92,78,21,14,79,32,88,69,99,34,56,93,74
41,63,75,58,33,73,21,11,29
79,63,88,54,33,91,35,17,29,92,43,11,21
16,18,95,82,41,43,63,75,97,28,54,71,92,94,62,35,78,58,14
21,58,17,79,84,91,32,88,69,99,34,56,93,76,74,26,96,57,64,44,55
73,82,41,43,63,75,71,94,62,33,11,58,84
84,32,57,17,36,79,58,76,69
11,14,78,26,69,84,34,88,58,79,32
78,11,58,17,79,84,69,76,74,26,96,89,57
56,65,18,34,64,53,93,96,89,44,26,95,66,99,57
75,97,28,71,92,94,62,35,78,11,29,21,58,79,84,32,88,69,99
97,71,33,21,17,91,34
73,69,99,56,55,93,82,76,57,74,64,44,96,16,66,26,95,36,18
89,74,78,88,17,14,11,32,57,76,56,26,29,84,21
95,41,17,63,28,75,58,35,14,54,11,73,21,97,33
35,62,54,92,97,84,32
84,54,88,21,35,93,62
14,29,34,17,99,88,69,21,84,79,11,91,56,74,78,93,89,58,26,96,76,47,32
66,79,56,36,88,91,84,64,74,34,47,96,14
55,92,66,54,95,82,16,44,18,96,73,97,43,65,63
44,18,91,76,88,16,65,93,64,32,34,47,56,57,96,36,74,55,89
17,29,32,14,34,56,33,78,71
14,56,29,99,88,17,71,28,84
93,26,57,65,16,18,82,41,75
78,29,28,14,71,63,58,43,41,97,94,33,62,84,82,17,54,79,75,92,35,21,11
65,53,95,73,82,41,43,63,75,97,28,54,71,94,62,35,33,78,11,29,21
36,65,53,18,73,82,54,78,11
18,73,75,28,92,94,62,35,78,11,29,21,58,14,17
18,16,55,69,96,91,66,34,44
69,34,56,93,26,47,96,57,55,66,53,18,95,73,82
63,75,28,54,94,35,11,29,21,79,84,91,88
44,26,89,16,18,69,66,95,57,47,53,73,55,74,36,82,65,76,56,34,99,64,96
93,69,65,82,57,89,66,56,53,16,73,34,64,76,55,26,95,44,36,96,74
11,58,97,63,35,33,73,29,53,21,92
28,71,92,94,62,35,33,78,11,29,21,58,14,17,79,84,91,32,88,69,99,34,56
73,58,97,41,18,14,28,43,82,54,62,16,35
53,55,44,93,26,89,66,43,16,57,36,82,65,73,96,76,41,34,74,47,95
74,76,36,65,69,55,17
84,32,11,33,63,92,78,28,91,79,35,58,41,54,97,71,43
74,44,76,84,29,91,34,21,32,69,96,64,57
62,35,29,21,17,79,84,91,32,88,69,99,34,56,76,74,47
28,94,33,11,58,91,56
47,55,88,79,65,64,53
63,97,28,94,78,11,29,21,32,88,69
73,97,54,71,92,62,35,33,11,29,21,17,84
29,21,58,14,17,79,84,69,99,34,74,47,89,57,64
29,43,54,58,35,82,92,71,91,11,62,84,63,17,94
73,41,43,63,54,71,94,62,35,33,78,11,29,21,14,17,84
64,55,66,53,82,43,63,75,97,28,54,92,94,62,35
54,94,62,78,11,58,32
57,47,84,96,14,99,56,64,34,17,55,76,44,58,89,91,69,74,26,79,36
14,79,84,91,32,88,69,99,34,56,93,76,74,26,47,96,89,57,64,44,55,36,66
16,95,73,41,63,97,28,54,92,94,35,78,11,29,14
32,69,74,84,91,76,78,33,26,34,99,89,17,58,79,96,14
47,57,55,66,65,53,95,43,63,97,71
89,44,55,66,65,53,16,95,82,43,63,75,28,54,71,92,94
33,78,29,21,58,17,84,91,88,99,56,93,76,74,26,96,89
94,78,76,62,11,26,29,91,14,79,17,35,74,69,32,99,21,58,56
93,89,96,32,56,74,64,79,44,55,99
89,14,33,21,74,88,91,47,76,26,93
28,54,71,94,62,33,78,29,21,17,79,84,91,32,88,69,56
63,75,97,54,71,92,94,62,35,33,11,29,21,58,17,79,84,91,32,88,69
33,14,17,34,76
88,69,34,56,93,76,74,26,47,96,89,57,64,44,55,36,66,65,53,16,18,95,73
36,66,65,18,95,73,41,63,97,54,92,33,11
62,11,41,94,21,92,75,73,82,14,28
18,36,16,56,47,43,93,53,34,44,26,66,96,89,55,74,95,64,73
89,64,44,55,36,65,16,18,95,82,43,63,97,28,54,92,94
99,71,93,79,35,76,84,32,62,29,91,78,11,92,88,21,94,14,17,33,56,69,58
93,16,88,65,44,56,55,96,84,53,57
47,64,44,55,65,53,16,95,82,41,43,97,28,54,71
29,58,84,34,56,93,76,26,47,89,57,64,44
32,69,17,35,94,11,99,88,56,92,79,21,74,84,91
16,95,73,63,75,92,35,11,29,21,14
88,69,34,76,74,26,57,44,55,53,16,95,73
99,14,17,56,32,93,79,47,35
54,97,33,21,43,14,11,75,73,71,78,17,41
62,78,11,88,69
93,74,96,57,64,44,55,53,18,95,73,41,63
54,29,79,91,99,92,93"""



#### parse the input

## rules

orderingrules = orderingrules.split("\n")
#orderingrules = orderingrules.replace("|",",")
frules = []
for rule in orderingrules:
    frules.append(rule.split("|"))
    

## updates

updates = updates.split("\n")


### look for which updates are already in the right order

i=0
def checkrules(updatelist, rules):
    for before, after in rules:
        if before in updatelist and after in updatelist:
            if updatelist.index(before) > updatelist.index(after):
                return False  # Rule is violated
    return True  # All rules are satisfied



### Validate updates
validitems = []
for update in updates:
    if checkrules(update, frules):
        validitems.append(update)

### once found, locate the middle item and sum them

result = 0
for items in validitems:
    #print(items)
    items = items.split(',')  ### first answer was wrong because i lost the list of lists type somewhere, became a string.
    middle = items[len(items) // 2] ### assumes a odd numbered string, I figure that's a given based on the question
    #print(middle)
    result += int(middle)
    #print(result)

print(result)



