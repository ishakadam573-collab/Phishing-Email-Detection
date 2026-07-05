Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

=== RESTART: C:/Users/20stock/AppData/Local/Programs/Python/Python314/pnq.py ===
Traceback (most recent call last):
  File "C:/Users/20stock/AppData/Local/Programs/Python/Python314/pnq.py", line 9, in <module>
    data = pd.read_csv("emails.csv")
  File "C:\Users\20stock\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\20stock\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\20stock\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\20stock\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Users\20stock\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\common.py", line 930, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'emails.csv'
>>> 
= RESTART: C:/Users/20stock/AppData/Local/Programs/Python/Python314/pnq.py
Traceback (most recent call last):
  File "C:/Users/20stock/AppData/Local/Programs/Python/Python314/pnq.py", line 9, in <module>
    data = pd.read_csv("emails.csv")
  File "C:\Users\20stock\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\20stock\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\20stock\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\20stock\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Users\20stock\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\common.py", line 930, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'emails.csv'
>>> 
= RESTART: C:/Users/20stock/AppData/Local/Programs/Python/Python314/pnq.py
Accuracy: 50.0

Confusion Matrix:
[[0 0]
 [1 1]]

Enter an email (or type exit): exit
