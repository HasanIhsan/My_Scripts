

-- Function to prompt user input and ensure it's a number
function getNumberInput(prompt)
    print(prompt)
    local input = read()
    local number = tonumber(input)
    if number == nil then
        print("Invalid input. Please enter a number.")
        return getNumberInput(prompt)
    else
        return number
    end
end

-- Get width, length, and depth from user input
local width = getNumberInput("Enter the width of the mining area:")
local length = getNumberInput("Enter the length of the mining area:")
local depth = getNumberInput("Enter the depth of the mining area (how many blocks deep):")

function refuelNow()
    for i = 1, 16 do -- loop through the slots
        turtle.select(i) -- change to the slot
        if turtle.refuel(0) then -- if it's valid fuel

        turtle.refuel() -- consume half the stack as fuel
        end
    end

-- Function to check fuel level and output debug info
function checkFuel()
    local fuel = turtle.getFuelLevel()
    local requiredFuel = 20000  -- Total required fuel, including movement back up
  
    if fuel == "unlimited" then
        print("Fuel is unlimited.")
    elseif fuel < requiredFuel then
       
         
        refuelNow()
        fuel = turtle.getFuelLevel()  --   Recheck fuel after refueling
    else
            print("Fuel level sufficient: " .. fuel)
    end
    
    end
end

-- Function to move forward and handle obstacles
function moveForward()
    while not turtle.forward() do
        if turtle.detect() then
            turtle.dig()
        elseif turtle.attack() then
            print("Attacked an entity in the way.")
        else
            print("Waiting for obstacle to clear...")
            sleep(0.5)
        end
    end
end

-- Function to move down and dig
function moveDown()
    while not turtle.down() do
        turtle.digDown()
    end
end

-- Function to turn the turtle at the end of each row (zig-zag pattern)
function turnRight()
    turtle.turnRight()
    moveForward()
    turtle.turnRight()
end

function turnLeft()
    turtle.turnLeft()
    moveForward()
    turtle.turnLeft()
end

-- Function to dig a single row
function digRow()
    for i = 1, width - 1 do
        turtle.digDown()
        moveForward()
    end
    turtle.digDown()  -- Dig at the final position of the row
end

-- Function to return the turtle back up after digging
function returnToSurface()
    for i = 1, depth do
        if not turtle.up() then
            turtle.digUp()
            turtle.up()
        end
    end
end

-- Main function to mine the whole area for each depth layer
-- Main function to mine the whole area for each depth layer
function mineArea()
    checkFuel()  -- Check fuel before starting

    for d = 1, depth do
        print("Mining depth level " .. d)
        for row = 1, length do
            digRow()
            if row < length then
                if row % 2 == 1 then
                    checkFuel()
                    turnRight()
                   
                else
                    checkFuel()
                    turnLeft()
                end
            end
        end

        -- Move down to the next depth level
        if d < depth then
            moveDown()  
            -- After moving down, reorient the turtle to face the original direction
            if length % 2 == 1 then
                turtle.turnRight()  -- Flip direction if the last row was odd
                turtle.turnRight()  -- This resets the direction for the next depth layer
            end
        end
    end

    returnToSurface()  -- Return to the surface once finished
end

-- Start mining the area
mineArea()

