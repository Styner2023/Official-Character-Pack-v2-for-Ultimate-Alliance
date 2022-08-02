# Generated by BehavEd
# ( "PERSISTENCE--indicate nightcrawler has been saved" )
setGameFlag("mephisto3", 2, 1 )
# ( "start cut scene; focus on nightcrawler's cage" )
startCutScene("FALSE", "FALSE" )
cameraFocusToEntity("lock_nightcrawler", 320.000, 45.000, 45.000, 1.500 )
waittimed ( 1.500 )
# ( "prepare phoenix' cage for dropping" )
spawn("cage_open_p", "cage_drop", "cage_drop_p", " 0.000 0.000 0.000 ", " 0.000 0.000 0.000 " )

magneto = isActorOnTeam("Magneto" )
if magneto == 1
	# Save both X-men
	# ( "open nightcrawler's cage" )
	playanim (  "EA_USE_BUTTON", "_ACTIVATOR_", "NONE", "" )
	waittimed ( 0.500 )
	act("lock_nightcrawler", "lock_nightcrawler" )
	act("cage_open_n", "cage_open_n" )
	remove ( "cage_drop_p", "cage_drop_p" )
	# ( "release phoenix" )
	startConversation("act2/mephisto/mephisto3/2_mephisto3_050m" )
else
	# Normal conditions
	remove ( "cage_open_p", "cage_open_p" )
	# ( "open nightcrawler's cage" )
	playanim (  "EA_USE_BUTTON", "_ACTIVATOR_", "NONE", "" )
	waittimed ( 0.500 )
	act("lock_nightcrawler", "lock_nightcrawler" )
	act("cage_open_n", "cage_open_n" )
	waittimed ( 1.000 )
	# ( "drop phoenix into the abyss" )
	cameraFocusToEntity("lock_phoenix", 320.000, 45.000, 225.000, 1.500 )
	waittimed ( 1.500 )
	remove ( "trig_phoenix", "trig_phoenix" )
	remove ( "trig_phoenix_no", "trig_phoenix_no" )
	waittimed ( 0.500 )
	act("cage_drop_p", "cage_drop_p" )
	remove ( "phoenix_npc", "phoenix_npc" )
	waittimed ( 1.500 )
	remove ( "cage_drop_p", "cage_drop_p" )
	endCutScene("FALSE", "TRUE" )
	# ( "mark objectives; start conversation" )
	setEpilogue(4, 1 )
	unlockCharacter("nightcrawlerdlc", "04" )
	lockCharacter("cyclops", "SKIN" )
	lockCharacter("Psylocke_Hero", "SKIN" )
	waittimed ( 1.000 )
	startConversation("act2/mephisto/mephisto3/2_mephisto3_050" )
endif