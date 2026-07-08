Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
====== RESTART: C:/Users/laksh/AppData/Local/Programs/Python/Python313/.py =====
Text: AABAACAADAABAABA
Pattern: AABA

Naive -> Matches at: [0, 9, 12] , Comparisons: 30
KMP   -> Matches at: [0, 9, 12] , Comparisons: 18
RK    -> Matches at: [0, 9, 12] , Comparisons: 12

     Pattern      Naive        KMP         RK
--------------------------------------------------
          AB      12508      10000       1234
        ABCD      13286      10000        223
      ABCDAB      13329      10010        144
    ABCDABCD      13328      10011        109
