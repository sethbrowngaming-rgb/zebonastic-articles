local Players = game:GetService("Players")
local player = Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()
local humanoid = character:WaitForChild("Humanoid")

-- Stop movement
humanoid.WalkSpeed = 0
humanoid.JumpPower = 0

-- Lock camera in place
local camera = workspace.CurrentCamera
camera.CameraType = Enum.CameraType.Scriptable

-- Keep camera at its current position/rotation
camera.CFrame = camera.CFrame

local TextLable = script.Parent

TextLable.BackgroundTransparency = 0
TextLable.TextTransparency = 1

-- Fade in slowly
for i = 1, 0, -0.05 do
	TextLable.TextTransparency = i
	task.wait(0.05)
end

task.wait(5)

for i = 0, 1, 0.05 do
	TextLable.TextTransparency = i
	task.wait(0.05)
end

TextLable.Visible = false

-- Call the menu once the intro is done
require(game.StarterGui.MenuLocalScript).open()
