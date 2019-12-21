semi_bluff           = float(input("% Hold a draw: "))
against_semi_win_p   = float(input("\nagainst_semi_win%: "))
strong               = float(input("\n% Hold nuts: "))
against_strong_win_p = float(input("\nagainst_strong_win%: "))
air                  = float(input("\n% Bluff: "))
against_air_win_p    = float(input("\nagainst_air_win%: "))

if semi_bluff + strong + air != 100:
    print("Plz input opponent's data again")
    semi_bluff           = float(input("% Hold a draw: "))
    strong               = float(input("% Hold nuts: "))
    air                  = float(input("% Bluff: "))

# EV
Call_range = int(semi_bluff*against_semi_win_p + strong*against_strong_win_p + air*against_air_win_p)/100
print()
print("Call_range = %d" % Call_range + "%")
# win rate


