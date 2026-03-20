def volume_bar(current_volume, max_volume= 20):

    bar = ("=" * current_volume) + (" " * (max_volume - current_volume))
    if current_volume == 0:
        # Grayscale 244 forespace 8-bit colour.
        return f"\033[38;5;244m[{bar}]\033[0m"
        # Greenish-yellow 184 forespace 8-bit colour.
    elif 0 < current_volume <= 5:
        return f"\033[38;5;184m[{bar}]\033[0m"
        # Blue-ish 38 forespace 8-bit colour.
    elif 5 < current_volume < 15:
        return f"\033[38;5;38m[{bar}]\033[0m"
        # Light purple 177 forespace 8-bit colour.
    elif 15 <= current_volume < max_volume:
        return f"\033[38;5;177m[{bar}]\033[0m"
        # Sharp pink 201 forespace 8-bit colour.
    elif current_volume == max_volume:
        return f"\033[38;5;201m[{bar}]\033[0m"
    else:
        return f"[{bar}]"

def volume(default_volume):
    current_volume = default_volume
    min_volume = 0
    max_volume = 20

    adjuster = input("Would you like to increase or decrease the volume? (yes/no) ").casefold().strip()
    if adjuster == 'yes':
        while True:
            x = input("Press \"+\" to increase the volume by 1 increment.\nPress \"-\" to decrease volume by 1 increment.\nType \"enough\" to stop.\n").casefold().strip()
            if x == "+":
                if current_volume < max_volume:
                    current_volume += 1
                else:
                    # Red 196 forespace, yellow background, 8-bit colour.
                    print("\033[38;5;196;48;5;227mVolume is already at MAX.\033[0m")
                    continue
            elif x == "-":
                if current_volume > min_volume:
                    current_volume -= 1
                else:
                    # White 231 forespace, greyish-blue 102 background, 8-bit colour.
                    print("\033[38;5;231;48;5;102mVolume is already at MUTE.\033[0m")
                    continue
            elif x == 'enough':
                if current_volume == max_volume:
                    # Red 196 forespace, yellow 227 background, 8-bit colour.
                    print("\033[38;5;196;48;5;227mVolume: MAX\033[0m")
                    # Dark Red 88 forespace, Orange 166 background, 8-bit colour.
                    print("\033[38;5;88;48;5;166mDanger of losing an eardrum! Lower the volume immediately!\033[0m")
                    continue
                elif current_volume == min_volume:
                    # White 231 forespace, greyish-blue 102 background, 8-bit colour.
                    print("\033[38;5;231;48;5;102mVolume: MUTE\033[0m")
                    print("I shall leave you in peace.")
                    break
                else:
                    # bold 1 font styling, white 37 forespace 4-bit,  bright green 102 background 4-bit.
                    print(f"\033[1;37;102mVolume: {current_volume}\033[0m")
                    break
            else:
                print("Please refer to instructions to try again.")
                continue

            print(volume_bar(current_volume, max_volume))
            if current_volume == min_volume:
                # White 231 forespace, greyish-blue 102 background, 8-bit colour.
                print("\033[38;5;231;48;5;102mVolume: MUTE\033[0m")
                # Dark purple 18 forespace, turquoise 75 background, 8-bit colour.
                print("\033[38;5;18;48;5;75mI wonder if you can hear me O.o \033[0m")
            elif min_volume < current_volume <= 5:
                # Pink 205 forespace, light-blue-pink 189 background, 8-bit colour.
                print(f"\033[38;5;205;48;5;189mVolume: {current_volume}\033[0m")
                # Light green 118 forespace, Light orange 220 background, 8-bit colour.
                print("\033[38;5;118;48;5;220mYou may want to turn it up a notch.\033[0m")
            elif 5 < current_volume < 15:
                # bold 1 font styling, light green 102 background 4-bit colour.
                print(f"\033[1;102mVolume: {current_volume}\033[0m")
            elif 15 <= current_volume < max_volume:
                # Orange 166 text, pale yellow 229 background, 8-bit colour.
                print(f"\033[38;5;166;48;5;229mVolume: {current_volume}\033[0m")
                # Purple 97 foreground, Purple 140 background, 8-bit colour.
                print("\033[38;5;97;48;5;140mYou may want to turn it down a notch.\033[0m")
            elif current_volume == max_volume:
                # Red 196 forespace, yellow background, 8-bit colour.
                print("\033[38;5;196;48;5;227mVolume: MAX\033[0m")
                # Dark Red 88 forespace, Orange 166 background, 8-bit colour. 
                print("\033[38;5;88;48;5;166mHopefully you can still hear me ^_^' \033[0m")
    else:
        print("No adjustments have been made.")


default_volume = 10
volume(default_volume)
    
                

