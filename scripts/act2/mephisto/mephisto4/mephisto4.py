# Generated by BehavEd
# ( "mephisto boss battle" )
setZoneVar("painthresh", 90 )
remove ( "the_weapon", "the_weapon" )
cameraSetClipPlane(10000.000 )
beat = getGameFlag("bosses", 18 )
if beat == 0
     setRecallActive("FALSE" )
     setRecallActive("FALSE" )
     through = getGameFlag("bossCP", 3 )
     if through == 1
          setEnable("hole_trigger", "TRUE" )
          act("hole_trigger", "_ACTIVE_HERO_" )
     else
          act("sp_mephisto1", "sp_mephisto1" )
     endif
     # ( "remove appropriate statues" )
     jeandead = getGameFlag("mephisto3", 2 )
     if jeandead == 1
          remove ( "statue_nightcrawler", "statue_nightcrawler" )
     else
          remove ( "statue_phoenix", "statue_phoenix" )
     endif
     waittimed ( 0.100 )
     if through == 0
          cameraMove(" 798.780 -122.000 36.520 ", 0.000 )
          cameraPan(" 0.000 25.500 69.300 ", 0.000, "FALSE" )
          cameraFade(0.000, 0.500 )
          waittimed ( 0.500 )
          startCharConversation("act2/mephisto/mephisto4/2_mephisto4_010", "nightcrawlerdlc", "act2/mephisto/mephisto4/2_mephisto4_020_DLC" )
     endif
else
     cameraFade(0.000, 0.500 )
     act("portal_back", "portal_back" )
     setEnable("portal", "TRUE" )
     act("portal", "portal" )
endif

