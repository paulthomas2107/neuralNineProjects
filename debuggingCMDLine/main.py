values = [10, 6, 17, 5, 14, 18, 85, 0, 9, 12, 13]

for value in values:
    # breakpoint()
    print(10 / value)
    if value % 5 == 0:
        print('Div by 5')
    print("Hello Paul")

"""
    ~/neuralNineProjects    master +1  cd debuggingCMDLine                                                                                                                       ✔  base  
    ~/neuralNineProjects/debuggingCMDLine    master +1  python -m pdb main.py main.py                                                                                            ✔  base  
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(1)<module>()
-> values = [10, 6, 17, 5, 14, 18, 85, 0, 9, 12, 13]
(Pdb) break 4
Breakpoint 1 at /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py:4
(Pdb) c
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(4)<module>()
-> print(10 / value)
(Pdb) p value
10
(Pdb) p values
[10, 6, 17, 5, 14, 18, 85, 0, 9, 12, 13]
(Pdb) c
1.0
Div by 5
Hello Paul
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(4)<module>()
-> print(10 / value)
(Pdb) p value
6
(Pdb) c
1.6666666666666667
Hello Paul
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(4)<module>()
-> print(10 / value)
(Pdb) next
0.5882352941176471
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(5)<module>()
-> if value % 5 == 0:
(Pdb) next
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(7)<module>()
-> print("Hello Paul")
(Pdb) step
Hello Paul
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(3)<module>()
-> for value in values:
(Pdb) q
    ~/neuralNineProjects/debuggingCMDLine    master +1 !1  python -m pdb main.py main.py                                                                              ✔  2m 59s   base  
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(1)<module>()
-> values = [10, 6, 17, 5, 14, 18, 85, 0, 9, 12, 13]
(Pdb) c
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(5)<module>()
-> print(10 / value)
(Pdb) c
1.0
Div by 5
Hello Paul
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(4)<module>()
-> breakpoint()
(Pdb) step
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(5)<module>()
-> print(10 / value)
(Pdb) step
1.6666666666666667
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(6)<module>()
-> if value % 5 == 0:
(Pdb) step
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(8)<module>()
-> print("Hello Paul")
(Pdb) step
Hello Paul
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(3)<module>()
-> for value in values:
(Pdb) next
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(4)<module>()
-> breakpoint()
(Pdb) --KeyboardInterrupt--
(Pdb) q
The program finished and will be restarted
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(1)<module>()
-> values = [10, 6, 17, 5, 14, 18, 85, 0, 9, 12, 13]
(Pdb) q
    ~/neuralNineProjects/debuggingCMDLine    master +1 !1  python -m pdb main.py main.py                                                                                 ✔  53s   base  
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(1)<module>()
-> values = [10, 6, 17, 5, 14, 18, 85, 0, 9, 12, 13]
(Pdb) until 6
1.0
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(6)<module>()
-> if value % 5 == 0:
(Pdb) next
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(7)<module>()
-> print('Div by 5')
(Pdb) next
Div by 5
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(8)<module>()
-> print("Hello Paul")
(Pdb) next
Hello Paul
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(3)<module>()
-> for value in values:
(Pdb) next
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(5)<module>()
-> print(10 / value)
(Pdb) p value
6
(Pdb) until 6
1.6666666666666667
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(6)<module>()
-> if value % 5 == 0:
(Pdb) q
    ~/neuralNineProjects/debuggingCMDLine    master +1 !1  python -m pdb main.py main.py                                                                              ✔  1m 30s   base  
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(1)<module>()
-> values = [10, 6, 17, 5, 14, 18, 85, 0, 9, 12, 13]
(Pdb) tbreak 6
Breakpoint 1 at /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py:6
(Pdb) c
1.0
Deleted breakpoint 1 at /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py:6
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(6)<module>()
-> if value % 5 == 0:
(Pdb) c
Div by 5
Hello Paul
1.6666666666666667
Hello Paul
0.5882352941176471
Hello Paul
2.0
Div by 5
Hello Paul
0.7142857142857143
Hello Paul
0.5555555555555556
Hello Paul
0.11764705882352941
Div by 5
Hello Paul
Traceback (most recent call last):
  File "/Users/paulthomas/opt/anaconda3/lib/python3.9/pdb.py", line 1726, in main
    pdb._runscript(mainpyfile)
  File "/Users/paulthomas/opt/anaconda3/lib/python3.9/pdb.py", line 1586, in _runscript
    self.run(statement)
  File "/Users/paulthomas/opt/anaconda3/lib/python3.9/bdb.py", line 580, in run
    exec(cmd, globals, locals)
  File "<string>", line 1, in <module>
  File "/Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py", line 6, in <module>
    if value % 5 == 0:
ZeroDivisionError: division by zero
Uncaught exception. Entering post mortem debugging
Running 'cont' or 'step' will restart the program
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(6)<module>()
-> if value % 5 == 0:
(Pdb) --KeyboardInterrupt--
(Pdb) q
Post mortem debugger finished. The /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py will be restarted
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(1)<module>()
-> values = [10, 6, 17, 5, 14, 18, 85, 0, 9, 12, 13]
(Pdb) q
    ~/neuralNineProjects/debuggingCMDLine    master +1 !1  python -m pdb main.py main.py                                                                                 ✔  57s   base  
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(1)<module>()
-> values = [10, 6, 17, 5, 14, 18, 85, 0, 9, 12, 13]
(Pdb) next
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(3)<module>()
-> for value in values:
(Pdb) next
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(5)<module>()
-> print(10 / value)
(Pdb) next
1.0
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(6)<module>()
-> if value % 5 == 0:
(Pdb) next
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(7)<module>()
-> print('Div by 5')
(Pdb) next
Div by 5
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(8)<module>()
-> print("Hello Paul")
(Pdb) 
Hello Paul
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(3)<module>()
-> for value in values:
(Pdb) 
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(5)<module>()
-> print(10 / value)
(Pdb) p value
6
(Pdb) jump 6
> /Users/paulthomas/neuralNineProjects/debuggingCMDLine/main.py(6)<module>()
-> if value % 5 == 0:
(Pdb) p value
6
(Pdb) l
  1     values = [10, 6, 17, 5, 14, 18, 85, 0, 9, 12, 13]
  2     
  3     for value in values:
  4         # breakpoint()
  5         print(10 / value)
  6  ->     if value % 5 == 0:
  7             print('Div by 5')
  8         print("Hello Paul")
[EOF]
(Pdb) p value
6
(Pdb) q
    ~/neuralNineProjects/debuggingCMDLine    master +1 !1                                                                                                             ✔  1m 26s   base  


"""

