
#
#   generatePlinths - creates 5 brushes from 30 planes to create a new plinth
#

def generatePlinths (r, o):
    for p in rooms[r].plinths:

        floor = getFloorLevel(r)*inchesPerUnit
        o.write ('    // plinth middle \n')
        o.write ('    {\n')
        o.write ('         brushDef3\n')
        o.write ('         {\n')
        o.write ('             ( 1 0 0 '+ str(distance([(p[0]-1+0.25)*inchesPerUnit, (p[1]-1+0.5)*inchesPerUnit, floor], -1, 0, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 1 0 '+ str(distance([(p[0]-1+0.5)*inchesPerUnit, (p[1]-1+0.25)*inchesPerUnit, floor], 0, -1, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 -1 0 '+ str(distance([(p[0]-1+0.5)*inchesPerUnit, (p[1]-1+0.75)*inchesPerUnit, floor], 0, 1, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( -1 0 0 '+ str(distance([(p[0]-1+0.75)*inchesPerUnit, (p[1]-1+0.5)*inchesPerUnit, floor], 1, 0, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 0 -1 '+ str(distance([(p[0]-1+0.5)*inchesPerUnit, (p[1]-1+0.5)*inchesPerUnit, floor], 0, 0, -1)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 0 1 '+ str(distance([(p[0]-1+0.5)*inchesPerUnit, (p[1]-1+0.5)*inchesPerUnit, (floor+p[2])], 0, 0, 1)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('         }\n')
        o.write ('    }\n')
        o.write ('    // plinth high top \n')
        o.write ('    {\n')
        o.write ('         brushDef3\n')
        o.write ('         {\n')
        o.write ('             ( 1 0 0 '+ str(distance([(p[0]-1)*inchesPerUnit, (p[1]-1+0.5)*inchesPerUnit, floor], -1, 0, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 1 0 '+ str(distance([(p[0]-1+0.5)*inchesPerUnit, (p[1]-1)*inchesPerUnit, floor], 0, -1, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 -1 0 '+ str(distance([(p[0]-1+0.5)*inchesPerUnit, (p[1]-1+1)*inchesPerUnit, floor], 0, 1, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( -1 0 0 '+ str(distance([(p[0]-1+1)*inchesPerUnit, (p[1]-1+0.5)*inchesPerUnit, floor], 1, 0, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 0 -1 '+ str(distance([(p[0]-1+0.5)*inchesPerUnit, (p[1]-1+0.5)*inchesPerUnit, (floor + p[2]-6)], 0, 0, -1)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 0 1 '+ str(distance([(p[0]-1+0.5)*inchesPerUnit, (p[1]-1+0.5)*inchesPerUnit, (floor + p[2])], 0, 0, 1)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('         }\n')
        o.write ('    }\n')

        o.write ('    // plinth low top \n')
        o.write ('    {\n')
        o.write ('         brushDef3\n')
        o.write ('         {\n')
        o.write ('             ( 1 0 0 '+ str(distance([(p[0]-1+0.125)*inchesPerUnit, (p[1]-1+0.5)*inchesPerUnit, floor], -1, 0, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 1 0 '+ str(distance([(p[0]-1+0.5)*inchesPerUnit, (p[1]-1+0.125)*inchesPerUnit, floor], 0, -1, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 -1 0 '+ str(distance([(p[0]-1+0.5)*inchesPerUnit, (p[1]-1+0.875)*inchesPerUnit, floor], 0, 1, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( -1 0 0 '+ str(distance([(p[0]-1+0.875)*inchesPerUnit, (p[1]-1+0.5)*inchesPerUnit, floor], 1, 0, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 0 -1 '+ str(distance([(p[0]-1+0.5)*inchesPerUnit, (p[1]-1+0.5)*inchesPerUnit, (floor + p[2]-12)], 0, 0, -1)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 0 1 '+ str(distance([(p[0]-1+0.5)*inchesPerUnit, (p[1]-1+0.5)*inchesPerUnit, (floor + p[2])], 0, 0, 1)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('         }\n')
        o.write ('    }\n')

        o.write ('    // plinth low bottom \n')
        o.write ('    {\n')
        o.write ('         brushDef3\n')
        o.write ('         {\n')
        o.write ('             ( 1 0 0 '+ str(distance([(p[0]-1)*inchesPerUnit, (p[1]-1+0.5)*inchesPerUnit, floor], -1, 0, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 1 0 '+ str(distance([(p[0]-1+0.5)*inchesPerUnit, (p[1]-1)*inchesPerUnit, floor], 0, -1, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 -1 0 '+ str(distance([(p[0]-1+0.5)*inchesPerUnit, (p[1]-1+1)*inchesPerUnit, floor], 0, 1, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( -1 0 0 '+ str(distance([(p[0]-1+1)*inchesPerUnit, (p[1]-1+0.5)*inchesPerUnit, floor], 1, 0, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 0 -1 '+ str(distance([(p[0]-1+0.5)*inchesPerUnit, (p[1]-1+0.5)*inchesPerUnit, (floor)], 0, 0, -1)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 0 1 '+ str(distance([(p[0]-1+0.5)*inchesPerUnit, (p[1]-1+0.5)*inchesPerUnit, (floor+6)], 0, 0, 1)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('         }\n')
        o.write ('    }\n')

        o.write ('    // plinth low top \n')
        o.write ('    {\n')
        o.write ('         brushDef3\n')
        o.write ('         {\n')
        o.write ('             ( 1 0 0 '+ str(distance([(p[0]-1+0.125)*inchesPerUnit, (p[1]-1+0.5)*inchesPerUnit, floor], -1, 0, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 1 0 '+ str(distance([(p[0]-1+0.5)*inchesPerUnit, (p[1]-1+0.125)*inchesPerUnit, floor], 0, -1, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 -1 0 '+ str(distance([(p[0]-1+0.5)*inchesPerUnit, (p[1]-1+0.875)*inchesPerUnit, floor], 0, 1, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( -1 0 0 '+ str(distance([(p[0]-1+0.875)*inchesPerUnit, (p[1]-1+0.5)*inchesPerUnit, floor], 1, 0, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 0 -1 '+ str(distance([(p[0]-1+0.5)*inchesPerUnit, (p[1]-1+0.5)*inchesPerUnit, (floor)], 0, 0, -1)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 0 1 '+ str(distance([(p[0]-1+0.5)*inchesPerUnit, (p[1]-1+0.5)*inchesPerUnit, (floor+12)], 0, 0, 1)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('         }\n')
        o.write ('    }\n')

#
#   WriteStep - compiles 6 planes into a brush to create a single step
#

def WriteStep(posX, posY, tread, rise, floor, stepNo, o):
    o.write ('    // step \n')
    o.write ('    {\n')
    o.write ('         brushDef3\n')
    o.write ('         {\n')
    o.write ('             ( 1 0 0 '+ str(distance([(posX)*inchesPerUnit, (posY)*inchesPerUnit+stepNo*tread, floor], -1, 0, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
    o.write ('             ( 0 1 0 '+ str(distance([(posX)*inchesPerUnit, (posY)*inchesPerUnit-tread+stepNo*tread, floor], 0, -1, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
    o.write ('             ( 0 -1 0 '+ str(distance([(posX)*inchesPerUnit, (posY)*inchesPerUnit+stepNo*tread, floor], 0, 1, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
    o.write ('             ( -1 0 0 '+ str(distance([(posX)*inchesPerUnit+48, (posY)*inchesPerUnit+stepNo*tread, floor], 1, 0, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
    o.write ('             ( 0 0 -1 '+ str(distance([(posX)*inchesPerUnit, (posY)*inchesPerUnit+stepNo*tread, floor], 0, 0, -1)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
    o.write ('             ( 0 0 1 '+ str(distance([(posX)*inchesPerUnit, (posY)*inchesPerUnit+stepNo*tread, floor+rise*stepNo], 0, 0, 1)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
    o.write ('         }\n')
    o.write ('    }\n')

#
#   generateStairs - generates a stair staircase, each loop creates a single step
#

def generateStairs (r, o):
    tread = 11
    rise = 6
    numberofSteps = 25
    for p in rooms[r].stairs:
        for s in range(numberofSteps):
            WriteStep(p[0]-1, p[1]-1, tread, rise, getFloorLevel(r)*inchesPerUnit, s, o)

#def RotateNormalAboutZ(nX, nY, nZ, rotation, outputText):
#    rotX = nX*math.cos(rotation) - nY*math.sin(rotation)
#    rotY = nX*math.sin(rotation) + nY*math.cos(rotation)
#    if outputText:
#        return str(str(rotX)+" "+str(rotY)+" "+str(nZ)+" ")
#    else:
#        print(str([rotX, rotY, nZ]))
#        return [rotX, rotY, nZ]

#
#   WriteSpiralStepFace - This does the heavy lifting for creating the spiral staircase
#

def WriteSpiralStepFace(posX, posY, nX, nY, nZ, rotation, floorLevel, tread, width, rise, o):
    #Convert the positions to inches instead of units
    posX = posX*inchesPerUnit
    posY = posY*inchesPerUnit
    #initialise offsets
    Xoffset = 0
    Yoffset = 0
    
    #Rotate the X and Y planes, Z is fine
    NormalX = 0 + math.cos(rotation*math.pi/180) * (nX - 0) - math.sin((radians(-rotation))) * (nY - 0)
    NormalY = 0 - math.sin(rotation*math.pi/180) * (nX - 0) + math.cos((radians(-rotation))) * (nY - 0)
    NormalZ = nZ #If I change the radians or remove the zeros the code breaks, ask Gaius about this

    #offset rotations 
    Xoffset = 0 + math.cos(radians(rotation)) * (tread - 0) - math.sin((-radians(rotation))) * (width - 0)
    Yoffset = 0 - math.sin(radians(rotation)) * (tread - 0) + math.cos((-radians(rotation))) * (width - 0)

    #work out the distance from the face to map origin
    FaceDistance = - ((-posX+Xoffset) * NormalX + NormalY * (-posY+Yoffset) + NormalZ * (floorLevel+rise))

    #FaceDistance = - ((-posX+Xoffset) * NormalX + NormalY * (-posY+Yoffset) + NormalZ * (floorLevel+rise))
    #FaceDistance = - ((-Xoffset) * NormalX + NormalY * (-Yoffset) + NormalZ * (floorLevel+rise))

    o.write ('             ( '+str(NormalX)+' '+str(NormalY)+' '+str(NormalZ)+' '+str(FaceDistance)+' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
    o.write ('// '+str(posX)+'   '+str(posY)+'   '+str(Xoffset)+"  "+str(Yoffset))

#
#   WriteSpiralStep - Where the planes of the step are called and assembled into a brush
#

def WriteSpiralStep(posX, posY, tread, rise, floor, stepNo, rotation, o):
    o.write ('    // spiralstep \n')
    o.write ('    {\n')
    o.write ('         brushDef3\n')
    o.write ('         {\n')
    WriteSpiralStepFace(posX, posY, 1, -0.07, 0, rotation, floor, 5.5, 0, 0, o) #side
    o.write ('    // side \n')
    WriteSpiralStepFace(posX, posY, 0, 1, 0, rotation, floor, 0, 128, 0, o) #wide end
    o.write ('    // wide end \n')
    WriteSpiralStepFace(posX, posY, 0, -1, 0, rotation, floor, 0, -8, 0, o) #narrow end
    o.write ('    // narrow end \n')
    WriteSpiralStepFace(posX, posY, -1, -0.07, 0, rotation, floor, -5.5, 0, 0, o) #side
    o.write ('    // side \n')
    WriteSpiralStepFace(posX, posY, 0, 0, -1, rotation, floor, 0, 0, 0, o) #bottom
    o.write ('    // bottom \n')
    WriteSpiralStepFace(posX, posY, 0, 0, 1, rotation, floor, 0, 0, 6, o) #top
    o.write ('    // top \n')
    o.write ('         }\n')
    o.write ('    }\n')
    print("step no "+str(stepNo))


#
# generateSpiralStairs - the first of the 3 functions used to draw a spiral staircase
#

def generateSpiralStairs (r, o):
    rise = 6
    tread = 11
    numberofSteps = 25
    for p in rooms[r].spiralstairs:
        for s in range(numberofSteps):
            WriteSpiralStep(p[0]-1, p[1]-1, tread, rise, getFloorLevel(r)*inchesPerUnit+rise*s, s, s*15, o)

#
#generateInnerWalls - draws a single cuboid from 6 planes to act as a wall, identical to the old plinths
#

def generateInnerWalls (r, o):
    for p in rooms[r].innerwalls:
        floor = getFloorLevel(r)*inchesPerUnit
        print(str(floor))
        #pos = [int (p[0]+1), int (p[1]+1), getFloorLevel (r)]
        #size = [1, 1, float (p[2]) / inchesPerUnit]
        #newcuboid (pos, size, 'plinth', r)
        o.write ('    {\n')
        o.write ('         brushDef3\n')
        o.write ('         {\n')
        o.write ('             ( 1 0 0 '+ str(distance([(p[0]-1)*inchesPerUnit, (p[1]-0.5)*inchesPerUnit, floor], -1, 0, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 1 0 '+ str(distance([(p[0]-0.5)*inchesPerUnit, (p[1]-0)*inchesPerUnit, floor], 0, -1, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 -1 0 '+ str(distance([(p[0]-0.5)*inchesPerUnit, (p[1])*inchesPerUnit, floor], 0, 1, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( -1 0 0 '+ str(distance([(p[0])*inchesPerUnit, (p[1]-0.5)*inchesPerUnit, floor], 1, 0, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 0 -1 '+ str(distance([(p[0]-0.5)*inchesPerUnit, (p[1]-0.5)*inchesPerUnit, floor], 0, 0, -1)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 0 1 '+ str(distance([(p[0]-0.5)*inchesPerUnit, (p[1]-0.5)*inchesPerUnit, (floor+p[2])], 0, 0, 1)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('         }\n')
        o.write ('    }\n')

#
# generateWindows - draws 2 cuboids from planes with a gap between them, looks like a window between other windows or walls
#

def generateWindows (r, o):
    for p in rooms[r].windows:
        floor = getFloorLevel(r)*inchesPerUnit
        o.write ('    {\n')
        o.write ('         brushDef3\n')
        o.write ('         {\n')
        o.write ('             ( 1 0 0 '+ str(distance([(p[0]-1)*inchesPerUnit, (p[1]-0.5)*inchesPerUnit, floor], -1, 0, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 1 0 '+ str(distance([(p[0]-0.5)*inchesPerUnit, (p[1]-1)*inchesPerUnit, floor], 0, -1, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 -1 0 '+ str(distance([(p[0]-0.5)*inchesPerUnit, (p[1])*inchesPerUnit, floor], 0, 1, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( -1 0 0 '+ str(distance([(p[0])*inchesPerUnit, (p[1]-0.5)*inchesPerUnit, floor], 1, 0, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 0 -1 '+ str(distance([(p[0]-0.5)*inchesPerUnit, (p[1]-0.5)*inchesPerUnit, floor], 0, 0, -1)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 0 1 '+ str(distance([(p[0]-0.5)*inchesPerUnit, (p[1]-0.5)*inchesPerUnit, (floor+48)], 0, 0, 1)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('         }\n')
        o.write ('    }\n')

        o.write ('    {\n')
        o.write ('         brushDef3\n')
        o.write ('         {\n')
        o.write ('             ( 1 0 0 '+ str(distance([(p[0]-1)*inchesPerUnit, (p[1]-0.5)*inchesPerUnit, floor], -1, 0, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 1 0 '+ str(distance([(p[0]-0.5)*inchesPerUnit, (p[1]-1)*inchesPerUnit, floor], 0, -1, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 -1 0 '+ str(distance([(p[0]-0.5)*inchesPerUnit, (p[1])*inchesPerUnit, floor], 0, 1, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( -1 0 0 '+ str(distance([(p[0])*inchesPerUnit, (p[1]-0.5)*inchesPerUnit, floor], 1, 0, 0)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 0 -1 '+ str(distance([(p[0]-0.5)*inchesPerUnit, (p[1]-0.5)*inchesPerUnit, (floor + p[2]-48)], 0, 0, -1)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('             ( 0 0 1 '+ str(distance([(p[0]-0.5)*inchesPerUnit, (p[1]-0.5)*inchesPerUnit, (floor + p[2])], 0, 0, 1)) +' ) ( ( 0.0078125 0 0 ) ( 0 0.0078125 0 ) ) "textures/hell/cbrick2" 0 0 0\n')
        o.write ('         }\n')
        o.write ('    }\n')

#
# generateInnerCeilings - uses cuboids to draw mid level objects the player can walk on or under
#

def generateInnerCeilings (r, o):
    cThickness = 12
    for p in rooms[r].innerceilings:
        floor = getFloorLevel(r)
        cPosition = [int(p[0]+1), int(p[1]+1), (floor + (p[2]-cThickness)/inchesPerUnit) ]
        size = [1, 1, cThickness/inchesPerUnit ]
        newcuboid(cPosition, size, 'plinth', r)

