# Generated by BehavEd
# ( "Zone script for stark1" )
waittimed ( 0.200 )
setCurrentAct(1 )

setSegmentVisible("Magneto", "helmet_segment", "0")

# ( "allows proper display of all stark objectives in objectives menu" )
objective ( "stark_obj0",  "EOBJCMD_SHOW" )
# ( "This unlocks the extraction point" )
extractionUnlock("" )
# ( "*****************************************************" )
addObjectiveCategory("act1_omega" )
addObjectiveCategory("act1_atlantis" )
addObjectiveCategory("act1_mandarin" )
# ( "*****************************************************" )
cameraSetClipPlane(10000.000 )
elevator_intro = getObjective("omega_obj10", "HIDDEN" )
if elevator_intro == 1
     cameraFade(0.000, 0.000 )
     objective ( "omega_obj0",  "EOBJCMD_SHOW" )
     objective ( "omega_obj10",  "EOBJCMD_SHOW" )
endif
# ( "**********************************************" )
# ( "Conversations change after omega" )
omega_done = getObjective("Omega_Obj30", "COMPLETE" )
if omega_done == 1
     omega_once = getGameFlag("stark", 6 )
     if omega_once == 0
          act("intro_setup", "intro_setup" )
          setGameFlag("stark", 6, 1 )
          startConversation("act1/stark/1_stark1_310" )
     endif
endif
atlantis_done = getObjective("Atlantis_Obj60", "COMPLETE" )
if atlantis_done == 1
     atlantis_once = getGameFlag("stark", 7 )
     if atlantis_once == 0
          act("intro_setup", "intro_setup" )
          setGameFlag("stark", 7, 1 )
          startConversation("act1/stark/1_stark1_510" )
     endif
endif
mandarin_done = getObjective("Mandarin_Obj10", "COMPLETE" )
if mandarin_done == 1
     mandarin_once = getGameFlag("stark", 8 )
     if mandarin_once == 0
          act("intro_setup", "intro_setup" )
          setGameFlag("stark", 8, 1 )
          startConversation("act1/stark/1_stark1_710" )
     endif
endif
# ( "**********************************************" )
# ( "If omega_done is set to 1 then the way to stark2 should be enabled" )
# ( "stark2 1, should be only used once" )
if omega_done == 1
     # ( "stark2 1, should be only used once" )
     bridge_intro = getGameFlag("stark", 2 )
     if bridge_intro == 0
          # ( "The game var stark, 2 is set to in the open_bridge.py" )
          setEnable("bridge_railing", "TRUE" )
     else
          # ( "Once the bridge has been opened then the zone_link should be enabled" )
          setEnable("link_stark2", "TRUE" )
          act("bridge", "bridge" )
     endif
endif
# ( "This readys the cufflinks mission stuff" )
remove_cufflinks = getGameFlag("stark", 11 )
if remove_cufflinks == 1
     remove ( "pickup_cufflinks", "" )
     remove ( "cufflinks", "" )
else
     cufflinks_hide = getObjective("stark_obj60", "HIDDEN" )
     if cufflinks_hide == 0
          # ( "This shows the objective hintypefor the cufflinks" )
          setEnable("cufflinks", "TRUE" )
     endif
endif
cameraFade(0.000, 0.000 )

