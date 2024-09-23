; Mining automation for Minecraft using AHK
#Persistent
SetTitleMatchMode, 2  ; Makes sure script works when part of the window title is matched
WinActivate, Minecraft ; Ensures Minecraft is the active window

; Variables for width, height, and delay
width := 10  ; Width of the mining area
height := 10  ; Height of the mining area
move_delay := 200  ; Delay between moves in milliseconds
turn_sensitivity := 500  ; Adjusted sensitivity for turning (higher value for larger turn)
stop_mining := false  ; Flag to stop the mining

; Key to start mining (Alt + M)
!m::
    stop_mining := false  ; Reset the stop flag
    Loop %height%  ; Loop over rows (height of the area)
    {
        if (stop_mining)  ; Break out of loop if stop is triggered
            break

        Loop %width%  ; Mine a single row (width of the area)
        {
            if (stop_mining)  ; Break out of loop if stop is triggered
                break

            ; Simulate mining (holding left-click)
            Click Down
            Sleep 100  ; Delay for holding left-click
            Click Up

            ; Move forward (W key)
            Send {w Down}
            Sleep %move_delay%
            Send {w Up}
        }

        if (stop_mining)  ; Break out of loop if stop is triggered
            break

        ; End of row: Turn and move to the next row
        if (A_Index & 1)  ; If odd row, turn right
        {
            TurnRight()
            Send {d Down}  ; Move one block to the right
            Sleep %move_delay%
            Send {d Up}
            TurnRight()  ; Face the opposite direction for the next row
        }
        else  ; If even row, turn left
        {
            TurnLeft()
            Send {a Down}  ; Move one block to the left
            Sleep %move_delay%
            Send {a Up}
            TurnLeft()  ; Face the opposite direction for the next row
        }
    }
return

; Key to stop mining (Alt + X)
!x::
    stop_mining := true  ; Set the flag to stop the mining loop
return

; Function to turn right (move mouse to the right)
TurnRight()
{
    MouseMove, %turn_sensitivity%, 0, 0
    Sleep 200
}

; Function to turn left (move mouse to the left)
TurnLeft()
{
    MouseMove, -%turn_sensitivity%, 0, 0
    Sleep 200
}
