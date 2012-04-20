### Welcome to the *php api signature*!

## what?

I love VIM and I write a lot php program using VIM, so I need a php functions list to improve my VIM. This python script can build a list of php api signature from php document.

## how to?

    download the php document(Many HTML files) and unzip it to some dir, eg: /home/simon/php-chunked-xhtml/
    
 - test it
 
    python php-api-signature.py /path/to/php-chunked-xhtml/function.mysql-query.html
    
 - generate all the php api signature
    
    for i in $(ls /home/simon/php-chunked-xhtml/); do python php-api-signature.py "/home/simon/php-chunked-xhtml/$i"; done;
    
    the output is like this:

    abstract bool FilterIterator::accept ( void )

    abstract int SplHeap::compare ( mixed $value1 , mixed $value2 )

    abstract public array Yaf_Config_Abstract::toArray ( void )

    ......

    you can redirect the output to some file:

    for i in $(ls /home/simon/php-chunked-xhtml/); do python php-api-signature.py "/home/simon/php-chunked-xhtml/$i" >> phpfuncs.txt; done;
