# Generated by BehavEd
# ( "This is the load script" )
# ( "Zone script for stark1" )
setCurrentAct(2 )

setSegmentVisible("Magneto", "helmet_segment", "0")

# ( "This allows all strange objectives to be properly displayed in the objectives menu" )
objective ( "strange_obj0",  "EOBJCMD_SHOW" )
# ( "***************This allows professor X to talk about Nightcrawler***************" )
# ( "This is over written later on in this script" )
setGameFlag("strange", 18, 1 )
# ( "***************END This allows professor X to talk about Nightcrawler***************" )
# ( "This unlocks the extraction point" )
extractionUnlock("" )
# ( "*****************************************************" )
addObjectiveCategory("act2_murder" )
addObjectiveCategory("act2_mephisto" )
# ( "*****************************************************" )
waittimed ( 0.250 )
intro = getGameFlag("strange", 1 )
murder_done = getObjective("Murder_Obj40", "COMPLETE" )
mephisto_hide = getObjective("Mephisto_Obj10", "HIDDEN" )
mephisto_done = getObjective("Mephisto_Obj70", "COMPLETE" )
if intro == 1
     remove ( "drstrangeintro", "" )
endif
if intro == 0
     # ( "This checks if the intro is entered normally" )
     mandarin_done = getObjective("Mandarin_Obj10", "COMPLETE" )
     if mandarin_done == 0
          moveHeroesToEnt("player_start_all01" )
          faceEntity("_ALL_HEROES_", "wp_intro02" )
     endif
     startCutScene("FALSE", "FALSE" )
     lockControls(0.000 )
     setGameFlag("strange", 1, 1 )
     # ( "This makes a conversation available" )
     setGameFlag("strange", 19, 1 )
     setEnable("drstrange", "FALSE" )
     setInvisible("drstrange", "FALSE" )
     drstrange_pc = isActorOnTeam("drstrange" )
     if drstrange_pc == 1
          controlPlayerHeroWithAI(-1.000 )
          copyOriginAndAngles("drstrange", "spawn_pt" )
     endif
     cameraToLocationAngles(" 539.500 95.000 -173.000 ", " 539.500 195.000 -169.000 ", 0.000 )
     # ( "pitch -2., yaw 90" )
     waittimed ( 0.200 )
     cameraFade(0.000, 0.000 )
     waittimed ( 0.500 )
     if drstrange_pc == 1
          setWaypointPath("drstrange", "intro", 1 )
     else
          setWaypointPath("drstrangeintro", "intro", 1 )
     endif
     waittimed ( 0.250 )
     cameraMove(" 371.000 535.000 -29.000 ", 0.000 )
     cameraPan(" 0.000 14.700 103.800 ", 0.000, "FALSE" )
     waittimed ( 0.750 )
     startConversation("act2/strange/2_strange1_010" )
     waittimed ( 0.100 )
     cameraMove(" 371.000 535.000 -29.000 ", 0.000 )
     cameraPan(" 0.000 14.700 57.600 ", 3.000, "FALSE" )
elif mephisto_hide == 1
     if murder_done == 1
          # ( "If Mephisto hasn't been shown and murder is done" )
          # ( "Then the second phase of the town center should be loaded" )
          # ( "The next mission should be shown" )
          # ( "*******************" )
          # ( "This camera intro should look the same as the first one in go_to_sanctum" )
          act("intro_setup", "intro_setup" )
          startConversation("act2/strange/2_strange1_210" )
     endif
elif mephisto_done == 1
     # ( "This makes it so Prof X doesn't talk about Nightcrawler" )
     setGameFlag("strange", 18, 0 )
     m_intro = getGameFlag("strange", 22 )
     if m_intro == 0
          setGameFlag("strange", 22, 1 )
          act("intro_setup", "intro_setup" )
          startConversation("act2/strange/2_strange1_710" )
     else
          cameraFade(0.000, 0.000 )
          waittimed ( 1.000 )
     endif
else
     cameraFade(0.000, 0.000 )
     waittimed ( 1.000 )
endif
# ( "The mirror with the gem needs to be removed if the player hasn't return the gem." )
mirror_swap = getGameFlag("strange", 7 )
if mirror_swap == 1
     remove ( "new_mirror", "" )
     waittimed ( 0.100 )
     spawn("mirror", "mirror_gem", "new_mirror", " 0.000 0.000 0.000 ", " 0.000 0.000 0.000 " )
     waittimed ( 0.100 )
     remove ( "mirror", "" )
endif

# ( "This spawns Jean, if she's rescued from Murderworld or Mephisto's Realm" )
jeanremove = isActorOnTeam("phoenix" )
jeandead = getGameFlag("mephisto3", 2 )
pitfall_won = getGameFlag("murder2", 4 )
if jeanremove == 0
     if jeandead == 0
         if pitfall_won == 1
             act("sp_jeansimple01", "" )
         endif
     endif
endif

got_mirror_gem = getGameFlag("strange", 4 )
if got_mirror_gem == 1
     # ( "The player has the gem, but hasn't put it on the mirror yet" )
     remove ( "gem_of_oshtur", "" )
     remove ( "trigger_grab_gem", "" )
     # ( "Check if the player has put the gem in the mirror" )
     mirror_readied = getGameFlag("strange", 5 )
     if mirror_readied == 1
          copyOriginAndAngles("mirror_gem", "mirror" )
          waittimed ( 0.100 )
          remove ( "mirror", "" )
     else
          remove ( "mirror_gem", "" )
     endif
else
     remove ( "mirror_gem", "" )
endif
ghost_ring = isActorOnTeam("drstrange" )
if ghost_ring == 1
     remove ( "soul_ring", "" )
     remove ( "meditation_ring", "" )
endif
cameraFade(0.000, 0.000 )

