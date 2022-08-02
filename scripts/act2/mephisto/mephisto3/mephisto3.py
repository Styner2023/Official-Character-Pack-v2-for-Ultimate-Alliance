# Generated by BehavEd
# ( "has blackheart been met?" )
cameraSetClipPlane(8000.000 )
# ( "has blackheart been defeated?" )
check = getGameFlag("bosses", 17 )
if check == 1
     # ( "blackheart has been defeated; remove him" )
     remove ( "trig_blackheart", "trig_blackheart" )
     act("s_nightcrawler", "s_nightcrawler" )
     act("s_phoenix", "s_phoenix" )
     waittimed ( 0.100 )
     remove ( "blackheart", "blackheart" )
     remove ( "ff_cages", "ff_cages" )
     killEntitySilent("soul01" )
     killEntitySilent("soul02" )
     killEntitySilent("soul03" )
     killEntitySilent("soul04" )
     killEntitySilent("soul05" )
     killEntitySilent("soul06" )
endif
# ( "is phoenix the x-man the player chose to save?" )
check = getGameFlag("mephisto3", 1 )
if check == 1
     # ( "phoenix was saved--prepare cages; remove actors" )
     waittimed ( 0.100 )
     remove ( "trig_phoenix", "trig_phoenix" )
     remove ( "trig_nightcrawler", "trig_nightcrawler" )
     remove ( "end_camera_magnet", "end_camera_magnet" )
     act("lock_phoenix", "lock_phoenix" )
     actSilent("cage_open_p", "cage_open_p" )
     remove ( "cage_open_n", "cage_open_n" )
     remove ( "phoenix_npc", "phoenix_npc" )
     remove ( "trig_phoenix_no", "trig_phoenix_no" )
     remove ( "nightcrawler", "nightcrawler" )
     remove ( "trig_nightcrawler_no", "trig_nightcrawler_no" )
     # ( "prepare zone link to mephisto4" )
     act("fx_mephisto4", "fx_mephisto4" )
     setEnable("link_mephisto4", "TRUE" )
endif
# ( "is nightcrawler the x-man the player chose to save?" )
check = getGameFlag("mephisto3", 2 )
if check == 1
     # ( "nightcrawler was saved--prepare cages; remove actors" )
     waittimed ( 0.100 )
     remove ( "trig_phoenix", "trig_phoenix" )
     remove ( "trig_nightcrawler", "trig_nightcrawler" )
     remove ( "end_camera_magnet", "end_camera_magnet" )
     act("lock_nightcrawler", "lock_nightcrawler" )
     actSilent("cage_open_n", "cage_open_n" )
     remove ( "cage_open_p", "cage_open_p" )
     remove ( "phoenix_npc", "phoenix_npc" )
     remove ( "trig_phoenix_no", "trig_phoenix_no" )
     remove ( "nightcrawler", "nightcrawler" )
     remove ( "trig_nightcrawler_no", "trig_nightcrawler_no" )
     # ( "prepare zone link to mephisto4" )
     act("fx_mephisto4", "fx_mephisto4" )
     setEnable("link_mephisto4", "TRUE" )
endif
