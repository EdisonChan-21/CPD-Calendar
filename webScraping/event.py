from datetime import datetime

class Event:
    def __init__(self, name="", date="", type="", url=""):
        self.name = name
        self.date = datetime.strptime(date, '%d/%m/%Y').date()
        self.type = type
        self.url = url

    def getName(self): return self.name;

    def getDate(self): return self.date;

    def getType(self): return self.type;

    def getUrl(self): return self.url;

    def getEventDict(self): return {"eventName": self.name, "eventDate": str(self.date), "eventType": self.type, "eventUrl": self.url};

    def setName(self, name): self.name = name;

    def setDate(self, date): self.date = date;

    def setType(self, type): self.type = type;

    def setUrl(self, url): self.url = url;
