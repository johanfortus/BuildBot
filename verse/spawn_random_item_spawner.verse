using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /Verse.org/Simulation/Tags }
using { /Verse.org/Random }
using { /UnrealEngine.com/Temporary/Diagnostics }


spawn_random_item_spawner := class(creative_device):

    @editable var CurrentItemSpawner : item_spawner_device = item_spawner_device{}
    @editable var ItemSpawnersArray : []item_spawner_device = array{}
    @editable var HUD : hud_message_device = hud_message_device{}
    @editable var ItemRemover : item_remover_device = item_remover_device{}

    var PrevIdx : int = 0

    OnBegin<override>()<suspends>:void=
        CurrentItemSpawner.ItemPickedUpEvent.Subscribe(SpawnItemSpawner)
    
    SpawnItemSpawner(Agent : agent) : void=
        HUD.Show()
        ItemRemover.Remove(Agent)
        CurrentItemSpawner.Disable()
        Print("PrevIdx: {PrevIdx}")
        var RandomIdx : int = 0
        loop:
            set RandomIdx = GetRandomInt(0, 75)
            if(RandomIdx <> PrevIdx):
                break
        Print("New Idx: {RandomIdx}")
        set PrevIdx = RandomIdx
        
        if(ItemSpawner := ItemSpawnersArray[RandomIdx]):
            set CurrentItemSpawner = ItemSpawner
            ItemSpawner.Enable()
            ItemSpawner.ItemPickedUpEvent.Subscribe(SpawnItemSpawner)
