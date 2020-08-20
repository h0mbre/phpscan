## phpscan
A hacky python3 script to search for php files with traditionally vulnerable functions. 
Currently looks for: 
+ system
+ shell_exec
+ exec
+ passthru
+ popen
+ proc_open
+ pcntl_exec
+ eval
+ assert

## usage
To just search the current working directory:
```
python3 phpscan.py
```

To search the current working directory recursively:
```
python3 phpscan.py -r
```

To search a specific directory:
```
python3 phpscan.py -d /usr/local/open-audit/code-igniter
```

To search a specific directory recurisively:
```
python3 phpscan.py -d /usr/local/open-audit/code-igniter -r
```

To display the syntax of the vulnerable function call, enable verbose mode:
```
python3 phpscan.py -r -v
```

## non-verbose output example
```
> found 127 php files
> core/Security.php
   eval -- line 446
> core/Loader.php
   eval -- line 830
> libraries/Upload.php
   shell_exec -- line 1034
   exec -- line 1034
   popen -- line 1034
   exec -- line 1044
   exec -- line 1048
   shell_exec -- line 1058
   exec -- line 1058
   popen -- line 1072
> libraries/Email.php
   popen -- line 1575
> libraries/Xmlrpc.php
   eval -- line 1338
   eval -- line 1348
   eval -- line 1377
   eval -- line 1380
> libraries/Image_lib.php
   exec -- line 604
> database/DB.php
   eval -- line 115
   eval -- line 130
   eval -- line 137
> database/drivers/odbc/odbc_driver.php
   exec -- line 154
> database/drivers/postgre/postgre_driver.php
   exec -- line 222
   exec -- line 246
   exec -- line 270
> database/drivers/sqlite/sqlite_driver.php
   popen -- line 86
```

## verbose output example 
```
> found 127 php files
> core/Security.php
   eval -- line 446: eval('some code')
> core/Loader.php
   eval -- line 830: eval('?>'.preg_replace("/;*\s*\?>/", "; ?>", str_replace('<?=', '<?php echo ', file_get_contents($_ci_path))));
> libraries/Upload.php
   shell_exec -- line 1034: shell_exec(), popen() and similar functions
   exec -- line 1034: exec(), shell_
   popen -- line 1034: popen() and similar functions
   exec -- line 1044: exec(), and as such - it overwrites
   exec -- line 1048: exec($cmd, $mime, $return_status);
   shell_exec -- line 1058: shell_exec($cmd);
   exec -- line 1058: exec($cmd);
   popen -- line 1072: popen($cmd, 'r');
> libraries/Email.php
   popen -- line 1575: popen($this->mailpath . " -oi -f ".$this->clean_email($this->_headers['From'])." -t", 'w');
> libraries/Xmlrpc.php
   eval -- line 1338: eval($val2);
   eval -- line 1348: eval($val[$i]);
   eval -- line 1377: eval($this);
   eval -- line 1380: eval($o)
> libraries/Image_lib.php
   exec -- line 604: exec($cmd, $output, $retval);
> database/DB.php
   eval -- line 115: eval()
   eval -- line 130: eval('class CI_DB extends CI_DB_active_record { }');
   eval -- line 137: eval('class CI_DB extends CI_DB_driver { }');
> database/drivers/odbc/odbc_driver.php
   exec -- line 154: exec($this->conn_id, $sql);
> database/drivers/postgre/postgre_driver.php
   exec -- line 222: exec($this->conn_id, "begin");
   exec -- line 246: exec($this->conn_id, "commit");
   exec -- line 270: exec($this->conn_id, "rollback");
> database/drivers/sqlite/sqlite_driver.php
   popen -- line 86: popen($this->database, FILE_WRITE_MODE, $error))
```

