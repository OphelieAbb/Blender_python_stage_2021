import bpy



# Call user prefs window
bpy.ops.screen.userpref_show("INVOKE_DEFAULT")

# Change area type
area = bpy.context.window_manager.windows[-1].screen.areas[0]
area.type = 'PREFERENCES'

#'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR'(VSE), 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR'(rien), 'STATUSBAR'(rien), 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'PREFERENCES'