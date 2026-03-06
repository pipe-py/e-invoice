class Generic():
    @staticmethod
    def generic_header(access_token: str):
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json"
        }