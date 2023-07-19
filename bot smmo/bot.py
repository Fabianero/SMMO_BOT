import pyautogui
import sys
import time

i = 1
b = 2
c = 3

# def Catching
def Catching():
    while i == 1:

        catch = pyautogui.locateOnScreen('catch.png')
        if catch is not None:
            catch = pyautogui.locateOnScreen('catch.png')
            catch1 = pyautogui.center(catch)
            pyautogui.click(catch1)
            pyautogui.moveTo(10, 10)
                
        else:
            Gather_Catching = pyautogui.locateOnScreen('gather.png')
            if Gather_Catching is not None:
                gather = pyautogui.locateOnScreen('gather.png')
                gather1 = pyautogui.center(gather)
                pyautogui.click(gather1)
                pyautogui.moveTo(10, 10)
                    
            else:
                Gather_Catching1 = pyautogui.locateOnScreen('gather1.png')
                if Gather_Catching1 is not None:
                    gather2 = pyautogui.locateOnScreen('gather1.png')
                    gather2_1 = pyautogui.center(gather2)
                    pyautogui.click(gather2_1)
                    pyautogui.moveTo(10, 10)
                        
                else:
                    Close_Catching = pyautogui.locateOnScreen('close.png')
                    if Close_Catching is not None:
                        close = pyautogui.locateOnScreen('close.png')
                        close1 = pyautogui.center(close)
                        pyautogui.click(close1)
                        break
                    else:
                        print('Kolejna iteracja')                          
    return

# def Choping
def Choping():
    while i == 1:
        chop = pyautogui.locateOnScreen('chop.png')
        if chop is not None:
            chop1 = pyautogui.center(chop)
            pyautogui.click(chop1)
            pyautogui.moveTo(10, 10)
        else:
            gather = pyautogui.locateOnScreen('gather.png')
            if gather is not None:
                gather1 = pyautogui.center(gather)
                pyautogui.click(gather1)
                pyautogui.moveTo(10, 10)
            else:
                gather2 = pyautogui.locateOnScreen('gather1.png')
                if gather2 is not None:
                    gather2_1 = pyautogui.center(gather2)
                    pyautogui.click(gather2_1)
                    pyautogui.moveTo(10, 10)
                else:
                    close = pyautogui.locateOnScreen('close.png')
                    if close is not None:
                        close1 = pyautogui.center(close)
                        pyautogui.click(close1)
                        pyautogui.moveTo(10, 10)
                        break
                    
                    else:
                        print('Kolejna iteracja')                       
    return

# def Attack
def Attacking():
    while i == 1:
        attack = pyautogui.locateOnScreen('attack.png')
        if attack is not None:
            attack = pyautogui.locateOnScreen('attack.png')
            attack1 = pyautogui.center(attack)
            pyautogui.click(attack1)
            pyautogui.moveTo(10, 10)
        else:
            attack_cont = pyautogui.locateOnScreen('attack_test.png')
            if attack_cont is not None:
                attack2 = pyautogui.locateOnScreen('attack_test.png')
                attack21 = pyautogui.center(attack2)
                pyautogui.click(attack21)
                pyautogui.moveTo(10, 10)

            else:
                attack_end = pyautogui.locateOnScreen('end.png')
                if attack_end is not None:
                    end = pyautogui.locateOnScreen('end.png')
                    end2 = pyautogui.center(end)
                    pyautogui.click(end2)
                    pyautogui.moveTo(10, 10)
                    break
                else:
                    print('kolejna iteracja')         
    return

# def Salvage
def Salvaging():
    while i == 1:
        salvage = pyautogui.locateOnScreen('salvage.png')
        if salvage is not None:
            salvage = pyautogui.locateOnScreen('salvage.png')
            salvage1 = pyautogui.center(salvage)
            pyautogui.click(salvage1)
            pyautogui.moveTo(10, 10)
        else:
            Gather_Salvage = pyautogui.locateOnScreen('gather.png')
            if Gather_Salvage is not None:
                gather = pyautogui.locateOnScreen('gather.png')
                gather1 = pyautogui.center(gather)
                pyautogui.click(gather1)
                pyautogui.moveTo(10, 10)
            else:
                Gather_Salvage1 = pyautogui.locateOnScreen('gather1.png')
                if Gather_Salvage1 is not None:
                    gather2 = pyautogui.locateOnScreen('gather1.png')
                    gather2_1 = pyautogui.center(gather2)
                    pyautogui.click(gather2_1)
                    pyautogui.moveTo(10, 10)
                else:
                    Close_Salvage = pyautogui.locateOnScreen('close.png')
                    if Close_Salvage is not None:
                        close = pyautogui.locateOnScreen('close.png')
                        close1 = pyautogui.center(close)
                        pyautogui.click(close1)
                        pyautogui.moveTo(10, 10)
                        break
                    else:
                        print('kolejan iteracja')
    return

# def Mining
def Mining():
    while i == 1:
                Mine = pyautogui.locateOnScreen('mine.png')
                if Mine is not None:
                    mine = pyautogui.locateOnScreen('mine.png')
                    mine1 = pyautogui.center(mine)
                    pyautogui.click(mine1)
                    pyautogui.moveTo(10, 10)
                        
                else:
                    Gather_Mining = pyautogui.locateOnScreen('gather.png')
                    if Gather_Mining is not None:
                        gather = pyautogui.locateOnScreen('gather.png')
                        gather1 = pyautogui.center(gather)
                        pyautogui.click(gather1)
                        pyautogui.moveTo(10, 10)
                            
                    else:
                        Gather_Mining1 = pyautogui.locateOnScreen('gather1.png')
                        if Gather_Mining1 is not None:
                            gather2 = pyautogui.locateOnScreen('gather1.png')
                            gather2_1 = pyautogui.center(gather2)
                            pyautogui.click(gather2_1)
                            pyautogui.moveTo(10, 10)

                        else:
                            Close_Mining = pyautogui.locateOnScreen('close.png')
                            if Close_Mining is not None:
                                close = pyautogui.locateOnScreen('close.png')
                                close1 = pyautogui.center(close)
                                pyautogui.click(close1)
                                pyautogui.moveTo(10, 10)
                                break
                            else:
                                print('kolejna iteracja')                 
    return

while b == 2:

# Stepping
    while c == 3:
        if pyautogui.locateOnScreen('step.png'):
            step = pyautogui.locateOnScreen('step.png')
            step1 = pyautogui.center(step)
            pyautogui.click(step1)
            pyautogui.moveTo(10, 10)

        elif pyautogui.locateOnScreen('catch.png'):
            Catching()
        elif pyautogui.locateOnScreen('chop.png'):
            Choping()
        elif pyautogui.locateOnScreen('attack.png'):
            Attacking()
        elif pyautogui.locateOnScreen('salvage.png'):
            Salvaging()
        elif pyautogui.locateOnScreen('mine.png'):
            Mining()

        else:
            print('przejscie dalej')

else:
    print('koniec')