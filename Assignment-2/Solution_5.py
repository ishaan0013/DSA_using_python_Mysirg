class Team:
    Team_list = ["ishaan", "keshav", "harshit", "sumit"]

    def AddMembers(self, a):
        self.Team_list.append(a)

    def Show(self):
        print(self.Team_list)


t1 = Team()
t1.AddMembers("mohit")
t1.Show()
