# MyCalculator
A GUI Calculator created by myself

Memory Functions:

    There are some memory functions on this calculator and this is what each one means
        -ms
            * This is a memory set button, when clicked the value on screen takes the slot of memory
        -mc
            * This is a memory clear button, when clicked this will clear the value in memory and set it to 0
        -mr
            * This is a memory recall button, when clicked this will take the value stored in memory and put it on the screen, the user can do whatever operation they want to do with the value
        -m+
            * This value will add whatever value is on screen to the value in memory and then store it in memory
            ex) if memory value = 5 and 2 is on the screen, clicking m+ will change the memory value to 7
        -m-
                        * This value will subtract whatever value is on screen to the value in memory and then store it in memory
            ex) if memory value = 5 and 2 is on the screen, clicking m+ will change the memory value to 3
            
Weather Function:

    There is a weather button that can be found in the 2nd features of the calculator
        - Upon clicking the weather button, a window will pop up requesting the name of the city the user desires
            to get the temperature of
            * If the city exists and the spelling is correct, the temperature should be placed into the entry box on
                calculator
        - The api for this is from the website openweathermap.org
        - If this function continually fails for no apparent reason, the api may have been used too many times and has
            lost access
            * In the case of this, I have recorded myself using the weather function for multiple cities as proof