class Builder:

    def __init__(self):
        self.ui_components = []
        self.app_components = []
        self.skelet = {}
        for filename in ["open", "action", "close"]:
            with open("skelet/{}.html".format(filename), "rb") as file:
                self.skelet[filename] = file.read()
    
    def add(self, template):
        self.ui_components.append("_elements/{}.html".format(template))
        self.app_components.append("_builders/{}.js.html".format(template))

    def render(self):
        ui = b""
        for component in self.ui_components:
            with open(component, "rb") as file:
                ui += file.read()
        app = b""
        for component in self.app_components:
            with open(component, "rb") as file:
                app += file.read()
        self.page = b"".join([self.skelet["open"],
                              ui,
                              self.skelet["action"],
                              app,
                              self.skelet["close"]])
