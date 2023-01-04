# Generated by BehavEd
# ( "This script runs when any mirror is used" )
usetrigger = getGameFlag("asgard4", 24 )
if usetrigger == 0
     setGameFlag("asgard4", 24, 1 )
     mirrorname = getName("_OWNER_" )
     iceshell01 = getGameFlag("asgard4", 13 )
     iceshell02 = getGameFlag("asgard4", 14 )
     iceshell03 = getGameFlag("asgard4", 15 )
     if mirrorname == "mirror01"
          setEnable("mirror01", "FALSE" )
          waittimed ( 0.800 )
          act("beam01", "beam01" )
     endif
     if mirrorname == "mirror02"
          setEnable("mirror02", "FALSE" )
          waittimed ( 0.800 )
          act("beam02", "beam02" )
     endif
     if mirrorname == "mirror03"
          setEnable("mirror03", "FALSE" )
          waittimed ( 0.800 )
          act("beam03", "beam03" )
     endif
     if mirrorname == "mirror04"
          setEnable("mirror04", "FALSE" )
          waittimed ( 0.800 )
          act("beam04", "beam04" )
     endif
     if iceshell01 == 0
          startCutScene("FALSE", "FALSE" )
          waittimed ( 0.500 )
          cameraFocusToEntity("heimdall", 500.000, 35.000, 180.000, 2.000 )
          spawnEffect("ice_shell_spot", "map/asgard/water_drip", " 0.000 0.000 0.000 ", " 0.000 0.000 0.000 " )
          sound (  "PLAY_SOUND", "zone_shared/asgard/melt_heim", "", "" )
          waittimed ( 3.000 )
          playanim (  "EA_POWER1", "ice_shell01", "STOP", "" )
          setGameFlag("asgard4", 13, 1 )
          waittimed ( 3.000 )
          startConversation("act3/asgard/asgard4/3_ASGARD4_100" )
          setGameFlag("asgard4", 24, 0 )
          setEnable("mirror02", "TRUE" )
          setHintType("mirror02", "use" )
     else
          if iceshell02 == 0
               startCutScene("FALSE", "FALSE" )
               waittimed ( 0.500 )
               cameraFocusToEntity("heimdall", 500.000, 35.000, 180.000, 2.000 )
               spawnEffect("ice_shell_spot", "map/asgard/water_drip", " 0.000 0.000 0.000 ", " 0.000 0.000 0.000 " )
               waittimed ( 3.000 )
               playanim (  "EA_POWER2", "ice_shell01", "STOP", "" )
               setGameFlag("asgard4", 14, 1 )
               waittimed ( 3.000 )
               endCutScene("FALSE", "TRUE" )
               setGameFlag("asgard4", 24, 0 )
               setEnable("mirror03", "TRUE" )
               setHintType("mirror03", "use" )
          else
               if iceshell03 == 0
                    startCutScene("FALSE", "FALSE" )
                    waittimed ( 0.500 )
                    cameraFocusToEntity("heimdall", 500.000, 35.000, 180.000, 2.000 )
                    spawnEffect("ice_shell_spot", "map/asgard/water_drip", " 0.000 0.000 0.000 ", " 0.000 0.000 0.000 " )
                    waittimed ( 3.000 )
                    playanim (  "EA_POWER3", "ice_shell01", "STOP", "" )
                    setGameFlag("asgard4", 15, 1 )
                    waittimed ( 3.000 )
                    endCutScene("FALSE", "TRUE" )
                    setGameFlag("asgard4", 24, 0 )
                    setEnable("mirror04", "TRUE" )
                    setHintType("mirror04", "use" )
               else
                    startCutScene("FALSE", "FALSE" )
                    remove ( "heimdall_clip_tom", "heimdall_clip_tom" )
                    remove ( "ice_shell01", "ice_shell01" )
                    copyOriginAndAngles("heimdall_ice_top", "ice_shell_spot" )
                    copyOriginAndAngles("heimdall_ice_bottom", "ice_shell_spot" )
                    waittimed ( 1.000 )
                    cameraFocusToEntity("heimdall", 500.000, 35.000, 180.000, 2.000 )
                    waittimed ( 1.000 )
                    moveHeroesToEnt("herospot06" )
                    spawnEffect("ice_shell_spot", "map/asgard/water_drip", " 0.000 0.000 0.000 ", " 0.000 0.000 0.000 " )
                    setNoCollide("heimdall", "TRUE" )
                    setNoGravity("heimdall", "TRUE" )
                    setNoClip("heimdall", "TRUE" )
                    waittimed ( 2.000 )
                    playanim (  "EA_ZONE3", "heimdall", "NONE", "walkingdown" )
                    setEnable("horn_conv_trig", "TRUE" )
                    killEntity("heimdall_ice_top" )
                    waittimed ( 1.000 )
                    killEntity("heimdall_ice_bottom" )
                    waittimed ( 1.000 )
                    cameraFocusToEntity("hd_conv_spot", 500.000, 35.000, 180.000, 10.000 )
                    waitsignal ( "walkingdown" )
                    setNoCollide("heimdall", "FALSE" )
                    setNoGravity("heimdall", "FALSE" )
                    setNoClip("heimdall", "FALSE" )
                    setRecallActive("TRUE" )
                    setGameFlag("asgard4", 11, 1 )
                    setGameFlag("asgard4", 24, 0 )
                    objective ( "asgard_obj50",  "EOBJCMD_SHOW" )
                    waittimed ( 1.000 )
                    startConversation("act3/asgard/asgard4/3_ASGARD4_110" )
               endif
          endif
     endif
endif

