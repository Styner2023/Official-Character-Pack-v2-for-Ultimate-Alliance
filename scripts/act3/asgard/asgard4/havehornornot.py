# Generated by BehavEd
# ( "If the player agrees to find his horn, this is enabled" )
# ( "If the player hasn't found the horn, heimdall tells them to go find it" )
# ( "If they found it, he awards them" )
gothorn = getGameFlag("asgard4", 12 )
if gothorn == 0
     startConversation("act3/asgard/asgard4/3_ASGARD4_120" )
else
     remove ( "horn_conv_trig", "horn_conv_trig" )
     setGameFlag("asgard4", 16, 1 )
     objective ( "asgard_obj50",  "EOBJCMD_COMPLETE" )
     startConversation("act3/asgard/asgard4/3_ASGARD4_130" )
endif

