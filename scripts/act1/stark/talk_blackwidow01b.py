# Generated by BehavEd
# ( "This script is called after the black winow conversationn is called" )
actor = getZoneVar("conv_actor" )
# ( "And put the characters back into there poses" )
cameraFade(1.000, 0.150 )
waittimed ( 0.150 )
copyOriginAndAngles("blackwindow_chair", "chair_spot01" )
copyOriginAndAngles("hero_chair", "chair_spot05" )
state = getZoneVar("bw" )
if state == 0
     copyOriginAndAngles("blackwindow", "bw_spot02" )
     # ( "This makes Black Widow pick an standing animation" )
     playanim (  "EA_IDLE1", "blackwindow", "LOOP", "" )
     act("pick_stance", "blackwindow" )
elif state == 2
     # ( "She is sitting at the conference table" )
     # ( "This is only played if both Black Widow and Fury are at the conference table" )
     act("3Dvo_fury_bw", "3Dvo_fury_bw" )
     copyOriginAndAngles("blackwindow", "chair_spot03" )
     playanim (  "EA_ZONE1", "blackwindow", "LOOP", "" )
     copyOriginAndAngles(actor, "bw_spot01" )
else
     # ( "She is sitting at the conference table" )
     # ( "This is only played if both Black Widow and Fury are at the conference table" )
     act("3Dvo_fury_bw", "3Dvo_fury_bw" )
     copyOriginAndAngles("blackwindow", "chair_spot03" )
     playanim (  "EA_ZONE1", "blackwindow", "LOOP", "" )
     copyOriginAndAngles(actor, "bw_spot01" )
endif
cameraFade(0.000, 0.250 )
playanim (  "EA_ZONE15", actor, "", "" )
# ( "This script also needs to reset camera" )
cameraReset( )

