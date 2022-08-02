# Generated by BehavEd
# ( "Attilan1 load script" )

setSegmentVisible("Magneto", "helmet_segment", "0")
# ( "This is to initialize the effect variable for Uatu" )
setZoneVar("effect", 0 )

waittimed ( 0.500 )
setCurrentAct(4 )
# ( "This unlocks the extraction point" )
extractionUnlock("" )
# ( "****************Unlock the objective categories****************" )
addObjectiveCategory("act4_shiar" )
addObjectiveCategory("act4_skrull" )
# ( "****************END Unlock the objective categories****************" )
cameraSetClipPlane(10000.000 )
# ( "This removes the template shuttle" )
remove ( "shuttle", "shuttle" )
shiar_done = getObjective("shiar_obj10", "COMPLETE" )
skrull_done = getObjective("skrull_obj10", "COMPLETE" )
attilan1 = getGameFlag("attilan", 1 )
if skrull_done == 1
     actend_revealed = getGameFlag("attilan1", 3 )
     if actend_revealed == 0
          setGameFlag("attilan1", 3, 1 )
          # ( "This setsup the intro camera" )
          act("intro_setup1", "" )
          waittimed ( 0.250 )
          cameraFade(0.000, 0.000 )
          startConversation("act4/attilan/4_attilan1_510" )
     else
          playanim (  "EA_BORED_LOOP_1", "watcher", "LOOP", "" )
          setWaypointPath("nick", "walk_fury", 1 )
          cameraFade(0.000, 1.000 )
     endif
elif shiar_done == 1
     skrull_revealed = getGameFlag("attilan1", 2 )
     if skrull_revealed == 0
          setGameFlag("attilan1", 2, 1 )
          # ( "This setsup the intro camera" )
          act("intro_setup1", "" )
          waittimed ( 0.250 )
          cameraFade(0.000, 0.000 )
          startConversation("act4/attilan/4_attilan1_310" )
     else
          playanim (  "EA_BORED_LOOP_1", "watcher", "LOOP", "" )
          setWaypointPath("nick", "walk_fury", 1 )
          cameraFade(0.000, 1.000 )
     endif
elif attilan1 == 0
     setGameFlag("attilan", 1, 1 )
     lockControls(3.500 )
     playanim (  "EA_ZONE9", "watcher", "LOOP", "" )
     # ( "This setsup the intro camera" )
     act("intro_setup1", "" )
     waittimed ( 0.250 )
     cameraFade(0.000, 0.000 )
     setallaiactive("TRUE" )
     startConversation("act4/attilan/4_attilan1_010" )
else
     playanim (  "EA_BORED_LOOP_1", "watcher", "LOOP", "" )
     setWaypointPath("nick", "walk_fury", 1 )
     cameraFade(0.000, 0.000 )
endif

