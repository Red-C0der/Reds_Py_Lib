# coding=utf-8
__author__ = 'Red_C0der'

#   /=============================================================================\
#  |   ██████╗ ███████╗██████╗          ██████╗ ██████╗ ██████╗ ███████╗██████╗    |
#  |   ██╔══██╗██╔════╝██╔══██╗        ██╔════╝██╔═████╗██╔══██╗██╔════╝██╔══██╗   |
#  |   ██████╔╝█████╗  ██║  ██║        ██║     ██║██╔██║██║  ██║█████╗  ██████╔╝   |
#  |   ██╔══██╗██╔══╝  ██║  ██║        ██║     ████╔╝██║██║  ██║██╔══╝  ██╔══██╗   |
#  |   ██║  ██║███████╗██████╔╝███████╗╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║   |
#  |                                                                               |
#  |   Project-Name: Reds Python Lib                                               |
#  |   Version: 0.0.2                                                              |
#  |   Development-State: Alpha                                                    |
#  |   Project-ID: 0024                                                            |
#  |   GitHub-Page: https://red-c0der.github.io/Reds_Py_Lib/site/index.html        |
#  |   License: /LICENSE.txt                                                       |
#  |                                                                               |
#  |                                                                               |
#  |   Personal-Info:                                                              |
#  |   Twitter: https://twitter.com/red_c0der                                      |
#  |   FaceBook: -                                                                 |
#  |   E-Mail: redc0der.mail@gmail.com                                             |
#   \=============================================================================/




def write(level, message, lloc="", LogFile=""):
    try:
        import logging
        if LogFile == "":
            from time import gmtime, strftime
            LogName = strftime("%d-%m-%Y", gmtime())
            LogLoc = "../logs/"
            LogF = LogLoc+LogName+".log"
        else:
            LogF = LogFile
        logging.basicConfig(filename=LogF, level=logging.DEBUG, format='%(asctime)s | %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S')
        if lloc != "":
            if level == "i":
                logging.info(lloc+message)
            if level == "w":
                logging.warning(lloc+message)
            if level == "e":
                logging.error(lloc+message)
            if level == "c":
                logging.critical(lloc+message)
            if level == "ex":
                logging.exception(lloc+message)
            if level == "d":
                logging.debug(lloc+message)
            if level != "i" and level != "w" and level != "e" and level != "c" and level != "ex" and level != "d":
                import inspect
                logging.exception("Function " + inspect.stack()[1][3] + " tried to use logger.write() with invalid logging level " + level +  " !")
                return False
            return True
        else:
            if level == "i":
                logging.info(message)
            if level == "w":
               logging.warning(message)
            if level == "e":
                logging.error(message)
            if level == "c":
                logging.critical(message)
            if level == "ex":
                logging.exception(message)
            if level == "d":
                logging.debug(message)
            if level != "i" and level != "w" and level != "e" and level != "c" and level != "ex" and level != "d":
                import inspect
                logging.exception("Function " + inspect.stack()[1][3] + " tried to use logger.write() with invalid logging level " + level +  " !")
                return False
            return True
    except StopIteration:
        write("e", "StopIteration: next() method does not point at any object!", lloc=lloc)
        return False
    except SystemExit:
        write("e", "SystemExit: sys.exit() was executed!", lloc=lloc)
        return False
    except ArithmeticError:
        write("e", "ArithmeticError: Numeric calculation error!", lloc=lloc)
        return False
    except OverflowError:
        write("e", "OverflowError: Calculation exceeded maximum limit for numeric type!", lloc=lloc)
        return False
    except FloatingPointError:
        write("e", "FloatingPointError: FloatingPoint calculation failed!", lloc=lloc)
        return False
    except ZeroDivisionError:
        write("e", "ZeroDivisionError: Division or modulo by Zero took place!", lloc=lloc)
        return False
    except AssertionError:
        write("e", "AssertionError: Assert statement failed!", lloc=lloc)
        return False
    except AttributeError:
        write("e", "AttributeError: Failure of attribute reference or assignment!", lloc=lloc)
        return False
    except EOFError:
        write("e", "EOFError: No input from raw_input() or input() as the file has ended!", lloc=lloc)
        return False
    except ImportError:
        write("e", "ImportError: Import statement failed!", lloc=lloc)
        return False
    except KeyboardInterrupt:
        write("e", "KeyboardInterrupt: Program has ended, during KeyboardInterrupt (Ctrl + C)!", lloc=lloc)
        return False
    except LookupError:
        write("e", "LookupError: LookupError!", lloc=lloc)
        return False
    except IndexError:
        write("e", "IndexError: Index in sequence was not found!", lloc=lloc)
        return False
    except KeyError:
        write("e", "KeyError: Key in dictionary was not found!", lloc=lloc)
        return False
    except NameError:
        write("e", "NameError: Identifier was not found in local or global namespace!", lloc=lloc)
        return False
    except UnboundLocalError:
        write("e", "UnboundLocalError: No value was assigned to variable in function or method!", lloc=lloc)
        return False
    except EnvironmentError:
        write("e", "EnvironmentError: Exception occurred outside the Python environment!", lloc=lloc)
        return False
    except IOError:
        write("e", "IOError: Input / Output operation failed!", lloc=lloc)
        return False
    except SyntaxError:
        write("e", "SyntaxError: Syntax error in python code!", lloc=lloc)
        return False
    except IndentationError:
        write("e", "IndentationError: Indentation is not specified properly!", lloc=lloc)
        return False
    except SystemError:
        write("e", "SystemError: Interpreter found internal problem, but interpreter has not exited!", lloc=lloc)
        return False
    except TypeError:
        write("e", "TypeError: Operation or Function is attempted which is invalid for the specific data type!", lloc=lloc)
        return False
    except ValueError:
        write("e", "ValueError: Built-in function for data type has valid type of arguments, but arguments have invalid values specified!", lloc=lloc)
        return False
    except RuntimeError:
        write("e", "RuntimeError: Generated error does not fall into any category!", lloc=lloc)
        return False
    except NotImplementedError:
        write("e", "NotImplementedError: Abstract method that needs to be implemented in an inherited class is not actually implemented!", lloc=lloc)
        return False