# ------------------------------------------------------------------------#
# pattern                                                                 #
# ------------------------------------------------------------------------#
# Purpose: Create patterns of alternating characters, to a specified size #
# Author:Samuel Pitchforth                                                #
# Date: 25/03/2022                                                        #
# ------------------------------------------------------------------------#

BEGIN pattern
    print - - - - - - - - - - - - - - -
    print | Pattern generator
    print - - - - - - - - - - - - - - -
    GET userinput char_one
    Get userinpur char_two
    GET num

    //if the first character isnt exactly 1 symbol give an error
    //and request a new one
    WHILE char_one length != 1
        print |    ---ERROR---
        print |   Character 1 must
        print Re-enter
        get userinput char_one
    ENDWHILE

    //same as above for char_two

    WHILE num < 2 | num > 50
        print |       ---ERROR---
        print |   Number must be within
        print |        range 2-50
        print Re - enter
        get userinput nump
    ENDWHILE

    print - - - - - - - - - - - - - - -
    print -
    //times numpy

    FOR y = 0 TO num STEP 1
        FOR x = 0 TO num STEP 1
            IF x+y is even
                print char_one
            ELSE
                print char_two
            ENDIF
        NEXT x
        print
    NEXT y
    print -
    //times numpy
END pattern

