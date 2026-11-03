
# %%writefile no.py - collab
class No:

    def __init__(self, item):
        self.item = item
        self.proximo: "No" = None
