# Generated by BehavEd
# ( "This puts Jarvis on his path to get out of the way." )
setWaypointPath("jarvis", "standjarvis", 1 )
waittimed ( 2.000 )
setWaypointPath("weasel", "walkby", 1 )
faceEntity("jarvis", "weasel" )
waittimed ( 1.000 )
faceEntity("jarvis", "_ACTIVE_HERO_" )
# ( "55 643 71, 17 89" )
cameraMove(" 55.000 643.000 71.000 ", 2.000 )
cameraPan(" 0.000 17.000 120.000 ", 2.000, "FALSE" )
waittimed ( 1.000 )
faceEntity("weasel", "_ACTIVE_HERO_" )
waittimed ( 1.000 )
startConversation("act1/stark/1_stark2_320" )
objective ( "stark_obj10",  "EOBJCMD_SHOW" )

