# -*- coding: utf-8 -*-
__author__ = 'Red_C0der'

#   /=============================================================================\
#  |   ██████╗ ███████╗██████╗          ██████╗ ██████╗ ██████╗ ███████╗██████╗    |
#  |   ██╔══██╗██╔════╝██╔══██╗        ██╔════╝██╔═████╗██╔══██╗██╔════╝██╔══██╗   |
#  |   ██████╔╝█████╗  ██║  ██║        ██║     ██║██╔██║██║  ██║█████╗  ██████╔╝   |
#  |   ██╔══██╗██╔══╝  ██║  ██║        ██║     ████╔╝██║██║  ██║██╔══╝  ██╔══██╗   |
#  |   ██║  ██║███████╗██████╔╝███████╗╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║   |
#  |                                                                               |
#  |   Project-Name: Reds Python Lib                                               |
#  |   Version: 0.0.1                                                              |
#  |   Development-State: Alpha                                                    |
#  |   Project-ID: 0024                                                            |
#  |   GitHub-Page: https://github.com/Red-C0der/                                  |
#  |   License: /LICENSE.txt                                                       |
#  |                                                                               |
#  |                                                                               |
#  |   Personal-Info:                                                              |
#  |   Twitter: https://twitter.com/red_c0der                                      |
#  |   FaceBook: -                                                                 |
#  |   E-Mail: redc0der.mail@gmail.com                                             |
#   \=============================================================================/

# TODO: Add customPrint(sender, message, debug=0) and replace %color% in message with termcolors / colored colors!


def colorPrint(text, fgc=500, bgc=500, attrc="", newline=True, debug=0):
    from colored import fg, style, attr, bg
    import sys
    if newline is True:
        if fgc != 500:
            if bgc == 500:
                if attrc == "":
                    color = fg(fgc)
                    att = attr(attrc)
                    print (color + text + style.RESET)
                else:
                    color = fg(fgc)
                    att = attr(attrc)
                    print (color + att + text + style.RESET)
            else:
                if attrc == "":
                    color = fg(fgc) + bg(bgc)
                    att = attr(attrc)
                    print (color + text + style.RESET)
                else:
                    color = fg(fgc) + bg(bgc)
                    att = attr(attrc)
                    print (color + att + text + style.RESET)
        else:
            if bgc != 500:
                if attrc == "":
                    color = bg(bgc)
                    att = attr(attrc)
                    print (color + text + style.RESET)
                else:
                    color = bg(bgc)
                    att = attr(attrc)
                    print (color + att + text + style.RESET)
    else:
        if fgc != 500:
            if bgc == 500:
                if attrc == "":
                    color = fg(fgc)
                    att = attr(attrc)
                    sys.stdout.write(color + text + style.RESET)
                else:
                    color = fg(fgc)
                    att = attr(attrc)
                    sys.stdout.write(color + att + text + style.RESET)
            else:
                if attrc == "":
                    color = fg(fgc) + bg(bgc)
                    att = attr(attrc)
                    sys.stdout.write(color + text + style.RESET)
                else:
                    color = fg(fgc) + bg(bgc)
                    att = attr(attrc)
                    sys.stdout.write(color + att + text + style.RESET)
        else:
            if bgc != 500:
                if attrc == "":
                    color = bg(bgc)
                    att = attr(attrc)
                    sys.stdout.write(color + text + style.RESET)
                else:
                    color = bg(bgc)
                    att = attr(attrc)
                    sys.stdout.write(color + att + text + style.RESET)


def statePrint(state, message, debug=0):
    #import reds_py_lib.logger as logger
    #lloc = "File: output.py | Function: statePrint | Message: "
    #logger.write("i", "Trying to use statePrint with arguments: state=["+str(state)+"], message=["+str(message)+"], debug=["+str(debug)+"]!", lloc=lloc)
    import termcolor
    if state == "":
        print("[....] " + message)
    if state == "ok":
        print("[ " + termcolor.colored("OK", "green", attrs=["bold"]) + " ] " + termcolor.colored(message, "green", attrs=["bold"]))
    if state == "error":
        print("[" + termcolor.colored("ERROR", "red", attrs=["blink", "bold"]) + "] " + termcolor.colored(message, "red", attrs=["bold"]))
    if state == "warning":
        # 208
        from colored import fg, attr, style
        print("[" + fg(241) + attr("bold") + attr("blink") + "WARNING" + style.RESET + "] " + fg(241) + attr("bold") + message + style.RESET)
    if state == "info":
        print("[" + termcolor.colored("INFO", "cyan", attrs=["bold"]) + "] " + termcolor.colored(message, "cyan", attrs=["bold"]))
    if state == "debug":
        print("[" + termcolor.colored("DEBUG", "magenta", attrs=["bold"]) + "] " + termcolor.colored(message, "magenta", attrs=["bold"]))
    if state == "sys":
        print("[" + termcolor.colored("SYSTEM", "blue", attrs=["bold"]) + "] " + termcolor.colored(message, "blue", attrs=["bold"]))

#  For more Information about the message_as_list_with_ccodes argument, visit the Wiki!
def customPrint(message_as_list_with_ccodes, debug=0):
    import sys
    import termcolor
    for item in message_as_list_with_ccodes:
        output = ""
        if "[%" in item and "%]" in item or "[$" in item and "$]" in item:
            open_bracket = False
            close_bracket = False
            perc = 0
            dollar = 0
            plain_text = ""
            formatter = ""
            attribute = ""
            curr_read_state = "plain_text"
            last_read_state = ""
            for char in item:
                if char == "[":
                    close_bracket = False
                    open_bracket = True
                elif char == "%":
                    if perc == 0:
                        perc = 1
                    elif perc == 1:
                        perc = 0
                elif char == "$":
                    if dollar == 0:
                        dollar = 1
                    elif dollar == 1:
                        dollar = 0
                elif char == "]":
                    open_bracket = False
                    close_bracket = True

                if open_bracket == True and perc == 1:
                    last_read_state = curr_read_state
                    curr_read_state = "formatter"
                elif close_bracket == True and perc == 0:
                    last_read_state = curr_read_state
                    curr_read_state = "plain_text"
                elif open_bracket == True and dollar == 1:
                    last_read_state = curr_read_state
                    curr_read_state = "attribute"
                elif close_bracket == True and dollar == 0:
                    last_read_state = curr_read_state
                    curr_read_state = "plain_text"
                else:
                    pass

                if curr_read_state == "plain_text":
                    if last_read_state == "formatter":
                        if char == "]":
                            pass
                    elif last_read_state == "attribute":
                        if char == "]":
                            pass
                    else:
                        plain_text = plain_text + char
                elif curr_read_state == "formatter":
                    plain_text = plain_text[:-1]
                    if char is not "$" or "%":
                        formatter = formatter + char
                elif curr_read_state == "attribute":
                    plain_text = plain_text[:-1]
                    if char is not "$" or "%":
                        attribute = attribute + char

                #print "====================================="
                #print "Stats:"
                #print "item = " + str(item)
                #print "char = " + str(char)
                #print "open_bracket = " + str(open_bracket)
                #print "close_bracket = " + str(close_bracket)
                #print "perc = " + str(perc)
                #print "dollar = " + str(dollar)
                #print "plain_text = " + plain_text
                #print "formatter = " + formatter
                #print "attribute = " + attribute
                #print "curr_read_state = " + curr_read_state
                #print "last_read_state = " + last_read_state

            # Last Variable Cleanups
            formatter = formatter.strip("%")
            attribute = attribute.strip("$")

            if attribute != "" and formatter != "":
                output = termcolor.colored(plain_text, formatter, attrs=[attribute])
            elif attribute == "" and formatter != "":
                output = termcolor.colored(plain_text, formatter)

        else:
            output = item
        sys.stdout.write(output)