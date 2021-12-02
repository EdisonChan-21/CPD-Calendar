from datetime import datetime

class Division:
    def __init__(self, name, url, event = []):
        self.name = name
        self.url = url
        self.event = event

    def getName(self): return self.name;

    def getUrl(self): return self.url;

    def getEvent(self): return self.event;

    def getDivisionDict(self):
        if (self.event != []):
            # print(self.event)
            self.event.sort(key=lambda x: x.date)
            return {"divisionName": self.name, "divisionUrl": self.url, "divisionEvent": [event.getEventDict() for event in self.event]};
        else:
            return {"divisionName": self.name, "divisionUrl": self.url, "divisionEvent": self.event};

    def setAll(self,name, date, event):
        self.setName(name)
        self.setUrl(url)
        self.setEvent(event)

    def setName(self, name): self.name = name;

    def setUrl(self, url): self.url = url;

    def setEvent(self, event): self.event = event;

    def extendEvent(self, event): self.event.extend(event);

    def appendEvent(self, event): self.event.append(event);

    def sortEvent(self):
        # self.event.sort(key=lambda x: x.datetime.strptime(date, '%d/%m/%Y').date())
        self.event.sort(key=lambda x: x.date)
