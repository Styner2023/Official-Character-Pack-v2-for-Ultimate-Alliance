# Generated by BehavEd
# ( "temp enable for arcade trigger--5/10" )
# ( "====================" )
setGameFlag("murder2", 3, 1 )
startCutScene("FALSE", "FALSE" )
cameraFade(1.000, 1.000 )
waittimed ( 1.000 )
remove ( "jean", "jean" )
moveHeroesToEnt("hero_spot_tent" )
setEnable("phoenix_npc", "TRUE" )
act("phoenix_npc", "phoenix_npc" )
waittimed ( 0.100 )
copyOriginAndAngles("jean", "jean_place01" )
cameraFocusToEntity("jean_place01", 384.000, 45.000, 210.000, 0.000 )
waittimed ( 0.750 )
cameraFocusToEntity("jean_place01", 288.000, 30.000, 225.000, 2.000 )
cameraFade(0.000, 1.000 )
setNoCollide("_OWNER_", "TRUE" )
playanim (  "EA_ZONE4", "jean", "NONE", "jeandone" )
waittimed ( 0.750 )
startConversation("act2/murder/murder2/2_murder2_025" )

