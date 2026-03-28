local showMenuEvent = script.Parent:WaitForChild("ShowMenuEvent")
local menuFrame = script.Parent:WaitForChild("MenuFrame")
local textLabel = script.Parent:WaitForChild("FadeFrame"):WaitForChild("TextLabel")
local Camera = workspace.CurrentCamera
local player = game.Players.LocalPlayer

showMenuEvent.Event:Connect(function()
	-- Stop the player
	local char = player.Character or player.CharacterAdded:Wait()
	char:WaitForChild("HumanoidRootPart").Anchored = true

	-- Stop the camera (Set to Scriptable)
	Camera.CameraType = Enum.CameraType.Scriptable
	-- Tip: Set your CFrame here if you want a specific view!

	-- Show the menu UI
	menuFrame.Visible = true
	textLabel.Visible = false
	print("Menu is now active.")
end)
