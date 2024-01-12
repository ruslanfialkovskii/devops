**Bytecode**
```
python -c "import dis; dis.dis('f = (c + 9 / 5) + 32')"
  1           0 LOAD_NAME                0 (c)
              2 LOAD_CONST               0 (1.8)
              4 BINARY_ADD
              6 LOAD_CONST               1 (32)
              8 BINARY_ADD
             10 STORE_NAME               1 (f)
             12 LOAD_CONST               2 (None)
             14 RETURN_VALUE
```

**repl**
Use repl for testing. It is interactive python. 
exit() - for exit from repl