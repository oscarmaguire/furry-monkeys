def on_up_pressed():
    if derek.vy == 0:
        derek.vy = -100
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile(sprite, location):
    game.game_over(False)
    game.set_game_over_message(False, "GAME OVER")
scene.on_overlap_tile(SpriteKind.player,
    sprites.castle.tile_dark_grass3,
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    game.game_over(True)
    game.set_game_over_message(True, "WINNER")
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_open,
    on_overlap_tile2)

derek: Sprite = None
controller.move_sprite(derek)
derek = sprites.create(assets.image("""
    derek
"""), SpriteKind.player)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
controller.move_sprite(derek, 100, 0)
derek.ay = 200
scene.set_background_color(15)
scene.camera_follow_sprite(derek)