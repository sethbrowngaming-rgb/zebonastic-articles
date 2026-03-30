-- FadeIntroScript.lua (LocalScript inside StarterGui)
-- Fades out the intro screen, then calls MenuLocalScript when done

local TweenService = game:GetService("TweenService")

local screenGui = script.Parent
local fadeFrame = screenGui:WaitForChild("FadeFrame") -- black Frame covering the screen

-- Fade out (black to transparent)
local tween = TweenService:Create(fadeFrame, TweenInfo.new(2), { BackgroundTransparency = 1 })
tween:Play()

tween.Completed:Connect(function()
    fadeFrame.Visible = false
    require(game.StarterGui.MenuLocalScript).open()
end)
