# Generated by BehavEd
# ( "PERSISTENCE--indicate phoenix has been saved" )
setGameFlag("mephisto3", 1, 1 )
# ( "start cut scene; focus on phoenix' cage" )
startCutScene("FALSE", "FALSE" )
cameraFocusToEntity("lock_phoenix", 320.000, 45.000, 225.000, 1.500 )
waittimed ( 1.500 )
# ( "prepare nightcrawler's cage for dropping" )
spawn("cage_open_n", "cage_drop", "cage_drop_n", " 0.000 0.000 0.000 ", " 0.000 0.000 0.000 " )

magneto = isActorOnTeam("Magneto" )
if magneto == 1
	# Save both X-men
	# ( "open phoenix' cage" )
	playanim (  "EA_USE_BUTTON", "_ACTIVATOR_", "NONE", "" )
	waittimed ( 0.500 )
	act("lock_nightcrawler", "lock_nightcrawler" )
	act("cage_open_p", "cage_open_p" )
	remove ( "cage_drop_n", "cage_drop_n" )

	# ( "PERSISTENCE--indicate nightcrawler has been saved" )
	setGameFlag("mephisto3", 2, 1 )
	# ( "release nightcrawler" )
	cameraFocusToEntity("lock_nightcrawler", 320.000, 45.000, 45.000, 1.500 )
	waittimed ( 1.500 )
	spawnEffect("nightcrawler", "char/magneto/p3_power", " 0.000 0.000 40.000 ", " 0.000 0.000 0.000 " )
	sound (  "PLAY_SOUND", "char/magnet_m/p2_charge", "phoenix_npc", "" )
	spawnEffect("lock_nightcrawler", "char/magneto/p3_power", " 0.000 0.000 0.000 ", " 0.000 0.000 0.000 " )
	waittimed ( 1.500 )
	act("lock_nightcrawler", "lock_nightcrawler" )
	act("cage_open_n", "cage_open_n" )
	remove ( "trig_nightcrawler", "trig_nightcrawler" )
	remove ( "trig_nightcrawler_no", "trig_nightcrawler_no" )

	# These values are later in the game used to check if a person is alive:
	# Contrary to previous comments, a value of "1" actually means that Nightcrawler is dead: 
	setGameFlag("mephisto3", 1, 0 )
	# Contrary to previous comments, a value of "1" actually means that Phoenix is dead:
	setGameFlag("mephisto3", 2, 0 )

	endCutScene("FALSE", "TRUE" )
	unlockCharacter("Phoenix", "" )
	waittimed ( 0.100 )
	unlockCharacter("nightcrawlerdlc", "" )
	waittimed ( 1.000 )
	startConversation("act2/mephisto/mephisto3/2_mephisto3_053m" )
else
	# Normal conditions
	remove ( "cage_open_n", "cage_open_n" )
	# ( "open phoenix' cage" )
	playanim (  "EA_USE_BUTTON", "_ACTIVATOR_", "NONE", "" )
	waittimed ( 0.500 )
	act("lock_phoenix", "lock_phoenix" )
	act("cage_open_p", "cage_open_p" )
	waittimed ( 1.000 )
	# ( "drop nightcrawler into the abyss" )
	cameraFocusToEntity("lock_nightcrawler", 320.000, 45.000, 45.000, 1.500 )
	waittimed ( 1.500 )
	remove ( "trig_nightcrawler", "trig_nightcrawler" )
	remove ( "trig_nightcrawler_no", "trig_nightcrawler_no" )
	waittimed ( 0.500 )
	act("cage_drop_n", "cage_drop_n" )
	remove ( "nightcrawler", "nightcrawler" )
	waittimed ( 1.500 )
	remove ( "cage_drop_n", "cage_drop_n" )
	endCutScene("FALSE", "TRUE" )
	# ( "mark objectives; start conversation" )
	setEpilogue(5, 1 )
	unlockCharacter("Phoenix", "" )
	lockCharacter("Psylocke_Hero", "SKIN" )
	waittimed ( 1.000 )
	startConversation("act2/mephisto/mephisto3/2_mephisto3_030" )
endif