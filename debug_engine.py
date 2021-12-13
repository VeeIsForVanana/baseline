from __future__ import annotations

from engine import Engine

class DebugEngine(Engine):
    """
    Special handler for debug mode allowing the player to see all tiles and place any and all objects.
    Essentially, godmode.
    """

    def update_fov(self) -> None:
        """Updates fov by making all tiles visible"""
        self.game_map.visible[:] = True