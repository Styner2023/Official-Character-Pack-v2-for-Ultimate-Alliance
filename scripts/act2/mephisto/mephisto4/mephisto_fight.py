# Generated by BehavEd
# ( "mephisto starts attacking you" )
cameraMove(" 574.900 -4018.840 284.250 ", 0.500 )
cameraPan(" 0.000 45.400 71.500 ", 0.500, "FALSE" )
setDefaultTarget("mephisto" )
setAIActive("mephisto", "TRUE" )
attackEntityWithType("mephisto", "_ACTIVE_HERO_", "ANY", "FALSE" )
waittimed ( 0.100 )
jeandead = getGameFlag("mephisto3", 2 )
if jeandead == 1
     act("phoenix_spawner", "phoenix_spawner" )
     remove ( "nightcrawler_spawner", "nightcrawler_spawner" )
else
     act("nightcrawler_spawner", "nightcrawler_spawner" )
     remove ( "phoenix_spawner", "phoenix_spawner" )
endif
waittimed ( 0.400 )
cameraResetOldSchool( )

