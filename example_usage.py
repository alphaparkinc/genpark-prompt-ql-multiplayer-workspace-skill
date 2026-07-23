from client import PromptQlMultiplayerWorkspaceClient

def main():
    client = PromptQlMultiplayerWorkspaceClient()
    res = client.post_multiplayer_prompt("dev-channel", "Draft API spec for auth service", ["Alice", "Bob"])
    print(f"State: {res['synced_context']['state']}")
    print(f"Response: {res['thread_response']}")

if __name__ == "__main__":
    main()
