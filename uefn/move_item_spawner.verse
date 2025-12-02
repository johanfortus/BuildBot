
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /Verse.org/Random }
using { /UnrealEngine.com/Temporary/Diagnostics }
using { /UnrealEngine.com/Temporary/SpatialMath }

move_item_spawner := class(creative_device):

    @editable var ItemPlacer : item_placer_device = item_placer_device{}
    @editable var TriggerDevice : trigger_device = trigger_device{}
    @editable var HUD : hud_message_device = hud_message_device{}
    
    @editable var MinPosition : vector3 = vector3{}
    @editable var MaxPosition : vector3 = vector3{}

    OnBegin<override>()<suspends>:void=
        TriggerDevice.TriggeredEvent.Subscribe(OnItemPickup)


    OnItemPickup(Agent : ?agent) : void=
        HUD.Show()
        RandomX := GetRandomFloat(MinPosition.X, MaxPosition.X)
        RandomY := GetRandomFloat(MinPosition.Y, MaxPosition.Y)
        NewPosition := vector3{X := RandomX, Y := RandomY, Z := 80.0}
        if (ItemPlacer.TeleportTo[NewPosition, ItemPlacer.GetTransform().Rotation]) {}
