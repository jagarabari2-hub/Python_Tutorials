from itertools import count


print()
print("|========================================|"
      "| TEAM STATUS "
      "||========================================|")
print()
class MyTeam():
        def __teamRecord(s):
            A = {"A":145, "B":784, "C":471, "D":154, "E":789, "F":654, "G":123, "H":456, "I":789, "J":258, "K":549, "STATUS":"WIN"}
            B = {"A1":23, "B1":34, "C1":56, "D1":11, "E1":50, "F1":20, "G1":10, "H1":0, "I1":15, "J1":2, "K1":18, "STATUS":"LOSE"}
            C = {"A2":0, "B2":0, "C2":1, "D2":2, "E2":3, "F2":10, "G2":5, "H2":17, "I2":23, "J2":35, "K2":0, "STATUS":"LOSE"}
            D = {"A3":12, "B3":13, "C3":5, "D3":15, "E3":0, "F3":0, "G3":28, "H3":9, "I3":4, "J3":10, "K3":8, "STATUS":"LOSE"}
            E = {"A4":256, "B4":895, "C4":582, "D4":265, "E4":899, "F4":123, "G4":12, "H4":12, "I4":18, "J4":56, "K4":543, "STATUS":"WIN"}
            F = {"A5":45, "B5":47, "C5":17, "D5":14, "E5":19, "F5":29, "G5":13, "H5":46, "I5":9, "J5":11, "K5":59, "STATUS":"LOSE"}
            G = {"A6":645, "B6":487, "C6":271, "D6":320, "E6":653, "F6":230, "G6":120, "H6":321, "I6":195, "J6":111, "K6":221, "STATUS":"WIN"}
            H = {"A7":15, "B7":74, "C7":41, "D7":14, "E7":0, "F7":0, "G7":11, "H7":18, "I7":12, "J7":17, "K7":32, "STATUS":"LOSE"}
            I = {"A8":445, "B8":712, "C8":371, "D8":54, "E8":189, "F8":210, "G8":12, "H8":56, "I8":989, "J8":458, "K8":749, "STATUS":"WIN"}
            J = {"A9":15, "B9":99, "C9":17, "D9":33, "E9":42, "F9":89, "G9":13, "H9":23, "I9":23, "J9":11, "K9":198, "STATUS":"LOSE"}
            print("Team A:", A , "\nTeam B :", B, "\nTeam C :", C, "\nTeam D :", D, "\nTeam E :", E, "\nTeam F :", F, "\nTeam G :", G, "\nTeam H :", H, "\nTeam I :", I, "\nTeam J :", J)
            if A["STATUS"] == "WIN":
                print("Team A is the winner")
            if B["STATUS"] == "WIN":
                print("Team B is the winner")
            if C["STATUS"] == "WIN":
                print("Team C is the winner")
            if D["STATUS"] == "WIN":
                print("Team D is the winner")
            if E["STATUS"] == "WIN":
                print("Team E is the winner")
            if F["STATUS"] == "WIN":
                print("Team F is the winner")
            if G["STATUS"] == "WIN":
                print("Team G is the winner")
            if H["STATUS"] == "WIN":
                print("Team H is the winner")
            if I["STATUS"] == "WIN":
                print("Team I is the winner")
            if J["STATUS"] == "WIN":
                print("Team J is the winner")   
            else:
                print("Team LOSE")
            print("Count Total Score Of all Teams")
            print("Total Score Of Team A:", sum(A.values()))
obj = MyTeam()
print(obj._MyTeam__teamRecord())