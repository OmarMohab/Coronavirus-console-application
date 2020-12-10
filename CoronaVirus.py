import urllib.request
import urllib.parse
import urllib.error
import json


class Data:
    def __init__(self):
        self.data = None
        self.get_data()

    def get_data(self):
        url = urllib.request.urlopen("https://api.covid19api.com/summary")
        self.data = json.loads(url.read().decode())

    def get_total_new(self):
        data = self.data["Global"]

        for k, v in data.items():
            if k == "NewConfirmed":
                return v

    def get_total_cases(self):
        data = self.data["Global"]

        for k, v in data.items():
            if k == "TotalConfirmed":
                return v

    def get_new_deaths(self):
        data = self.data["Global"]

        for k, v in data.items():
            if k == "NewDeaths":
                return v

    def get_total_deaths(self):
        data = self.data["Global"]

        for k, v in data.items():
            if k == "TotalDeaths":
                return v

    def get_new_recovered(self):
        data = self.data["Global"]
        for k, v in data.items():
            if k == "NewRecovered":
                return v

    def get_total_recovered(self):
        data = self.data["Global"]
        for k, v in data.items():
            if k == "TotalRecovered":
                return v

    def get_country_new_cases(self, country):
        data = self.data["Countries"]
        for i in range(len(data)):
            for k, v in data[i].items():
                if v == country:
                    return data[i]["NewConfirmed"]

    def get_country_total_cases(self, country):
        data = self.data["Countries"]
        for i in range(len(data)):
            for k, v in data[i].items():
                if v == country:
                    return data[i]["TotalConfirmed"]

    def get_country_new_deaths(self, country):
        data = self.data["Countries"]
        for i in range(len(data)):
            for k, v in data[i].items():
                if v == country:
                    return data[i]["NewDeaths"]

    def get_country_total_deaths(self, country):
        data = self.data["Countries"]
        for i in range(len(data)):
            for k, v in data[i].items():
                if v == country:
                    return data[i]["TotalDeaths"]

    def get_country_new_racovered(self, country):
        data = self.data["Countries"]
        for i in range(len(data)):
            for k, v in data[i].items():
                if v == country:
                    return data[i]["NewRecovered"]

    def get_country_total_racovered(self, country):
        data = self.data["Countries"]
        for i in range(len(data)):
            for k, v in data[i].items():
                if v == country:
                    return data[i]["TotalRecovered"]


data = Data()
while True:
    print("1 - Global Numbers")
    print("2 - Numbers by Country")
    print("3 - Exit")
    choice1 = int(input())
    if choice1 == 1:
        print(f"New Cases: {data.get_total_new()}")
        print(f"Total Cases: {data.get_total_cases()}")
        print(f"New Deaths: {data.get_new_deaths()}")
        print(f"Total Deaths: {data.get_total_deaths()}")
        print(f"New Recovered: {data.get_new_recovered()}")
        print(f"Total Recovered: {data.get_total_recovered()}")
    elif choice1 == 2:
        print("Please Enter the country name")
        choice2 = input().capitalize()
        print(f"{choice2} New Cases: {data.get_country_new_cases(choice2)}")
        print(f"{choice2} Total Cases: {data.get_country_total_cases(choice2)}")
        print(f"{choice2} New Deaths: {data.get_country_new_deaths(choice2)}")
        print(f"{choice2} Total Deaths: {data.get_country_total_deaths(choice2)}")
        print(f"{choice2} New Recovered: {data.get_country_new_racovered(choice2)}")
        print(f"{choice2} Total Recoered: {data.get_country_total_racovered(choice2)}")
    elif choice1 == 3:
        exit()
    else:
        print("the choice is out of range")
        continue
