class BrowserHistory:
    def __init__(self):
        self.history = []
        self.current_index = -1

    def visit(self, url):
        """Adds a new URL to the history, truncating forward history."""
        # Truncate any forward history
        self.history = self.history[:self.current_index + 1]
        self.history.append(url)
        self.current_index += 1

    def back(self):
        """Moves back one step in the history."""
        if self.current_index > 0:
            self.current_index -= 1
        return self.current()

    def forward(self):
        """Moves forward one step in the history."""
        if self.current_index < len(self.history) - 1:
            self.current_index += 1
        return self.current()

    def current(self):
        """Returns the current URL."""
        if self.current_index == -1:
            return None
        return self.history[self.current_index]