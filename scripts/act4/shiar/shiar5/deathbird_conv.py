# Generated by BehavEd
# ( "comment" )
cameraFade(1.000, 0.100 )
waittimed ( 0.100 )
setInvisible("deathbird", "FALSE" )
copyOriginAndAngles("_HERO1_", "e_hero_spot01" )
copyOriginAndAngles("_HERO2_", "e_hero_spot02" )
copyOriginAndAngles("_HERO3_", "e_hero_spot03" )
copyOriginAndAngles("_HERO4_", "e_hero_spot04" )
startCutScene("FALSE", "FALSE" )
act("debris_effect06", "debris_effect06" )
act("debris_effect07", "debris_effect07" )
waittimed ( 0.100 )
cameraMove(" 4708.440 2640.800 177.780 ", 0.000 )
cameraPan(" 0.000 30.200 228.000 ", 0.000, "FALSE" )
cameraFade(0.000, 1.000 )
sound (  "PLAY_SOUND", "Zone_shared/shiar/screen_shake_shiar", "", "" )
cameraShake(1.000, 1.500 )
waittimed ( 1.250 )
cameraMove(" 4888.290 2840.660 341.200 ", 1.750 )
cameraPan(" 0.000 42.500 228.000 ", 1.500, "FALSE" )
waittimed ( 0.250 )
attackEntityWithType("deathbird", "console_smash", "ANY", "TRUE" )
waittimed ( 2.500 )
killEntity("console_smash" )
waittimed ( 0.750 )
remove ( "debris_effect06", "debris_effect06" )
faceEntity("deathbird", "_HERO1_" )
waittimed ( 1.000 )
remove ( "debris_effect07", "debris_effect07" )
act("debris_effect05", "debris_effect05" )
Sabretooth = isActorOnTeam("Sabretooth" )
if Sabretooth == 1
	startConversation("act4/shiar/shiar5/4_shiar5_052_DLC" ) 
else
	startCharConversation("act4/shiar/shiar5/4_shiar5_050", "WOLVERINE", "act4/shiar/shiar5/4_shiar5_052" )
endif 


