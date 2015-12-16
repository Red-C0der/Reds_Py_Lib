# Usage

In this section, I'll go over all the classes, functions, files, which you can use with my library!



### File: output.py | Function: customPrint()

This Function can output a message containing formatting and colorcodes

`output.customPrint(message_as_list_with_ccodes, debug=0)`

    message_as_list_with_ccodes - Takes a list, which contains the message!
    
        Example without formatting:
            ["This is", "cool", "stuff", "!"]
        Example with formatting:
            ["This will", "[%green%]be", "[%blue%]colored", "[$bold$]cause colored is cool!"]
    
    debug - Can be 0 or 1. Determinates whether to give back some debug information or not.
    
        debug=0: Will not give back specially detailed debug information.
        debug=1: Will give back specially detailed debug information.



### File: output.py | Function: statePrint()

`output.statePrint(state, message, debug=0)`

    state - Determinates what stands inside the first pair of brackets.
    
        ""        - This stands for working! It will print [....].
                    Use this when you want to print out a working task!
        "ok"      - Message after will be green!
        "error"   - Message after will be red!
        "warning" - Message after will be orange!
        "info"    - Message after will be turquoise and bold!
        "debug"   - Message after will be magenta!
        "sys"     - Message after will be blue!
    
    message - The message, which you want to display after the brackets.
    
    debug - Can be 0 or 1. Determinates whether to give back some debug information or not.
    
        debug=0: Will not give back specially detailed debug information.
        debug=1: Will give back specially detailed debug information.





### File: logger.py | Function: write()

This function handles logging and also the corresponding log-files.

`logger.write(level, message, lloc="", LogFile="")`

    level - The logging level (what it writes in front of the logging message).
        "i"     - INFO
        "w"     - WARNING
        "e"     - ERROR
        "c"     - CRITICAL
        "ex"    - EXCEPTION
        "d"     - DEBUG
    
    message - The message, which it writes after the logging-level
        For example: "This is an informative message!"
    
    lloc = Write this in here and replace it with correct data: "File: Test.py | Class: Main | Function: test | Message: "



