# Generated by BehavEd
# ( "enable zone link to mephisto4; remove phoenix" )
act("relay_exit", "relay_exit" )
fade("phoenix_npc", 0.000, 1.000, "TRUE" )
waittimed ( 1.000 )
remove ( "phoenix_npc", "phoenix_npc" )
objective ( "mephisto_obj50",  "EOBJCMD_HIDE" )
objective ( "mephisto_obj60",  "EOBJCMD_COMPLETE" )

