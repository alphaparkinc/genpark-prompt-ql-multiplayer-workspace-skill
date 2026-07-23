class PromptQlMultiplayerWorkspaceClient:
    def post_multiplayer_prompt(self, channel_id: str, user_prompt: str, active_peers: list) -> dict:
        peers_str = ", ".join(active_peers) if active_peers else "solo"
        resp = f"[Channel {channel_id}] Synthesized response for '{user_prompt}' with active peers: {peers_str}."
        return {
            "thread_response": resp,
            "synced_context": {"peers_count": len(active_peers), "state": "SYNCED"}
        }
