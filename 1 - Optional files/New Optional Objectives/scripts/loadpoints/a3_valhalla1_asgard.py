# Generated by BehavEd
# ( "The player has finished asgard" )
setCurrentAct(3 )
# ( "**************************" )
# ( "This marks the intro to Valhalla as done" )
setGameFlag("valhalla1", 1, 1 )
setGameFlag("conv_var2", 2, 1 )
# ( "This randomly makes Jean or Nightcrawler alive" )
randint = randomInt(0, 1 )
if randint == 1
     setGameFlag("mephisto3", 1, 1 )
else
     setGameFlag("mephisto3", 2, 1 )
endif
# ( "The game vars for asgard need to be added here as well" )
# ( "**************************" )
# ( "--- Bifrost Obj's" )
objective ( "bifrost_obj10",  "EOBJCMD_SHOW" )
# ( "--- Asgard Obj's" )
objective ( "asgard_obj0",  "EOBJCMD_SHOW" )
objective ( "asgard_obj10",  "EOBJCMD_SHOW" )
objective ( "asgard_obj20",  "EOBJCMD_SHOW" )
objective ( "asgard_obj30",  "EOBJCMD_SHOW" )
objective ( "asgard_obj40",  "EOBJCMD_SHOW" )
objective ( "asgard_obj50",  "EOBJCMD_SHOW" )
objective ( "asgard_obj10",  "EOBJCMD_COMPLETE" )
objective ( "asgard_obj20",  "EOBJCMD_COMPLETE" )
objective ( "asgard_obj30",  "EOBJCMD_COMPLETE" )
objective ( "asgard_obj40",  "EOBJCMD_COMPLETE" )
objective ( "asgard_obj50",  "EOBJCMD_COMPLETE" )
loadMap("act3/valhalla/valhalla1" )

