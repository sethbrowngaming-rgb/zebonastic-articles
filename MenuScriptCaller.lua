-- MenuScriptCaller.lua
-- Place this LocalScript in StarterPlayerScripts or StarterGui
-- It calls MenuLocalScript (must be a ModuleScript) using require()

local MenuLocalScript = require(game.StarterGui.MenuLocalScript)

MenuLocalScript.open()
